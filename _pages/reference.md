---
title: ""
permalink: /pages/reference/
classes: wide
toc: false
---

<img alt="Shows the CASM logo" src="{{ "/assets/images/logo.svg" | relative_url }}" width="600" />

## CASM file formats

These are quick links to descriptions of the most commonly used CASM project input and output files.

**Note:** A complete description of the CASM project directory structure with file locations is available [here]({{ "/formats/project_directory_structure" | relative_url }}).
{: .notice--info}

| Name | Description | Format |
|-|-|-|
| `basis.json` | Basis set information | [Basis Set] |
| `bspecs.json` | Basis set specifications | [Basis Set Specs] |
| `chemical_reference.json` | Chemical reference states | [Chemical Reference] |
| `clust.json` | Cluster orbits information | [Cluster Orbits] |
| `composition_axes.json` | Composition axes definitions | [Composition Axes] |
| `config.json` | Configuration DoF values | [Configuration] |
| `crystal_point_group.json` | Crystal point group information | [Symmetry Group] |
| `dof_space_<dof_type>.json` | DoF-space analysis information | [DoF Space] |
| `eci.json` | Basis set with effective cluster interaction (ECI) values | [Basis Set] |
| `factor_group.json` | Prim factor group information | [Symmetry Group] |
| `lattice_point_group.json` | Lattice point group information | [Symmetry Group] |
| `prim.json` | Primitive crystal structure and allowed degrees of freedom (DoF) | [Prim] |
| `project_settings.json` | Project settings | [Project Settings] |
| `properties.calc.json` | Structure information with calculated properties |  [Structure] |
| `structure.json`  | Structure information | [Structure] |


## Additional documentation links

- [CASM project directory structure]({{ "/formats/project_directory_structure" | relative_url }})
- [JSON data formats]({{ "/formats/json_data_formats" | relative_url }})
- [Degrees of freedom (DoF) and properties]({{ "/formats/dof_and_properties/" | relative_url }})
- [Lattice canonical form]({{ "/formats/lattice_canonical_form" |  relative_url }})


### CASM Python packages

- [CASM v1 Packages Overview](https://prisms-center.github.io/CASMcode_pydocs/overview/1.0/)


## CASM v2+ transition

For CASM v2+, the large existing distributions [CASMcode](https://github.com/prisms-center/CASMcode) (for C++ code) and [CASMpython](https://github.com/prisms-center/CASMpython) (for Python code) are split into smaller distributions focused on particular topics. They are organized into two namespaces: `libcasm`, for packages that include C++ implementations, and `casm`, for pure Python packages.

Python [namespace packages](https://packaging.python.org/en/latest/guides/packaging-namespace-packages/) allow distributing subpackages seperately so a project may be split into smaller more focused efforts. For example, the CASM structure mapping package (libcasm.mapping) and the CASM cluster expansion Monte Carlo package (libcasm.clexmonte) can be developed and distributed separately. Each distribution package installs one or more Python namespace packages into the particular namespace.

- [CASM v2+ Packages Overview](https://prisms-center.github.io/CASMcode_pydocs/overview/latest/)
- [Contributing to libcasm packages]({{ "/pages/contributing_to_libcasm_packages/" | relative_url }})
- [Contributing to casm packages]({{ "/pages/contributing_to_casm_packages/" | relative_url }})

{% include file_formats_and_locations.md %}
