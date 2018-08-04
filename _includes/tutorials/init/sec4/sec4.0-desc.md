The `` `casm composition` `` command enables checking and setting composition axes.

Each configuration has a composition and there are various ways to measure it:
- Atomic fraction (`` `atom_frac` ``):
  - Number of a species (Au, Cu, etc.) divided by the total number of atoms. Vacancies are ignored.
  - In `` `casm query` ``-format: `` `atom_frac(Zr)` ``, `` `atom_frac(Au)` ``, etc...
- Number per unit cell (`` `comp_n` ``):
    - Number of a species (Au, Cu, etc.) divided by the number of primitive cells (volume). Accounts for vacancies. Sum over all allowed components equals the number of basis sites in the primitive cell.
    - In `` `casm query` ``-format: `` `comp_n(Zr)` ``, `` `comp_n(Va)` ``, etc...
- Parametric composition (`` `comp` ``):
    - Primitive-cell-based formula parameters (`` `a` ``, `` `b` ``, `` `c` ``, ...) determined by user-defined composition axes. Accounts for vacancies. Sum over all allowed axes equals 1.0.
    - Parametric composition is particularly convenient for Monte Carlo calculations because it allows for varying each parametric composition independently while running calculations throughout the entire composition space.
    - For details, see [Parametric Composition]({{ site.baseurl }}/assets/definitions/CASM_param_comp.pdf)
    - In `` `casm query` ``-format: `` `comp(a)` ``, `` `comp(b)` ``, etc...

As an example, in the Zr-O system of HCP-Zr with O/Va disorder on the octahedral interstitial positions, the composition can be defined in terms of the amount of O (x) or the amount of Va (1-y). Here are formation energy vs composition calculations plotted with the two options of axes:

|![x_in_ZrOx](/assets/tutorials/init/x_in_ZrOx.png){:width="300px"}| ![y_in_ZrOy](/assets/tutorials/init/y_in_ZrO1-y.png){:width="300px"}|
|(a) Composition axes defined as $x$ in $ZrO_x$|(b) Composition axes defined as $y$ in $ZrO_{1-y}$|

When a project is initialized, CASM automatically generates standard composition axes which maximize/minimize the number of each component at the composition axes end states. The results are stored in the file `` `.casm/composition_axes.json` `` If the standard composition axes are not sufficient for your purposes, additional custom composition axes can be added to the `` `.casm/composition_axes.json` `` file. Use `` `casm format --comp` `` for a description of the `` `composition_axes.json` `` file format.  If anything happens to the file, `` `casm composition --calc` `` can be used to re-calculate the standard composition axes.

The complete list of standard and custom composition axes can be displayed with `` `casm composition -d` ``. Note in the output:
- Each choice composition axes is given a "KEY"
- Each choice of composition axes is specified via a formula, and the set of end states (named `ORIGIN`, `a`, `b`, etc.)
- The sum of components at each end member, and also the sum of components in the formula, is equal to the number of basis sites in the primitive cell, not 1.0.
