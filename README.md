# PhD Thesis

### "*Black-hole Ringdown: Quasinormal Modes in Numerical-relativity Simulations and Gravitational-wave Observations*"

---

### [Download PDF](https://github.com/EliotFinch/thesis/raw/build/main.pdf)
![Makefile CI](https://github.com/eliotfinch/thesis/actions/workflows/makefile.yml/badge.svg)

---

## Comments

Comments on Chapter 2

Sec 2.1 
- Paragraph 2. When discussing why this is a “surprising” result you might also consider adding some more recent references, perhaps to some of the nonlinear QNM studies from 2022.

Sec 2.2
- In section 2.3.2, did you want to explain why this stacking of all the lm modes is equivalent to doing a least-squares fit averaged over Omega?

Comments on Chapter 3 (Added 06/03/2023)

Sec 3.1
 - end of paragraph 3, “The applications mentioned so far use only the QNM frequencies; however, the excitation amplitudes and phases of the QNMs also carry useful information about the progenitor binary”. There are some recent papers you could cite here. E.g. by Swetha.

## Outline

### Introduction

> #### Binary black-hole mergers
>
> #### Black-hole ringdown
>
> #### Quasinormal modes
>  - Scalar field on a Schwarzschild background
>  - Quasinormal modes from the geodesic correspondence
>  - Limitations of quasinormal modes
> 
> #### Black-hole spectroscopy
  
### Modelling the Ringdown from Precessing Black-hole Binaries
> [Phys. Rev. D 103, 084048 (2021)](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.103.084048) | [arXiv:2102.07794](https://arxiv.org/abs/2102.07794)

### Frequency-domain Analysis of Black-hole Ringdowns
> [Phys. Rev. D 104, 123034 (2021)](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.104.123034) | [arXiv:2108.09344](https://arxiv.org/abs/2108.09344)

### Searching for a Ringdown Overtone in GW150914
> [Phys. Rev. D 106, 043005 (2022)](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.106.043005) | [arXiv:2205.07809](https://arxiv.org/abs/2205.07809)

---

The [workflow](https://github.com/EliotFinch/thesis/blob/main/.github/workflows/makefile.yml) to compile the PDF on push and create a link to the artifact was taken from the tutorial available [here](https://davidegerosa.com/githubforlatex/). Note that in the repository settings under `Actions -> General` I had to change the `Workflow permissions` to have `Read and write permissions`.
