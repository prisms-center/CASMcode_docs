## CASM Online documentation

This repository is used to generate the [CASM online documentation](https://prisms-center.github.io/CASMcode_docs/).

The contents of the tutorials are generated via scripts. To generate the tutorials, first:

- Set environment variables:
  - `CASMcode_docs_DIR`: Path to this repository
  - `CASM_TEST_PROJECTS_DIR`: Path to CASM test projects directory (cloned from Materials Commons)
- Activate a CASM conda environment

Then run:

    rm -r CASM_TEST_PROJECTS_DIR/0.3.X/*_tutorial
    python $CASMcode_docs_DIR/scripts/tutorials.py

The content in the tutorials is specified via JSON files.  For an example of the format, see the contents of `scripts/tutorials/init` which is used to create the [Project initialization](https://prisms-center.github.io/CASMcode_docs/pages/tutorials/init.html) tutorial.
