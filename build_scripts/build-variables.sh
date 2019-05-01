set -e

# create conda environment:
check_var "CASM_VERSION" "CASM version" "0.3.dev269+gd07b42"
check_var "CASM_CHANNEL" "CASM conda channel" "bpuchala"
check_var "CASM_PYTHON_VERSION" "CASM Python version" "3.6"
check_var "CASM_DOCS_ENV" "Conda environment name" "casmdocs_${CASM_CHANNEL}_${CASM_VERSION}_py${CASM_PYTHON_VERSION}"
check_var "CASM_TEST_PROJECTS_DIR" "Location of CASM test projects" "$HOME/mcproj/CASM_test_projects"
check_var "CASM_DOCS_CONDA_INSTALL" "Conda install command" "--override-channels -c $CASM_CHANNEL/label/dev -c prisms-center -c defaults -c conda-forge"
check_var "CASM_CONDA_INIT" "Location of conda.sh" "$HOME/.local/conda/etc/profile.d/conda.sh"
