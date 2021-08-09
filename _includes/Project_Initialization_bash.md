## Defining the primitive crystal structure and degrees of freedom 

This tutorial demonstrates:
- Defining the primitive crystal structure and degrees of freedom (DoF) (the "prim")
- `casm init`: Initializing a CASM project
- `casm sym`: Getting symmetry information
- `casm info -m PrimInfo`: Querying information about a prim without initializing a project

It includes three examples:

1. [HCP Zr with O octahedral interstitial -- Occupation cluster expansion project](#occupation_clex)
2. [ZrH<sub>2</sub> -- Strain polynomial effective Hamiltonian prim](#strain_polynomial)
3. [ZrH<sub>2</sub> -- Coupled strain-displacement cluster expansion effective Hamiltonian prim](#coupled)


<a id='occupation_clex'></a>

## 1) HCP Zr with O octahedral interstitial -- Occupation cluster expansion project

### HCP Zr with octahedral interstitial O / vacancy disorder

Compared to most metals, HCP Zr has a unusually high solubility of O, up to around 35 at%, which fills octahedral interstitial positions in the HCP structure. 

This CASM project was used to:
- study the thermodynamic properties of Zr and its oxides
- fit a configurational cluster expansion effective Hamiltonian
- construct a first-principles based phase diagram 

Based on empirical knowledge of the system, this model makes the approximations:
- that the HCP Zr crystal is perfect
- octahedral interstitial positions may be either vacant or filled with oxygen atoms.

To begin, CASM requires a "prim", a primitive description of the crystal structure and allowed degrees of freedom (DoF). It is provided as a JSON formatted file.

<div class="alert alert-success">
<b>Note:</b> The Prim JSON format reference is located <a href=https://prisms-center.github.io/CASMcode_docs/formats/casm/crystallography/BasicStructure/> here</a>.
</div>

### Components of the "prim"

The "prim" defines the primitive crystal structure and degrees of freedom. 

In general the "prim" includes:
- lattice vectors
- crystal basis sites
- global degrees of freedom
- site degrees of freedom, including allowed occupant species on each basis site. 


For this particular project, it contains:

- **lattice_vectors**: Row-vector matrix of crystal lattice vectors. Units are typically Angstrom, but are ultimately determined by the method used to perform calculations. 

- **basis**: An array of crystal basis sites, including coordinate and allowed degrees of freedom. For this ZrO project, the basis sites contain:

  - **coordinate**: The location of the basis site, according to the "coordinate_mode".
  
  - **occupants**: A list of the possible occupant species that may reside at each site. The names are case sensitive, and “Va” is reserved for vacancies.

- **coordinate_mode**: Defines the units of basis site coordinates. May be one of:

  - "Cartesian": To specify basis coordinates using Cartesian coordinates:
    $$ r_{cart} = (x, y, z) $$

  - "Fractional" or "Direct": To specify basis coordinates defined in terms of the lattice vectors:
    $$ r_{cart} = L r_{frac}, $$
    where:
    - $r_{frac}$ are the coordinates in the fractional representation
    - $r_{cart}$ are the coordinates in the Cartesian representation
    - $L$ is the lattice as a column-vector matrix. 
  
<div class="alert alert-info">
For "lattice_vectors", it is common, but not required, to use the results of a fully relaxed calculation of the structure with the default occupation values. The default occupation on each site is the species listed first in "occupants". For occupation cluster expansions, ideal supercells of the prim lattice are used for the initial state of DFT calculations and it is the default reference for strain.
</div>


```bash
prim_str='
{
  "basis" : [
    {
      "coordinate" : [ 0.0000000, 0.0000000, 0.0000000 ],
      "occupants" : [ "Zr" ]
    },
    {
      "coordinate" : [ 0.6666666666, 0.3333333333, 0.5000000 ],
      "occupants" : [ "Zr" ]
    },
    {
      "coordinate" : [ 0.3333333333, 0.6666666666, 0.2500000 ],
      "occupants" : [ "Va", "O" ]
    },
    {
      "coordinate" : [ 0.3333333333, 0.6666666666, 0.7500000 ],
      "occupant_dof" : [ "Va", "O" ]
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

### Initializing a CASM Project

Running `casm init` will:
1. Read a [Prim](https://prisms-center.github.io/CASMcode_docs/formats/casm/crystallography/BasicStructure/) file and perform some checks
2. Perform a symmetry analysis
3. Generate default directories

When the prim file is read, CASM will check for a standardized representation:
- **primitive form:** 
  - CASM checks if there is an equivalent, smaller unit cell
  - If there is, CASM will print the recommended prim and prompt the user to consider using it
- **standard orientation:**
  - CASM uses a standardized comparison to identify unique lattices
  - Upon initialization:
    - CASM checks if the lattice is the Niggli reduced cell
    - CASM checks if the lattice is oriented in a standard way
  - If the input lattice is not in the standard form, CASM will print a recommended prim and prompt the user to consider using it

#### The `.casm` directory

Project files that the user should not typically modify directly, including a copy of the prim, are stored in a hidden `.casm` sub-directory of the CASM project directory. The presense or absence of the `.casm` directory is used by CASM to detect a CASM project.

### Getting started

The following code creates an `init/ZrO` subdirectory of the current working directory for purposes of this example. For a real project, modify the paths to the location where you want to create a CASM project.


```bash
# remember the directory where we start
start=$(pwd)

# make a subdirectory for our ZrO CASM project
mkdir -p $start/init/ZrO && cd $start/init/ZrO
```


```bash
# create the prim.json file
echo "$prim_str" > prim.json

# print the prim.json file contents
cat prim.json
```

    
    {
      "basis" : [
        {
          "coordinate" : [ 0.0000000, 0.0000000, 0.0000000 ],
          "occupants" : [ "Zr" ]
        },
        {
          "coordinate" : [ 0.6666666666, 0.3333333333, 0.5000000 ],
          "occupants" : [ "Zr" ]
        },
        {
          "coordinate" : [ 0.3333333333, 0.6666666666, 0.2500000 ],
          "occupants" : [ "Va", "O" ]
        },
        {
          "coordinate" : [ 0.3333333333, 0.6666666666, 0.7500000 ],
          "occupant_dof" : [ "Va", "O" ]
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
    }



```bash
# initialize the new CASM project
ccasm init

# view the project directory
ls .
```

    
    ***************************
    
    Already in a casm project. To create a project at "/Users/bpuchala/Work/codes/CASMcode_tutorials/v1.2/init/ZrO", try again using the --sub flag.
    LOG                          info_input.json
    ZrH2_GLstrain_disp_info.json prim.json
    ZrH2_GLstrain_info.json      prim_info.json
    ZrO_info.json                [1m[34mreports[39;49m[0m
    [1m[34mbasis_sets[39;49m[0m                   [1m[34msymmetry[39;49m[0m
    [1m[34mcluster_expansions[39;49m[0m           [1m[34mtraining_data[39;49m[0m


### Checking the initialized project

After initializing the project:
- Check that CASM has identified all the expected symmetries.
  - Add signicificant digits if necessary.
  - Default tolerance is 1e-5 for crysllographic comparisons.
  
<div class="alert alert-info">
If the prim symmetry is incorrect, the effective Hamiltonians that CASM generates will also have the wrong symmetry!
</div>


### The `casm sym` command

After the project is initialized, the symmetry CASM has found can be printed using the `sym` command. `sym` will print information about three important symmetry groups. Each group is a vector of representative symmetry operations. 

The symmetery operations transform a spatial coordinate $ x \rightarrow x'$ according to:

$$  x' = A*x+b, $$

where:
- $A$ is the 3x3 "operation matrix"
- $b$ is the "shift" translation vector. 

Operations may be printed either in fractional coordinates (FRAC) or Cartesian coordinates (CART).

### Important symmetry groups

The `casm sym` command provides information on three symmetry groups:

- **lattice point group**: Maps lattice points, keeps origin fixed
  - This is the point group of the Bravais lattice: the list of operations that map the lattice (i.e. all points that are integer multiples of the lattice vectors) onto itself and keep the origin fixed.
  - The "shift" vectors will always be zero. 

- **factor group**: Maps lattice points and equivalent basis sites
  - The crystal space group is the set of all symmetry operations that map the lattice onto itself and map basis sites onto equivalent basis sites (i.e. all degrees of freedom are equivalent).
  - The crystal space group is not limited to operations that keep the origin fixed, so due to the perdiodicity of the crystal the crystal space group is infinite.
  - The factor group is a finite description of the crystal space group, in which all operations that differ only by a "shift" are represented by a single operation whose "shift" lies within the primitive cell.
  - Formally, this is a group formed by the cosets of $T$ in $S$, where $T$ is the translation group of the Bravais lattice and $S$ is the crystal space group.

- **crystal point group**: Factor group, with "shift"$=\vec{0}$
 - This is the group of point operations formed by taking the factor group operations and setting their "shift" to zero.
 - Macroscopic properties of the crystal must exhibit the symmetries of the crystal point group. 
 - It is by definition a subgroup of the lattice point group.





```bash
# print the factor group using the Cartesian representation
ccasm sym --coord CART --factor-group
```

    Factor group:
    24 # Cartesian representation of group containing 24 elements:
    
    1  Identity Operation
    Symmetry Operation Matrix                            Shift 
       1.000000000   0.000000000   0.000000000           0.000000000
       0.000000000   1.000000000   0.000000000           0.000000000
       0.000000000   0.000000000   1.000000000          -0.000000000
    Time Reversal: no
    
    2  60-degree Screw Operation along axis               0.000000    0.000000    1.000000           
     Screw Vector: 0.000000 0.000000 2.584339
    Symmetry Operation Matrix                            Shift 
       0.500000000  -0.866025404   0.000000000           1.616993428
       0.866025404   0.500000000   0.000000000           0.933571589
       0.000000000   0.000000000   1.000000000           2.584339170
    Time Reversal: no
    
    3  300-degree Screw Operation along axis               0.000000    0.000000    1.000000           
     Screw Vector: 0.000000 0.000000 2.584339
    Symmetry Operation Matrix                            Shift 
       0.500000000   0.866025404   0.000000000           1.616993432
      -0.866025404   0.500000000   0.000000000           0.933571591
       0.000000000   0.000000000   1.000000000           2.584339170
    Time Reversal: no
    
    4  120-degree Rotation Operation about axis 0.000000 0.000000 1.000000
    Symmetry Operation Matrix                            Shift 
      -0.500000000  -0.866025404   0.000000000          -0.000000002
       0.866025404  -0.500000000   0.000000000          -0.000000001
       0.000000000   0.000000000   1.000000000          -0.000000000
    Time Reversal: no
    
    5  240-degree Rotation Operation about axis 0.000000 0.000000 1.000000
    Symmetry Operation Matrix                            Shift 
      -0.500000000   0.866025404   0.000000000           0.000000002
      -0.866025404  -0.500000000   0.000000000           0.000000001
       0.000000000   0.000000000   1.000000000          -0.000000000
    Time Reversal: no
    
    6  180-degree Rotation Operation about axis  0.5000000 -0.8660254   0.000000
    Symmetry Operation Matrix                            Shift 
      -0.500000000  -0.866025404   0.000000000           1.616993428
      -0.866025404   0.500000000   0.000000000           0.933571591
       0.000000000   0.000000000  -1.000000000           2.584339170
    Time Reversal: no
    
    7  180-degree Screw Operation along axis                1.000000 2.403090e-16     0.000000           
     Screw Vector:     1.616993 3.885781e-16     0.000000
    Symmetry Operation Matrix                            Shift 
       1.000000000  -0.000000000   0.000000000           1.616993430
       0.000000000  -1.000000000   0.000000000           0.933571590
       0.000000000   0.000000000  -1.000000000           2.584339170
    Time Reversal: no
    
    8  180-degree Screw Operation along axis              0.5000000   0.8660254   -0.000000           
     Screw Vector: 0.8084967  1.400357 -0.000000
    Symmetry Operation Matrix                            Shift 
      -0.500000000   0.866025404   0.000000000           1.616993432
       0.866025404   0.500000000   0.000000000           0.933571589
       0.000000000   0.000000000  -1.000000000           2.584339170
    Time Reversal: no
    
    9  180-degree Screw Operation along axis               0.000000    0.000000    1.000000           
     Screw Vector: 0.000000 0.000000 2.584339
    Symmetry Operation Matrix                            Shift 
      -1.000000000   0.000000000   0.000000000           1.616993430
       0.000000000  -1.000000000   0.000000000           0.933571590
       0.000000000   0.000000000   1.000000000           2.584339170
    Time Reversal: no
    
    10  180-degree Rotation Operation about axis  0.8660254 -0.5000000   0.000000
    Symmetry Operation Matrix                            Shift 
       0.500000000  -0.866025404   0.000000000          -0.000000002
      -0.866025404  -0.500000000   0.000000000           0.000000001
       0.000000000   0.000000000  -1.000000000           0.000000000
    Time Reversal: no
    
    11  180-degree Rotation Operation about axis 3.330669e-16     1.000000    -0.000000
    Symmetry Operation Matrix                            Shift 
      -1.000000000   0.000000000   0.000000000          -0.000000000
      -0.000000000   1.000000000   0.000000000           0.000000000
       0.000000000   0.000000000  -1.000000000           0.000000000
    Time Reversal: no
    
    12  180-degree Rotation Operation about axis 0.8660254 0.5000000  0.000000
    Symmetry Operation Matrix                            Shift 
       0.500000000   0.866025404   0.000000000           0.000000002
       0.866025404  -0.500000000   0.000000000          -0.000000001
       0.000000000   0.000000000  -1.000000000           0.000000000
    Time Reversal: no
    
    13  Mirror Operation with plane normal  0.5000000 -0.8660254   0.000000
    Symmetry Operation Matrix                            Shift 
       0.500000000   0.866025404   0.000000000           0.000000002
       0.866025404  -0.500000000   0.000000000          -0.000000001
       0.000000000   0.000000000   1.000000000          -0.000000000
    Time Reversal: no
    
    14  Mirror Operation with plane normal     1.000000 2.403090e-16     0.000000
    Symmetry Operation Matrix                            Shift 
      -1.000000000   0.000000000   0.000000000          -0.000000000
      -0.000000000   1.000000000   0.000000000           0.000000000
       0.000000000   0.000000000   1.000000000          -0.000000000
    Time Reversal: no
    
    15  Mirror Operation with plane normal 0.5000000 0.8660254 -0.000000
    Symmetry Operation Matrix                            Shift 
       0.500000000  -0.866025404   0.000000000          -0.000000002
      -0.866025404  -0.500000000   0.000000000           0.000000001
       0.000000000   0.000000000   1.000000000          -0.000000000
    Time Reversal: no
    
    16  Mirror Operation with plane normal 0.000000 0.000000 1.000000
    Symmetry Operation Matrix                            Shift 
       1.000000000   0.000000000   0.000000000           0.000000000
       0.000000000   1.000000000   0.000000000           0.000000000
       0.000000000   0.000000000  -1.000000000           0.000000000
    Time Reversal: no
    
    17  Glide Operation with plane normal 0.8660254      -0.5         0
    Glide Vector: 0.8084967  1.400357  2.584339
    Symmetry Operation Matrix                            Shift 
      -0.500000000   0.866025404   0.000000000           1.616993432
       0.866025404   0.500000000   0.000000000           0.933571589
       0.000000000   0.000000000   1.000000000           2.584339170
    Time Reversal: no
    
    18  Glide Operation with plane normal 3.330669e-16            1           -0
    Glide Vector:      1.616993 -5.551115e-16      2.584339
    Symmetry Operation Matrix                            Shift 
       1.000000000  -0.000000000   0.000000000           1.616993430
       0.000000000  -1.000000000   0.000000000           0.933571590
       0.000000000   0.000000000   1.000000000           2.584339170
    Time Reversal: no
    
    19  Glide Operation with plane normal 0.8660254       0.5         0
    Glide Vector:            0 1.110223e-16     2.584339
    Symmetry Operation Matrix                            Shift 
      -0.500000000  -0.866025404   0.000000000           1.616993428
      -0.866025404   0.500000000   0.000000000           0.933571591
       0.000000000   0.000000000   1.000000000           2.584339170
    Time Reversal: no
    
    20  120-degree Rotoinversion Operation about axis 0.000000 0.000000 1.000000
    Symmetry Operation Matrix                            Shift 
       0.500000000   0.866025404   0.000000000           1.616993432
      -0.866025404   0.500000000   0.000000000           0.933571591
       0.000000000   0.000000000  -1.000000000           2.584339170
    Time Reversal: no
    
    21  240-degree Rotoinversion Operation about axis 0.000000 0.000000 1.000000
    Symmetry Operation Matrix                            Shift 
       0.500000000  -0.866025404   0.000000000           1.616993428
       0.866025404   0.500000000   0.000000000           0.933571589
       0.000000000   0.000000000  -1.000000000           2.584339170
    Time Reversal: no
    
    22  60-degree Rotoinversion Operation about axis 0.000000 0.000000 1.000000
    Symmetry Operation Matrix                            Shift 
      -0.500000000   0.866025404   0.000000000           0.000000002
      -0.866025404  -0.500000000   0.000000000           0.000000001
       0.000000000   0.000000000  -1.000000000           0.000000000
    Time Reversal: no
    
    23  300-degree Rotoinversion Operation about axis 0.000000 0.000000 1.000000
    Symmetry Operation Matrix                            Shift 
      -0.500000000  -0.866025404   0.000000000          -0.000000002
       0.866025404  -0.500000000   0.000000000          -0.000000001
       0.000000000   0.000000000  -1.000000000           0.000000000
    Time Reversal: no
    
    24  Inversion Operation
    Symmetry Operation Matrix                            Shift 
      -1.000000000   0.000000000   0.000000000           1.616993430
       0.000000000  -1.000000000   0.000000000           0.933571590
       0.000000000   0.000000000  -1.000000000           2.584339170
    Time Reversal: no
    


### Brief symmetry representation

- Use `ccasm sym --brief` to print a brief description of:
  - The lattice point group
  - The factor group
  - The crystal point group
- The brief description follows the conventions of the International Tables for Crystallography. 
- The option `--coord CART` can be used to print the Cartesian representation.


```bash
# view the lattice point group (brief form)
ccasm sym --brief --lattice-point-group
```

    Lattice point group: (Direct representation)
    1: 1
    2: 6⁺ 0, 0, z
    3: 6⁻ 0, 0, z
    4: 3⁺ 0, 0, z
    5: 3⁻ 0, 0, z
    6: 2 0, y, 0
    7: 2 x, 0, 0
    8: 2 x, x, 0
    9: 2 0, 0, z
    10: 2 x, -x, 0
    11: 2 x, 2*x, 0
    12: 2 2*x, x, 0
    13: m 2*x, x, z
    14: m x, 2*x, z
    15: m x, -x, z
    16: m x, y, 0
    17: m x, x, z
    18: m x, 0, z
    19: m 0, y, z
    20: -3⁺ 0, 0, z; 0.0000000 0.0000000 0.0000000
    21: -3⁻ 0, 0, z; 0.0000000 0.0000000 0.0000000
    22: -6⁺ 0, 0, z; 0.0000000 0.0000000 0.0000000
    23: -6⁻ 0, 0, z; 0.0000000 0.0000000 0.0000000
    24: -1 0.0000000 0.0000000 0.0000000



```bash
# view the factor group (brief form)
ccasm sym --brief --factor-group
```

    Factor group: (Direct representation)
    1: 1
    2: 6⁺ (0.0000000 0.0000000 0.5000000) 0.3333333, 0.6666667, z
    3: 6⁻ (0.0000000 0.0000000 0.5000000) 0.3333333, -0.3333333, z
    4: 3⁺ 0, 0, z
    5: 3⁻ 0, 0, z
    6: 2 0.3333333, y, 0.25
    7: 2 (0.5000000 0.0000000 0.0000000) x, 0.1666667, 0.25
    8: 2 (0.5000000 0.5000000 0.0000000) 0.08333333+x, -0.08333333+x, 0.25
    9: 2 (0.0000000 0.0000000 0.5000000) 0.3333333, 0.1666667, z
    10: 2 x, -x, 0
    11: 2 x, 2*x, 0
    12: 2 2*x, x, 0
    13: m 2*x, x, z
    14: m x, 2*x, z
    15: m x, -x, z
    16: m x, y, 0
    17: g (0.5000000 0.5000000 0.5000000) 0.08333333+x, -0.08333333+x, z
    18: g ( 0.5000000 -0.0000000  0.5000000) 0.08333333+x, 0.1666667, z
    19: g (0.0000000 0.0000000 0.5000000) 0.3333333, 0.1666667+y, z
    20: -3⁺ 0.3333333, -0.3333333, z;  0.3333333 -0.3333333  0.2500000
    21: -3⁻ 0.3333333, 0.6666667, z; 0.3333333 0.6666667 0.2500000
    22: -6⁺ 0, 0, z;  0.0000000 -0.0000000  0.0000000
    23: -6⁻ 0, 0, z; -0.0000000 -0.0000000  0.0000000
    24: -1 0.3333333 0.1666667 0.2500000



```bash
# view the crystal point group (brief form)
ccasm sym --brief --crystal-point-group
```

    Crystal point group: (Direct representation)
    1: 1
    2: 6⁺ 0, 0, z
    3: 6⁻ 0, 0, z
    4: 3⁺ 0, 0, z
    5: 3⁻ 0, 0, z
    6: 2 0, y, 0
    7: 2 x, 0, 0
    8: 2 x, x, 0
    9: 2 0, 0, z
    10: 2 x, -x, 0
    11: 2 x, 2*x, 0
    12: 2 2*x, x, 0
    13: m 2*x, x, z
    14: m x, 2*x, z
    15: m x, -x, z
    16: m x, y, 0
    17: m x, x, z
    18: m x, 0, z
    19: m 0, y, z
    20: -3⁺ 0, 0, z; 0.0000000 0.0000000 0.0000000
    21: -3⁻ 0, 0, z; 0.0000000 0.0000000 0.0000000
    22: -6⁺ 0, 0, z; 0.0000000 0.0000000 0.0000000
    23: -6⁻ 0, 0, z; 0.0000000 0.0000000 0.0000000
    24: -1 0.0000000 0.0000000 0.0000000


### The `info` method

The `info` method gives more direct and flexible access to CASM data and methods via JSON input and output. 

It currently allows for getting detailed information about a prim, supercells, and the neighbor lists used in effective Hamiltonian evalautions, with additional options planned for the future. 

For any data that does not require a CASM project it will work whether or not a CASM project exists, but if called from within a CASM project, then that project will be used for default input values such as the prim. 


```bash
# list available "info" methods
ccasm info -h
```

    'casm info' usage:
      -s [ --settings ] <path>     Settings input file specifying which parameters 
                                   should be used. See 'casm format --info'.
      -i [ --input ] arg           String specifying input settings. See 'casm 
                                   format --info'.
      -h [ --help ]                Print help message including a list of all 
                                   available methods.
      --desc <infomethod>          Print extended usage description. Use '--desc 
                                   [MethodName [MethodName2...]]' for detailed 
                                   method descriptions. Partial matches of method 
                                   names are acceptable.
      -m [ --method ] <infomethod> Method to use: Can use method name (including 
                                   partial matches) or index.
    
    The `casm info` methods are:
      0) NeighborListInfo
      1) PrimInfo
      2) SupercellInfo
    
    For complete options description, use 'casm info --desc MethodName'.
    



```bash
# list input and output options for a particular method
ccasm info --desc PrimInfo
```

    
    PrimInfo: 
    
    Get information about a prim structure.
    
      prim: JSON object (optional, default=prim of current project) 
        See `casm format --prim` for details on the prim format.
    
      properties: array of string                                      
        An array of strings specifying which prim properties to output.
        The allowed options are:                                       
    
         asymmetric_unit                 Sets of indices of equivalent basis sites
    
         basis_rep                       Describes how integral site coordinates transform under application
                                         of symmetry. The element `basis_rep[i]` contains `matrix`, `sublattice_permute`,
                                         and `sublattice_shift`, which describe how the `i`th factor group
                                         operation transforms a basis site (b, r_frac) -> (b', r_frac')
                                         according to: `b' = sublattice_permute[b]` and `r_frac' = matrix
                                         * r_frac + sublattice_shift[b]`, where `b` is the basis index
                                         and `r_frac` is the integer unit cell coordinate of a site.
    
         crystal_point_group             Crystal point group, in JSON format.
    
         crystal_point_group_name        Crystal point group name.
    
         crystal_point_group_size        Crystal point group size
    
         factor_group                    Factor group, in JSON format.
    
         factor_group_name               Factor group name.
    
         factor_group_size               Factor group size.
    
         is_primitive                    Returns true if structure is the primitive structure
    
         lattice                         Lattice vectors, unrolled: (a0, a1, a2, b0, ...)
    
         lattice_column_matrix           Lattice vectors, as column vector matrix
    
         lattice_params                  Lattice parameters, as: (a, b, c, alpha, beta, gamma)
    
         lattice_point_group             Lattice point group, in JSON format.
    
         lattice_point_group_name        Lattice point group name.
    
         lattice_point_group_size        Lattice point group size.
    
         occ_permutation_rep             The permutation occ_permutation_rep[b][i] describes how the `i`th
                                         factor group operation transforms anisotropic occupant values
                                         on sublattice `b`. The convention when applying symmetry operations
                                         to transform occupation values is to first transform the occupant
                                         value on site `l` (which is on sublattice `b`) according to `occ(l)
                                         = occ_permutation_rep[b][i][occ(l)]`, then to permute occupant
                                         values among sites.
    
         primitive                       Returns the primitive structure, in prim JSON format.
    
         volume                          Prim cell volume (length^3)
    
    


### Using `info` 

As an example, we can get information about the ZrO prim without initializing a CASM project.

In this case, we request the indices of the sites in each orbit of the asymmetric unit.

The asymmetric unit is the minimum set of sites necessary to generate all the other sites upon application of the factor group.

In other words, the asymmetric unit is the set of symmetrically distinct sites.


```bash
# create and check the input file
info_input_str='{
  "prim": '${prim_str}',
    "properties": [
      "asymmetric_unit"
  ]
}'
echo $info_input_str
```

    { "prim": { "basis" : [ { "coordinate" : [ 0.0000000, 0.0000000, 0.0000000 ], "occupants" : [ "Zr" ] }, { "coordinate" : [ 0.6666666666, 0.3333333333, 0.5000000 ], "occupants" : [ "Zr" ] }, { "coordinate" : [ 0.3333333333, 0.6666666666, 0.2500000 ], "occupants" : [ "Va", "O" ] }, { "coordinate" : [ 0.3333333333, 0.6666666666, 0.7500000 ], "occupant_dof" : [ "Va", "O" ] } ], "coordinate_mode" : "Fractional", "description" : "hcp Zr with octahedral interstitial O ", "lattice_vectors" : [ [ 3.23398686, 0.00000000, 0.00000000 ], [ -1.61699343, 2.80071477, 0.00000000 ], [ -0.00000000, 0.00000000, 5.16867834 ] ], "title" : "ZrO" }, "properties": [ "asymmetric_unit" ] }



```bash
# run the `info` command and store output to a file `ZrO_info.json`
ccasm info -m PrimInfo -i "$info_input_str" > ZrO_info.json
```

### Example using `jq`

For those comfortable with the command line, the [`jq` program](https://stedolan.github.io/jq/) is a very useful tool for parsing JSON data.

The shows just two examples using `jq`:
- Printing the keys from the top level of the document
- Printing the value of one of the attributes


```bash
# list names of output properties in ZrO_info.json
jq 'keys' ZrO_info.json

echo "asymmetric_unit:"
jq '.asymmetric_unit' ZrO_info.json
```

    [1;39m[
      [0;32m"asymmetric_unit"[0m[1;39m
    [1;39m][0m
    asymmetric_unit:
    [1;39m[
      [1;39m[
        [0;39m0[0m[1;39m,
        [0;39m1[0m[1;39m
      [1;39m][0m[1;39m,
      [1;39m[
        [0;39m2[0m[1;39m,
        [0;39m3[0m[1;39m
      [1;39m][0m[1;39m
    [1;39m][0m


<a id='strain_polynomial'></a>

## 2) ZrH<sub>2</sub> -- Strain polynomial effective Hamiltonian prim

<div class="alert alert-success">
<b>Note:</b> The Prim JSON format reference is located <a href=https://prisms-center.github.io/CASMcode_docs/formats/casm/crystallography/BasicStructure/> here</a>.
</div>

All continuous DoF are represented as vectors having a standard basis that is related to the fixed reference frame of the crystal. The DoF object may optionally encode a user-specified basis in terms of the standard basis. The user-specified basis may fully span the standard basis or only a subspace. Within a `"dofs"` object, each DoF is given by the key/object pair `"<dofname>" : {...}` where `<dofname>` is the name specifier of a particular DoF type and the associated object specifies non-default options.

The options include:

- `axis_names`: array of string

  Names given to the user-specified basis vectors when writing basis function formulas. The length of `axis_names` must match the number of rows in `basis`. 
  
- `basis`: row-vector matrix

  The basis provides the user-specified basis vectors in terms of the standard basis. The number of rows is the dimension of user-specified basis. The number of columns must equal the number of dimensions in the standard basis (i.e. 3 for displacement, 6 for strain).
  

#### Example: Strain DoF, using the Green-Lagrange strain metric with custom user basis excluding shear strain:

    "dofs" : {
      "GLstrain" : {
        "axis_names" : ["E_{xx}", "E_{yy}", "E_{zz}"], 
        "basis" : [
          [1.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
          [0.0, 1.0, 0.0, 0.0, 0.0, 0.0],
          [0.0, 0.0, 1.0, 0.0, 0.0, 0.0]
        ]
      }
    }


Allowed global DoF include:

- "GLstrain": Green-Lagrange strain metric, $\frac{1}{2}(C-I)$
- "Hstrain": Hencky strain metric, $\frac{1}{2}ln(C)$
- "Bstrain": Biot strain metric, $(U-I)$ 
- "Ustrain": Stretch tensor, $U$
- "EAstrain": Euler-Almansi strain metric, $\frac{1}{2}(I-(F F^{T})^{-1})$

The strain metrics are defined in terms of the deformation gradient tensor, $F$, and Green's deformation tensor, $C$. The deformation gradient tensor relates the strained and unstrained lattices through $L^{strained} = F * L^{ideal}$, and can be decomposed, via $F = R * U$, into a rotation tensor, $R$, and stretch tensor, $U$. Green's deformation tensor, $C = F^{T}*F$, excludes rigid rotations.

For all strain metrics, the standard basis is:

$$ [E_{xx}, E_{yy}, E_{zz}, \sqrt(2)E_{yz}, \sqrt(2)E_{xz}, \sqrt(2)E_{xy}],$$

and the default axis names are:

$$[e_1, e_2, e_3, e_4, e_5, e_6].$$



```bash
ZrH2_GLstrain_prim_str='{
  "basis" : [
    {
      "coordinate" : [ 0.000000000000, 0.000000000000, 0.000000000000 ],
      "occupants" : [ "Zr" ]
    },
    {
      "coordinate" : [ 0.250000000000, 0.250000000000, 0.250000000000 ],
      "occupants" : [ "H" ]
    },
    {
      "coordinate" : [ 0.750000000000, 0.750000000000, 0.750000000000 ],
      "occupants" : [ "H" ]
    }
  ],
  "dofs": {
      "GLstrain": {}
  },
  "coordinate_mode" : "Fractional",
  "lattice_vectors" : [
    [ 0.000000000000, 2.410696500000, 2.410696500000 ],
    [ 2.410696500000, 0.000000000000, 2.410696500000 ],
    [ 2.410696500000, 2.410696500000, 0.000000000000 ]
  ],
  "title" : "ZrH2"
}'

ZrH2_GLstrain_info_input_str='{ 
  "prim": '${ZrH2_GLstrain_prim_str}',
  "properties": [
    "factor_group"
  ]
}'
echo $ZrH2_GLstrain_info_input_str > info_input.json
cat info_input.json
```

    { "prim": { "basis" : [ { "coordinate" : [ 0.000000000000, 0.000000000000, 0.000000000000 ], "occupants" : [ "Zr" ] }, { "coordinate" : [ 0.250000000000, 0.250000000000, 0.250000000000 ], "occupants" : [ "H" ] }, { "coordinate" : [ 0.750000000000, 0.750000000000, 0.750000000000 ], "occupants" : [ "H" ] } ], "dofs": { "GLstrain": {} }, "coordinate_mode" : "Fractional", "lattice_vectors" : [ [ 0.000000000000, 2.410696500000, 2.410696500000 ], [ 2.410696500000, 0.000000000000, 2.410696500000 ], [ 2.410696500000, 2.410696500000, 0.000000000000 ] ], "title" : "ZrH2" }, "properties": [ "factor_group" ] }



```bash
pwd
```

    /Users/bpuchala/Work/codes/CASMcode_tutorials/v1.2/init/ZrO



```bash
# write the factor group information to the `ZrH2_GLstrain_info.json`
ccasm info -m PrimInfo -i "$ZrH2_GLstrain_info_input_str" > ZrH2_GLstrain_info.json

