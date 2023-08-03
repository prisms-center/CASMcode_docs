---
title: ""
permalink: /pages/libcasm_packages_overview/
sidebar: true
toc: true
layout: single

---

<img alt="Shows the CASM logo" src="{{ "/assets/images/logo.svg" | relative_url }}" width="600" />

## Overview of libcasm Packages

For CASM v2, the libcasm distribution packages (i.e. libcasm-global, libcasm-xtal, etc.) are used to distribute a set of related CASM Python subpackages that rely in some part on a C++ implementation. The libcasm distribution packages are organized as follows:

### `libcasm-global`

Generically useful tools for CASM

- Repository: [CASMcode_global](https://github.com/prisms-center/CASMcode_global/)
- Docs: [v2.0](https://prisms-center.github.io/CASMcode_pydocs/libcasm/global/2.0/index.html)
- Includes:
  - CASM global constants and definitions
  - Input / output tools, especially for JSON parsing and formatting
  - An Eigen distribution and methods using Eigen
  - Helpers for runtime library compiling and linking
  - Miscellaneous mathematical functions
  - Other tools for C++ development
- CASM dependencies: None
- Python namespace packages:
  - `libcasm.casmglobal`: Constants and definitions
  - `libcasm.counter`: Counters allows iterating over many incrementing variables in one loop
- C++ library: `libcasm_global`


### `libcasm-xtal`

The CASM crystallography module

- Repository: [CASMcode_global](https://github.com/prisms-center/CASMcode_crystallography/)
- Docs: [v2.0](https://prisms-center.github.io/CASMcode_pydocs/libcasm/xtal/2.0/index.html)
- Includes:
  - Data structures for representing lattices, crystal structures, and degrees of freedom (DoF).
  - Methods for enumerating superlattices, making super structures, finding primitive and reduced cells, and finding symmetry operations.
- CASM dependencies:
  - libcasm-global
- Python namespace package: `libcasm.xtal`
- C++ library: `libcasm_crystallography`
