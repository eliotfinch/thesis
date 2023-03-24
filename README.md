# Thesis
PhD Thesis: "*Black-hole Ringdown: Quasinormal Modes in Numerical-relativity Simulations and Gravitational-wave Observations*"

Other subtitle ideas:
- Modelling and Data Analysis
- Numerical-relativity and Gravitational-wave observations

---

### [Download PDF](https://github.com/EliotFinch/thesis/raw/build/main.pdf)
![Makefile CI](https://github.com/eliotfinch/thesis/actions/workflows/makefile.yml/badge.svg)

---

## Comments

Comments on Chapter 2

Sec 2.1 
- Paragraph 2. When discussing why this is a “surprising” result you might also consider adding some more recent references, perhaps to some of the nonlinear QNM studies from 2022.
- Paragraph 2. “The primary aim of this paper…” change to “this study” or “this chapter”.

Sec 2.2
- In section 2.3.2, did you want to explain why this stacking of all the lm modes is equivalent to doing a least-squares fit averaged over Omega?

Comments on Chapter 3 (Added 06/03/2023)

Sec 3.1
 - paragraph 2. You could (but don’t have to) go into a little more detail on the “no hair” theorem here. Or maybe you discuss this in the intro?
 - end of paragraph 3, “The applications mentioned so far use only the QNM frequencies; however, the excitation amplitudes and phases of the QNMs also carry useful information about the progenitor binary”. There are some recent papers you could cite here. E.g. by Swetha.
 - para 5, “increasing computational cost of the likelihood” -> “”increasing THE computational cost of the likelihood”
- Fig. 3.1. Make graphic full textwdith

Sec. 3.3
- Para 1. You say “results from the GW150914-like analyses are shown in Appendix 3.5”. Is this still true? It looks like this is now in the main body
- Fig. 3.3, the fig sizes look strange

Sec. 3.4
- FInal paragraph… “In future we hope to test our method on a larger set of simulated signals, including those with more extreme mass ratios and different spin configurations, and to apply the method to real GW data”. You have now done this and the results are in the next chapter.



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
