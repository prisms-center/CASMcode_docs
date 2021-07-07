## CASM Online documentation

This repository contains the [CASM online documentation](https://prisms-center.github.io/CASMcode_docs/).

## Running the site locally

- Get basic help [here](https://help.github.com/articles/setting-up-your-github-pages-site-locally-with-jekyll/#step-3-optional-generate-jekyll-site-files)
- Get minimal-mistakes theme help [here](https://mmistakes.github.io/minimal-mistakes/docs/quick-start-guide/)

Install / update ruby gems:

- rm -f Gemfile.lock
- bundle

To run (from repo root directory):

- (optional) export `JEKYLL_GITHUB_TOKEN=<your token here>`
- bundle exec jekyll serve --incremental

Open in browser:

- http://localhost:4000
