## CASM Online documentation

This repository is used to generate the [CASM online documentation](https://prisms-center.github.io/CASMcode_docs/).

## Running the tutorials and examples

The contents of the tutorials and examples are generated via scripts. To generate the tutorials, and examples first:

- Set environment variables:
  - `CASM_TEST_PROJECTS_DIR`: Path to CASM test projects directory (cloned from Materials Commons)
- To create a conda environment for installing CASM, executing tutorials and examples, and generating Jekyll documentation:
  - Edit `build_scripts/build_variables` if necessary to specify CASM version and source
  - Execute `. create_env.sh`
- Subsequently, activate the tutorial environment directly or with `. set_env.sh`
- To clean up test projects before & after executing the tutorials and examples use: `. clean_all.sh`
- To run all tutorials and examples use: `. run_all.sh`

The content in the tutorials is specified via YAML files.  For an example of the format, see the contents of `scripts/tutorials/init` which is used to create the [Project initialization](https://prisms-center.github.io/CASMcode_docs/pages/tutorials/init.html) tutorial.

## Running the site locally

- Get basic help [here](https://help.github.com/articles/setting-up-your-github-pages-site-locally-with-jekyll/#step-3-optional-generate-jekyll-site-files)

Update jekyll:

- bundle update github-pages

To run (from repo root directory):

- export `JEKYLL_GITHUB_TOKEN=<your token here>`
- bundle exec jekyll serve

Open in browser:

- http://localhost:4000
