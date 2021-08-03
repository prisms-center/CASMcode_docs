---
title: "Tutorial environment"
permalink: /pages/tutorials/tutorial_env/
sidebar: false
toc: false
---

Installation and setup instructions for running [Jupyter](https://jupyter.org) notebook examples:

- If necessary, install Conda and create and activate a CASM environment, as described on the [CASM installation]({{ "/pages/tutorials/tutorial_env" | relative_url }}) page, installing both `casm-cpp` and `casm-python`.

- In the CASM environment, install Jupyter and other dependencies:

      conda install --override-channels \
        -c conda-forge jupyter jq

- Activate the CASM conda environment:

      conda activate casm_1.X

- To enable bash notebook examples:

      pip install bash_kernel && \
        python -m bash_kernel.install

- To install plotting dependencies for python notebook examples:

      pip install holoviews

- Launch jupyter:

      jupyter notebook
