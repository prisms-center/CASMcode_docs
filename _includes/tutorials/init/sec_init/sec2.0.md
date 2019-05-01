{% include tutorials/init/sec2/sec2.0-desc.md %}
```
$ casm format --prim
```
<details><summary markdown="span">See result</summary>

```
$ casm format --prim

### prim.json ##################

LOCATION WHEN GENERATED:
$ROOT/prim.json
$ROOT/PRIM (legacy)


DESCRIPTION:
'prim.json' describes the primitive cell structure. It includes the lattice 
vectors, crystal basis sites and a list of possible occupant molecules on each
basis site.

'prim.json' parameters:                                            

"title" (string):                                                
  A title for the project. Must consist of alphanumeric characters 
  and underscores only. The first character may not be a number.   

"lattice_vectors" (JSON array of 3 JSON arrays of 3 numbers):    
  Lattice vectors for the primitive structure, in Angstroms.       

"coordinate_mode" (string):                                      
  Coordinate mode for basis sites. One of:                         
    "Fractional" or "Direct",                                  
    "Cartesian"                                                  

"basis" (JSON array of JSON objects):                            

  /"coordinate" (JSON array of 3 numbers):                       
    Coordinate of the basis site with units as specified by the    
    the "coordinate_mode" parameter. The default tolerance for   
    checking symmetry is 1e-5, so basis site coordinates should    
    include 6 significant digits or more.                          
  /"occupant_dof" (JSON array of string):                        
    A list of the possible occupant atoms (and in future versions  
    CASM, molecules) that on each site. The names are case         
    sensitive, and "Va" is reserved for vacancies.               


EXAMPLE 1: An FCC ternary alloy of elements A, B, and C
-------
{
  "basis" : [
    {
      "coordinate" : [ 0.000000000000, 0.000000000000, 0.000000000000 ],
      "occupant_dof" : [ "A", "B", "C" ]
    }
  ],
  "coordinate_mode" : "Fractional",
  "description" : "Face-centered Cubic (FCC, cF)",
  "lattice_vectors" : [
    [ 2.000000000000, 2.000000000000, 0.000000000000 ],
    [ 0.000000000000, 2.000000000000, 2.000000000000 ],
    [ 2.000000000000, 0.000000000000, 2.000000000000 ]
  ],
  "title" : "ABC"
}
-------

EXAMPLE 2: HCP Zr with O in octahedral interstitial positions
-------

{
  "basis" : [
    {
      "coordinate" : [ 0.0, 0.0, 0.0 ],
      "occupant_dof" : [ "Zr" ]
    },
    {
      "coordinate" : [ 0.666666, 0.333333, 0.5 ],
      "occupant_dof" : [ "Zr" ]
    },
    {
      "coordinate" : [ 0.333333, 0.666666, 0.25 ],
      "occupant_dof" : [ "Va", "O" ]
    },
    {
      "coordinate" : [ 0.333333, 0.666666, 0.75 ],
      "occupant_dof" : [ "Va", "O" ]
    }
  ],
  "coordinate_mode" : "Fractional",
  "description" : "hcp Zr with oct (O) ",
  "lattice_vectors" : [
    [ 3.233986860000, 0.000000000000, 0.000000000000 ],
    [ -1.616993430000, 2.800714770000, 0.000000000000 ],
    [ -0.000000000000, 0.000000000000, 5.168678340000 ]
  ],
  "title" : "ZrO"
}
-------


### PRIM ##################

DESCRIPTION:
PRIM is the input file used by previous version of casm. It can be read and        
converted to 'prim.json'. The format of PRIM is very similar to the VASP POSCAR    
except a list of possible occupant molecules is included with each basis site.     

- Molecule names are case sensitive.
- 'Va' is reserved for vacancies.
- The default tolerance for checking symmetry is 1e-5, so basis site coordinates
  should include 6 significant digits or more.


EXAMPLE 1: An FCC ternary alloy of elements A, B, and C
-------
Face-centered Cubic (FCC, cF)
1.0
0 2.0 2.0
2.0 0 2.0
2.0 2.0 0
1
D
0.00 0.00 0.00 A B C
-------

EXAMPLE 2: A structure with some alloying sites and some non-alloying sites
-------
LiTiO2 - Bronze
 1.00000000
       1.91357600      0.00000000     -6.23799200
       6.08935000     -1.87060000      0.00000000
       0.00000000     -3.74120000      0.00000000
 5 4 8
Direct
   0.0000000   0.0000000   0.0000000 Li Va
   0.3800000   0.9000000   0.5500000 Li Va
   0.6200000   0.1000000   0.4500000 Li Va
   0.0000000   0.2600000   0.3700000 Li Va
   0.0000000   0.7400000   0.6300000 Li Va
   0.7080000   0.3940000   0.8030000 Ti
   0.2920000   0.6060000   0.1970000 Ti
   0.2950000   0.1980000   0.9010000 Ti
   0.7050000   0.8020000   0.0990000 Ti
   0.9960000   0.2640000   0.8680000 O
   0.0040000   0.7360000   0.1320000 O
   0.3470000   0.5280000   0.7360000 O
   0.6530000   0.4720000   0.2640000 O
   0.6290000   0.1200000   0.9400000 O
   0.3710000   0.8800000   0.0600000 O
   0.7070000   0.7240000   0.6380000 O
   0.2930000   0.2760000   0.3620000 O
-------
```
</details>
<br>
