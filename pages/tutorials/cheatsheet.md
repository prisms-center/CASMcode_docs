---
layout: default
---

[![CASM Logo]({{ site.baseurl }}/assets/logo.png)](https://prisms-center.github.io/CASMcode_docs/)

***
## [CASM Tutorials]({{ site.baseurl }}/pages/tutorials.html) - (temporary) PRISMS Workshop cheatsheet

```
# environment setup
PUBLIC=/afs/umich.edu/user/b/p/bpuchala/Public
source $PUBLIC/modules/casm

# example ZrO project input files
cd ~
mkdir casm_demo
cd casm_demo
cp -r $PUBLIC/casm_demo/ZrO .
cd ZrO
casm status -n

### Initialize project
casm init

### Set composition axes
casm status -n
casm composition --select 0

### Enumerate configurations
casm status -n
casm enum -m ScelEnum --max 4
casm enum -m ConfigEnumAllOccupations -a

### Enable VESTA visualization
casm settings --set-view-command 'casm.view VESTA'
casm view SCEL4_2_2_1_0_0_0/12

### Calculate DFT energies
casm status -n
casm select --set-on
emacs training_data/settings/calctype.default/SPECIES
emacs training_data/settings/calctype.default/INCAR
emacs training_data/settings/calctype.default/KPOINTS
emacs training_data/settings/calctype.default/relax.json
casm calc --setup

# Can't actually submit jobs, would use:
#   casm-calc --submit
#   casm update
# Instead, copy calculation results:
cp $PUBLIC/casm_demo/ZrO_data/.casm/config_list.json .casm/config_list.json
casm status -d

### Set chemical reference
casm ref --set-auto

### Specify basis set
emacs basis_sets/bset.default/bspecs.json
casm bset -u

### Select configurations
casm select –set 'and(is_calculated,lt(comp(a),0.695))' -o calc_lt_0p7

### Query properties
casm query -c ALL -k 'scel_size comp'
casm query -c calc_lt_0p7 -k 'scel_size comp'

### ECI fitting

# Create a directory for fitting work
cd ~/casm_demo/ZrO/fit_1

# Create new eci setting
casm settings --new-eci test

# Select structures to fit with
casm select --set 'lt(comp(a),0.695)' -o all_lt_0p7
casm select -c all_lt_0p7 --set-off 'not(is_calculated)' -o train

# Create a 'casm-learn' input file
casm learn --exGeneticAlgorithm > fit_1_ga.json
emacs fit_1_ga.json

# Run 'casm-learn'
casm learn -s fit_1_ga.json

# Check results
casm learn -s fit_1_ga.json --hall
casm learn -s fit_1_ga.json --checkhull --indiv 0
python plot.py

# Select ECI to use
casm learn -s fit_1_ga.json --select 0

### Run Monte Carlo

# semi-grand canonical setup
cd ~/casm_demo/ZrO/mc/example_grand_canonical
casm format --monte
emacs metropolis_grand_canonical.json

# run
casm monte -s metropolis_grand_canonical.json --verbosity verbose

# check results
cat results.json
cat results.csv
python ploy.py

# lte1 setup
cd ~/casm_demo/ZrO/mc/example_lte1
emacs lte1_grand_canonical.json

# run
casm monte -s lte1_grand_canonical.json

# check results
cat results.csv
cat results.json
python ploy.py

# run a coarse grid
cd ~/casm_demo/mc/grid
python run.py

# analyze fine grid results
cd ~/casm_demo/mc/fine_grid

# extract pre-calculated results
tar -xzvf results.tar.gz
python parse.py

# look at varying T results
# check results for paths with varying T
python plot_vary_T.py
python plot_vary_T_all.py

python plot_vary_xi.py
python plot_vary_xi_all.py

# free energy integration
python free_energy.py

# find phase boundary
python plot_phi_vary_xi.py
python plot_boundary_vary_xi.py

```
