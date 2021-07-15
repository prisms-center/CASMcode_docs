---
title: "Degrees of Freedom (DoF) and Properties"
permalink: /formats/dof_and_properties/
---

### Overview

CASM distinguishes between degrees of freedom (DoF), which are independent variables, and properties, which are dependent variables.

Whether a particular type of value is a degree of freedom or a property varies depending on the context.

<div>
**Example:**
- When constructing a phonon Hamiltonian, atomic displacements are DoF.
- When constructing an effective Hamiltonian that is a function of occupation only, atomic displacements are a property that is calculated.
</div>
{: .notice--info}

In some cases, it is useful to treat some values of the same type as degrees of freedom.

**Example:** A system with some high mass elements with atomic displacements treated as DoF, and some low mass elements with atomic displacements treated as properties dependent on the location of the high mass atoms
{: .notice--info}

In general, both DoF and properties may be anisotropic values, and the type of value determines how the value transforms under application of symmetry.

<div>
**Example:**
- Cartesian coordinates, displacements, and lattice vectors all transform by applying the Cartesian matrix of a symmetry operation to the value being transformed.
- Other types of values, such as strain and magnetic moments, require different symmetry representations.
</div>
{: .notice--info}

In CASM, all types of values are represented using vectors, and symmetry representations take the form of permutations or transformation matrices.


### Naming conventions

A particular instance of a DoF or property is labeled with a name string.


#### DoF Naming

DoF must use an exact name.

DoF name strings are used in:
- [BasicStructure] (the "prim")
- [Configuration]


#### Property Naming

Property name strings must end with the type name (i.e. `"disp"`, `"Ustrain"`, `"energy"`, etc.) and may also include a modifier describing the particular property (i.e. `"formation"` in `"formation_energy"`).

If a modifier exists, it must be separated from the type name by an underscore character (`_`). The name of a new type may not include an underscore.

Thus, whenever a particular property name is encountered, the property type can be determined and used to lookup the traits information needed to act on the property values.

<div>
**Examples:**
- instance name: `"energy"` -> type name: `"energy"`
- instance name: `"relaxed_energy"` -> type name: `"energy"`
- instance name: `"formation_energy"` -> type name: `"energy"`
- instance name: `"relaxedenergy"` -> Error (because there is no underscore)
- instance name: `"Ustrain"` -> AnisoValTraits type name:  `"Ustrain"`
- instance name: `"strain"` ->  Error (because there no strain metric)
</div>
{: .notice--info}

Property name strings are used in:
- [SimpleStructure]
- [MappedProperties]


### Properties list

Standard property types included in CASM:

{% include properties_list.md %}


### DoF list

Standard DoF types included in CASM:

{% include dof_list.md %}


### Implementation

**Note:** This is an topic for developers. Please contact the CASM developers for additional information.
{: .notice--warning}


#### Implementing new properties

CASM implements a traits system, using the [AnisoValTraits] class, in which the value type name, as a string (i.e. `"energy"` for energy, `"disp"` for displacement, `"occ"` for occupation value), is used to lookup traits or methods that customize how a particular type is treated. This allows CASM to implement very general methods and provides for extensibility to new types of DoF and properties. Methods which work for a subset of value types are given the responsibility of checking their applicability and handling exceptions. Examples of supported value types and traits are given.

See implementations of [AnisoValTraits] instances for examples. To become a standard AnisoValTraits type, an instance must be added to the [AnisoValTraits parsing dictionary].


#### Implementing new DoF

In order to implement a new DoF type, CASM must know how to convert between Configuration and SimpleStructure, and must know how to construct, write, and evaluate basis functions for that type. This requires an [AnisoValTraits] instance for the type and also that additional traits information must be provided by implementing a traits class derived from [DoFType::Traits].

Current DoF implementations include:
- [DisplacementDoFTraits] (`"disp"`)
- [OccupationDoFTraits] (`"occ"`)
- [MagSpinDoFTraits] (`"Cmagspin"`, `"Cunitmagspin"`, `"NCmagspin"`, `"NCunitmagspin"`, `"SOmagspin"`, `"SOunitmagspin"`)
- [StrainDoFTraits] (`"EAstrain"`, `"Hstrain"`, `"GLstrain"`)

After a DoF traits class is implemented, it must be added it to the [DoF traits parsing dictionary], which is accessed via [DoFType::traits_dict()].

[AnisoValTraits]: https://prisms-center.github.io/CASMcode_cppdocs/latest/class_c_a_s_m_1_1_aniso_val_traits.html
[AnisoValTraits parsing dictionary]: https://prisms-center.github.io/CASMcode_cppdocs/latest/namespace_c_a_s_m.html#a41ba764cb5d20f103a5d7488f330dfed
[BasicStructure]: ({{ "/formats/casm/crystallography/BasicStructure" |  relative_url }})
[Configuration]: ({{ "/formats/casm/crystallography/Configuration" |  relative_url }})
[DisplacementDoFTraits]: https://prisms-center.github.io/CASMcode_cppdocs/latest/class_c_a_s_m_1_1_do_f__impl_1_1_displacement_do_f_traits.html
[DoF traits parsing dictionary]: https://prisms-center.github.io/CASMcode_cppdocs/latest/namespace_c_a_s_m.html#ac98d0bd522cf85dc66a6a7fb332b161c
[DoFType::traits_dict()]: https://prisms-center.github.io/CASMcode_cppdocs/latest/namespace_c_a_s_m_1_1_do_f_type.html#a64cd4554c24561f4ef8f20d72b814fe6
[OccupationDoFTraits]: https://prisms-center.github.io/CASMcode_cppdocs/latest/class_c_a_s_m_1_1_do_f__impl_1_1_occupation_do_f_traits.html
[MagSpinDoFTraits]: https://prisms-center.github.io/CASMcode_cppdocs/latest/class_c_a_s_m_1_1_do_f__impl_1_1_mag_spin_do_f_traits.html
[MappedProperties]: ({{ "/formats/casm/clex/MappedProperties" |  relative_url }})
[SimpleStructure]: ({{ "/formats/casm/crystallography/SimpleStructure" |  relative_url }})
[StrainDoFTraits]: https://prisms-center.github.io/CASMcode_cppdocs/latest/class_c_a_s_m_1_1_do_f__impl_1_1_strain_do_f_traits.html
