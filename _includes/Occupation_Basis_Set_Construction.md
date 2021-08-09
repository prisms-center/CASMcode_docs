## Constructing a basis set (occupational DoF)

### Create a CASM project

This example will begin with the same ZrO project used in the [Defining the "prim"](https://prisms-center.github.io/CASMcode_docs/pages/tutorials/#defining-the-prim) tutorial.


```bash
prim_str='
{
  "basis" : [
    {
      "coordinate" : [ 0.0000000, 0.0000000, 0.0000000 ],
      "occupants" : [ "Zr" ]
    },
    {
      "coordinate" : [ 0.6666666667, 0.3333333333, 0.5000000 ],
      "occupants" : [ "Zr" ]
    },
    {
      "coordinate" : [ 0.3333333333, 0.6666666667, 0.2500000 ],
      "occupants" : [ "Va", "O" ]
    },
    {
      "coordinate" : [ 0.3333333333, 0.6666666667, 0.7500000 ],
      "occupants" : [ "Va", "O" ]
    }
  ],
  "coordinate_mode" : "Fractional",
  "description" : "hcp Zr with octahedral interstitial O ",
  "lattice_vectors" : [
    [ 3.23398686, 0.00000000, 0.00000000 ],
    [ -1.61699343, 2.80071477, 0.00000000 ],
    [ -0.00000000, 0.00000000, 5.16867834 ]
  ],
  "title" : "ZrO"
}'
```


```bash
start=$(pwd)
mkdir -p $start/bset/ZrO && cd $start/bset/ZrO

echo "$prim_str" > prim.json
ccasm init
```

    
    ***************************
    
    Initializing CASM project 'ZrO'
    Creating CASM project directory tree at: "/Users/bpuchala/Work/codes/CASMcode_tutorials/v1.2/bset/ZrO"
    Writing prim file: "/Users/bpuchala/Work/codes/CASMcode_tutorials/v1.2/bset/ZrO/.casm/prim.json"
      DONE
    


### The basis set specifications file (bspecs.json)

A cluster expansion basis set is specified using:
- [Basis Set Specs](https://prisms-center.github.io/CASMcode_docs/formats/casm/clex/ClexBasisSpecs/): Specifications, written in a "bspecs.json" file, consisting of two components:
  - [Basis Function Specs](https://prisms-center.github.io/CASMcode_docs/formats/casm/basis_set/BasisFunctionSpecs/): Control the type and order of basis functions 
  - [Cluster Specs](https://prisms-center.github.io/CASMcode_docs/formats/casm/clusterography/ClusterSpecs/): Control which cluster basis functions are generated


By default, the "bspecs.json" file is written to:

    <root>/basis_sets/bset.default/bspecs.json
    
Where:
- `<root>`: indicates the CASM project root directory
- `bset.default`: indicates the choice of basis set
  - The is a directory, prefixed with `bset.`, that allows CASM to track multiple basis sets in a single project.
  - Use `casm settings` for creating additional basis sets and switching the current choice of basis set

### Example "bspecs.json"


```bash
bspecs_str='{
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
}'
```


```bash
# create the bspecs.json file
echo "$bspecs_str" > basis_sets/bset.default/bspecs.json

# print the prim.json file contents
cat basis_sets/bset.default/bspecs.json
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


### Generate the basis set

The `-u,--update` command:
- Generates the basis set based on the current "bspecs.json" file
- Writes C++ source code
- Compiles the source code
  - For large basis sets this may be slow, but it only has to be done once
  - Use `--no-compile` to get basis set information without waiting for compilation
- Use `-f,--force` to update and overwrite any existing generated files 



```bash
ccasm bset -u
```

      Adding null orbit branch.  New orbits: 1
      Calculating orbit branch 1:  Expanding orbit 0 / 1  of branch 0.  New orbits: 1                   
      Calculating orbit branch 2:  Expanding orbit 0 / 1  of branch 1.  New orbits: 5                   
      Calculating orbit branch 3:  Expanding orbit 0 / 5  of branch 2.  New orbits: 0                   
      Calculating orbit branch 3:  Expanding orbit 1 / 5  of branch 2.  New orbits: 0                   
      Calculating orbit branch 3:  Expanding orbit 2 / 5  of branch 2.  New orbits: 0                   
      Calculating orbit branch 3:  Expanding orbit 3 / 5  of branch 2.  New orbits: 0                   
      Calculating orbit branch 3:  Expanding orbit 4 / 5  of branch 2.  New orbits: 0                   
    
    -- Compiling: /Users/bpuchala/Work/codes/CASMcode_tutorials/v1.2/bset/ZrO/basis_sets/bset.default/ZrO_Clexulator.cc -- 
    compile time depends on how many basis functions are included
    compile time: 8.54349 (s)
    


### Print basis set properties - Basis functions

Use `bset --functions` to print basis functions
- This prints the basis functions for easy viewing
  - It only prints the basis functions associated with the prototype cluster
- Use `--align` to print nicely formatted formulas for Latex
- The underlying data can be found in:
  - The `basis.json` file:
  
        <root>/basis_sets/bset.default/basis.json
        
  - The generated source code for the "clexulator" (cluster expansion calculator):
  
        <root>/basis_sets/bset.default/ZrO_clexulator.cc
- Use `--print-invariant-group` to print the symmetry operations that leave the prototype cluster function invariant


**Notes:**
- Occupation site basis functions are printed as:
      \phi_{b,i}(s_{j})
  where:
  - `b`: is the sublattice index
  - `i`: is the site basis function index
  - `s_{n}`: is the occupation value on the `j`-th site in the cluster (not the entire configurationn)
- The constant site basis function is implicitly included only:
  - A site with two allowed occupants will show as having 1 site basis function, with index 0
  - A site with three allowed occupants will show as having 2 site basis functions, with indices [0, 1]
  - etc.


```bash
# print basis functions
ccasm bset --functions
```

    Site basis functions for DoF "occ":
    
    Asymmetric unit 1:
        Basis site 0:  0 0 0 Zr  
        [No site basis functions]
    
        Basis site 1:  0.6666667 0.3333333       0.5 Zr  
        [No site basis functions]
    
    Asymmetric unit 2:
        Basis site 2:  0.3333333 0.6666667      0.25 Va  O  
            \phi_{2,0}[Va] = 0,   \phi_{2,0}[O] = 1     
        Basis site 3:  0.3333333 0.6666667 0.75      Va  O  
            \phi_{3,0}[Va] = 0,   \phi_{3,0}[O] = 1     
    
    
    Prototype cluster functions: 
    
    COORD_MODE = Fractional
    
    ** Branch 0 ** 
        ** 0 of 7 Orbits **  Points: 0  Mult: 1  MinLength: 0.00000  MaxLength: 0.00000
            Prototype of 1 Equivalent Clusters in Orbit 0
                Coordinates:
            Prototype basis functions:
                \Phi_{0} = 1
    
    ** Branch 1 ** 
        ** 1 of 7 Orbits **  Points: 1  Mult: 2  MinLength: 0.0000000  MaxLength: 0.0000000
            Prototype of 2 Equivalent Clusters in Orbit 1
                Coordinates:
                    0.3333333 0.6666667 0.2500000 Va  O  
            Prototype basis functions:
                \Phi_{1} = \phi_{2,0}(s_{0})
    
    ** Branch 2 ** 
        ** 2 of 7 Orbits **  Points: 2  Mult: 2  MinLength: 2.5843392  MaxLength: 2.5843392
            Prototype of 2 Equivalent Clusters in Orbit 2
                Coordinates:
                    0.3333333 0.6666667 0.2500000 Va  O  
                    0.3333333 0.6666667 0.7500000 Va  O  
            Prototype basis functions:
                \Phi_{2} = \phi_{2,0}(s_{0})\phi_{3,0}(s_{1})
    
        ** 3 of 7 Orbits **  Points: 2  Mult: 6  MinLength: 3.2339869  MaxLength: 3.2339869
            Prototype of 6 Equivalent Clusters in Orbit 3
                Coordinates:
                    0.3333333 0.6666667 0.2500000 Va  O  
                    0.3333333 1.6666667 0.2500000 Va  O  
            Prototype basis functions:
                \Phi_{3} = \phi_{2,0}(s_{0})\phi_{2,0}(s_{1})
    
        ** 4 of 7 Orbits **  Points: 2  Mult: 12  MinLength: 4.1397439  MaxLength: 4.1397439
            Prototype of 12 Equivalent Clusters in Orbit 4
                Coordinates:
                    0.3333333 0.6666667 0.2500000 Va  O  
                    1.3333333 1.6666667 -0.2500000 Va  O  
            Prototype basis functions:
                \Phi_{4} = \phi_{2,0}(s_{0})\phi_{3,0}(s_{1})
    
        ** 5 of 7 Orbits **  Points: 2  Mult: 2  MinLength: 5.1686783  MaxLength: 5.1686783
            Prototype of 2 Equivalent Clusters in Orbit 5
                Coordinates:
                    0.3333333 0.6666667 0.2500000 Va  O  
                    0.3333333 0.6666667 1.2500000 Va  O  
            Prototype basis functions:
                \Phi_{5} = \phi_{2,0}(s_{0})\phi_{2,0}(s_{1})
    
        ** 6 of 7 Orbits **  Points: 2  Mult: 6  MinLength: 5.6014295  MaxLength: 5.6014295
            Prototype of 6 Equivalent Clusters in Orbit 6
                Coordinates:
                    0.3333333 0.6666667 0.2500000 Va  O  
                    2.3333333 1.6666667 0.2500000 Va  O  
            Prototype basis functions:
                \Phi_{6} = \phi_{2,0}(s_{0})\phi_{2,0}(s_{1})
    


### Print basis set properties - Clusters and cluster orbits

- Use `--orbits` to print the generated cluster orbits for easy viewing
- Use `--clusters` to print the generated clusters in each orbit
- The underlying data can be found in:

      <root>/basis_sets/bset.default/clust.json
      
- Use `--print-invariant-group` to print the symmetry operations that leave the prototype cluster invariant
- Use `--print-equivalence-map` with `--clusters` to print the symmetry operations that map prototype cluster onto an equivalent cluster


```bash
# print cluster orbits
ccasm bset --clusters --print-invariant-group --print-equivalence-map
```

    COORD_MODE = Fractional
    
    ** Branch 0 ** 
        ** 0 of 7 Orbits **  Points: 0  Mult: 1  MinLength: 0.00000  MaxLength: 0.00000
            0 of 1 Equivalent Clusters in Orbit 0
                Coordinates:
                Invariant group:
                    1: 1
                    2: 6⁺ (0.0000000 0.0000000 0.5000000) 0.3333333, 2.666667, z
                    3: 6⁻ (0.0000000 0.0000000 0.5000000) 2.333333, -0.3333333, z
                    4: 3⁺ 0.6666667, 1.333333, z
                    5: 3⁻ 1.333333, 0.6666667, z
                    6: 2 1.333333, y, 0.25
                    7: 2 (1.5000000 0.0000000 0.0000000) x, 1.166667, 0.25
                    8: 2 (2.5000000 2.5000000 0.0000000) 0.08333333+x, -0.08333333+x, 0.25
                    9: 2 (0.0000000 0.0000000 0.5000000) 1.333333, 1.166667, z
                    10: 2 1+x, 1-x, 0
                    11: 2 0.5+x, 2*x, 0
                    12: 2 2*x, 0.5+x, 0
                    13: m 2*x, 0.5+x, z
                    14: m 0.5+x, 2*x, z
                    15: m 1+x, 1-x, z
                    16: m x, y, 0
                    17: g (2.5000000 2.5000000 0.5000000) 0.08333333+x, -0.08333333+x, z
                    18: g ( 1.5000000 -0.0000000  0.5000000) 0.5833333+x, 1.166667, z
                    19: g (0.0000000 1.0000000 0.5000000) 1.333333, 0.6666667+y, z
                    20: -3⁺ 2.333333, -0.3333333, z;  2.3333333 -0.3333333  0.2500000
                    21: -3⁻ 0.3333333, 2.666667, z; 0.3333333 2.6666667 0.2500000
                    22: -6⁺ 1.333333, 0.6666667, z; 1.3333333 0.6666667 0.0000000
                    23: -6⁻ 0.6666667, 1.333333, z; 0.6666667 1.3333333 0.0000000
                    24: -1 1.3333333 1.1666667 0.2500000
                Equivalence map: 
                    0: (0) 1
                    1: (1) 6⁺ (0.0000000 0.0000000 0.5000000) 0.3333333, 2.666667, z
                    2: (2) 6⁻ (0.0000000 0.0000000 0.5000000) 2.333333, -0.3333333, z
                    3: (3) 3⁺ 0.6666667, 1.333333, z
                    4: (4) 3⁻ 1.333333, 0.6666667, z
                    5: (5) 2 1.333333, y, 0.25
                    6: (6) 2 (1.5000000 0.0000000 0.0000000) x, 1.166667, 0.25
                    7: (7) 2 (2.5000000 2.5000000 0.0000000) 0.08333333+x, -0.08333333+x, 0.25
                    8: (8) 2 (0.0000000 0.0000000 0.5000000) 1.333333, 1.166667, z
                    9: (9) 2 1+x, 1-x, 0
                    10: (10) 2 0.5+x, 2*x, 0
                    11: (11) 2 2*x, 0.5+x, 0
                    12: (12) m 2*x, 0.5+x, z
                    13: (13) m 0.5+x, 2*x, z
                    14: (14) m 1+x, 1-x, z
                    15: (15) m x, y, 0
                    16: (16) g (2.5000000 2.5000000 0.5000000) 0.08333333+x, -0.08333333+x, z
                    17: (17) g ( 1.5000000 -0.0000000  0.5000000) 0.5833333+x, 1.166667, z
                    18: (18) g (0.0000000 1.0000000 0.5000000) 1.333333, 0.6666667+y, z
                    19: (19) -3⁺ 2.333333, -0.3333333, z;  2.3333333 -0.3333333  0.2500000
                    20: (20) -3⁻ 0.3333333, 2.666667, z; 0.3333333 2.6666667 0.2500000
                    21: (21) -6⁺ 1.333333, 0.6666667, z; 1.3333333 0.6666667 0.0000000
                    22: (22) -6⁻ 0.6666667, 1.333333, z; 0.6666667 1.3333333 0.0000000
                    23: (23) -1 1.3333333 1.1666667 0.2500000
    
    ** Branch 1 ** 
        ** 1 of 7 Orbits **  Points: 1  Mult: 2  MinLength: 0.0000000  MaxLength: 0.0000000
            0 of 2 Equivalent Clusters in Orbit 1
                Coordinates:
                    0.3333333 0.6666667 0.2500000 Va  O  
                Invariant group:
                    1 (1): 1
                    2 (4): 3⁺ 0.3333333, 0.6666667, z
                    3 (5): 3⁻ 0.3333333, 0.6666667, z
                    4 (6): 2 0.3333333, y, 0.25
                    5 (7): 2 x, 0.6666667, 0.25
                    6 (8): 2 -0.1666667+x, 0.1666667+x, 0.25
                    7 (13): m 2*x, 0.5+x, z
                    8 (14): m x, 2*x, z
                    9 (15): m 0.5+x, 0.5-x, z
                    10 (20): -3⁺ 0.3333333, 0.6666667, z; 0.3333333 0.6666667 0.2500000
                    11 (21): -3⁻ 0.3333333, 0.6666667, z; 0.3333333 0.6666667 0.2500000
                    12 (24): -1 0.3333333 0.6666667 0.2500000
                Equivalence map: 
                    0: (0) 1
                    1: (3) 3⁺ 0.3333333, 0.6666667, z
                    2: (4) 3⁻ 0.3333333, 0.6666667, z
                    3: (5) 2 0.3333333, y, 0.25
                    4: (6) 2 x, 0.6666667, 0.25
                    5: (7) 2 -0.1666667+x, 0.1666667+x, 0.25
                    6: (12) m 2*x, 0.5+x, z
                    7: (13) m x, 2*x, z
                    8: (14) m 0.5+x, 0.5-x, z
                    9: (19) -3⁺ 0.3333333, 0.6666667, z; 0.3333333 0.6666667 0.2500000
                    10: (20) -3⁻ 0.3333333, 0.6666667, z; 0.3333333 0.6666667 0.2500000
                    11: (23) -1 0.3333333 0.6666667 0.2500000
            1 of 2 Equivalent Clusters in Orbit 1
                Coordinates:
                    0.3333333 0.6666667 0.7500000 Va  O  
                Invariant group:
                    1 (1): 1
                    2 (4): 3⁺ 0.3333333, 0.6666667, z
                    3 (5): 3⁻ 0.3333333, 0.6666667, z
                    4 (6): 2 0.3333333, y, 0.75
                    5 (7): 2 x, 0.6666667, 0.75
                    6 (8): 2 -0.1666667+x, 0.1666667+x, 0.75
                    7 (13): m 2*x, 0.5+x, z
                    8 (14): m x, 2*x, z
                    9 (15): m 0.5+x, 0.5-x, z
                    10 (20): -3⁺ 0.3333333, 0.6666667, z; 0.3333333 0.6666667 0.7500000
                    11 (21): -3⁻ 0.3333333, 0.6666667, z; 0.3333333 0.6666667 0.7500000
                    12 (24): -1 0.3333333 0.6666667 0.7500000
                Equivalence map: 
                    0: (1) 6⁺ (0.0000000 0.0000000 0.5000000) 0.3333333, 0.6666667, z
                    1: (8) 2 (0.0000000 0.0000000 0.5000000) 0.3333333, 0.6666667, z
                    2: (2) 6⁻ (0.0000000 0.0000000 0.5000000) 0.3333333, 0.6666667, z
                    3: (9) 2 0.5+x, 0.5-x, 0.5
                    4: (11) 2 2*x, 0.5+x, 0.5
                    5: (10) 2 x, 2*x, 0.5
                    6: (16) g (-0.0000000 -0.0000000  0.5000000) -0.1666667+x, 0.1666667+x, z
                    7: (18) g (0.0000000 0.0000000 0.5000000) 0.3333333, 0.1666667+y, z
                    8: (17) g (-0.0000000  0.0000000  0.5000000) 0.3333333+x, 0.6666667, z
                    9: (15) m x, y, 0.5
                    10: (22) -6⁻ 0.3333333, 0.6666667, z; 0.3333333 0.6666667 0.5000000
                    11: (21) -6⁺ 0.3333333, 0.6666667, z; 0.3333333 0.6666667 0.5000000
    
    ** Branch 2 ** 
        ** 2 of 7 Orbits **  Points: 2  Mult: 2  MinLength: 2.5843392  MaxLength: 2.5843392
            0 of 2 Equivalent Clusters in Orbit 2
                Coordinates:
                    0.3333333 0.6666667 0.2500000 Va  O  
                    0.3333333 0.6666667 0.7500000 Va  O  
                Invariant group:
                    1 (1): 1
                    2 (4): 3⁺ 0.3333333, 0.6666667, z
                    3 (5): 3⁻ 0.3333333, 0.6666667, z
                    4 (10): 2 0.5+x, 0.5-x, 0.5
                    5 (11): 2 x, 2*x, 0.5
                    6 (12): 2 2*x, 0.5+x, 0.5
                    7 (13): m 2*x, 0.5+x, z
                    8 (14): m x, 2*x, z
                    9 (15): m 0.5+x, 0.5-x, z
                    10 (16): m x, y, 0.5
                    11 (22): -6⁺ 0.3333333, 0.6666667, z; 0.3333333 0.6666667 0.5000000
                    12 (23): -6⁻ 0.3333333, 0.6666667, z; 0.3333333 0.6666667 0.5000000
                Equivalence map: 
                    0: (0) 1
                    1: (3) 3⁺ 0.3333333, 0.6666667, z
                    2: (4) 3⁻ 0.3333333, 0.6666667, z
                    3: (9) 2 0.5+x, 0.5-x, 0.5
                    4: (10) 2 x, 2*x, 0.5
                    5: (11) 2 2*x, 0.5+x, 0.5
                    6: (12) m 2*x, 0.5+x, z
                    7: (13) m x, 2*x, z
                    8: (14) m 0.5+x, 0.5-x, z
                    9: (15) m x, y, 0.5
                    10: (21) -6⁺ 0.3333333, 0.6666667, z; 0.3333333 0.6666667 0.5000000
                    11: (22) -6⁻ 0.3333333, 0.6666667, z; 0.3333333 0.6666667 0.5000000
            1 of 2 Equivalent Clusters in Orbit 2
                Coordinates:
                    0.3333333 0.6666667 0.7500000 Va  O  
                    0.3333333 0.6666667 1.2500000 Va  O  
                Invariant group:
                    1 (1): 1
                    2 (4): 3⁺ 0.3333333, 0.6666667, z
                    3 (5): 3⁻ 0.3333333, 0.6666667, z
                    4 (10): 2 0.5+x, 0.5-x, 1
                    5 (11): 2 x, 2*x, 1
                    6 (12): 2 2*x, 0.5+x, 1
                    7 (13): m 2*x, 0.5+x, z
                    8 (14): m x, 2*x, z
                    9 (15): m 0.5+x, 0.5-x, z
                    10 (16): m x, y, 1
                    11 (22): -6⁺ 0.3333333, 0.6666667, z; 0.3333333 0.6666667 1.0000000
                    12 (23): -6⁻ 0.3333333, 0.6666667, z; 0.3333333 0.6666667 1.0000000
                Equivalence map: 
                    0: (1) 6⁺ (0.0000000 0.0000000 0.5000000) 0.3333333, 0.6666667, z
                    1: (8) 2 (0.0000000 0.0000000 0.5000000) 0.3333333, 0.6666667, z
                    2: (2) 6⁻ (0.0000000 0.0000000 0.5000000) 0.3333333, 0.6666667, z
                    3: (6) 2 x, 0.6666667, 0.75
                    4: (5) 2 0.3333333, y, 0.75
                    5: (7) 2 -0.1666667+x, 0.1666667+x, 0.75
                    6: (16) g (-0.0000000 -0.0000000  0.5000000) -0.1666667+x, 0.1666667+x, z
                    7: (18) g (0.0000000 0.0000000 0.5000000) 0.3333333, 0.1666667+y, z
                    8: (17) g (-0.0000000  0.0000000  0.5000000) 0.3333333+x, 0.6666667, z
                    9: (20) -3⁻ 0.3333333, 0.6666667, z; 0.3333333 0.6666667 0.7500000
                    10: (19) -3⁺ 0.3333333, 0.6666667, z; 0.3333333 0.6666667 0.7500000
                    11: (23) -1 0.3333333 0.6666667 0.7500000
    
        ** 3 of 7 Orbits **  Points: 2  Mult: 6  MinLength: 3.2339869  MaxLength: 3.2339869
            0 of 6 Equivalent Clusters in Orbit 3
                Coordinates:
                    0.3333333 0.6666667 0.2500000 Va  O  
                    0.3333333 1.6666667 0.2500000 Va  O  
                Invariant group:
                    1 (1): 1
                    2 (6): 2 0.3333333, y, 0.25
                    3 (13): m 2*x, 1+x, z
                    4 (24): -1 0.3333333 1.1666667 0.2500000
                Equivalence map: 
                    0: (0) 1
                    1: (5) 2 0.3333333, y, 0.25
                    2: (12) m 2*x, 1+x, z
                    3: (23) -1 0.3333333 1.1666667 0.2500000
            1 of 6 Equivalent Clusters in Orbit 3
                Coordinates:
                    1.3333333 0.6666667 0.7500000 Va  O  
                    0.3333333 0.6666667 0.7500000 Va  O  
                Invariant group:
                    1 (1): 1
                    2 (7): 2 x, 0.6666667, 0.75
                    3 (14): m 0.5+x, 2*x, z
                    4 (24): -1 0.8333333 0.6666667 0.7500000
                Equivalence map: 
                    0: (1) 6⁺ (0.0000000 0.0000000 0.5000000) 1.333333, 1.666667, z
                    1: (9) 2 ( 0.5000000 -0.5000000  0.0000000) 0.75+x, 0.75-x, 0.5
                    2: (16) g (-0.0000000 -0.0000000  0.5000000) -0.1666667+x, 0.1666667+x, z
                    3: (21) -6⁺ 0.3333333, 0.6666667, z; 0.3333333 0.6666667 0.5000000
            2 of 6 Equivalent Clusters in Orbit 3
                Coordinates:
                    0.3333333 0.6666667 0.7500000 Va  O  
                    1.3333333 1.6666667 0.7500000 Va  O  
                Invariant group:
                    1 (1): 1
                    2 (8): 2 -0.1666667+x, 0.1666667+x, 0.75
                    3 (15): m 1+x, 1-x, z
                    4 (24): -1 0.8333333 1.1666667 0.7500000
                Equivalence map: 
                    0: (2) 6⁻ (0.0000000 0.0000000 0.5000000) 0.3333333, 0.6666667, z
                    1: (10) 2 x, 2*x, 0.5
                    2: (17) g ( 0.5000000 -0.0000000  0.5000000) 0.5833333+x, 1.166667, z
                    3: (22) -6⁻ 0.6666667, 1.333333, z; 0.6666667 1.3333333 0.5000000
            3 of 6 Equivalent Clusters in Orbit 3
                Coordinates:
                    1.3333333 1.6666667 0.2500000 Va  O  
                    0.3333333 0.6666667 0.2500000 Va  O  
                Invariant group:
                    1 (1): 1
                    2 (8): 2 -0.1666667+x, 0.1666667+x, 0.25
                    3 (15): m 1+x, 1-x, z
                    4 (24): -1 0.8333333 1.1666667 0.2500000
                Equivalence map: 
                    0: (3) 3⁺ 0.6666667, 1.333333, z
                    1: (6) 2 (0.5000000 0.0000000 0.0000000) x, 1.166667, 0.25
                    2: (13) m x, 2*x, z
                    3: (19) -3⁺ 0.3333333, 0.6666667, z; 0.3333333 0.6666667 0.2500000
            4 of 6 Equivalent Clusters in Orbit 3
                Coordinates:
                    0.3333333 0.6666667 0.2500000 Va  O  
                    1.3333333 0.6666667 0.2500000 Va  O  
                Invariant group:
                    1 (1): 1
                    2 (7): 2 x, 0.6666667, 0.25
                    3 (14): m 0.5+x, 2*x, z
                    4 (24): -1 0.8333333 0.6666667 0.2500000
                Equivalence map: 
                    0: (4) 3⁻ 0.3333333, 0.6666667, z
                    1: (7) 2 -0.1666667+x, 0.1666667+x, 0.25
                    2: (14) g ( 0.5000000 -0.5000000 -0.0000000) 0.75+x, 0.75-x, z
                    3: (20) -3⁻ 1.333333, 1.666667, z; 1.3333333 1.6666667 0.2500000
            5 of 6 Equivalent Clusters in Orbit 3
                Coordinates:
                    0.3333333 1.6666667 0.7500000 Va  O  
                    0.3333333 0.6666667 0.7500000 Va  O  
                Invariant group:
                    1 (1): 1
                    2 (6): 2 0.3333333, y, 0.75
                    3 (13): m 2*x, 1+x, z
                    4 (24): -1 0.3333333 1.1666667 0.7500000
                Equivalence map: 
                    0: (8) 2 (0.0000000 0.0000000 0.5000000) 0.3333333, 1.166667, z
                    1: (11) 2 2*x, 1+x, 0.5
                    2: (18) g (0.0000000 0.0000000 0.5000000) 0.3333333, 0.1666667+y, z
                    3: (15) m x, y, 0.5
    
        ** 4 of 7 Orbits **  Points: 2  Mult: 12  MinLength: 4.1397439  MaxLength: 4.1397439
            0 of 12 Equivalent Clusters in Orbit 4
                Coordinates:
                    0.3333333 0.6666667 0.2500000 Va  O  
                    1.3333333 1.6666667 -0.2500000 Va  O  
                Invariant group:
                    1 (1): 1
                    2 (10): 2 1+x, 1-x, 0
                Equivalence map: 
                    0: (0) 1
                    1: (9) 2 1+x, 1-x, 0
            1 of 12 Equivalent Clusters in Orbit 4
                Coordinates:
                    0.3333333 0.6666667 0.7500000 Va  O  
                    0.3333333 1.6666667 0.2500000 Va  O  
                Invariant group:
                    1 (1): 1
                    2 (12): 2 2*x, 1+x, 0.5
                Equivalence map: 
                    0: (1) 6⁺ (0.0000000 0.0000000 0.5000000) 0.3333333, 0.6666667, z
                    1: (6) 2 (-0.5000000 -0.0000000  0.0000000) x, 1.166667, 0.25
            2 of 12 Equivalent Clusters in Orbit 4
                Coordinates:
                    0.3333333 0.6666667 0.7500000 Va  O  
                    1.3333333 0.6666667 0.2500000 Va  O  
                Invariant group:
                    1 (1): 1
                    2 (11): 2 0.5+x, 2*x, 0.5
                Equivalence map: 
                    0: (2) 6⁻ (0.0000000 0.0000000 0.5000000) 0.3333333, 0.6666667, z
                    1: (5) 2 (-0.0000000 -0.5000000  0.0000000) 0.8333333, y, 0.25
            3 of 12 Equivalent Clusters in Orbit 4
                Coordinates:
                    1.3333333 0.6666667 1.2500000 Va  O  
                    0.3333333 0.6666667 0.7500000 Va  O  
                Invariant group:
                    1 (1): 1
                    2 (11): 2 0.5+x, 2*x, 1
                Equivalence map: 
                    0: (3) 3⁺ 1, 1, z
                    1: (11) 2 2*x, 0.5+x, 0.5
            4 of 12 Equivalent Clusters in Orbit 4
                Coordinates:
                    0.3333333 1.6666667 1.2500000 Va  O  
                    0.3333333 0.6666667 0.7500000 Va  O  
                Invariant group:
                    1 (1): 1
                    2 (12): 2 2*x, 1+x, 1
                Equivalence map: 
                    0: (4) 3⁻ 0.6666667, 1.333333, z
                    1: (10) 2 x, 2*x, 0.5
            5 of 12 Equivalent Clusters in Orbit 4
                Coordinates:
                    0.3333333 0.6666667 0.2500000 Va  O  
                    1.3333333 1.6666667 0.7500000 Va  O  
                Invariant group:
                    1 (1): 1
                    2 (10): 2 1+x, 1-x, 0.5
                Equivalence map: 
                    0: (7) 2 -0.1666667+x, 0.1666667+x, 0.25
                    1: (8) 2 (0.0000000 0.0000000 0.5000000) 0.8333333, 1.166667, z
            6 of 12 Equivalent Clusters in Orbit 4
                Coordinates:
                    0.3333333 0.6666667 0.2500000 Va  O  
                    1.3333333 0.6666667 -0.2500000 Va  O  
                Invariant group:
                    1 (1): 1
                    2 (11): 2 0.5+x, 2*x, 0
                Equivalence map: 
                    0: (12) m 2*x, 0.5+x, z
                    1: (22) -6⁻ 1, 1, z; 1.0000000 1.0000000 0.0000000
            7 of 12 Equivalent Clusters in Orbit 4
                Coordinates:
                    0.3333333 0.6666667 0.2500000 Va  O  
                    0.3333333 1.6666667 -0.2500000 Va  O  
                Invariant group:
                    1 (1): 1
                    2 (12): 2 2*x, 1+x, 0
                Equivalence map: 
                    0: (13) m x, 2*x, z
                    1: (21) -6⁺ 0.6666667, 1.333333, z; 0.6666667 1.3333333 0.0000000
            8 of 12 Equivalent Clusters in Orbit 4
                Coordinates:
                    1.3333333 1.6666667 1.2500000 Va  O  
                    0.3333333 0.6666667 0.7500000 Va  O  
                Invariant group:
                    1 (1): 1
                    2 (10): 2 1+x, 1-x, 1
                Equivalence map: 
                    0: (14) m 1+x, 1-x, z
                    1: (15) m x, y, 0.5
            9 of 12 Equivalent Clusters in Orbit 4
                Coordinates:
                    0.3333333 0.6666667 0.7500000 Va  O  
                    1.3333333 1.6666667 0.2500000 Va  O  
                Invariant group:
                    1 (1): 1
                    2 (10): 2 1+x, 1-x, 0.5
                Equivalence map: 
                    0: (16) g (-0.0000000 -0.0000000  0.5000000) -0.1666667+x, 0.1666667+x, z
                    1: (23) -1 0.8333333 1.1666667 0.2500000
            10 of 12 Equivalent Clusters in Orbit 4
                Coordinates:
                    0.3333333 1.6666667 0.7500000 Va  O  
                    0.3333333 0.6666667 0.2500000 Va  O  
                Invariant group:
                    1 (1): 1
                    2 (12): 2 2*x, 1+x, 0.5
                Equivalence map: 
                    0: (17) g (-0.5000000  0.0000000  0.5000000) 0.5833333+x, 1.166667, z
                    1: (20) -3⁻ 0.3333333, 0.6666667, z; 0.3333333 0.6666667 0.2500000
            11 of 12 Equivalent Clusters in Orbit 4
                Coordinates:
                    1.3333333 0.6666667 0.7500000 Va  O  
                    0.3333333 0.6666667 0.2500000 Va  O  
                Invariant group:
                    1 (1): 1
                    2 (11): 2 0.5+x, 2*x, 0.5
                Equivalence map: 
                    0: (18) g (-0.0000000 -0.5000000  0.5000000) 0.8333333, 0.4166667+y, z
                    1: (19) -3⁺ 0.3333333, 0.6666667, z; 0.3333333 0.6666667 0.2500000
    
        ** 5 of 7 Orbits **  Points: 2  Mult: 2  MinLength: 5.1686783  MaxLength: 5.1686783
            0 of 2 Equivalent Clusters in Orbit 5
                Coordinates:
                    0.3333333 0.6666667 0.2500000 Va  O  
                    0.3333333 0.6666667 1.2500000 Va  O  
                Invariant group:
                    1 (1): 1
                    2 (4): 3⁺ 0.3333333, 0.6666667, z
                    3 (5): 3⁻ 0.3333333, 0.6666667, z
                    4 (6): 2 0.3333333, y, 0.75
                    5 (7): 2 x, 0.6666667, 0.75
                    6 (8): 2 -0.1666667+x, 0.1666667+x, 0.75
                    7 (13): m 2*x, 0.5+x, z
                    8 (14): m x, 2*x, z
                    9 (15): m 0.5+x, 0.5-x, z
                    10 (20): -3⁺ 0.3333333, 0.6666667, z; 0.3333333 0.6666667 0.7500000
                    11 (21): -3⁻ 0.3333333, 0.6666667, z; 0.3333333 0.6666667 0.7500000
                    12 (24): -1 0.3333333 0.6666667 0.7500000
                Equivalence map: 
                    0: (0) 1
                    1: (3) 3⁺ 0.3333333, 0.6666667, z
                    2: (4) 3⁻ 0.3333333, 0.6666667, z
                    3: (5) 2 0.3333333, y, 0.75
                    4: (6) 2 x, 0.6666667, 0.75
                    5: (7) 2 -0.1666667+x, 0.1666667+x, 0.75
                    6: (12) m 2*x, 0.5+x, z
                    7: (13) m x, 2*x, z
                    8: (14) m 0.5+x, 0.5-x, z
                    9: (19) -3⁺ 0.3333333, 0.6666667, z; 0.3333333 0.6666667 0.7500000
                    10: (20) -3⁻ 0.3333333, 0.6666667, z; 0.3333333 0.6666667 0.7500000
                    11: (23) -1 0.3333333 0.6666667 0.7500000
            1 of 2 Equivalent Clusters in Orbit 5
                Coordinates:
                    0.3333333 0.6666667 0.7500000 Va  O  
                    0.3333333 0.6666667 1.7500000 Va  O  
                Invariant group:
                    1 (1): 1
                    2 (4): 3⁺ 0.3333333, 0.6666667, z
                    3 (5): 3⁻ 0.3333333, 0.6666667, z
                    4 (6): 2 0.3333333, y, 1.25
                    5 (7): 2 x, 0.6666667, 1.25
                    6 (8): 2 -0.1666667+x, 0.1666667+x, 1.25
                    7 (13): m 2*x, 0.5+x, z
                    8 (14): m x, 2*x, z
                    9 (15): m 0.5+x, 0.5-x, z
                    10 (20): -3⁺ 0.3333333, 0.6666667, z; 0.3333333 0.6666667 1.2500000
                    11 (21): -3⁻ 0.3333333, 0.6666667, z; 0.3333333 0.6666667 1.2500000
                    12 (24): -1 0.3333333 0.6666667 1.2500000
                Equivalence map: 
                    0: (1) 6⁺ (0.0000000 0.0000000 0.5000000) 0.3333333, 0.6666667, z
                    1: (8) 2 (0.0000000 0.0000000 0.5000000) 0.3333333, 0.6666667, z
                    2: (2) 6⁻ (0.0000000 0.0000000 0.5000000) 0.3333333, 0.6666667, z
                    3: (9) 2 0.5+x, 0.5-x, 1
                    4: (11) 2 2*x, 0.5+x, 1
                    5: (10) 2 x, 2*x, 1
                    6: (16) g (-0.0000000 -0.0000000  0.5000000) -0.1666667+x, 0.1666667+x, z
                    7: (18) g (0.0000000 0.0000000 0.5000000) 0.3333333, 0.1666667+y, z
                    8: (17) g (-0.0000000  0.0000000  0.5000000) 0.3333333+x, 0.6666667, z
                    9: (15) m x, y, 1
                    10: (22) -6⁻ 0.3333333, 0.6666667, z; 0.3333333 0.6666667 1.0000000
                    11: (21) -6⁺ 0.3333333, 0.6666667, z; 0.3333333 0.6666667 1.0000000
    
        ** 6 of 7 Orbits **  Points: 2  Mult: 6  MinLength: 5.6014295  MaxLength: 5.6014295
            0 of 6 Equivalent Clusters in Orbit 6
                Coordinates:
                    0.3333333 0.6666667 0.2500000 Va  O  
                    2.3333333 1.6666667 0.2500000 Va  O  
                Invariant group:
                    1 (1): 1
                    2 (6): 2 1.333333, y, 0.25
                    3 (13): m 2*x, 0.5+x, z
                    4 (24): -1 1.3333333 1.1666667 0.2500000
                Equivalence map: 
                    0: (0) 1
                    1: (5) 2 1.333333, y, 0.25
                    2: (12) m 2*x, 0.5+x, z
                    3: (23) -1 1.3333333 1.1666667 0.2500000
            1 of 6 Equivalent Clusters in Orbit 6
                Coordinates:
                    0.3333333 0.6666667 0.7500000 Va  O  
                    1.3333333 2.6666667 0.7500000 Va  O  
                Invariant group:
                    1 (1): 1
                    2 (7): 2 x, 1.666667, 0.75
                    3 (14): m x, 2*x, z
                    4 (24): -1 0.8333333 1.6666667 0.7500000
                Equivalence map: 
                    0: (1) 6⁺ (0.0000000 0.0000000 0.5000000) 0.3333333, 0.6666667, z
                    1: (9) 2 (-0.5000000  0.5000000 -0.0000000) 1.25+x, 1.25-x, 0.5
                    2: (16) g (-0.0000000 -0.0000000  0.5000000) -0.1666667+x, 0.1666667+x, z
                    3: (21) -6⁺ 1.333333, 1.666667, z; 1.3333333 1.6666667 0.5000000
            2 of 6 Equivalent Clusters in Orbit 6
                Coordinates:
                    0.3333333 0.6666667 0.7500000 Va  O  
                    1.3333333 -0.3333333 0.7500000 Va  O  
                Invariant group:
                    1 (1): 1
                    2 (8): 2 0.3333333+x, -0.3333333+x, 0.75
                    3 (15): m 0.5+x, 0.5-x, z
                    4 (24): -1 0.8333333 0.1666667 0.7500000
                Equivalence map: 
                    0: (2) 6⁻ (0.0000000 0.0000000 0.5000000) 0.3333333, 0.6666667, z
                    1: (10) 2 (-0.5000000 -1.0000000  0.0000000) 0.75+x, 2*x, 0.5
                    2: (17) g (-0.0000000  0.0000000  0.5000000) 0.3333333+x, 0.6666667, z
                    3: (22) -6⁻ 1.333333, 0.6666667, z; 1.3333333 0.6666667 0.5000000
            3 of 6 Equivalent Clusters in Orbit 6
                Coordinates:
                    1.3333333 -0.3333333 0.2500000 Va  O  
                    0.3333333 0.6666667 0.2500000 Va  O  
                Invariant group:
                    1 (1): 1
                    2 (8): 2 0.3333333+x, -0.3333333+x, 0.25
                    3 (15): m 0.5+x, 0.5-x, z
                    4 (24): -1 0.8333333 0.1666667 0.2500000
                Equivalence map: 
                    0: (3) 3⁺ 1.333333, 0.6666667, z
                    1: (6) 2 x, 0.6666667, 0.25
                    2: (13) g (-0.5000000 -1.0000000 -0.0000000) 0.75+x, 2*x, z
                    3: (19) -3⁺ 0.3333333, 0.6666667, z; 0.3333333 0.6666667 0.2500000
            4 of 6 Equivalent Clusters in Orbit 6
                Coordinates:
                    1.3333333 2.6666667 0.2500000 Va  O  
                    0.3333333 0.6666667 0.2500000 Va  O  
                Invariant group:
                    1 (1): 1
                    2 (7): 2 x, 1.666667, 0.25
                    3 (14): m x, 2*x, z
                    4 (24): -1 0.8333333 1.6666667 0.2500000
                Equivalence map: 
                    0: (4) 3⁻ 1.333333, 1.666667, z
                    1: (7) 2 -0.1666667+x, 0.1666667+x, 0.25
                    2: (14) g (-0.5000000  0.5000000 -0.0000000) 1.25+x, 1.25-x, z
                    3: (20) -3⁻ 0.3333333, 0.6666667, z; 0.3333333 0.6666667 0.2500000
            5 of 6 Equivalent Clusters in Orbit 6
                Coordinates:
                    2.3333333 1.6666667 0.7500000 Va  O  
                    0.3333333 0.6666667 0.7500000 Va  O  
                Invariant group:
                    1 (1): 1
                    2 (6): 2 1.333333, y, 0.75
                    3 (13): m 2*x, 0.5+x, z
                    4 (24): -1 1.3333333 1.1666667 0.7500000
                Equivalence map: 
                    0: (8) 2 (0.0000000 0.0000000 0.5000000) 1.333333, 1.166667, z
                    1: (11) 2 2*x, 0.5+x, 0.5
                    2: (18) g ( 0.0000000 -0.0000000  0.5000000) 1.333333, 0.6666667+y, z
                    3: (15) m x, y, 0.5
    



```bash
# show the beginning of the clust.json file 
head basis_sets/bset.default/clust.json
```

    {
      "bspecs" : {
        "basis_function_specs" : {
          "dof_specs" : {
            "occ" : {
              "site_basis_functions" : "OCCUPATION"
            }
          },
          "dofs" : [ "occ" ],
          "global_max_poly_order" : 3,


### Evaluate correlations

Use `casm select` and `casm query` to selection configuration in the CASM database and query correlations.


```bash
# First, generate configurations to query
# This enumerates unique configurations up to volume 4 unit cells
ccasm enum -m ConfigEnumAllOccupations --max 4
```

    -- Begin: ConfigEnumAllOccupations -- 
    Input from JSON (--input or --setings):
    {
    }
    
    Input from `casm enum` options:
    {
      "max" : 4,
      "method" : "ConfigEnumAllOccupations"
    }
    
    Combined Input:
    {
      "supercells" : {
        "max" : 4
      }
    }
    
    -- Checking input -- 
    primitive_only: true
    filter: false
    verbosity: 10
    dry_run: false
    output_configurations: false
    # of initial enumeration states: 20
    
    -- Begin: ConfigEnumAllOccupations enumeration -- 
    # configurations in this project: 0
    Begin enumeration
    
    Enumerate configurations for: SCEL1_1_1_1_0_0_0
    3 configurations (3 new, 0 excluded by filter).
    
    Enumerate configurations for: SCEL2_1_2_1_0_0_0
    4 configurations (4 new, 0 excluded by filter).
    
    Enumerate configurations for: SCEL2_1_2_1_1_0_0
    3 configurations (3 new, 0 excluded by filter).
    
    Enumerate configurations for: SCEL2_1_1_2_0_0_0
    3 configurations (3 new, 0 excluded by filter).
    
    Enumerate configurations for: SCEL3_3_1_1_0_0_1
    10 configurations (10 new, 0 excluded by filter).
    
    Enumerate configurations for: SCEL3_3_1_1_0_0_2
    10 configurations (10 new, 0 excluded by filter).
    
    Enumerate configurations for: SCEL3_1_3_1_2_0_0
    16 configurations (16 new, 0 excluded by filter).
    
    Enumerate configurations for: SCEL3_3_1_1_0_2_2
    10 configurations (10 new, 0 excluded by filter).
    
    Enumerate configurations for: SCEL3_1_1_3_0_0_0
    10 configurations (10 new, 0 excluded by filter).
    
    Enumerate configurations for: SCEL4_1_4_1_0_0_0
    27 configurations (27 new, 0 excluded by filter).
    
    Enumerate configurations for: SCEL4_2_2_1_0_0_1
    27 configurations (27 new, 0 excluded by filter).
    
    Enumerate configurations for: SCEL4_1_4_1_1_0_0
    42 configurations (42 new, 0 excluded by filter).
    
    Enumerate configurations for: SCEL4_4_1_1_0_3_2
    24 configurations (24 new, 0 excluded by filter).
    
    Enumerate configurations for: SCEL4_1_4_1_2_0_0
    24 configurations (24 new, 0 excluded by filter).
    
    Enumerate configurations for: SCEL4_2_2_1_0_1_1
    21 configurations (21 new, 0 excluded by filter).
    
    Enumerate configurations for: SCEL4_2_2_1_0_0_0
    15 configurations (15 new, 0 excluded by filter).
    
    Enumerate configurations for: SCEL4_2_2_1_0_1_0
    18 configurations (18 new, 0 excluded by filter).
    
    Enumerate configurations for: SCEL4_1_2_2_0_0_0
    21 configurations (21 new, 0 excluded by filter).
    
    Enumerate configurations for: SCEL4_1_2_2_1_0_0
    24 configurations (24 new, 0 excluded by filter).
    
    Enumerate configurations for: SCEL4_1_1_4_0_0_0
    24 configurations (24 new, 0 excluded by filter).
    
    Enumeration complete
    
    # new configurations: 336
    # configurations in this project: 336
    
    Write supercell database... DONE
    Write configuration database... DONE



```bash
# Select all configurations, and write the correlation matrix
ccasm select --set-on
```

    -- Input config list: MASTER -- 
    # configs in this project: 336
    # configs included in this list: 336
    # configs selected in this list: 0
    
    -- set-on:  -- 
    selection time: 4.931e-05 (s)
    
    -- Write: Selection -- 
    write: "MASTER"
    
    -- Output config list: MASTER -- 
    # configs in this project: 336
    # configs included in this list: 336
    # configs selected in this list: 336
    



```bash
# Query correlations ('corr') and output to corr.txt
ccasm query -k corr -o corr.txt
```

    Print:
       - corr
    to "/Users/bpuchala/Work/codes/CASMcode_tutorials/v1.2/bset/ZrO/corr.txt"
    
    -- Compiling: /Users/bpuchala/Work/codes/CASMcode_tutorials/v1.2/bset/ZrO/basis_sets/bset.default/ZrO_Clexulator.cc -- 
    compile time depends on how many basis functions are included
    compile time: 0.0010143 (s)
    
      DONE.
    



```bash
# View the beginning of the file containing the correlation matrix
head corr.txt
```

    #                  name    selected               corr(0)           corr(1)           corr(2)           corr(3)           corr(4)           corr(5)           corr(6)
        SCEL1_1_1_1_0_0_0/0           1                                                1.00000000  0.00000000  0.00000000  0.00000000  0.00000000  0.00000000  0.00000000
        SCEL1_1_1_1_0_0_0/1           1                                                1.00000000  0.50000000  0.00000000  0.50000000  0.00000000  0.50000000  0.50000000
        SCEL1_1_1_1_0_0_0/2           1                                                1.00000000  1.00000000  1.00000000  1.00000000  1.00000000  1.00000000  1.00000000
        SCEL2_1_1_2_0_0_0/0           1                                                1.00000000  0.25000000  0.00000000  0.25000000  0.00000000  0.00000000  0.25000000
        SCEL2_1_1_2_0_0_0/1           1                                                1.00000000  0.50000000  0.25000000  0.50000000  0.25000000  0.00000000  0.50000000
        SCEL2_1_1_2_0_0_0/2           1                                                1.00000000  0.75000000  0.50000000  0.75000000  0.50000000  0.50000000  0.75000000
        SCEL2_1_2_1_0_0_0/0           1                                                1.00000000  0.25000000  0.00000000  0.08333333  0.00000000  0.25000000  0.08333333
        SCEL2_1_2_1_0_0_0/1           1                                                1.00000000  0.50000000  0.50000000  0.16666667  0.16666667  0.50000000  0.16666667
        SCEL2_1_2_1_0_0_0/2           1                                                1.00000000  0.75000000  0.50000000  0.58333333  0.50000000  0.75000000  0.58333333


Clean up tutorial data:


```bash
cd $start && rm -r $start/bset
```


```bash

```
