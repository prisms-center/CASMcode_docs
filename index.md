---
layout: default
---
CASM is an open source software package designed to perform first-principles statistical mechanical studies of multi-component crystalline solids. CASM interfaces with first-principles electronic structure codes, automates the construction and parameterization of effective Hamiltonians and subsequently builds highly optimized (kinetic) Monte Carlo codes to predict finite-temperature thermodynamic and kinetic properties. CASM uses group theoretic techniques that take full advantage of crystal symmetry in order to rigorously construct effective Hamiltonians for almost arbitrary degrees of freedom in crystalline solids. This includes cluster expansions for configurational disorder in multi-component solids and lattice-dynamical effective Hamiltonians for vibrational degrees of freedom involved in structural phase transitions.

The public version of CASM supports:

- Constructing, fitting, and evaluating cluster expansion effective Hamiltonians with:
  - Occupational degrees of freedom
  - Strain degrees of freedom
  - Displacement degrees of freedom
- High-throughput calculations using:
  - [VASP](https://www.vasp.at)  
  - [Quantum Espresso](https://www.quantum-espresso.org/)
- Occupantional cluster expansion Monte Carlo calculations using:
  - Semi-grand canonical ensemble
  - Canonical ensemble

### Acknowledgements

CASM is developed by the [Van der Ven group](https://labs.materials.ucsb.edu/vanderven/anton/), originally at the University of Michigan and currently at the University of California Santa Barbara.

- **Lead developers**:  John C. Thomas and Brian Puchala
- **Developers**:  John Goiri and Anirudh Natarajan
- **Other contributors**: Min-Hua Chen, Jonathon Bechtel, Max Radin, Elizabeth Decolvenaere, Anna Belak, Liang Tian, Naga Sri Harsha Gunda, Julija Vinckeviciute, Sanjeev Kolli, and Sesha Sai Behara.

The development of CASM was made possible with support from:
- The U.S. Department of Energy, Office of Basic Energy Sciences, Division of Materials Sciences and Engineering under Award #DE-SC0008637 that funds the PRedictive Integrated Structural Materials Science (PRISMS) Center at University of Michigan.
- The National Science Foundation under Awards DMR-1410242, DMR-1105672, DMR-1436154, and OAC-1642433.

### License

CASM is released under the GNU Lesser General Public License (LGPL).

***
## Announcements
- 3/23/2021: CASM 1.1.0 is available from the prisms-center conda channel

***
## Using CASM
- [Overview](pages/overview.md)
- [Installation](pages/installation.md)
- [Tutorials](pages/tutorials.md)
- [Formats reference](pages/formats.md)
- [Citing CASM and algorithms](pages/citing.md)

***
## Getting Help
- [Email the developers](mailto:casm-developers@lists.engr.ucsb.edu)
- [Join the announcements mailing list](https://lists.engr.ucsb.edu/mailman/listinfo/casm-users)
- [Request features or report bugs](https://github.com/prisms-center/CASMcode/issues)
- C++ library documentation [[v1.X]](https://prisms-center.github.io/CASMcode_cppdocs/latest/modules.html) [[v0.3]](https://prisms-center.github.io/CASMcode_cppdocs/0.3/modules.html)
- Python package documentation [[v1.X]](https://prisms-center.github.io/CASMcode_pydocs/latest/index.html) [[v0.3]](https://prisms-center.github.io/CASMcode_pydocs/0.3/index.html)
- [Learn how to contribute](pages/contributing.md)

***
## Links
- [PRISMS Center homepage](http://www.prisms-center.org/#/home)
- [Code repository](https://github.com/prisms-center/CASMcode)
- [casm-python repository](https://github.com/prisms-center/CASMpython)
- [Demonstrations repository (0.3)](https://github.com/prisms-center/CASMcode_demo)
