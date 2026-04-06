# NanoTools

NanoAOD skimmer and analysis framework for VBS VVH.

## Environment & Setup

Runs on **HiPerGator** (el9) with `CMSSW_14_1_6`:

```bash
git clone https://github.com/cmstas/NanoTools
cd NanoTools/
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=el9_amd64_gcc12
cd /cvmfs/cms.cern.ch/el9_amd64_gcc12/cms/cmssw/CMSSW_14_1_6/ && cmsenv && cd -
```

## NanoCORE

```bash
cd NanoCORE
make test -j12
cd ..
```

Unit tests are in `NanoCORE/Tools/unit_tests/` and run via `make test`.

## Skimmer

See [`skimmer/README.md`](skimmer/README.md) for building, submitting jobs, output structure, and validation tooling.

## Style

We use `clang-format` based on LLVM style to format our code. To format the `ElectronSelections.cc` file in-place, do
```bash
clang-format -style="{BasedOnStyle: llvm, IndentWidth: 4, ColumnLimit: 120, AllowShortIfStatementsOnASingleLine: true, AllowShortBlocksOnASingleLine: true}" -i ElectronSelections.cc
```

Add this to the `~/.vimrc` and use `vim` to code:
```
autocmd BufNewFile,BufRead *.cc,*.h,*.C,*.cxx set formatprg=clang-format\ -style=\"{BasedOnStyle:\ llvm,\ IndentWidth:\ 4,\ ColumnLimit:\ 100,\ AllowShortIfStatementsOnASingleLine:\ true,\ AllowShortBlocksOnASingleLine:\ false,\ BreakBeforeBraces:\ Allman}\"
```

To format your code, press `ggvGgq`.

## Grid Certificate

Copy the certificate to a file named `myCert.p12` to the computer where you will run `voms-proxy-init`.

Extract your certificate (which contains the public key) and the private key:

```bash
# Extract the certificate
openssl pkcs12 -in myCert.p12 -clcerts -nokeys -out $HOME/.globus/usercert.pem

# Extract the encrypted private key
openssl pkcs12 -in myCert.p12 -nocerts -out $HOME/.globus/userkey.pem

# Set permissions
chmod 600 $HOME/.globus/userkey.pem
chmod 600 $HOME/.globus/usercert.pem
```

Delete the `myCert.p12` file after extracting to avoid security issues.

See https://ca.cern.ch/ca/ for more information.
