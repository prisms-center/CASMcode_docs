{% include tutorials/init/sec2/sec2.1-desc.md %}
```
$ mkdir -p $CASM_TEST_PROJECTS_DIR/0.3.X/ZrO_tutorial
$ cd $CASM_TEST_PROJECTS_DIR/0.3.X/ZrO_tutorial
$ cp $CASM_TEST_PROJECTS_DIR/0.3.X/ZrO.0/prim.json .
$ cat prim.json
```
<details><summary markdown="span">See result</summary>

```
$ mkdir -p $CASM_TEST_PROJECTS_DIR/0.3.X/ZrO_tutorial
$ cd $CASM_TEST_PROJECTS_DIR/0.3.X/ZrO_tutorial
$ cp $CASM_TEST_PROJECTS_DIR/0.3.X/ZrO.0/prim.json .
$ cat prim.json
{
  "basis" : [
    {
      "coordinate" : [ 0.000000000000, 0.000000000000, 0.000000000000 ],
      "occupant_dof" : [ "Zr" ]
    },
    {
      "coordinate" : [ 0.666666700000, 0.333333400000, 0.500000000000 ],
      "occupant_dof" : [ "Zr" ]
    },
    {
      "coordinate" : [ 0.333333300000, 0.666666600000, 0.250000000000 ],
      "occupant_dof" : [ "Va", "O" ]
    },
    {
      "coordinate" : [ 0.333333300000, 0.666666600000, 0.750000000000 ],
      "occupant_dof" : [ "Va", "O" ]
    }
  ],
  "coordinate_mode" : "Fractional",
  "description" : "hcp Zr with octahedral interstitial O ",
  "lattice_vectors" : [
    [ 3.233986860000, 0.000000000000, 0.000000000000 ],
    [ -1.616993430000, 2.800714770000, 0.000000000000 ],
    [ -0.000000000000, 0.000000000000, 5.168678340000 ]
  ],
  "title" : "ZrO"
}
```
</details>
<br>
