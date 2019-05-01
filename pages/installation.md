---
layout: default
---

[![CASM Logo]({{ site.baseurl }}/assets/logo.png)](https://prisms-center.github.io/CASMcode_docs/)

***
## Installation

The recommended method for obtaining CASM is to install the ``casm`` conda package available online from [anaconda.org](https://anaconda.org/prisms-center). For help installing and using conda, see [conda.io](https://conda.io/docs/index.html).

It can be installed using:

```
$ conda create -n casm --override-channels -c bpuchala/label/dev -c prisms-center -c defaults -c conda-forge casm
```

This will install:

- Required dependencies
- The `libcasm` and `libccasm` shared libraries.
- The ``casm-python`` Python package, a collection of python packages that provide a Python interface to the CASM libraries, implement wrappers to fitting methods and DFT software, and provide other tools for plotting and analysis. It is imported using: ``import casm``.
- The ``casm`` command line program.

- It will also install some legacy programs, now available as ``casm`` command line program subcommands:
  - ``casm-learn`` a program for fitting effective cluster interactions (ECI)
  - ``casm-calc`` a program that helps setup and run high throughput *ab initio* calculations
    - ``$CASM_PREFIX/bin/vasp.setup`` a script for setting up VASP jobs
    - ``$CASM_PREFIX/bin/vasp.relax`` a script for setting up and submitting VASP jobs
    - ``$CASM_PREFIX/bin/vasp.relax.report`` a script for setting up and submitting VASP jobs
  - ``casm.plot.<type>`` programs to generate ``bokeh`` plots

***
## Downloading demonstration projects

CASM demonstration projects can be found in the [CASMcode_demo](https://github.com/prisms-center/CASMcode_demo) GitHub repo.

To use a demonstration project you can clone the demonstration project repository:

    git clone git@github.com:prisms-center/CASMcode_demo.git

Or you can download a single project using ``svn export <repo>/trunk/<folder>``, for example:

    svn export https://github.com/prisms-center/CASMcode_demo/trunk/TMS_ICME_PRISMS_workshop_May_2017

***
## Installing the test projects

CASM projects used for testing and tutorial documentation purposes are stored at [Materials Commons](https://materialscommons.org).

[[Up]]({{ site.baseurl }}/index.html#using-casm)
