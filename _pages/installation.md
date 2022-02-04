---
title: ""
permalink: /pages/installation/
---

![image-center]({{ "/assets/images/logo.png" | relative_url }})


_Note: CASM is available for macOS and Linux_
{: .notice--info}

## Install using Conda

The recommended method for obtaining CASM is to install the ``casm-cpp`` conda package available online from [anaconda.org](https://anaconda.org/prisms-center). Conda is a package and environment management system that works on Windows, macOS, and Linux. For help installing and using conda, see the [Conda user guide](https://docs.conda.io/projects/conda/en/latest/user-guide/index.html) and [installation page](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html). We recommend using the Miniconda installation.

To install the latest version of CASM:

    conda create -n casm \
      --override-channels -c prisms-center -c conda-forge \
      casm-cpp=1.2.0 python=3

_Note: Include the version number to ensure the latest version is installed. The latest version is ``casm-cpp=1.2.0``._
{: .notice--info}

This will create a conda environment named `casm` in which the following are installed:

- Required dependencies
- The `libcasm` and `libccasm` shared libraries.
- The ``ccasm`` command line program.

To use CASM, activate the CASM environment:

    conda activate casm

The ``casm-python`` Python package is a collection of Python packages that provide a Python interface to the CASM libraries, implement wrappers to fitting methods and DFT software, and provide other tools for plotting and analysis. From inside the `casm` conda environment, it can be installed using:

    pip install casm-python

This will install the `casm-python` package and the `casm` command line program, which provides a combined interface for the command line methods available from both `casm-cpp` and `casm-python`.

{: .notice--info }
**Note:** Currently, the CASM VASP wrapper is updated for CASM 1.X. An updated Quantum ESPRESSO wrapper for CASM 1.X will be available in the near future along with a method for converting between additional structure file formats.

To deactivate the CASM environment when done using CASM:

    conda deactivate

### Other common commands

- To remove the `casm` conda environment:

      conda remove --name casm --all

- To update to the latest version of ``casm-cpp`` (from the activated conda environment):

      conda update casm-cpp

- To update to the latest version of ``casm-python`` (from the activated conda environment):

      pip install -U casm-python

- To install dependencies for the CASM [tutorials]({{ "/pages/tutorials/" | relative_url }}), see [this]({{ "/pages/tutorials/tutorial_env" | relative_url }}) page.


## Install using Docker

A CASM docker image is available. To use this image, first install Docker with the instructions found [here](https://docs.docker.com/engine/install/). A brief introduction to Docker and its usage may be found at this [link](https://docs.docker.com/get-started/overview/).

Once Docker is installed, the CASM Docker image can be pulled with:

    docker pull casmcode/casm

Once the CASM image is on your computer it can be invoked by using:

    docker run --rm -it -v <data_folder>:/root/ \
        casmcode/casm bash

The value `<data_folder>` should be replaced with the path to folder on your computer that will be mounted as volume to the docker container. Any changes you make to it from inside the container will persist on your computer and be available outside the container.

For more details, including suggested configuration, see the CASM Docker page [here](https://hub.docker.com/r/casmcode/casm-base).

## Install from source

See CASM installation instructions [here](https://github.com/prisms-center/CASMcode/blob/1.X/INSTALL.md).
