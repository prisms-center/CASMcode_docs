This tutorial will demonstrate using CASM to construct a portion of the Zr-O phase diagram from first-principles calculations, as was done in B. Puchala, A. Van der Ven, *Thermodynamics of the Zr-O system from first-principles calculations*, *Physical Review B*, **88**, 094108 (2013). [[doi:10.1103/PhysRevB.88.094108]](https://doi.org/10.1103/PhysRevB.88.094108)

The Zr-O system is remarkable for its extremely high O solubility. HCP Zr can dissolve up to ~35 at% O. At low temperatures, the phase diagram shows that a series of $ZrO_x$ suboxide phases form, each a different ordering of the O octahedral interstitials. For understanding oxidation processes in Zr, it is valuable to understand and predict the formation of the suboxide phases.

|![Zr-O_expt_pd]({{ site.baseurl }}/assets/tutorials/init/Zr-O_expt_pd.png){:width="400px"}|![prim_file]({{ site.baseurl }}/assets/tutorials/init/prim.png){:width="250px"}|
|Zr-O phase diagram, from J.P. Abriata, J. Garcés, and R. Versaci, Bulletin of Alloy Phase Diagrams Vol. 7 No. 2 1986.|HCP Zr with O/Va disorder on octahedral interstitial positions|

The `` `prim.json` `` for HCP Zr with O/Va disorder on octahedral interstitial positions can be obtained from the `` `casm format --prim` `` output (Example 2), or from the online demonstration project. Save it in a new directory called `` `ZrO_tutorial` `` which will become our project directory.
