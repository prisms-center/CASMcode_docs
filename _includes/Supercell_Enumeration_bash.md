# Introduction to Supercells

Within CASM, a configuration is used to represent a single crystal state.

A configuration is itself defined in terms of:
- The primitive crystal structure and allowed degrees of freedom (DoF) (the "prim").
- A supercell, which specifies the translational periodicity of the configuration. 
- DoF values, including:
  - Site DoF "within" the supercell (i.e. the translationally unique part of the crystal state)
    - Discrete occupation DoF (atom type)
    - Continuous site DoF (displacment or magnetic spin) 
  - Continuous global DoF (strain)


Supercells may be generated automatically when enumerating configurations, but it is also common to enumerate supercells independently and then choose which supercells to enumerate configurations in.

## Supercell lattices

Supercell lattices are multiples of the prim lattice: 

$$ L^{scel} = L^{prim} * T, $$

where:

- $T$ is a 3x3 integer transformation matrix
- $L^{scel}$ and $L^{prim}$ are the supercell and prim lattices, as column vector matrices 


## Equivalence of supercell lattices

Two supercell lattices, $L^{scel}$ and ${L^{scel}}^{\prime}$ are symmetrically equivalent if:

$$ {L^{scel}}^{\prime} = A*L^{scel}*T, $$

where:

- $A$ is a crystal point group operation matrix
- $T$ is an integer transformation matrix

Of all the symmetrically equivalent supercell lattices, CASM deterministically chooses one to be the "canonical" supercell lattice, based on an algorithm that favors symmetric, positive, diagonal $T$.

## Supercell naming convention

CASM gives supercells a unique name of the form `SCELV_A_B_C_D_E_F` based on:
- The supercell volume, V, which is the determinant of the supercell transformation matrix, $T$
- The six non-zero elements (A-F) of the hermite normal form of $T$. The hermite normal form 


# Supercell Enumeration

The `ScelEnum` method of `enum` enables enumerating supercells. It includes options to control enumerating supercells within a range of volumes, as multiples of a non-primitive unit cell, and restricted to particular directions (i.e. 1d or 2d supercells).

In the following we give examples of supercell enumeration. A complete list of `ScelEnum` method parameters can be obtained with:

    ccasm enum --desc ScelEnum
    
The examples will all use this prim structure for the system of HCP Zr with O or vacancy occupation of the octahedral interstitial sites:


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
mkdir -p $start/enum/ZrO && cd $start/enum/ZrO