# list names of output properties in ZrH2_GLstrain_info.json
cat ZrH2_GLstrain_info.json | jq 'keys'
```

    [1;39m[
      [0;32m"factor_group"[0m[1;39m
    [1;39m][0m



```bash
# get factor group size
cat ZrH2_GLstrain_info.json | jq '.factor_group.group_operations | length'
```

    [0;39m48[0m


<a id='coupled'></a>

## 3) ZrH<sub>2</sub> -- Coupled strain-displacement cluster expansion effective Hamiltonian prim

<div class="alert alert-success">
<b>Note:</b> The Prim JSON format reference is located <a href=https://prisms-center.github.io/CASMcode_docs/formats/casm/crystallography/BasicStructure/> here</a>.
</div>

Continuous site DoF are specified with a "dofs" parameter that is equivalent to the global "dofs" paremeter, but specified for each basis site.

#### Example: Displacement DoF, in the xy plane only

    "dofs" : {
      "disp" : {
        "axis_names" : ["dx", "dy"], 
        "basis" : [
          [1.0, 0.0, 0.0],
          [0.0, 1.0, 0.0]
        ]
      }
    }


Allowed site DoF include:

- "disp": Displacement, with standard basis $[dx, dy, dz]$

Additionally, for this prim we will use the "selectivedynamics" species property to indicate that DFT calculations should fix Zr atoms at the position defined by the strain and displacement DoF, but allow H atoms to relax. Molecular occupants, and atomic occupants with user-specified properties are specified using the `"species"` parameter. The JSON format for Molecule specifications is given [here](https://prisms-center.github.io/CASMcode_docs/formats/casm/crystallography/BasicStructure/#molecule-json-object).



```bash
ZrH2_GLstrain_disp_prim_str='{
  "basis" : [
    {
      "coordinate" : [ 0.0000000, 0.0000000, 0.0000000 ],
      "occupant_dof" : [ "Zr" ],
      "dofs": {
        "disp": {}
      }
    },
    {
      "coordinate" : [ 0.2500000, 0.2500000, 0.2500000 ],
      "occupant_dof" : [ "H" ]
    },
    {
      "coordinate" : [ 0.7500000, 0.7500000, 0.7500000 ],
      "occupant_dof" : [ "H" ]
    }
  ],
  "species" : {
    "H": {
      "properties": {
        "selectivedynamics": {
          "value": [1, 1, 1]
        }
      }
    },
    "Zr": {
      "properties": {
        "selectivedynamics": {
          "value": [0, 0, 0]
        }
      }
    }
  },
  "dofs" : {
      "GLstrain" : {}
  },
  "coordinate_mode" : "Fractional",
  "description" : "Cubic ZrH_{2}",
  "lattice_vectors" : [
    [0.0      , 2.4106965, 2.4106965],
    [2.4106965, 0.0      , 2.4106965],
    [2.4106965, 2.4106965, 0.0      ]
  ],
  "title" : "ZrH2"
}'

ZrH2_GLstrain_disp_info_input_str='{
  "prim": '${ZrH2_GLstrain_disp_prim_str}',
  "properties": [
    "factor_group"
  ]
}'
```


```bash
ccasm info -m PrimInfo -i "$ZrH2_GLstrain_disp_info_input_str" > ZrH2_GLstrain_disp_info.json

# list names of output properties in ZrH2_GLstrain_disp_info.json
jq 'keys' ZrH2_GLstrain_disp_info.json
```

    [1;39m[
      [0;32m"factor_group"[0m[1;39m
    [1;39m][0m



```bash
# get factor group size
cat ZrH2_GLstrain_info.json | jq '.factor_group.group_operations | length'
```

    [0;39m48[0m


### The following cleans up the data that was created


```bash
cd $start && rm -r $start/init
```
