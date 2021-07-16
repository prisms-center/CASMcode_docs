---
title: "Cluster"
permalink: /formats/casm/clusterography/IntegralClusterOrbitGenerator/
---

### Description

This specifies a cluster of sites.

If it is used to generate an orbit of clusters it also allows specifying if subcluster orbits should also be generated.


### JSON Attributes List

IntegralClusterOrbitGenerator attributes:

| Name | Description | Format |
|-|-|-|
| [`coordinate_mode`](#coordinate-mode) | Site coordinate type | string |
| [`sites`](#sites) | Cluster sites | array of arrays |
| [`prototype`](#prototype) | Alias for `sites` | array of arrays |
| [`include_subclusters`](#include-subclusters) | Option to include subclusters | bool |

### JSON Attributes Description

Orbit generating cluster input format:

- {: #coordinate-mode } `coordinate_mode`: string (optional, default=`"Integral"`)

  Specifies the coordinate mode used to specify cluster sites. One of:
  - `"Integral"`: 4-index coordinate `[b, i, j, k]`, where b=sublattice index, and i,j,k are lattice vector indices. Also accepts `"INT"`, `"INTEGRAL"`, or `"integral"`.
  - `"Cartesian"`: 3-index coordinate `[x, y, z]` giving the site in Cartesian coordinates. Also accepts `"CART"`, or `"cartesian"`.
  - `"Direct"` or `"Fractional"`: 3-index coordinate `[a, b, c]`, where a,b,c are multiplied by the lattice vectors to give the site coordinate in Cartesian coordinates. Also accepts `"FRAC"`, `"fractional"`, or `"direct"`.

- {: #sites } `sites`: array of arrays (required)

  An array of coordinates of sites in the cluster.

- {: #prototype } `prototype`: this is an allowed alias for `"sites"`

- {: #include-subclusters } `include_subclusters`: bool (optional, default=`true`)

  Whether all subclusters of the specified clusters should also be included. This is not relevant for "phenomenal" and ignored if present.


### Examples

#### Example 1) Using "Direct" coordinates

    {
        "coordinate_mode" : "Direct",
        "sites" : [
            [ 0.000000000000, 0.000000000000, 0.000000000000 ],
            [ 1.000000000000, 0.000000000000, 0.000000000000 ],
            [ 2.000000000000, 0.000000000000, 0.000000000000 ],
            [ 3.000000000000, 0.000000000000, 0.000000000000 ]],
        "include_subclusters" : true
    }

#### Example 2) Using "Integral" coordinates:

    {
        "coordinate_mode" : "Integral",
        "sites" : [
            [ 0, 0, 0, 0 ],
            [ 0, 1, 0, 0 ],
            [ 1, 0, 0, 0 ]],
        "include_subclusters" : true
    }

{% include file_formats_and_locations.md %}
