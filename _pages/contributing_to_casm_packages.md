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

Clone [CASMcode_pydocs](https://github.com/prisms-center/CASMcode_pydocs), then set an environment variable indicating where to store the docs:

    mkdir <path-to-pydocs>/docs/casm
    export LIBCASM_PYDOCS=<path-to-pydocs>/docs/casm


Install the casm package first, then build and open the documentation:

    cd python/doc
    # In the following, replace:
    # - <package> with the distribution package name
    # - <vers> with the major.minor version number
    # Example: <package>=xtal, <vers>=2.0
    sphinx-build -b html . $CASM_PYDOCS/<package>/<vers>/
    open $CASM_PYDOCS/<package>/<vers>/index.html


## Testing

To install testing requirements, do:

    pip install -r test_requirements.txt

Use `pytest` to run the tests. To run all tests, do:

    pytest -rsap tests

As an example of running a specific test, do:

    pytest -rsap tests/<filepath>::<function_name>


## Python development

**Note** The following guidelines apply to casm packages v2+.
{: .notice--warning}

To install formatting requirements, do:

    pip install -r dev_requirements.txt


### Python linting

For Python code linting, use [ruff](https://beta.ruff.rs/docs/). Do:

    ruff check --fix python/


### Python formatting

For Python code formatting, use [black](https://black.readthedocs.io). Do:

    black python/

### Python docstring style

- When in doubt, refer to [numpydoc](https://numpydoc.readthedocs.io/en/latest/format.html), [pandas](https://pandas.pydata.org/docs/development/contributing_documentation.html), or [scikit-learn](https://scikit-learn.org/dev/developers/contributing.html#documentation).
- When referring to constructor arguments or function variables in docstring text, use the convention ``` `variable` ```, so variables appear italicized because (i.e. The *variable* is important).
- When describing that a variable has a particular value or how it is used in a code snippet, then use either inline code (```variable=True```) or a code block:

  ```
  .. code-block:: Python

      variable = 6
  ```
- Make use of ```.. rubric:: Special Methods``` to create a section in a class docstring to document any special members of a class, such as comparison operators (`<`, `<=`, `>`, `>=`, etc.) or overloaded operators (`*`, `+`, `+=`, `-`, `-=`, etc.).


### Adding tests

- Add Python tests for `casm.<subpackage>` in `python/tests/<subpackage>`, using pytest.
- If data files are needed for testing, they can be placed in `python/tests/<subpackage>/data/`.
- To access data files use the `shared_datadir` fixture available from the [`pytest-datadir`](https://pypi.org/project/pytest-datadir/) plugin.
- To create temporary testing directories for reading and writing files, use the [`tmpdir` and `tmpdir_factory`](https://docs.pytest.org/en/7.4.x/how-to/tmp_path.html#the-tmpdir-and-tmpdir-factory-fixtures) fixtures available from pytest.
- For tests that involve an expensive setup process, such as compiling Clexulators, a session-length shared datadir can be constructed once and re-used as done [here](https://github.com/prisms-center/CASMcode_clexulator/blob/main/python/tests/clexulator/conftest.py) in CASMcode_clexulator.
- Expensive tests can also be set to run optionally using flags as demonstrated in CASMcode_clexulator.


