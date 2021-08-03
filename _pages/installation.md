---
title: ""
permalink: /pages/installation/
---

![image-center]({{ "/assets/images/logo.png" | relative_url }})


_Note: CASM is available for macOS and Linux_
{: .notice--info}

## Install using Conda

The recommended method for obtaining CASM is to install the ``casm-cpp`` conda package available online from [anaconda.org](https://anaconda.org/prisms-center). Conda is a package and environment management system that works on Windows, macOS, and Linux. For help installing and using conda, see the [Conda user guide](https://docs.conda.io/projects/conda/en/latest/user-guide/index.html) and [installation page](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html). We recommend using the Miniconda installation.

To create a new conda environment for CASM named `"casm_1.X"`:

    conda create -n casm_1.X python=3

To activate the CASM environment:

    conda activate casm_1.X

To install CASM 1.X into the current conda environment:

    conda install --override-channels \
      -c prisms-center -c defaults -c conda-forge \
      python=3 casm-cpp

This will create a conda environment named `casm` in which the following are installed:

- Required dependencies
- The `libcasm` and `libccasm` shared libraries.
- The ``ccasm`` command line program.

The ``casm-python`` Python package is a collection of Python packages that provide a Python interface to the CASM libraries, implement wrappers to fitting methods and DFT software, and provide other tools for plotting and analysis. It can be installed using:

    pip install casm-python

This will install the `casm-python` package and the `casm` command line program, which provides a combined interface for the command line methods available from both `casm-cpp` and `casm-python`.

{: .notice--info }
**Note:** Currently, the CASM VASP wrapper is updated for CASM 1.X. An updated Quantum ESPRESSO wrapper for CASM 1.X will be available in the near future along with a method for converting between additional structure file formats.

To remove the CASM conda environment:

    conda remove --name casm_1.X --all

To install dependencies for the CASM [tutorials]({{ "/pages/tutorials/" | relative_url }}), see [this]({{ "/pages/tutorials/tutorial_env" | relative_url }}) page.

## Install from source

See CASM installation instructions [here](https://github.com/prisms-center/CASMcode/blob/1.X/INSTALL.md).
