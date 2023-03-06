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

- [ ] example comment; suggest title of chapter 1 be "Introduction to BH ringdown", or similar

Comments on Chapter 2

Sec 2.1 
- Paragraph 1, “previous studies” consider changing to “early studies”. I think the original wording was more appropriate when we wrote the paper, but a couple of years have passed since then and many papers now using multiple modes and overtones.
- Similarly… Also in para 1, the phrase “Several studies caution” could be changed to “Several early studies caution”
- Paragraph 2. When discussing why this is a “surprising” result you might also consider adding some more recent references, perhaps to some of the nonlinear QNM studies from 2022.
- Paragraph 2. “The primary aim of this paper…” change to “this study” or “this chapter”.
- Paragraph 3. There is another instance of “this paper”. Do a find replace. I will stop commenting on this from now on.
- Final paragraph. “Use natural units in which …” Do you want to say this here, or maybe in the introductory chapter? Or both, it doesn’t do any harm to repeat it here I suppose.

Sec 2.2
- Eq. 2.1. Do you want to explain the range of indices for l and m in the sum? Or is this already explained in the introduction?
- Paragraph 1. “We will assume the above has been rotated”. - make reference to fact that we will need to rotate the precessing systems
- Eqs. 2.8 and 2.9. Consider adding punctuation at end of equation.
- Eq. 2.10. Do you want to say that bold quantities refer to vectors containing discretely sampled versions of the waveform model?
- Eq. 2.11 and surrounding text. Is this really necessary? I’m not sure what exactly you are trying to say here.
- Eq. 2.12. You refer to this as the “coefficient matrix”. I don’t really like this name because I naturally associate the word coefficient with the C quantities. Does this quantity need a specific name? If not, then I suggest just saying “this matrix encodes the time dependence of all the QNMs included in the model”.
- In section 2.3.2, did you want to explain why this stacking of all the lm modes is equivalent to doing a least-squares fit averaged over Omega?
- 


Sec 2.5
 - Refs about precessing systems detected in the LIGO catalogs may be somewhat out to date now. You can fix by changing “Several of the GW detections already show signs of precession” -> “Several of the GW detections IN THE SECOND GW TRANSIENT CATALOG already show signs of precession”. And, optionally, you could add a sentence and references about by more recent events as well.

Discussion section: Another instance of “this paper” -> “this chapter”

OVERALL COMMENTS ON CHAPTER 2
- Figure placement is a nightmare! **Make captions wider?** 
 - What was Fig. 12 in the paper… this contains 6 panels and has a table in the figure caption. The layout here is a problem. Taking out could be an option? 


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
