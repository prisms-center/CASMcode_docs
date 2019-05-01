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

if conda list -n $CASM_DOCS_ENV > /dev/null 2>&1; then
  echo "conda environment '$CASM_DOCS_ENV' already exists."
  echo "To recreate it, first remove it with: "
  echo "  conda remove --name $CASM_DOCS_ENV --all -y"
  conda activate $CASM_DOCS_ENV

  # check for updates
  echo "Checking for updates..."
  conda update $CASM_DOCS_CONDA_INSTALL casm
else
  echo "Create conda environment '$CASM_DOCS_ENV'"
  conda create -n $CASM_DOCS_ENV $CASM_DOCS_CONDA_INSTALL "python =$CASM_PYTHON_VERSION" ruby "casm =$CASM_VERSION" -y
  conda activate $CASM_DOCS_ENV
fi

if [ ! -f "Gemfile.lock" ]; then
  echo "Installing github-pages gems..."

  # install github pages gems (this uses the Gemfile included in the repository)
  gem install bundler

  # better way?
  if [[ "$CASM_OS_NAME" == "osx" ]]; then
    echo "Configuring bundle for osx..."
    ln -f -s /usr/bin/clang $CONDA_PREFIX/bin/x86_64-apple-darwin13.4.0-clang
    bundle config --local build.eventmachine --with-cppflags=-I$CONDA_PREFIX/include
    bundle config --local build.nokogiri --use-system-libraries
  fi
  bundle install --path $CONDA_PREFIX/lib/ruby/gems/2.5.0
else
  echo "Updating github-pages gems..."
  bundle update
fi

if [ -d "$CASM_TEST_PROJECTS_DIR" ]; then
  echo "CASM_test_projects already exists."
  echo "To re-download it, first remove it with: "
  echo "  rm -r $CASM_TEST_PROJECTS_DIR"

else
  echo "Downloading CASM_test_projects from Materials Commons..."

  # if you don't already have it, ask bpuchala for access and download the CASM test projects
  check_var "MC_API_URL" "Materials Commons URL" "https://materialscommons.org/api"
  check_secret_var "MC_API_KEY" "Materials Commons API Key"

  pip install -U materials-commons
  cd $CASM_TEST_PROJECTS_DIR/..
  mc clone 2e794436-2700-48be-aded-321c460f0fd5
  cd CASM_test_projects && mc down -r 0.3.X

fi
