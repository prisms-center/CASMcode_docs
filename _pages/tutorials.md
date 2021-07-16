---
title: ""
permalink: /pages/tutorials/
---

![image-center]({{ "/assets/images/logo.png" | relative_url }})

# Tutorials

This section provides links to CASM tutorials written using Jupyter notebooks. Some tutorials are written to demonstrate using the CASM command line interface (CLI) `ccasm` and some are written to demonstrate using the CASM Python package `casm-python`. Notebooks can be downloaded and run locally to try using CASM and static versions showing results can be viewed online.

To setup a conda environment with all the dependencies necessary for running the tutorials, see [this]({{ "/tutorials/tutorial_env" | relative_url }}) page.

## Defining the "prim"

These tutorials demonstrate defining the primitive crystal structure and degrees of freedom (DoF) (the ["prim"][Prim]), initializing a CASM project, and checking [prim] symmetry.

The tutorial includes examples setting up three types of CASM projects:
- an occupation cluster expansion
- a strain polynomial effective Hamiltonian
- a coupled strain-displacement cluster expansion effective Hamiltonian.

- CLI: [view online]({{ "/_tutorials/Project_Initialization_bash" | relative_url }}), [download]({{ "/_tutorials/Project_Initialization_bash.ipynb" | relative_url}})
- Python: [view online]({{ "/_tutorials/Project_Initialization.html" | relative_url}}), [download]({{ "/_tutorials/Project_Initialization.ipynb" | relative_url}})


## Enumerating configurations

These tutorials provide an introduction to supercells and configurations and demonstrate several methods to enumerate them, depending on the type of DoF.

### Introduction to configurations and supercells, including supercell enumeration
- CLI: [view online]({{ "/_tutorials/Supercell_Enumeration_bash.html" | relative_url}}), [download]({{ "/_tutorials/Supercell_Enumeration_bash.ipynb" | relative_url}})
