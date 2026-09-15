#!/bin/bash
#SBATCH --job-name=v14stage
#SBATCH --output=/blue/avery/p.chang/work/skim/NanoTools_/skimmer/condor/logs_stage/stage_%A_%a.out
#SBATCH --error=/blue/avery/p.chang/work/skim/NanoTools_/skimmer/condor/logs_stage/stage_%A_%a.err
#SBATCH --partition=hpg-default
#SBATCH --qos=avery-b
#SBATCH --account=avery
#SBATCH --time=12:00:00
#SBATCH --mem=2gb
#SBATCH --cpus-per-task=1
#SBATCH --ntasks=1
#
# Stage v14 PFNano inputs from FNAL EOS onto /cmsuf, one array task per slice.
#
# Deliberately NOT a Metis job: this is a pure data movement pass with no skim
# step, and it must be safely re-runnable. Each task walks its slice of the
# manifest and copies anything not already present.
#
# IDEMPOTENT: a destination that already exists with a size matching the remote
# is skipped. Re-running after a partial or failed pass only moves what is
# missing, so the whole thing can be re-submitted without cleanup.
#
# Usage:
#   mkdir -p logs_stage
#   sbatch --array=0-39 stage_v14.sh stage_manifest_2022.txt 40

set -uo pipefail

MANIFEST="${1:?usage: stage_v14.sh <manifest> <nslices>}"
NSLICES="${2:?usage: stage_v14.sh <manifest> <nslices>}"
SLICE="${SLURM_ARRAY_TASK_ID:-0}"

source /cvmfs/oasis.opensciencegrid.org/osg-software/osg-wn-client/3.6/current/el9-x86_64/setup.sh 2>/dev/null
export X509_USER_PROXY=${X509_USER_PROXY:-$HOME/private/x509_proxy}
# Without an explicit CA dir the xrootd 5.x client falls back to ztn and the
# transfer dies with "Auth failed" -- same fix as the skim jobs.
export X509_CERT_DIR=/cvmfs/cms.cern.ch/grid/etc/grid-security/certificates
export X509_VOMS_DIR=/cvmfs/cms.cern.ch/grid/etc/grid-security/vomsdir

MAX_RETRIES=4
RETRY_SLEEP=30

n_total=0; n_skip=0; n_copy=0; n_fail=0
t0=$(date +%s)

echo "[stage] slice ${SLICE}/${NSLICES}  manifest=${MANIFEST}  host=$(hostname)"

# awk picks this slice's lines: line index mod NSLICES == SLICE
while IFS=$'\t' read -r SRC DEST; do
    [ -z "${SRC:-}" ] && continue
    n_total=$((n_total+1))

    # remote size (empty if stat fails; we still attempt the copy in that case)
    RSIZE=$(timeout 60 xrdfs cmseos.fnal.gov stat "${SRC#root://cmseos.fnal.gov/}" 2>/dev/null \
            | awk '/^Size/{print $2}')

    if [ -f "${DEST}" ]; then
        LSIZE=$(stat -c %s "${DEST}" 2>/dev/null || echo 0)
        if [ -n "${RSIZE}" ] && [ "${LSIZE}" = "${RSIZE}" ]; then
            n_skip=$((n_skip+1)); continue
        fi
        # present but wrong size => truncated from an earlier interrupted pass
        echo "[stage] RESTAGE (size ${LSIZE} != ${RSIZE:-?}): ${DEST}"
        rm -f "${DEST}"
    fi

    mkdir -p "$(dirname "${DEST}")"

    ok=0
    for (( a=1; a<=MAX_RETRIES; a++ )); do
        # redirector fallback mirrors the skim executable: FNAL -> UNL -> global
        case $a in
            1|2) URL="${SRC}" ;;
            3)   URL="${SRC/cmseos.fnal.gov/xrootd.unl.edu}" ;;
            *)   URL="${SRC/cmseos.fnal.gov/cms-xrd-global.cern.ch}" ;;
        esac
        # copy to a .part file so an interrupted transfer is never mistaken for
        # a complete one by the next run
        if timeout 3600 xrdcp --force --silent "${URL}" "${DEST}.part" 2>/dev/null; then
            PSIZE=$(stat -c %s "${DEST}.part" 2>/dev/null || echo 0)
            if [ -z "${RSIZE}" ] || [ "${PSIZE}" = "${RSIZE}" ]; then
                mv -f "${DEST}.part" "${DEST}"; ok=1; break
            fi
            echo "[stage] short copy (${PSIZE} != ${RSIZE}) attempt ${a}: ${SRC}"
        fi
        rm -f "${DEST}.part"
        sleep ${RETRY_SLEEP}
    done

    if [ "${ok}" = "1" ]; then
        n_copy=$((n_copy+1))
    else
        n_fail=$((n_fail+1))
        echo "[stage] FAILED after ${MAX_RETRIES}: ${SRC}"
    fi

    if (( n_total % 25 == 0 )); then
        echo "[stage] progress: ${n_total} seen, ${n_copy} copied, ${n_skip} skipped, ${n_fail} failed, $(( ($(date +%s)-t0)/60 )) min"
    fi
done < <(awk -v s="${SLICE}" -v n="${NSLICES}" 'NR % n == s' "${MANIFEST}")

echo "[stage] SLICE_DONE slice=${SLICE} seen=${n_total} copied=${n_copy} skipped=${n_skip} failed=${n_fail} elapsed=$(( ($(date +%s)-t0)/60 ))min"
exit $(( n_fail > 0 ? 1 : 0 ))
