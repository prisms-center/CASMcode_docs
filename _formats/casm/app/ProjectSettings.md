---
title: "Project Settings"
permalink: /formats/casm/app/ProjectSettings/
---

### Description

Holds CASM project settings.

It is recommended to modify settings using the `casm settings` command.


#### Project files

This format is used for the [`project_settings.json`] file, which is generated when a project is initialized with `casm init`.


### JSON Attributes List

Project Settings attributes:

| Name | Description | Format |
|-|-|-|
| [`cluster_expansions`](#cluster-expansions) | Named cluster expansions | dict |
| [`crystallography_tol`](#crystallography-tol) | Tolerance used for crystallographic comparisons | number |
| [`default_clex`](#default-clex) | Name of the default cluster expansion | string |
| [`lin_alg_tol`](#lin-alg-tol) | Tolerance used for linear algebra | number |
| [`name`](#name) | Project name / title | string |
| [`nlist_sublat_indices`](#nlist-sublat-indices) | Indices of sublattices included in the neighbor list | array of int |
| [`nlist_weight_matrix`](#nlist-weight-matrix) | Matrix used to determine the order of unit cells in the neighbor list | 2d array of int |
| [`query_alias`](#query-alias) | Stores `casm query` aliases | dict |
| [`required_properties`](#required-properties) | List of properties required for a particular `<calctype>` calculation to be complete | dict |
| [`view_command`](#view-command) | Command to support viewing POSCAR representations of configurations | string |


### JSON Attributes Description

#### Project Settings JSON Object

- {: #cluster-expansions } `cluster_expansions`: dict

  Named cluster expansions. The named cluster expansions make it easier to select the choice of basis set, calculation settings, reference, and ECI fit used to predict a particular property, and to switch and compare among multiple possible choices stored in a single CASM project.

  A single cluster expansion includes the choice of values for `<property>`, `<calctyp>`, `<ref>`, `<bset>`, and `<eci>` used to read data from [project directories].

  <div>
  **Example:**

      "cluster_expansions" : {
        "formation_energy" : {
          "bset" : "default",
          "calctype" : "default",
          "eci" : "default",
          "name" : "formation_energy",
          "property" : "formation_energy",
          "ref" : "default"
        },
        "formation_energy_lda" : {
          "bset" : "default",
          "calctype" : "lda",
          "eci" : "default",
          "name" : "formation_energy",
          "property" : "formation_energy",
          "ref" : "default"
        }
      }

  </div>
  {: .notice--info }

- {: #crystallography-tol } `crystallography_tol`: number (optional, `default=1e-5`)

  Tolerance used for crystallographic comparisons.

- {: #default-clex } `default_clex`: string (optional)

  Name of the default cluster expansion to use when not otherwise specified. A key in [`cluster_expansions`](#cluster-expansions). If not present, `"formation_energy"` is used. If that is also not present, then the first found is used.

- {: #lin-alg-tol } `lin_alg_tol`: number (optional, `default=1e-10`)

   Tolerance used by some methods when a stricter tolerance is needed for linear algebra, such as identifying the rank of a space.

- {: #name } `name`: string

  Project name. Typically read from "title" in [prim.json] when a project is initialized.

- {: #nlist-sublat-indices } `nlist_sublat_indices`: array of int

  Indices of sublattices included in the neighbor list. Typically determined from the [prim] and does not need to be modified. If for some reason it is modified, all basis set source code must be re-generated using `casm bset -uf`.

- {: #nlist-weight-matrix } `nlist_weight_matrix`: 2d array of int

  Used in determining the order of unit cels in the neighbor list. The default value is determined from the [prim] lattice vectors. Typically does not need to be modified. If for some reason it is modified, all basis set source code must be re-generated using `casm bset -uf`.

- {: #query-alias } `query_alias`: dict

  Stores `casm query` aliases.

  <div>
  **Example:**

      "query_alias" : {
        "Configuration" : {
          "is_dilute_O" : "and(lt(comp_n(O),0.01001),gt(comp_n(O),0.00001))",
        },
        "Supercell" : {
          "is_vol_4" : "eq(scel_size,4)"
        }
      }

  </div>
  {: .notice--info }

- {: #required-properties } `required_properties`: dict

  List of properties required for a particular `<calctype>` calculation to be complete.

  <div>
  **Example:**

      "required_properties" : {
        "Configuration" : {
          "default" : [ "energy" ],
          "lda": [ "energy" ]
        }
      }

  </div>
  {: .notice--info }

- {: #view-command } `view_command`: string

  Command to support viewing POSCAR representations of configurations directly from the `casm view` command.

  <div>
  **Example:** On Mac OSX, the following command uses the `casm.view` script installed by `casm-python` to view POSCAR representations of configurations in VESTA.

      "view_command" : "casm.view \"open -a /Applications/VESTA/VESTA.app\""

  </div>
  {: .notice--info }


[project directories]: {{ "/formats/project_directory_structure" | relative_url }}
{% include file_formats_and_locations.md %}
