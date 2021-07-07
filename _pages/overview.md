---
title: ""
permalink: /pages/overview/
---

![image-center]({{ "/assets/images/logo.png" | relative_url }})

# Overview

CASM is designed to perform first-principles based statistical mechanical studies of multi-component crystalline solids. A typical workflow involves the following steps:

1. Defining the "prim"

    - The primitive crystal structure ("prim") is a description of a crystal which includes: lattice vectors, basis site coordinates, and allowed degrees of freedom, which can either be global (associated with the entire crystal) or local (associated with a crystal site).
    - A CASM project consists of a primitive crystal structure and data files related to that primitive crystal structure. It is stored in a directory heirarchy.
    - The primitive crystal structure is defined in a `prim.json` file in the CASM project directory.
    - CASM project sub-directories are used to store symmetry information, first-principles calculation input files and results, input files for specifying expansion basis sets, files used for fitting and storing expansion coefficients, Monte Carlo results, and other data.
    - Project files that the user should not typically modify directly are stored in a hidden `.casm` sub-directory of the CASM project directory. The presense or absence of the `.casm` directory is used by CASM to detect project directories.

2. Generating configurations

    - Every configuration (a crystal state consistent with the primitive crystal structure) can be represented by specifying the supercell vectors used to repeat a unit cell into the infinite crystal, the value of the degrees of freedom at sites within that unit cell, and the value of any global degrees of freedom, such as strain.
    - Symmetrically unique supercells may be enumerated separately from configurations. For each supercell there is an associated "default configuration" corresponding to all degrees of freedom having value zero.
    - CASM includes methods for generating configurations, such as enumerating symmetrically unique occupations, sampling values in a symmetrically unique portion of strain space, or enumerating displacements via combinations of displacement modes.
    - A CASM project includes a database of enumerated configurations, stored as a JSON file. Configurations in the database are sorted by supercell, and placed in a canonical form so that per supercell only one of all symmetrically equivalent configurations with equivalent supercell lattice is stored. Non-primitive configurations may be stored in the database.
    - CASM includes methods (`casm select` and `casm query`) to create selections of supercells or configurations, query their properties, and performs actions with them, such as use them as input to another method or generate input files for calculations.
    - CASM also includes a method (`casm import`) to import structures in VASP POSCAR format or the CASM structure format and map them to a configuration.

3. Calculating properties of the configurations

    - Configurations may be converted to VASP POSCAR format or the CASM structure format.
    - Python wrappers allow CASM to interact with VASP, Quantum Espresso, and other first-principles software to setup input files, run calculations interactively or sumbit jobs on a cluster, handle errors, and parse output files.
    - Calculations in a CASM project are organized by named "calctype" so that configuration properties calculated using different methods (i.e. GGA+U vs HSE, or fixed vs relaxed lattice vectors and atomic positions) can be stored in parallel. This allows systematic management of different types of calculations and the analyses and cluster expansion of the results.

4. Generating crystal basis functions

    - A cluster expansion is an expansion of configuration properties in term of functions of the value of crystal degrees of freedom on clusters of crystal sites. The set of clusters which are symmetrically equivalent is called an "orbit" of clusters, and the set of symmetrically equivalent basis functions is called an "orbit" of basis functions. The coefficients for all basis functions in an orbit are required by symmetry to have the same value.
    - Due to translational symmetry, the cluster expansion can be written in terms of "correlations", the per unit cell average value of each orbit of basis functions. Given a crytal basis set, each configuration has a vector of correlations, which is invariant under transformation of the configuration by symmetry operations of the `prim`.
    - If the physics determining the value of a property is dominated by short-range interactions, the cluster expansion can be safely truncated based on the number of sites in a cluster and distance between sites.
    - Basis sets in a CASM project are organized by name so that multiple can be generated and evaluated in a single CASM project.

5. Fitting expansion coefficients

    - Expansion coefficients, `b`, often called "effective cluster interactions" (ECI) when defined on a per-cluster basis, can be determined by solving `X*b=y`, where `X` is a row matrix of correlations, and `y` is a column vector of intensive properties (i.e. formation energy per unit cell) of the corresponding configuration.
    - Generating crystal basis functions results in the output of a `basis.json` file describing the cluster basis functions. CASM reads fitting coefficents, `b`, from an `eci.json` file which is a copy of the `basis.json` file with coefficent values added.
    - The `casm-learn` Python package enables fitting coefficients using methods in `scikit-learn`, a widely used Python package for machine learning. It also includes geneatic algorithm methods and construction of the `eci.json` file.
    - A user may also query correlations and properties for a set of configurations using `casm select` and `casm query`, fit coefficients, and construct the `eci.json` file in any other manner they wish.
    - Multiple sets of expansion coefficients can be stored in a CASM project in order to compare predictions, and investigate differences due to choice of calculation method, basis set, fitting procedure, or other factors. A cluster expansion ("clex") is described by the property being parameterized ("property"), the choice of calculation method ("calctype"), basis set ("bset"), and reference states ("ref", if applicable), and the particular set of coefficients ("eci").

6. Use the expansion to predict properties

    - Once an expansion is constructed and fit it can be used to predict properties for any configurations in the project database and other configurations generated by the user.
    - Occupational cluster expansions can be used in (semi-) grand canoncical and canonical Monte Carlo calculations to predict finite temperature properties.

Besides the workflow outlined above, CASM can be used as a general purpose toolbox for enumerating, transforming, and comparing atomic structures and using cluster expansions.
