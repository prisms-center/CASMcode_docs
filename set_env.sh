# source this script to set your environment to run the tutorials and examples

set -e
export CASMcode_docs_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
. $CASMcode_docs_DIR/build_scripts/install-functions.sh
. $CASMcode_docs_DIR/build_scripts/build-variables.sh
detect_os

if [ ! -f $CASM_CONDA_INIT ] ; then
  echo "CASM_CONDA_INIT=\"$CASM_CONDA_INIT\" does not exist. exiting..."
  exit
fi
. $CASM_CONDA_INIT
conda activate $CASM_DOCS_ENV
set +e