echo "$prim_str" > prim.json
ccasm init
```

    
    ***************************
    
    Initializing CASM project 'ZrO'
    Creating CASM project directory tree at: "/Users/bpuchala/Work/codes/CASMcode_v0.2.X_reference/doc/examples/python_kernel/enum/ZrO"
    Writing prim file: "/Users/bpuchala/Work/codes/CASMcode_v0.2.X_reference/doc/examples/python_kernel/enum/ZrO/.casm/prim.json"
      DONE
    


## Enumerate supercells up to a maximum volume

Enumerate all supercells of volume 4 or less.


```bash
ccasm enum -m ScelEnum -i '{"max": 4}'
```

    -- Begin: ScelEnumByProps -- 
      Generated: SCEL1_1_1_1_0_0_0
      Generated: SCEL2_1_2_1_0_0_0
      Generated: SCEL2_1_2_1_1_0_0
      Generated: SCEL2_1_1_2_0_0_0
      Generated: SCEL3_3_1_1_0_0_1
      Generated: SCEL3_3_1_1_0_0_2
      Generated: SCEL3_1_3_1_2_0_0
      Generated: SCEL3_3_1_1_0_2_2
      Generated: SCEL3_1_1_3_0_0_0
      Generated: SCEL4_1_4_1_0_0_0
      Generated: SCEL4_2_2_1_0_0_1
      Generated: SCEL4_1_4_1_1_0_0
      Generated: SCEL4_4_1_1_0_3_2
      Generated: SCEL4_1_4_1_2_0_0
      Generated: SCEL4_2_2_1_0_1_1
      Generated: SCEL4_2_2_1_0_0_0
      Generated: SCEL4_2_2_1_0_1_0
      Generated: SCEL4_1_2_2_0_0_0
      Generated: SCEL4_1_2_2_1_0_0
      Generated: SCEL4_1_1_4_0_0_0
      DONE.
    
    Committing database...  DONE


## Enumerate supercells within a range of volumes

Enumerate all supercells of volume 6 or 7:


```bash
ccasm enum -m ScelEnum -i '{"min": 6, "max": 7}'
```

    -- Begin: ScelEnumByProps -- 
      Generated: SCEL6_1_6_1_0_0_0
      Generated: SCEL6_3_2_1_0_0_1
      Generated: SCEL6_6_1_1_0_0_4
      Generated: SCEL6_1_6_1_5_0_0
      Generated: SCEL6_6_1_1_0_5_2
      Generated: SCEL6_6_1_1_0_5_3
      Generated: SCEL6_1_6_1_4_0_0
      Generated: SCEL6_3_2_1_0_1_1
      Generated: SCEL6_3_2_1_0_1_2
      Generated: SCEL6_1_6_1_3_0_0
      Generated: SCEL6_6_1_1_0_3_2
      Generated: SCEL6_2_3_1_0_1_1
      Generated: SCEL6_1_3_2_0_0_0
      Generated: SCEL6_3_1_2_0_0_2
      Generated: SCEL6_1_3_2_1_0_0
      Generated: SCEL6_3_1_2_0_2_2
      Generated: SCEL6_1_2_3_0_0_0
      Generated: SCEL6_1_2_3_1_0_0
      Generated: SCEL6_1_1_6_0_0_0
      Generated: SCEL7_7_1_1_0_0_1
      Generated: SCEL7_7_1_1_0_0_2
      Generated: SCEL7_7_1_1_0_0_5
      Generated: SCEL7_1_7_1_1_0_0
      Generated: SCEL7_7_1_1_0_3_4
      Generated: SCEL7_7_1_1_0_5_5
      Generated: SCEL7_7_1_1_0_5_6
      Generated: SCEL7_1_7_1_5_0_0
      Generated: SCEL7_7_1_1_0_4_2
      Generated: SCEL7_1_7_1_3_0_0
      Generated: SCEL7_1_1_7_0_0_0
      DONE.
    
    Committing database...  DONE


## Enumerate supercells of a non-primitive unit cell

Using the 2x2x2 supercell as the base unit cell, enumerate up to volume 4 times its volume:


```bash
ccasm enum -m ScelEnum -i '{
  "max": 4, 
  "unit_cell": [
    [2, 0, 0],
    [0, 2, 0],
    [0, 0, 2]
  ]
}'
```

    -- Begin: ScelEnumByProps -- 
      Generated: SCEL8_2_2_2_0_0_0
      Generated: SCEL16_2_4_2_0_0_0
      Generated: SCEL16_2_4_2_2_0_0
      Generated: SCEL16_2_2_4_0_0_0
      Generated: SCEL24_6_2_2_0_0_2
      Generated: SCEL24_6_2_2_0_0_4
      Generated: SCEL24_2_6_2_4_0_0
      Generated: SCEL24_6_2_2_0_4_4
      Generated: SCEL24_2_2_6_0_0_0
      Generated: SCEL32_2_8_2_0_0_0
      Generated: SCEL32_4_4_2_0_0_2
      Generated: SCEL32_2_8_2_2_0_0
      Generated: SCEL32_8_2_2_0_6_4
      Generated: SCEL32_2_8_2_4_0_0
      Generated: SCEL32_4_4_2_0_2_2
      Generated: SCEL32_4_4_2_0_0_0
      Generated: SCEL32_4_4_2_0_2_0
      Generated: SCEL32_2_4_4_0_0_0
      Generated: SCEL32_2_4_4_2_0_0
      Generated: SCEL32_2_2_8_0_0_0
      DONE.
    
    Committing database...  DONE


## Restrict supercell enumeration to particular directions

<i>Note: The "dirs" values "a", "b", "c" indicate the first, second, and third lattice vector after applying "unit_cell".</i>

Using the 2x2x2 supercell as the basis unit cell, enumerate 2d supercells in the HCP basal plane. 


```bash
ccasm enum -m ScelEnum -i '{
  "max": 9, 
  "unit_cell": [
    [2, 0, 0],
    [0, 2, 0],
    [0, 0, 2]
  ],
  "dirs": "ab"
}'
```

    -- Begin: ScelEnumByProps -- 
      Generated: SCEL8_2_2_2_0_0_0 (already existed)
      Generated: SCEL16_2_4_2_0_0_0 (already existed)
      Generated: SCEL24_6_2_2_0_0_2 (already existed)
      Generated: SCEL24_6_2_2_0_0_4 (already existed)
      Generated: SCEL32_2_8_2_0_0_0 (already existed)
      Generated: SCEL32_4_4_2_0_0_2 (already existed)
      Generated: SCEL32_4_4_2_0_0_0 (already existed)
      Generated: SCEL40_10_2_2_0_0_2
      Generated: SCEL40_10_2_2_0_0_4
      Generated: SCEL48_2_12_2_0_0_0
      Generated: SCEL48_6_4_2_0_0_2
      Generated: SCEL48_12_2_2_0_0_8
      Generated: SCEL56_14_2_2_0_0_2
      Generated: SCEL56_14_2_2_0_0_4
      Generated: SCEL56_14_2_2_0_0_10
      Generated: SCEL64_2_16_2_0_0_0
      Generated: SCEL64_8_4_2_0_0_2
      Generated: SCEL64_8_4_2_0_0_6
      Generated: SCEL64_16_2_2_0_0_10
      Generated: SCEL64_4_8_2_0_0_0
      Generated: SCEL72_18_2_2_0_0_2
      Generated: SCEL72_18_2_2_0_0_4
      Generated: SCEL72_6_6_2_0_0_4
      Generated: SCEL72_6_6_2_0_0_0
      DONE.
    
    Committing database...  DONE


# Selecting and Querying Enumerated Supercells

Use the `-t scel` option to indicate `query` and `select` operations on supercells. CASM stores a default list of selected supercells called the `MASTER` selection within the ".casm" directory. Other standard selections CASM defines that can be used with the `-c` option are: 

- `All`: all supercells in the database included and selected
- `NONE`: all supercells in the database included but none selected
- `EMPTY`: no supercells included

_Note: `CALCULATED` is not allowed for supercells_

Custom user lists can be generated with `-o <filename>` and used with `-c <filename>`.

## Select all enumerated supercells


```bash
ccasm select -t scel --set-on
```

    -- Input scel list: MASTER -- 
    # scels in this project: 87
    # scels included in this list: 87
    # scels selected in this list: 0
    
    -- set-on:  -- 
    selection time: 1.9433e-05 (s)
    
    -- Write: Selection -- 
    write: "MASTER"
    
    -- Output scel list: MASTER -- 
    # scels in this project: 87
    # scels included in this list: 87
    # scels selected in this list: 87
    


## Query properties of selected supercells

- By default, the MASTER selection is queried
- A list of properties that can be queried can be printed with:

      ccasm query --help properties
 
In this example, the supercell volume as a multiple of the prim is queried (`scel_size`) and the results are written to a file name  `all_supercells_and_size`. Since the file is large, we only print the  beginning of the file here for an example.


```bash
ccasm query -t scel -k scel_size > all_supercells_and_size
head all_supercells_and_size
```

    Print:
       - scel_size
    
    #                name    selected    scel_size
        SCEL1_1_1_1_0_0_0           1            1
        SCEL2_1_1_2_0_0_0           1            2
        SCEL2_1_2_1_0_0_0           1            2
        SCEL2_1_2_1_1_0_0           1            2
        SCEL3_1_1_3_0_0_0           1            3
        SCEL3_1_3_1_2_0_0           1            3


## Combine selections and queries with operators

- Queried properties can be combined through boolean and comparison operations.
- A list of all operators can be printed with:

      ccasm query --help operators

This example selects all volume 4 supercells and saves them to a custom selection file named `volume_4_scel_list.txt`.


```bash
ccasm select -t scel -c ALL --set 'eq(scel_size,4)' -o volume_4_scel_list.txt
```

    -- Input scel list: ALL -- 
    # scels in this project: 87
    # scels included in this list: 87
    # scels selected in this list: 87
    
    -- set: eq(scel_size,4) -- 
    selection time: 0.000137277 (s)
    
    -- Write: Selection -- 
    write: "volume_4_scel_list.txt"
    
    -- Output scel list: volume_4_scel_list.txt -- 
    # scels in this project: 87
    # scels included in this list: 87
    # scels selected in this list: 11
    


## Using a custom selection, writing a JSON output file

This example queries some properties of just the volume 4 supercells and saves the output as a JSON file named `volume_4_props.json`. 

JSON output is obtained either by giving the output file a `.json` extension, or using the `--json,-j` option.


```bash
ccasm query -t scel -c volume_4_scel_list.txt -k multiplicity pointgroup_name lattice_params -o volume_4_props.json
head -n 30 volume_4_props.json
```

    Print:
       - multiplicity
       - pointgroup_name
       - lattice_params
    to "/Users/bpuchala/Work/codes/CASMcode_v0.2.X_reference/doc/examples/python_kernel/enum/ZrO/volume_4_props.json"
    
      DONE.
    
    [
      {
        "lattice_params" : [
          [ 3.233986860000 ],
          [ 3.233986854574 ],
          [ 20.674713360000 ],
          [ 90.000000000000 ],
          [ 90.000000000000 ],
          [ 120.000000055498 ]
        ],
        "multiplicity" : 1,
        "name" : "SCEL4_1_1_4_0_0_0",
        "pointgroup_name" : "D6h",
        "selected" : true
      },
      {
        "lattice_params" : [
          [ 3.233986860000 ],
          [ 5.601429540000 ],
          [ 10.337356680000 ],
          [ 90.000000000000 ],
          [ 90.000000000000 ],
          [ 90.000000000000 ]
        ],
        "multiplicity" : 3,
        "name" : "SCEL4_1_2_2_0_0_0",
        "pointgroup_name" : "D2h",
        "selected" : true
      },
      {


# Getting Supercell `info`

Sometimes it is useful to get information about a supercell outside of the context of a CASM project.

The `info` command allows querying properties of supercells without first creating a CASM project and enumerating supercells, although it can also be used within the context of a project.

The `SupercellInfo` method allows for getting information about the supercell lattice vectors, the ordering of the representation of DoF values in a configuration, permutation representations, and linear site ordering. 

To see a list of all supercell properties that may be obtained from the `SupercellInfo` method, and a description of their representation, use:

     ccasm info --desc SupercellInfo
 

## Query supercell site coordinates

This example queries the coordinates of the sites in a supercell, in Cartesian, fractional, and integral site coordinates.

Fractional coordinates in this context are defined as multiples of the supercell lattice vectors.

Integral site coordinates specify the position of a site using integers `[b, i, j, k]`, representing (`b`) the site's sublattice as an index into the in the prim basis, and (`i, j, k`) the unit cell it is in using multiples of the prim lattice vectors.


```bash
supercell_info_str="{
  \"prim\":$prim_str,
  \"transformation_matrix_to_super\": [[2, 0, 0], [0, 2, 0], [0, 0, 2]],
  \"properties\": [\"cart_coordinate\", \"frac_coordinate\", \"integral_site_coordinates\"] 
}"
ccasm info -m SupercellInfo -i "$supercell_info_str"
```

    {
      "cart_coordinate" : [
        [ 0.000000000000, 0.000000000000, 0.000000000000 ],
        [ 3.233986860000, 0.000000000000, 0.000000000000 ],
        [ -1.616993430000, 2.800714770000, 0.000000000000 ],
        [ 1.616993430000, 2.800714770000, 0.000000000000 ],
        [ 0.000000000000, 0.000000000000, 5.168678340000 ],
        [ 3.233986860000, 0.000000000000, 5.168678340000 ],
        [ -1.616993430000, 2.800714770000, 5.168678340000 ],
        [ 1.616993430000, 2.800714770000, 5.168678340000 ],
        [ 1.616993430162, 0.933571589907, 2.584339170000 ],
        [ 4.850980290162, 0.933571589907, 2.584339170000 ],
        [ 0.000000000162, 3.734286359907, 2.584339170000 ],
        [ 3.233986860162, 3.734286359907, 2.584339170000 ],
        [ 1.616993430162, 0.933571589907, 7.753017510000 ],
        [ 4.850980290162, 0.933571589907, 7.753017510000 ],
        [ 0.000000000162, 3.734286359907, 7.753017510000 ],
        [ 3.233986860162, 3.734286359907, 7.753017510000 ],
        [ -0.000000000162, 1.867143180093, 1.292169585000 ],
        [ 3.233986859838, 1.867143180093, 1.292169585000 ],
        [ -1.616993430162, 4.667857950093, 1.292169585000 ],
        [ 1.616993429838, 4.667857950093, 1.292169585000 ],
        [ -0.000000000162, 1.867143180093, 6.460847925000 ],
        [ 3.233986859838, 1.867143180093, 6.460847925000 ],
        [ -1.616993430162, 4.667857950093, 6.460847925000 ],
        [ 1.616993429838, 4.667857950093, 6.460847925000 ],
        [ -0.000000000162, 1.867143180093, 3.876508755000 ],
        [ 3.233986859838, 1.867143180093, 3.876508755000 ],
        [ -1.616993430162, 4.667857950093, 3.876508755000 ],
        [ 1.616993429838, 4.667857950093, 3.876508755000 ],
        [ -0.000000000162, 1.867143180093, 9.045187095000 ],
        [ 3.233986859838, 1.867143180093, 9.045187095000 ],
        [ -1.616993430162, 4.667857950093, 9.045187095000 ],
        [ 1.616993429838, 4.667857950093, 9.045187095000 ]
      ],
      "frac_coordinate" : [
        [ 0.000000000000, 0.000000000000, 0.000000000000 ],
        [ 0.500000000000, 0.000000000000, 0.000000000000 ],
        [ 0.000000000000, 0.500000000000, 0.000000000000 ],
        [ 0.500000000000, 0.500000000000, 0.000000000000 ],
        [ 0.000000000000, 0.000000000000, 0.500000000000 ],
        [ 0.500000000000, 0.000000000000, 0.500000000000 ],
        [ 0.000000000000, 0.500000000000, 0.500000000000 ],
        [ 0.500000000000, 0.500000000000, 0.500000000000 ],
        [ 0.333333333350, 0.166666666650, 0.250000000000 ],
        [ 0.833333333350, 0.166666666650, 0.250000000000 ],
        [ 0.333333333350, 0.666666666650, 0.250000000000 ],
        [ 0.833333333350, 0.666666666650, 0.250000000000 ],
        [ 0.333333333350, 0.166666666650, 0.750000000000 ],
        [ 0.833333333350, 0.166666666650, 0.750000000000 ],
        [ 0.333333333350, 0.666666666650, 0.750000000000 ],
        [ 0.833333333350, 0.666666666650, 0.750000000000 ],
        [ 0.166666666650, 0.333333333350, 0.125000000000 ],
        [ 0.666666666650, 0.333333333350, 0.125000000000 ],
        [ 0.166666666650, 0.833333333350, 0.125000000000 ],
        [ 0.666666666650, 0.833333333350, 0.125000000000 ],
        [ 0.166666666650, 0.333333333350, 0.625000000000 ],
        [ 0.666666666650, 0.333333333350, 0.625000000000 ],
        [ 0.166666666650, 0.833333333350, 0.625000000000 ],
        [ 0.666666666650, 0.833333333350, 0.625000000000 ],
        [ 0.166666666650, 0.333333333350, 0.375000000000 ],
        [ 0.666666666650, 0.333333333350, 0.375000000000 ],
        [ 0.166666666650, 0.833333333350, 0.375000000000 ],
        [ 0.666666666650, 0.833333333350, 0.375000000000 ],
        [ 0.166666666650, 0.333333333350, 0.875000000000 ],
        [ 0.666666666650, 0.333333333350, 0.875000000000 ],
        [ 0.166666666650, 0.833333333350, 0.875000000000 ],
        [ 0.666666666650, 0.833333333350, 0.875000000000 ]
      ],
      "integral_site_coordinates" : [
        [ 0, 0, 0, 0 ],
        [ 0, 1, 0, 0 ],
        [ 0, 0, 1, 0 ],
        [ 0, 1, 1, 0 ],
        [ 0, 0, 0, 1 ],
        [ 0, 1, 0, 1 ],
        [ 0, 0, 1, 1 ],
        [ 0, 1, 1, 1 ],
        [ 1, 0, 0, 0 ],
        [ 1, 1, 0, 0 ],
        [ 1, 0, 1, 0 ],
        [ 1, 1, 1, 0 ],
        [ 1, 0, 0, 1 ],
        [ 1, 1, 0, 1 ],
        [ 1, 0, 1, 1 ],
        [ 1, 1, 1, 1 ],
        [ 2, 0, 0, 0 ],
        [ 2, 1, 0, 0 ],
        [ 2, 0, 1, 0 ],
        [ 2, 1, 1, 0 ],
        [ 2, 0, 0, 1 ],
        [ 2, 1, 0, 1 ],
        [ 2, 0, 1, 1 ],
        [ 2, 1, 1, 1 ],
        [ 3, 0, 0, 0 ],
        [ 3, 1, 0, 0 ],
        [ 3, 0, 1, 0 ],
        [ 3, 1, 1, 0 ],
        [ 3, 0, 0, 1 ],
        [ 3, 1, 0, 1 ],
        [ 3, 0, 1, 1 ],
        [ 3, 1, 1, 1 ]
      ]
    }


Clean up tutorial data:


```bash
cd $start && rm -r $start/enum
```
