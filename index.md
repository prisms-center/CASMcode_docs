---
layout: default
---
[![CASM Logo]({{ site.baseurl }}/assets/logo.png)](https://prisms-center.github.io/CASMcode_docs/)

***
## Overview
 CASM is an open source software package designed to perform first-principles statistical mechanical studies of multi-component crystalline solids. CASM interfaces with first-principles electronic structure codes, automates the construction and parameterization of effective Hamiltonians and subsequently builds highly optimized (kinetic) Monte Carlo codes to predict finite-temperature thermodynamic and kinetic properties. CASM uses group theoretic techniques that take full advantage of crystal symmetry in order to rigorously construct effective Hamiltonians for almost arbitrary degrees of freedom in crystalline solids. This includes cluster expansions for configurational disorder in multi-component solids and lattice-dynamical effective Hamiltonians for vibrational degrees of freedom involved in structural phase transitions.

The public version of CASM supports:

- Constructing, fitting, and evaluating cluster expansion effective Hamiltonians with:
  - Occupational degrees of freedom
- High-throughput calculations using:
  - [VASP](https://www.vasp.at)  
  - [Quantum Espresso](https://www.quantum-espresso.org/)
  - [SeqQuest](https://dft.sandia.gov/Quest/SeqQ_Home.html)
- Monte Carlo calculations using:
  - Semi-grand canonical ensemble
  - Canonical ensemble

### Acknowledgements

CASM is developed by the [Van der Ven group](https://labs.materials.ucsb.edu/vanderven/anton/), originally at the University of Michigan and currently at the University of California Santa Barbara.

- **Lead developers**:  John C. Thomas and Brian Puchala
- **Developers**:  John Goiri and Anirudh Natarajan
- **Other contributors**: Min-Hua Chen, Jonathon Bechtel, Max Radin, Elizabeth Decolvenaere, Anna Belak, Liang Tian, Naga Sri Harsha Gunda, Julija Vinckeviciute, Sanjeev Kolli

The development of CASM was made possible with support from:
- The U.S. Department of Energy, Office of Basic Energy Sciences, Division of Materials Sciences and Engineering under Award #DE-SC0008637 that funds the PRedictive Integrated Structural Materials Science (PRISMS) Center at University of Michigan.
- The National Science Foundation under Awards DMR-1410242, DMR-1105672 and DMR-1436154.

### License

CASM is released under the GNU Lesser General Public License (LGPL).

***
## Announcements
- 7/27/2018: PRISMS Center will be holding its annual PRISMS Center workshop (August 6-10, 2018). PRISMS Software Training is August 6-8. [Details](http://prisms-center.org/#/community)

***
## Using CASM
- [Installation]({{ site.baseurl }}/pages/installation.html)
- [Tutorials]({{ site.baseurl }}/pages/tutorials.html)
- [CASM C++ library examples]({{ site.baseurl }}/pages/casm-cpp-examples.html) {% comment %}
- [CASM Python package (TODO)]({{ site.baseurl }}/pages/casm-python-examples.html){% endcomment %}
- [Citing CASM and algorithms]({{ site.baseurl }}/pages/citing.html)

***
## How CASM Works
- [Definitions]({{ site.baseurl }}/pages/definitions.html)
- [Methods]({{ site.baseurl }}/pages/methods.html)

{% comment %}
***
## CASM Projects
- [List of CASM projects avilable online]({{ site.baseurl }}/pages/projects_list.html)
- [Upload a CASM Project]({{ site.baseurl }}/pages/upload_a_project.html)
- [Publications citing CASM]({{ site.baseurl }}/pages/publications.html)
{% endcomment %}

***
## Getting Help
- [Email the developers](mailto:casm-developers@lists.engr.ucsb.edu)
- [Join the announcements mailing list](https://lists.engr.ucsb.edu/mailman/listinfo/casm-users)
- [Request features or report bugs](https://github.com/prisms-center/CASMcode/issues)
- [C++ library documentation](https://prisms-center.github.io/CASMcode_cppdocs/latest/modules.html)
- [Python package documentation](https://prisms-center.github.io/CASMcode_pydocs/latest/)
- [Learn how to contribute]({{ site.baseurl }}/pages/contributing.html)

***
## Links
- [PRISMS Center homepage](http://www.prisms-center.org/#/home)
- [Code repository](https://github.com/prisms-center/CASMcode)
- [Demonstrations repository](https://github.com/prisms-center/CASMcode_demo)
