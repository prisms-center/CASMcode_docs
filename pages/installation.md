---
layout: default
---
## Installation

The recommended method for obtaining CASM is to install the ``casm-cpp`` conda package available online from [anaconda.org](https://anaconda.org/prisms-center). For help installing and using conda, see [conda.io](https://conda.io/docs/index.html).

It can be installed using:

```
$ conda create -n casm --override-channels -c prisms-center -c defaults -c conda-forge casm-cpp
```

This will install:

- Required dependencies
- The `libcasm` and `libccasm` shared libraries.
- The ``ccasm`` command line program.

The ``casm-python`` Python package is a collection of python packages that provide a Python interface to the CASM libraries, implement wrappers to fitting methods and DFT software, and provide other tools for plotting and analysis. It can be installed using:

    git clone git@github.com:prisms-center/CASMpython.git
    cd CASMpython/casm
    pip install .

This will install the `casm-python` package and the `casm` command line program.

A PyPI package and updated quantumespresso wrapper  for CASM 1.0.X will be available in the near future.


[[Using CASM]](../index.md#using-casm)
