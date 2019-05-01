set -e

check_var "CASM_TEST_PROJECTS_DIR" "Location of CASM test projects"

python scripts/tutorials.py
python scripts/casm-cpp-examples.py
python scripts/casm-python-examples.py
