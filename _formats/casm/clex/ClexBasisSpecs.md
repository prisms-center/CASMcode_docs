---
title: "Basis Set Specs"
permalink: /formats/casm/clex/ClexBasisSpecs/
---

### Description

A cluster expansion basis set is specified by two components, one specifying basis function type and order, and one specifying cluster orbits.


#### Project files

This format is used for the [`bspecs.json`] file.


### JSON Attributes List

ClexBasisSpecs attributes:

| Name | Description | Format |
|-|-|-|
| [`basis_function_specs`](#basis-function-specs) | Basis function specifications | [Basis Function Specs] |
| [`cluster_specs`](#cluster-specs) | Cluster orbit specifications | [Cluster Specs] |

### JSON Attributes Description

- {: #basis-function-specs } `basis_function_specs`: [Basis Function Specs] (required)

  Specifies the type and order of basis functions. See the [Basis Function Specs] JSON input format.

- {: #cluster-specs } `cluster_specs`:  [Cluster Specs] (required)

  Specifies the cluster orbits on which basis functions are generated. See the [Cluster Specs] JSON input format.


### Examples

#### Example 1) Periodic cluster expansion
```
{
  "basis_function_specs" : {
    "global_max_poly_order": 3,
    "dof_specs": {
      "occ": {
        "site_basis_functions" : "occupation"
      }
    }
  },
  "cluster_specs": {
    "method": "periodic_max_length",
    "params": {
      "orbit_branch_specs": {
        "2" : {"max_length" : 6.},
	      "3" : {"max_length" : 3.}
      }
    }
  }
}
```

#### Example 2) Local cluster expansion
```
{
  "basis_function_specs" : {
    "dof_specs": {
      "occ": {
        "site_basis_functions" : "occupation"
      }
    }
  },
  "cluster_specs": {
    "method": "local_max_length",
    "params": {
      "phenomenal": {
        "coordinate_mode": "Integral",
        "sites": [
          [ 1, 0, 0, 0 ],
          [ 0, 1, 0, 0 ]
        ]
      },
      "generating_group": [ 0, 7, 11, 17, 18, 19, 26, 27, 28, 33, 37, 47 ],
      "orbit_branch_specs": {
        "1" : {"cutoff_radius": 6.},
        "2" : {"cutoff_radius": 3., "max_length" : 3.}
      }
    }
  }
}
```

{% include file_formats_and_locations.md %}
