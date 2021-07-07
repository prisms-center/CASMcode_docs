---
title: "Tutorial environment"
permalink: /pages/tutorial_env/
sidebar: false
toc: false
---

Installation and setup instructions for running jupyter notebook examples:

- Install and source conda. For help installing and using conda, see the [Conda user guide](https://conda.io/projects/conda/en/latest/user-guide/index.html). We recommend following the instructions for the [Miniconda installation](https://conda.io/projects/conda/en/latest/user-guide/install/index.html).
- Create and activate a conda environment for CASM examples:

      conda create -n casm_1.X_examples --override-channels -c prisms-center -c defaults -c conda-forge python=3 casm-cpp=1 jupyter jq
      conda activate casm_1.X_examples

- To enable bash_kernel examples:

      pip install bash_kernel
      python -m bash_kernel.install

- To install the casm-python package and other dependencies for python_kernel examples:

      pip install casm-python holoviews

- Launch jupyter:

      jupyter notebook
