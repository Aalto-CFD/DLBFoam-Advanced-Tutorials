# Sandia flame D

This is a demonstration of the capabilities of the DLBFoam on the well-known [Sandia flame D](https://tnfworkshop.org/data-archives/pilotedjet/ch4-air/) experimental setup, published in Ref.[[1]](#Morev2022) 

## Case description

Sandia flame D - is a partially-premixed piloted methane/air jet flame. The main jet is a mixture of methane and air at equivalence ratio 3.17. Pilot jet is a mixture of a combustion products at temperature 1880K. The main jet nozzle inner diameter is 7.2mm, whereas pilot jet has inner and outer diameters of 7.2mm and 18.2mm correspondingly. The main jet velocity is 49.6m/s, pilot jet velocity is 11.4m/s and air coflow velocity is 0.9m/s. More details on the setup can be found in Ref.[[2]](#Barlow1994).

![schematic](doc/schematic_sandiaD.png)

## Numerical setup

### Mesh

Computational grid is Cartesian with a refinement region close to the nozzle. In order to save computational resources, maximum mesh resolution is put close to the nozzle to capture the physics only close to the first sampling location.

### Boundary conditions

Intlet velocity profiles for main and pilot jets are set with ```codedFixedValue``` boundary condition, where experimental profiles are imposed. On top of the experimental profile for main jet, a turbulence of the form proposed by Pitsch and Steiner [[3]](#Pitsch2000) is superimposed. Turbulence parameters are generated randomly by a python script ```generate_turbulence_params.py```, called by ```Allrun```.

### Chemistry

A DRM19 chemical kinetics mechanism is used [[4]](#DRM19), compiled with for the use with DLBFoam. 

### Other details

Implicit Large-Eddy Simulation approach is used here, i.e. LES-like mesh is used with filtered equations, but no explicit TCI model is present (in ```constant/combustionProperties``` entry ```combustionModel``` is set to laminar).

Data averaging is done by ```fieldAverage```, activated after a time required for the jet to become statistically stable. 

In DLBFoam library, both load balancing and reference mapping are enabled. Improved ODE solution routines are also utilized.

## Running

You can execute Allrun script directly, which will set up the case and launch the simulation. Also, you can use it as a reference to set up your own workflow, e.g. run the simulation on an HPC.

## Post processing

In order to to post-process the simulation data, you can sample the lines you are interested in from the averaged fields (e.g. ```UMean```, ```TPrimeMean```).

## References

<a id="Morev2022">[1]</a> 
I. Morev, B. Tekgül, M. Gadalla, A. Shahanaghi, J. Kannan, S. Karimkashi, O. Kaario, V. Vuorinen, Fast reactive flow simulations using analytical Jacobian and dynamic load balancing in OpenFOAM, arXiv preprint arXiv:2105.12070 (2021).

<a id="Barlow1994">[2]</a> 
Barlow, R. S., and C. D. Carter. "Raman/Rayleigh/LIF measurements of nitric oxide formation in turbulent hydrogen jet flames." Combustion and Flame 97.3-4 (1994): 261-280.

<a id="Pitsch2000">[3]</a> 
Pitsch, Heinz, and Helfried Steiner. "Large-eddy simulation of a turbulent piloted methane/air diffusion flame (Sandia flame D)." Physics of fluids 12.10 (2000): 2541-2554.

<a id="DRM19">[4]</a> 
A. Kazakov, M. Frenklach, Reduced Reaction Sets based on GRI-Mech 1.2, http://combustion.berkeley.edu/drm/, accessed: 2021-10-21 (2005).
