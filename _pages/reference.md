---
title: ""
permalink: /pages/reference/
---

![image-center]({{ "/assets/images/logo.png" | relative_url }})

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


## Data and code documentation links

- [CASM project directory structure]({{ "/formats/project_directory_structure" | relative_url }})
- [JSON data formats]({{ "/formats/json_data_formats" | relative_url }})
- [Degrees of freedom (DoF) and properties]({{ "/formats/dof_and_properties/" | relative_url }})
- [Lattice canonical form]({{ "/formats/lattice_canonical_form" |  relative_url }})
- C++ library documentation [[v1.X]](https://prisms-center.github.io/CASMcode_cppdocs/latest/modules.html) [[v0.3]](https://prisms-center.github.io/CASMcode_cppdocs/0.3/modules.html)
- Python package documentation [[v1.X]](https://prisms-center.github.io/CASMcode_pydocs/latest/index.html) [[v0.3]](https://prisms-center.github.io/CASMcode_pydocs/0.3/index.html)


{% include file_formats_and_locations.md %}
