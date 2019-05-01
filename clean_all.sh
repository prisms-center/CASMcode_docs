set -e

check_var "CASM_TEST_PROJECTS_DIR" "Location of CASM test projects"

rm -r $CASM_TEST_PROJECTS_DIR/0.3.X/*_tutorial || true
rm -r $CASM_TEST_PROJECTS_DIR/0.3.X/*_pyex_proj || true
