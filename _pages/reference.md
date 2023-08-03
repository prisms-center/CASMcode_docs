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


## CASM data JSON formats

These are quick links to descriptions of the JSON format for CASM object serialization.

|  Format | Description |Python class | C++ class (v2) |
|-|-|-|-|
| [Prim] | Parent crystal structure and allowed degrees of freedom (DoF) | libcasm.xtal.Prim | CASM::xtal::BasicStructure |
| [Structure] | Crystal structure and properties | libcasm.xtal.Structure | CASM::xtal::SimpleStructure |
| [Symmetry Operation Info] | Symmetry operation information | libcasm.xtal.SymInfo | CASM::xtal::SymInfo |
| [Supercell] | Supercell of a Prim | libcasm.configuration.Supercell | CASM::config::Supercell |
| [Configuration] | Supercell and DoF values | libcasm.configuration.Configuration | CASM::config::Configuration |

## Additional documentation links

- [CASM project directory structure]({{ "/formats/project_directory_structure" | relative_url }})
- [JSON data formats]({{ "/formats/json_data_formats" | relative_url }})
- [Degrees of freedom (DoF) and properties]({{ "/formats/dof_and_properties/" | relative_url }})
- [Lattice canonical form]({{ "/formats/lattice_canonical_form" |  relative_url }})


## CASM v1

- C++ library documentation [[v1.X]](https://prisms-center.github.io/CASMcode_cppdocs/latest/modules.html) [[v0.3]](https://prisms-center.github.io/CASMcode_cppdocs/0.3/modules.html)
- ``casm`` Python package documentation [[v1.X]](https://prisms-center.github.io/CASMcode_pydocs/latest/index.html) [[v0.3]](https://prisms-center.github.io/CASMcode_pydocs/0.3/index.html)


## CASM v2+

For CASM v2+, the large existing distributions [CASMcode](https://github.com/prisms-center/CASMcode) (for C++ code) and [CASMpython](https://github.com/prisms-center/CASMpython) are split into smaller distributions focused on particular topics. They are organized into two namespaces: `libcasm`, for packages that include C++ implementations, and `casm`, for pure Python packages.

Python [namespace packages](https://packaging.python.org/en/latest/guides/packaging-namespace-packages/) allow distributing subpackages seperately so a project may be split into smaller more focused efforts. For example, the CASM structure mapping package (libcasm.mapping) and the CASM cluster expansion Monte Carlo package (libcasm.clexmonte) can be developed and distributed separately. Each distribution package installs one or more Python namespace packages into the particular namespace.

### `libcasm` Packages

The `libcasm` distribution packages (i.e. libcasm-global, libcasm-xtal, etc.) are used to distribute a set of related CASM Python subpackages that rely in some part on a C++ implementation.
- [libcasm Packages Overview]({{ "/pages/libcasm_packages_overview/" | relative_url }})
- [Contributing to libcasm packages]({{ "/pages/contributing_to_libcasm_packages/" | relative_url }})


### `casm` Packages

The `casm` distribution packages (i.e. casm-project, casm-learn, etc.) are used to distribute related CASM Pure Python subpackages.
- [casm Packages Overview]({{ "/pages/casm_packages_overview/" | relative_url }})
- [Contributing to casm packages]({{ "/pages/contributing_to_casm_packages/" | relative_url }})

{% include file_formats_and_locations.md %}
