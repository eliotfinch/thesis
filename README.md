# Thesis
PhD Thesis: "*Black-hole Ringdown: Quasinormal Modes in Numerical-relativity Simulations and Gravitational-wave Observations*"

Other subtitle ideas:
- Modelling and Data Analysis
- Numerical-relativity and Gravitational-wave observations

---

### [Download PDF](https://github.com/EliotFinch/thesis/raw/build/main.pdf)
![Makefile CI](https://github.com/eliotfinch/thesis/actions/workflows/makefile.yml/badge.svg?event=push)

---

## Comments

- [ ] example comment; suggest title of chapter 1 be "Introduction to BH ringdown", or similar

## Outline

### Introduction

#### Black-hole ringdown
- High-level overview of binary black hole mergers, gravitational waves, time and length scales, and why the ringdown is useful.
- A breif summary of the history either in here or throughout the introduction.
- This will lead into a discussion of quasinormal modes...

#### Quasinormal modes
- We can do a demonstrative calculation of a massless **scalar field evolving according to the Klein-Gordon equation on a Schwarzschild background**. This gets the form of the potential, but I am not sure the calculation of the actual QNMs is particularly easy...
- We can calculate QNMs easily with a **geodesic picture**.
- Show the full Kerr spectrum taxonomy and conventions. 
  
### Modelling the Ringdown from Precessing Black-hole Binaries
- Flesh out NR sims, what they are and how they're set up.
- Explain the framework for the full multimode fitting code.

### Developments to my Ringdown Fitting Code
- The code has developed a lot since the first paper. I would like to include a description of the more developed fitting procedure somewhere. Things I can do (which were not presented in my first paper) include multimode fits with mixing coefficients, fits to CCE waveforms, and fits with nonlinear QNMs.

### Frequency-domain Analysis of Black Hole Ringdown
- Expand detector response, TD vs FD analysis methods.

### Searching for a Ringdown Overtone in GW150914

---

The [workflow](https://github.com/EliotFinch/thesis/blob/main/.github/workflows/makefile.yml) to compile the PDF on push and create a link to the artifact was taken from the tutorial available [here](https://davidegerosa.com/githubforlatex/). Note that in the repository settings under `Actions -> General` I had to change the `Workflow permissions` to have `Read and write permissions`.
