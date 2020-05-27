---
layout: default
title: Research
nav: small
---

# The Structure, Kinematics and Dynamics of the Milky Way

<h4> <i> <a href="https://arxiv.org/abs/1706.00018"> The age-metallicity structure of the Milky Way disc using APOGEE </a> </i> </h4>
<p> I lead a paper in 2017 in which we measured the structure of the Milky Way disc's stars as
a function of their age and metallicity. We used data from the Sloan Digital Sky Survey's (SDSS)
<em> Apache Point Observatory Galactic Evolution Experiment </em> (APOGEE), which has measured
the element abundances and properties of over 100,000 stars in the Galaxy. We showed that the
Galaxy structure is very complex, and confirmed results that showed that the thick disc component
in the Milky Way is not spatially distinct from its thinner components.
An open access version of the paper is available  <a href="https://arxiv.org/abs/1706.00018">here</a>.</p>

<h4> <i> <a href="https://arxiv.org/abs/1802.02592"> Fast estimation of orbital parameters for Milky Way-like potentials </a> </i> </h4>
<p>With the recent advent of large spectroscopic surveys in the Milky Way (such as APOGEE, mentioned above), and the unprecedented set of data which is due to become available from the ESA-<i> Gaia </i> mission, the kinematic and dynamical structure of the Galaxy will be probed at a deeper level than ever before. These datasets will be large, and will require efficient computational techniques to be fully recognised. In 2018, I wrote a paper with <a href="http://astro.utoronto.ca/~bovy/">Jo Bovy (University of Toronto)</a>, where we developed and tested a fast method for estimating orbital parameters, without recourse to computationally expensive orbit integration. You can find that paper <a href="https://arxiv.org/abs/1802.02592">here</a>, and the related code and other exploration <a href="https://github.com/jmackereth/orbit-estimation">here</a>. A nice tutorial showing its implementation in Jo Bovy's <a href="https://github.com/jobovy/galpy">galpy</a> package is available <a href="http://galpy.readthedocs.io/en/latest/orbit.html#new-in-v1-3-fast-orbit-characterization">here</a>. I am now working on various projects which will explore the kinematic and dynamical structure and history of the Milky Way, using this code and other methods. </p>
<h4> <i> <a href="https://arxiv.org/abs/1901.04502"> Dynamical heating across the Milky Way disc using APOGEE and Gaia </a> </i> </h4>
<p> In another recent paper, using the <i>Gaia</i> DR2 dataset in conjunction with APOGEE, I fit models for the kinematics of mono-age, mono-metallicity populations in the Milky Way disc. For that paper, I developed a new catalogue of ages for stars in APOGEE which uses a neural network model from the <a href="https://astronn.readthedocs.io/en/latest/">astroNN</a> python package to estimate ages from the stellar spectra, trained on ages measured using asteroseismology, from the APOKASC-2 (APOGEE-<i>Kepler</i>) catalogue. Among many other interesting findings, we discovered that the history of dynamical heating of the high and low [&alpha;/Fe] populations (as mentioned above) appears to show that they really were formed and evolved completely differently. You can read the paper  <a href="https://arxiv.org/abs/1901.04502">here</a>, and see the code <a href="https://github.com/jmackereth/monoage-velocity-dispersion">here</a>. A summary page for that paper, including descriptions of the age catalogue which is made available there, can be found at <a href="dynamical-heating.html">this link</a>
</p>

# Simulating Galaxy Formation

<h4> <i> <a href="https://arxiv.org/abs/1801.03593"> The origin of diverse &alpha;-element enrichment in galaxy discs </a> </i> </h4>
<p> I am interested in the use of large volume cosmological simulations to help understand the
Milky Way in a cosmological context. In early 2018, I lead a project using the <em> Evolution and Assembly
of GaLaxies and their Environments </em> (EAGLE) suite of cosmological simulations to understand how the
patterns in element abundances we see in the Milky Way emerge. The Milky Way disc has two distinct
populations of stars when abundances of light elements such as Oxygen are considered, and the origin
of these populations has long been a problem in galaxy formation. EAGLE produces a large population
of galaxies which have similar properties to the Milky Way in terms of their element abundances and
so understanding the origins of these properties may inform how we understand the Milky Way as a
galaxy in the Universe. You can see the results and other material relating to that paper <a href="eagle-alpha.html">here</a>,
and see an open-access version of the paper <a href="https://arxiv.org/abs/1801.03593">here</a></p>

<h4> <i> <a href="https://arxiv.org/abs/1808.00968"> The origin of accreted stellar halo populations in the Milky Way using APOGEE, Gaia, and the EAGLE simulations </a> </i> </h4>
<p> Following the release of <i>Gaia</i>-DR2, many groups independently uncovered the presence of a large number of stars in the Milky Way stellar halo which appeared to originate from the accretion of a large and ancient satellite galaxy, now referred to as <i>Gaia</i>-Enceladus, onto ours (this discovery sparked a large number of <a href="https://www.space.com/42305-milky-way-absorbed-giant-dwarf-galaxy-gaia-enceladus.html">news stories</a> around the original articles). I lead one of the papers which was among the first to report the discovery, and also provided a precise estimate of the stellar mass of the progenitor of this stellar population, using the EAGLE simulations as a guide. The paper is available to read <a href="https://arxiv.org/abs/1808.00968">here</a>. We suggest in the paper that this large accretion event provides evidence that the Milky Way's history of assembly has been unusual, as we suggested in the work above.
</p>
