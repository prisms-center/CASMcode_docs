---
title: "ClexBasisSpecs (\"bspecs.json\")"
permalink: /formats/casm/clex/ClexBasisSpecs/
---

ClexBasisSpecs specifies how to construct a cluster expansion basis set. It has two components, one specifying basis function type and order, and one for specifying cluster orbits. In a CASM project it is read from `"bspecs.json"` files.

### JSON Attributes

  - `"basis_function_specs"`: [BasisFunctionSpecs]

    Specifies the type and order of basis functions. See the [BasisFunctionSpecs] JSON input format.

  - `"cluster_specs"`:  [ClusterSpecs]

    Specifies the cluster orbits on which basis functions are generated. See the [ClusterSpecs] JSON input format.

For use in a CASM project, ClexBasisSpecs is stored in a `bspecs.json` file at
```
<root>/basis_sets/<bset>/bspecs.json
```
where `<bset>` is a directory with name such as `bset.default`, `bset.occupation`, `bset.chebychev`, etc.


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

[BasisFunctionSpecs]: ../basis_set/BasisFunctionSpecs.md
[ClusterSpecs]: ../clusterography/ClusterSpecs.md
