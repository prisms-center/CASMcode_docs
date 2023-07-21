---
title: ""
permalink: /pages/tutorials/
---

<img alt="Shows the CASM logo" src="{{ "/assets/images/logo.svg" | relative_url }}" width="600" />

This section provides links to CASM tutorials written using [Jupyter](https://jupyter.org) notebooks. Some tutorials are written to demonstrate using the CASM command line interface (CLI) `ccasm` and some are written to demonstrate using the CASM Python package `casm-python`. Notebooks can be downloaded and run locally to try using CASM and static versions showing results can be viewed online.

To setup a conda environment with all the dependencies necessary for running the tutorials, see [this]({{ "/pages/tutorials/tutorial_env" | relative_url }}) page.

## Defining the "prim"

This tutorial demonstrates defining the primitive crystal structure and degrees of freedom (DoF) (the ["prim"][Prim]), initializing a CASM project, and checking [prim] symmetry.

The tutorial includes examples defining a prim for three types of CASM projects:
- an configurational cluster expansion
- a strain polynomial effective Hamiltonian
- a coupled strain-displacement cluster expansion effective Hamiltonian.

- CLI: [view online]({{ "/pages/tutorials/Project_Initialization_bash/" | relative_url }}), [download]({{ "/_tutorials/Project_Initialization_bash.ipynb" | relative_url}})


## Enumerating configurations

These tutorials provide an introduction to supercells and configurations and demonstrate several methods to enumerate them, depending on the type of DoF.

### Enumerating, Selecting, and Querying Supercells

- CLI: [view online]({{ "/pages/tutorials/Supercell_Enumeration_bash/" | relative_url}}), [download]({{ "/_tutorials/Supercell_Enumeration_bash.ipynb" | relative_url}})

### Viewing Configurations With `casm view` and VESTA

- Python: [view online]({{ "/pages/tutorials/Viewing_Configurations_With_VESTA/" | relative_url}}), [download]({{ "/_tutorials/Viewing_Configurations_With_VESTA.ipynb" | relative_url}})

## Constructing effective Hamiltonians

### Configurational Cluster Expansion Formulation

For an introduction the the cluster expansion see:
- [Configurational cluster expansion formulation]({{ "/pages/tutorials/Occupation_Cluster_Expansion/" | relative_url}})

### Occupation Basis Set Construction

- CLI: [view online]({{ "/pages/tutorials/Occupation_Basis_Set_Construction/" | relative_url}}), [download]({{ "/_tutorials/Occupation_Basis_Set_Construction.ipynb" | relative_url}})

## Phase diagram construction example

- [PRISMS Workshop 2021 example](https://raw.githubusercontent.com/prisms-center/CASMcode_tutorials/main/v1.2/projects/ZrO.tgz)

{% include file_formats_and_locations.md %}
