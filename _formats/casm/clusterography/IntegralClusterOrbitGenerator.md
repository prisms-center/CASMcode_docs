---
title: "IntegralClusterOrbitGenerator"
permalink: /formats/casm/clusterography/IntegralClusterOrbitGenerator/
---

IntegralClusterOrbitGenerator specifies a cluster of sites that will be used to generate an orbit of clusters. It also allows specifying if subcluster orbits should also be generated. It is used for the `"orbit_specs"` and `"phenomenal"` options for [ClusterSpecs](ClusterSpecs.md) JSON input.

### JSON Attributes

Orbit generating cluster input format (Used for ):

- `coordinate_mode`: string (optional, default=`"Integral"`)

  Specifies the coordinate mode used to specify cluster sites. One of:
  - `"Integral"`: 4-index coordinate `[b, i, j, k]`, where b=sublattice index, and i,j,k are lattice vector indices. Also accepts `"INT"`, `"INTEGRAL"`, or `"integral"`.
  - `"Cartesian"`: 3-index coordinate `[x, y, z]` giving the site in Cartesian coordinates. Also accepts `"CART"`, or `"cartesian"`.
  - `"Direct"` or `"Fractional"`: 3-index coordinate `[a, b, c]`, where a,b,c are multiplied by the lattice vectors to give the site coordinate in Cartesian coordinates. Also accepts `"FRAC"`, `"fractional"`, or `"direct"`.

- `sites`: array of arrays (required)

  An array of coordinates of sites in the cluster.

- `prototype`: this is an allowed alias for `"sites"`

- `include_subclusters`: boolean (optional, default=`true`)

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
