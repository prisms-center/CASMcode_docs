---
title: ""
permalink: /pages/reference/
---

![image-center]({{ "/assets/images/logo.png" | relative_url }})

# Reference

## CASM project file formats

These are quick links to descriptions of the most commonly used CASM project input and output files. For a complete description of the CASM project directory structure, see [this]({{ "/pages/project_directory_structure" | relative_url }}).

- The primitive crystal structure ("prim") file, [prim.json]({{ "/formats/casm/crystallography/BasicStructure" |  relative_url }})
- The basis set specification file, [bspecs.json]({{ "/formats/casm/basis_set/BasisFunctionSpecs" | relative_url }})
- The basis set and coefficients files, [basis.json](TODO), [eci.json](TODO)
- The cluster information file, [clust.json](TODO)
- The symmetry group file, [lattice_point_group.json](TODO), [factor_group.json](TODO), [crystal_point_group.json](TODO)
- The DoF space analysis file, [`dof_space_<dof_type>.json`](TODO)
- The structure file, [structure.json](TODO), [properties.calc.json](TODO)
- The configuration DoF values file, [config.json](TODO)
- The project settings file, [project_settings.json](TODO)
- The calculation settings file, [calc.json](TODO)
- The composition axes file, [composition_axes.json](TODO)


## CLI methods

The descriptions of the methods shown here can also be viewed from the command line via ``ccasm <method> --desc``.

- [`init` - Initialize new projects]({{ "/methods/init" | relative_url }})
- [`sym` - Symmetry analysis]({{ "/methods/sym" | relative_url }})
- etc.


## Data and code documentation

- CASM project directory structure [[v1.X]]({{ "/formats/project_directory_structure" | relative_url }})
- JSON data formats [[v1.X]]({{ "/formats/json_data_formats" | relative_url }})
- C++ library documentation [[v1.X]](https://prisms-center.github.io/CASMcode_cppdocs/latest/modules.html) [[v0.3]](https://prisms-center.github.io/CASMcode_cppdocs/0.3/modules.html)
- Python package documentation [[v1.X]](https://prisms-center.github.io/CASMcode_pydocs/latest/index.html) [[v0.3]](https://prisms-center.github.io/CASMcode_pydocs/0.3/index.html)
