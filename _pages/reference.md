---
title: ""
permalink: /pages/reference/
---

![image-center]({{ "/assets/images/logo.png" | relative_url }})

# Reference

## CASM file formats

These are quick links to descriptions of the most commonly used CASM project input and output files. For a complete description of the CASM project directory structure, see [this]({{ "/pages/project_directory_structure" | relative_url }}).

| Name | Description | Format |
|-|-|-|
| [`basis.json`] | Basis set information | [ClexBasis] |
| [`bspecs.json`] | Basis set specifications | [ClexBasisSpecs] |
| `calc.json` | Calculation settings |
| `chemical_reference.json` | Chemical reference states |
| `clust.json` | Cluster orbits information |
| `composition_axes.json` | Composition axes definitions |
| [`config.json`] | Configuration DoF values | [Configuration] |
| `crystal_point_group.json` | Crystal point group information |
| `dof_space_<dof_type>.json` | DoF-space analysis information |
| [`eci.json`] | Basis set with effective cluster interaction (ECI) values | [ClexBasis] |
| `factor_group.json` | Prim factor group information |
| `lattice_point_group.json` | Lattice point group information |
| [`prim.json`] | Primitive crystal structure (prim) specifications | [BasicStructure] |
| `project_settings.json` | Project settings |
| [`properties.calc.json`] | Structure information with calculated properties |  [SimpleStructure] |
| [`structure.json`]  | Structure information | [SimpleStructure] |


## CASM methods

The descriptions of the methods shown here can also be viewed from the command line via ``casm <method> --desc``.

| Name | Description |
|-|-|
| `init` | Initialize new projects |
| `sym` | Symmetry analysis |
| etc. | etc. |

## Data and code documentation links

- CASM project directory structure [[v1.X]]({{ "/formats/project_directory_structure" | relative_url }})
- JSON data formats [[v1.X]]({{ "/formats/json_data_formats" | relative_url }})
- [Degrees of freedom (DoF) and properties]({{ "/formats/dof_and_properties/" | relative_url }})
- [Lattice canonical form]({{ "/formats/lattice_canonical_form" |  relative_url }})
- C++ library documentation [[v1.X]](https://prisms-center.github.io/CASMcode_cppdocs/latest/modules.html) [[v0.3]](https://prisms-center.github.io/CASMcode_cppdocs/0.3/modules.html)
- Python package documentation [[v1.X]](https://prisms-center.github.io/CASMcode_pydocs/latest/index.html) [[v0.3]](https://prisms-center.github.io/CASMcode_pydocs/0.3/index.html)


[ClexBasis]: {{ "/formats/casm/clex/ClexBasis" | relative_url }}
[`basis.json`]: {{ "/formats/casm/clex/ClexBasis" | relative_url }}
[`eci.json`]: {{ "/formats/casm/clex/ClexBasis" | relative_url }}
[ClexBasisSpecs]: {{ "/formats/casm/clex/ClexBasisSpecs" | relative_url }}
[`bspecs.json`]: {{ "/formats/casm/clex/ClexBasisSpecs" | relative_url }}
[BasicStructure]: {{ "/formats/casm/crystallography/BasicStructure" |  relative_url }}
[`prim.json`]: {{ "/formats/casm/crystallography/BasicStructure" |  relative_url }}
[SimpleStructure]: {{ "/formats/casm/crystallography/SimpleStructure" |  relative_url }}
[`structure.json`]: {{ "/formats/casm/crystallography/SimpleStructure" |  relative_url }}
[`properties.calc.json`]: {{ "/formats/casm/crystallography/SimpleStructure" |  relative_url }}
[Configuration]: {{ "/formats/casm/clex/Configuration/" |  relative_url }}
[`config.json`]: {{ "/formats/casm/clex/Configuration/" |  relative_url }}
