---
title: ""
permalink: /pages/contributing_to_casm_packages/
sidebar: true
toc: true
layout: single

---

<img alt="Shows the CASM logo" src="{{ "/assets/images/logo.svg" | relative_url }}" width="600" />

## Contributing to casm Packages

Collaboration is welcome and new features can be incorporated by forking one of the libcasm repositories on GitHub, creating a bug fix or new feature, and submitting a pull request. If you are interested in developing features that involve a significant time investment we encourage you to first contact the CASM development team at <casm-developers@lists.engr.ucsb.edu>.

Pull requests should:

- Create a branch from the development branch for new features (i.e. `2.X`) and name it to indicate that it implements a new feature (i.e. `2.X-myfeature`) or a bug fix (i.e `2.0.0-patch-issue`)
- Propose a minimal set of changes
- Have code formatted and documented as described below
- Include appropriate tests
- Pass all CI tests
- Include a suggested CHANGELOG.md entry, see [keepachangelog.com](https://keepachangelog.com).


### Repository layout

The repository for each libcasm distribution packages is organized as follows:

- `casm/<name>/`: Python namespace packages
- `tests/<name>/`: Python tests
- `doc/`: Python documentation


### Installation layout

When the project is built and installed, components are added to the Python installation location (i.e. `<python package prefix> = <something>/lib/pythonX.Y/sites-packages/`) in the `libcasm/` folder at the following locations:

`<python package prefix>/casm/`:

- `<name>/`: casm Python namespace packages


## Installing from source

Installation of libcasm distribution packages from source requires Python >= 3.8.

The CASM package and its dependencies can be installed with:

    pip install .


## Building documentation

Install documentation requirements:

    pip install -r doc_requirements.txt

Install the CASM package first, then build and open the documentation:

    cd doc
    sphinx-build -b html . _build/html
    open _build/html/index.html


## Testing

To install testing requirements, do:

    pip install -r test_requirements.txt

Use `pytest` to run the tests. To run all tests, do:

    pytest -rsap tests

As an example of running a specific test, do:

    pytest -rsap tests/<filepath>::<function_name>


## Linting, formatting, and style

Follow the Python linting, formatting, and style guidelines [here](({{ "/pages/libcasm_packages_overview/#formatting-and-style" | relative_url }}).


## Adding tests

Follow the Python test guidelines [here](({{ "/pages/libcasm_packages_overview/#adding-tests" | relative_url }}).
