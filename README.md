# DLBFoam-Advanced-Tutorials

This repository provides advanced tutorial cases which demonstrate the scaling capability and computational efficiency of the **DLBFoam** library, a radically fast detailed chemistry solver for OpenFOAM. 

The detailed discussion and validation of the provided tutorial cases are openly available in Ref. [[1]](#1)


## Tutorial cases

The provided tutorial cases represent the following:

* [two-dimensional reacting shear layer](2D_Shear_Layer/README.md)
* [Three-dimensional stratified combustion](3D_Stratified_Combustion/README.md)
* [Engine Combustion Network Spray A](ECN_Spray_A/README.md)
* [Sandia flame D](Sandia_D/README.md)

As there are many more experimental benchmarks of various combustion phenomena that have not been tested, we would be happy to receive your contribution using the **DLBFoam** and reporting the speed-up and scaling effects against standard solvers.

## Citation

If you use our tutorial cases, please cite the paper discussing these test cases [[1]](#1), together with the [original DLBFoam paper](https://github.com/Aalto-CFD/DLBFoam#citation), also noted in Ref. [[2]](#2).

## References

</p>
</details>

<a id="1">[1]</a> 
I. Morev, B. Tekgül, M. Gadalla, A. Shahanaghi, J. Kannan, S. Karimkashi, O. Kaario, V. Vuorinen, Fast reactive flow simulations using analytical Jacobian and dynamic load balancing in OpenFOAM, Physics of Fluids 34, 021801, [doi:10.1063/5.0077437](https://doi.org/10.1063/5.0077437) (2022).
<details>
<summary>BibTex</summary>
<p>

```
@article{Morev2022,
  doi = {10.1063/5.0077437},
  url = {https://doi.org/10.1063/5.0077437},
  year = {2022},
  month = feb,
  publisher = {{AIP} Publishing},
  volume = {34},
  number = {2},
  pages = {021801},
  author = {Ilya Morev and Bulut Tekg\"{u}l and Mahmoud Gadalla and Ali Shahanaghi and Jeevananthan Kannan and Shervin Karimkashi and Ossi Kaario and Ville Vuorinen},
  title = {Fast reactive flow simulations using analytical Jacobian and dynamic load balancing in {OpenFOAM}},
  journal = {Physics of Fluids}
}
```

</p>
</details>

</p>
</details>

<a id="2">[2]</a> 
B. Tekgül, P. Peltonen, H. Kahila, O. Kaario, V. Vuorinen, DLBFoam: An open-source dynamic load balancing model for fast reacting flow simulations in OpenFOAM, Computer Physics Communications, Volume 267, [doi:10.1016/j.cpc.2021.108073](https://doi.org/10.1016/j.cpc.2021.108073) (2021).

<details>
<summary>BibTex</summary>
<p>

```
@article{tekgul2021dlbfoam,
  title={DLBFoam: An open-source dynamic load balancing model for fast reacting flow simulations in OpenFOAM},
  author={Tekg{\"u}l, Bulut and Peltonen, Petteri and Kahila, Heikki and Kaario, Ossi and Vuorinen, Ville},
  journal={Computer Physics Communications},
  pages={108073},
  year={2021},
  publisher={Elsevier}
}
```

</p>
</details>
