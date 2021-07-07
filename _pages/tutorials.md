---
title: ""
permalink: /pages/tutorials/
---

![image-center]({{ "/assets/images/logo.png" | relative_url }})

# Tutorials

This section provides links to CASM tutorials written using Jupyter notebooks. Some tutorials are written to demonstrate using the CASM command line interface (CLI) `ccasm` and some are written to demonstrate using the CASM Python package `casm-python`. Notebooks can be downloaded and run locally to try using CASM and static versions showing results can be viewed online.

To setup a conda environment with all the dependencies necessary for running the tutorials, see [this]({{ "/tutorials/tutorial_env" | relative_url }}) page.

## Defining the "prim"

These tutorials demonstrate defining the "prim", primitive crystal structure and degrees of freedom (DoF), initializing a CASM project, and checking prim symmetry. The tutorial include examples setting up three types of CASM projects: an occupation cluster expansion, a strain polynomial effective Hamiltonian, and a coupled strain-displacement cluster expansion effective Hamiltonian.

- CLI: [view online]({{ "/_tutorials/Project_Initialization_bash" | relative_url }}), [download]({{ "/_tutorials/Project_Initialization_bash.ipynb" | relative_url}})
- Python: [view online]({{ "/_tutorials/Project_Initialization.html" | relative_url}}), [download]({{ "/_tutorials/Project_Initialization.ipynb" | relative_url}})

## Symmetry analysis


## Basis set construction

Given an initialized CASM project, an effective Hamiltonian basis set can be constructed by specifying parameters that depend on the types of DoF. For local DoF such as occupation and displacement, the clusters that should be included in the cluster basis functions must be specified. For continuous site and global DoF, the order of polynomials to be generated must be specified. Some types of DoF also need additional information, such as the type of site basis functions to be used for an occupation cluster expansion. These tutorials demonstrate specifying all the parameters necessary, constructing the basis set, and inspecting the results.

### Occupation cluster expansion effective Hamiltonian

- CLI: [... coming soon ...]

### Strain polynomial effective Hamiltonian
- CLI: [... coming soon ...]

### Coupled strain-displacement cluster expansion effective Hamiltonian
- CLI: [... coming soon ...]


## Enumerating configurations

These tutorials provide an introduction to supercells and configurations and demonstrate several methods to enumerate them, depending on the type of DoF.

### Introduction to configurations and supercells, including supercell enumeration
- CLI: [view online]({{ "/tutorials/Supercell_Enumeration_bash.html" | relative_url}}), [download]({{ "/tutorials/Supercell_Enumeration_bash.ipynb" | relative_url}})

### Occupation configuration enumeration
- [... coming soon ...]

### Strain configuration enumeration
- [... coming soon ...]

### Displacement configuration enumeration
- [... coming soon ...]


## Defining order parameters


## Calculating properties


## Mapping structures to configurations


## Fitting basis function coefficients


## Evaluating effective Hamiltonians


## Monte Carlo calculations
