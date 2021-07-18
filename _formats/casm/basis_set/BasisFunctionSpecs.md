---
title: "Basis Function Specs"
permalink: /formats/casm/basis_set/BasisFunctionSpecs/
---

### Description

Basis function specifications control the type and order of basis functions that CASM generates.

#### Project files

This format is used for the following standard CASM project files:
- The `basis_function_specs` attribute of [`bspecs.json`]

### JSON Attributes List

Basis Function Specs attributes:

| Name | Description | Format |
|-|-|-|
| [`dof_specs`](#dof-specs) | DoF-particular specifications | dict |
| [`dofs`](#dofs) | DoFs to include in the basis set | array of string |
| [`global_max_poly_order`](#global-max-poly-order) | Global maximum polynomial order (global) | int |
| [`orbit_branch_max_poly_order`](#orbit-branch-max-poly-order) | Orbit branch specific maximum polynomial order| dict |
| [`param_pack_type`](#param-pack-type) | Automatic differentation option | string |

`occ` DoF specifications:

| Name | Description | Format |
|-|-|-|
| [`site_basis_functions`](#occ-site-basis-functions) | Occupation site basis function choice | string or array |

`<flavor>magspin` DoF specifications:

| Name | Description | Format |
|-|-|-|
| [`max_poly_order`](#magspin-max-poly-order) | Site basis function maximum polynomial order | int |


### JSON Attributes Description

- {: #dof-specs } `dof_specs`: dict (required for some dofs)

  Provides DoF-particular specifications for constructing basis functions. Not all DoF types require their own specifications. The options are:

    For "occ": (required if occupation dof included)

    - {: #occ-site-basis-functions } `site_basis_functions`: string or array (required)

      Must be one of:

      - "chebychev": For basis functions generated about the random alloy.
      - "occupation": For basis functions generated about the ordered alloy defined by the first occupant listed for every sublattice in the [prim].
      - An array specifying sublat compositions, for "composition" basis functions generated about an average composition speficified for each sublattice.

        Example sublattice composition specification, for a [prim] with four sublattices and two allowed occupants ("A" and "B") on each sublattice:

            [
              { // composition on sublattices 0 and 1, as listed
              in prim
                "sublat_indices": [0, 1],
                "composition": {"A": 0.25, "B": 0.75}
              },
              { // composition on sublattices 2 and 3, as listed
              in prim
                "sublat_indices": [2, 3],
                "composition": {"A": 0.75, "B": 0.25}
              }
            ]

  For `<flavor>magspin`: (optional if `<flavor>magspin` dof included)

  - {: #magspin-max-poly-order } `max_poly_order`: int (optional, default=-1)

    Specifies the maximum polynomial order for site basis functions.

- {: #dofs } `dofs`: array of string (optional, default= all [prim] DoF)

  An array of string of dof type names that should be used to construct basis functions. The default value is all DoF types included in the [prim].

- {: #global-max-poly-order} `global_max_poly_order`: int (optional, default=-1)

  See `orbit_branch_max_poly_order` documentation.

- {: #orbit-branch-max-poly-order } `orbit_branch_max_poly_order`: dict (optional, default={})

  By default, for a given cluster orbit, polynomials of order up to the cluster size are created. Higher order polynomials can be requested either on a per-orbit-branch or global basis. The most specific level specified is used. Orbit branches are specified using the string value of the cluster size as a key.

  <div>
  **Example:**

      "orbit_branch_max_poly_order": {
          "4": 7    // use maximum polynomial order == 7,
                    // for orbits of cluster size == 4
      },
      "global_max_poly_order": 3, // use max(3, cluster size),
      ...                         // for all other orbits

  </div>
  {: .notice--info }

- {: #param-pack-type } `param_pack_type`: string (optional, default="default")

  Controls the implementation used for evaluating the cluster expansion basis functions. Options are "default" or "diff", which enables `fadbad` automatic differentiating.


### Examples

#### Example 1) "occupation" site basis functions for "occ" DoF
```
{
  "dof_specs": {
    "occ": {
      "site_basis_functions" : "occupation"
    }
  }
}
```

#### Example 2) "chebychev" site basis functions for "occ" DoF, global maximum polynomial order of 5
```
"global_max_poly_order": 5,
"dof_specs": {
  "occ": {
    "site_basis_functions" : "chebychev"
  }
}
```

{% include file_formats_and_locations.md %}
