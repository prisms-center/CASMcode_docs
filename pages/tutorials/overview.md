---
layout: default
---

[![CASM Logo]({{ site.baseurl }}/assets/logo.png)](https://prisms-center.github.io/CASMcode_docs/)

***
## [CASM Tutorials]({{ site.baseurl }}/pages/tutorials.html) - CASM Overview

CASM is designed to perform first-principles based statistical mechanical studies of multi-
component crystalline solids. A typical workflow involves the following steps:

1. [Define the primitive crystal structure and create a CASM project.]({{ site.baseurl }}/pages/tutorials/init.html)

    - The primitive crystal structure includes: lattice vectors, basis site coordinates, and allowed degrees of freedom, which can either be global (associated with the entire crystal) or local (associated with a crystal site).
    - A CASM project consists of a primitive crystal structure and all the generated data related to that primitive crystal structure. It is stored in a directory heirarchy.
    - The primitive crystal structure is defined in a `` `prim.json` `` file in the CASM project directory.
    - CASM project sub-directories are used to store symmetry information, first-principles calculation input files and results, input files for specifying expansion basis sets, files used for fitting and storing expansion coefficients, Monte Carlo results, and other data.
    - Project files that the user should not typically modify directly are stored in a hidden `` `.casm` `` sub-directory of the CASM project directory.

2. Enumerate supercells and configurations.

    - Every configuration (a crystal state consistent with the primitive crystal structure) can be represented by specifying the supercell vectors used to repeat a unit cell into the infinite crystal, the value of the degrees of freedom at sites within that unit cell, and the value of any global degrees of freedom, such as strain.
    - Symmetrically unique supercells are typically enumerated first, and then configurations are enumerated within each supercell.

3. Calculate properties of the configurations.

    - Python wrappers allow CASM to interact with VASP, Quantum Espresso, and other first-principles software to setup input files, run calculations interactively or sumbit jobs on a cluster, handle errors, and parse output files.
    - Calculations in a CASM project are organized by named "calctype" so that configuration properties calculated using different methods (i.e. GGA+U vs HSE, or fixed vs relaxed lattice vectors) and expansion coefficients fit to that data can be systematically managed.

4. Generate a basis set that allows for the parameterization of configuration properties in terms of the value of degrees of freedom allowed by the primitive crystal structure.

    - A cluster expansion is an expansion of configuration properties in term of functions of the value of degrees of freedom on clusters of crystal sites. The set of clusters which are symmetrically equivalent is called an "orbit" of clusters, and the set of symmetrically equivalent basis functions is called an "orbit" of basis functions. The coefficients for all basis functions in an orbit are required by symmetry to have the same value.
    - Due to translational symmetry, the cluster expansion can be written in terms of "correlations", the per unit cell average value of each orbit of basis functions. Each configuration has a vector of correlations, which is symmetry invariant.
    - If the physics determining the value of a property is dominated by short-range interactions, the cluster expansion can be safely truncated based on the number of sites in a cluster and distance between sites.
    - Basis sets in a CASM project are organized by name so that multiple can be generated and evaluated in a single CASM project.

5. Fit expansion coefficients to the calculated configuration properties as a function of the evaluated basis functions.

    - Expansion coefficients, `b`, also called "effective cluster interactions" (ECI) when defined on a per-cluster basis, can be determined by solving `X*b=y`, where `X` is a row matrix of correlations, and `y` is a column vector of intensive properties (i.e. formation energy per unit cell) of the corresponding configuration.
    - CASM enables the use of a wide variety of fitting methods by:

        - Integrating with scikit-learn, a widely used Python package for machine learning
        - Including a genetic algorithm implementation
        - Allowing for easy implementation of custom fitting algorithms

    - Multiple sets of expansion coefficients can be stored in a CASM project in order to compare predictions, and investigate differences due to choice of calculation method, basis set, fitting procedure, or other factors. A cluster expansion ("clex") is described by the property being parameterized ("property"), the choice of calculation method ("calctype"), basis set ("bset"), and reference states ("ref", if applicable), and the particular set of coefficients ("eci").

6. Use the expansion to predict properties.

    - Once an expansion is constructed and fit it can be used to predict properties for other configurations and used in Monte Carlo calculations to predict finite temperature properties.

Besides the workflow outlined above, CASM can be used as a general purpose toolbox for enumerating, transforming, and comparing atomic structures.


[[Up]]({{ site.baseurl }}/pages/tutorials.html)
