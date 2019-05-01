The `` `bspecs.json` `` file that specifies how to generate a basis set is described by `` `casm format --bspecs` ``:

```
$ casm format --bspecs
```
<details><summary markdown="span">See result</summary>

```
$ casm format --bspecs

### bspecs.json ##################

LOCATION:
$ROOT/basis_sets/$CURR_BSET/bspecs.json


DESCRIPTION:
This JSON file contains specifications for generating the cluster
basis functions.                                                    

'site_basis_functions' may specify a string, which can be either 'occupation' or 
'chebychev'. Otherwise, specifies a JSON object containing a composition vector or
a JSON array containing multiple composition vectors. A single composition vector
is formatted as, e.g.
   "composition" : {"Au" : 0.25, "Cu" : 0.75} 
The site basis functions will then be constructed as to be optimized for that composition.

To specify different compositions on multiple sublattices, an array can be used. 
As an example, the following specifies a different composition on sublattice 0 than
on sublattices 1 and 3: 

   "site_basis_functions" : [
                                {
                                  "composition" : {"Ga" : 0.3, "In" : 0.7},
                                  "sublat_indices" : [0]
                                },
                                {
                                  "composition" : {"Ga" : 1.0, "In" : 0.0},
                                  "sublat_indices" : [1,2]
                                }
                             ]

Sublattices are specified in the same order as in prim.json. Sublattice compositions
are not allowed to break the symmetry of the crystal. If equivalent sublattices are
assigned inequivalent compositions, one will be chosen arbitrarily and propagated to
all equivalent sublattices.  The resulting site basis functions can be reviewed using
'casm bset --functions'

The JSON object 'orbit_branch_specs' specifies the maximum size of pair,   
triplet, quadruplet, etc. clusters in terms of the maximum distance 
between any two sites in the cluster.

The JSON array 'orbit_specs' allows specifying particular custom orbits    
by providing the prototype cluster coordinates. The 'include_subclusters'  
option allows including all orbits of subclusters of the specified cluster.
The cluster coordinates may be in "Direct"/"Fractional" coordinates,   
"Cartesian" coordinates, or "Integral" coordinates. "Integral"       
coordinates are 4-element integer arrays indicating sublattice index, b,   
followed by unit cell indices, i, j, k.                                    


EXAMPLE:
-------
{
  "basis_functions" : {
    "site_basis_functions" : "occupation"
  },
  "orbit_branch_specs" : {
    "2" : {"max_length" : 4.01},
    "3" : {"max_length" : 3.01}
  },
  "orbit_specs" : [
    {
      "coordinate_mode" : "Direct",
      "prototype" : [
        [ 0.000000000000, 0.000000000000, 0.000000000000 ],
        [ 1.000000000000, 0.000000000000, 0.000000000000 ],
        [ 2.000000000000, 0.000000000000, 0.000000000000 ],
        [ 3.000000000000, 0.000000000000, 0.000000000000 ]
      ],
      "include_subclusters" : true  
    },
    {
      "coordinate_mode" : "Integral",
      "prototype" : [
        [ 0, 0, 0, 0 ],
        [ 1, 0, 0, 0 ],
        [ 0, 0, 0, 3 ]
      ],
      "include_subclusters" : true
    }
  ]
}
-------
```
</details>
<br>
