#!/bin/bash
#SBATCH --job-name=v14dupaudit
#SBATCH --account=avery
#SBATCH --qos=avery
#SBATCH --partition=hpg-default
#SBATCH --cpus-per-task=16
#SBATCH --mem=32gb
#SBATCH --time=08:00:00
#SBATCH --output=/blue/avery/p.chang/work/skim/NanoTools_/skimmer/condor/logs_dedup/%x_%j.log
# Usage: sbatch dup_audit.sbatch <out.json> [categories]
# Reads the /cmsuf staged copy when present, else xrootd (needs the proxy).
set -uo pipefail
cd /blue/avery/p.chang/work/skim/NanoTools_/skimmer/condor
export X509_USER_PROXY=$HOME/private/x509_proxy
export X509_CERT_DIR=/cvmfs/cms.cern.ch/grid/etc/grid-security/certificates
OUT=${1:?out json}; CATS=${2:-}
echo "host=$(hostname) start=$(date) out=$OUT cats=${CATS:-ALL}"
python3 -u v14_dup_audit.py --out "$OUT" ${CATS:+--categories "$CATS"} -j 16
rc=$?
echo "DUP_AUDIT_DONE rc=$rc $(date)"
