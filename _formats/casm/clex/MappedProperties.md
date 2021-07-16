---
title: "Mapped Properties"
permalink: /formats/casm/clex/MappedProperties/
---

### Description

Holds the values of [properties] that have been mapped to a particular [Configuration].

### JSON Attributes List

Mapped Properties attributes:

| Name | Description | Format |
|-|-|-|
| [`init`](#init) | The name of the configuration calculated to generate these properties  | string |
| [`global`](#global) | Global property values | dict of array of number |
| [`origin`](#origin) | Source of the properties | string |
| [`path`](#path) | Path to properties file | string |
| [`site`](#site) | Site property values | dict of 2d array of number |
| [`timestamp`](#timestamp) | Last properties file read time | int |
| [`to`](#to) | The name of the configuration these properties have been mapped to| string |

### JSON Attributes Description

#### MappedProperties JSON object

- {: #init } `init`: string

  A string used to indicate the configuration that was calculated to generate these properties.

  Typically, it is the name of the configuration which was used to generate the initial structure input to a calculation.

  The string `"import"` may be used when the properties are imported from outside a CASM project and no initial ideal configuration is known.

- {: #global } `global`: dict of array of number

  A map of property name to value for global properties of the configuration such as energy, strain metrics, or cost functions. Property names must follow CASM [property naming conventions]. Properties are expected to be vectors expressed in the [standard basis].

  **Note:** This also holds derived properties such as structure mapping costs ("lattice_deformation_cost", "atomic_deformation_cost", "total_cost").
  {: .notice--info}

- {: #origin } `origin`: string

  A string indicating the source of the properties and used as a unique key to access the properties. Most commonly it is the path to the file the properties were generated from.

- {: #path } `path`: string

  Path to the file the properties were generated from, if one exists.

- {: #site } `site`: dict of 2d array of number

  A map of property name to value for site properties of the configuration such as displacement. Property names must follow CASM [property naming conventions]. Each column corresponds to the vector property at a particular site (in the same order as the configuration [`occ`](#occ) values). Property values are expected to be expressed in the [standard basis].

- {: #timestamp } `timestamp`: int

  Indicates the last time the properties file located at `path` was read (if one exists).

- {: #to } `to`: string

  A string giving the name of the configuration these properties have been mapped to. It must be a configuration name.


[properties]: {{ "/formats/dof_and_properties#properties-list" |  relative_url }}
[property naming conventions]:  {{ "/formats/dof_and_properties#property-naming" |  relative_url }}
[standard basis]:  {{ "/formats/casm/crystallography/BasicStructure#dof-list" |  relative_url }}
[prim basis]:  {{ "/formats/casm/crystallography/BasicStructure#user-specified-dof-basis" |  relative_url }}

{% include file_formats_and_locations.md %}
