---
layout: page
title: What is LFT?
description: A brief introduction to lattice quantum field theory
background: '/img/lattice-pipes.png'
---

Lattice Field Theory (LFT) is a computational approach
used in theoretical physics to study quantum field theories&mdash;most
famously Quantum Chromodynamics (QCD),
the theory of quarks and gluons.

In LFT,
space-time is replaced by a discrete grid (a lattice),
which makes it possible to simulate particle interactions using powerful supercomputers.
This framework enables first-principles calculations of
hadron masses,
decay constants,
form factors,
and many other key quantities in particle physics.

LFT was born from the seminal idea introduced by Kenneth Wilson in the 1970s,
who realized that
discretizing space–time provides a non-perturbative definition of gauge theories.

<figure class="image">
<img src="/img/phasediagram.png" alt='Phase diagram of QCD. A graph showing temperature on the vertical axis and baryon density on the horizontal axis. The region to the bottom left is marked "supernovae and neutron star mergers"; above this "hadron gas". This region is surrounded by a "chiral transition" and "deconfinement transition", ending in a "critical point". To the right of this is marked "Color superconductor?" To the top right "quark-gluon plasma", and to the top left "lattice QCD".' width="100%">
<figcaption>Phase diagram of QCD, from <a href="https://doi.org/10.1146/annurev-nucl-102419-041903">Drischler, Holt, and Wellenhofer, 2021</a>.</figcaption>
</figure>

Over the past decades,
lattice QCD has become a unique tool
for studying the dynamics of the strong interactions
non-perturbatively and from first principles.
Precision lattice calculations&mdash;leptonic decay constants,
semileptonic form factors,
neutral-meson mixing matrix elements and mass differences,
among many others&mdash;have
become essential for
interpreting key experimental measurements in flavour physics,
determining CKM matrix elements,
and placing stringent limits on physics beyond the Standard Model.
They have been central to landmark results such as
the validation of the CKM quark-flavour mixing pattern,
the determination of CP violation in the weak (quark) sector of the Standard Model,
and the interpretation of the muon &#119892; &minus; 2 anomaly.

In searches for physics beyond the Standard Model,
lattice calculations provide the non-perturbative matrix elements and hadronic inputs
that define the theoretical reach of experimental searches,
while new measurements continually shape and drive
the next generation of lattice computations.
Lattice methods are also yielding increasingly accurate predictions for
the properties of the Quark–Gluon Plasma,
from its equation of state to fluctuations of conserved charges,
the effects of strong electromagnetic fields,
hadronic dissociation,
transport coefficients,
and real-time dynamical phenomena,
including studies at finite baryon density.
Progress in each of these areas is crucial for
interpreting heavy-ion collision experiments without model-dependent assumptions.

<figure class="image">
<img src="/img/alpha-strong.svg" width="100%" alt="Graph of the strong coupling constant alpha-s as a function of mu (in GeV, on a logarithmic scale from 3 to 10000), showing an exponential decay fit from 0.35 at low mu to around 0.07 at high mu. Data from many different methods agree with the fit.">
<figcaption>The strong coupling constant for a wide range of energy scales, from <a href="https://doi.org/10.48550/arXiv.2501.06633">ALPHA Collaboration (2025)</a>.</figcaption>
</figure>

As a consequence,
the interaction
between Lattice Field Theory and experimental particle and nuclear physics
has evolved from a loose connection
into a tightly coupled,
mutually reinforcing synergy.
This interplay has matured to the point where
lattice predictions and experimental data are now analysed side by side,
each guiding the other.
Often LFT provides the non-perturbative inputs
that determine the theoretical reach of experiments,
while new measurements in turn drive
further lattice improvements required to fully exploit the experimental potential.

To keep pace with the experimental progress expected in the next decade,
the lattice community continuously strive to
access the most powerful HPC systems,
develop new high-performance algorithms,
and maintain highly parallel codes capable of running efficiently
on present and future supercomputers.

## Links

### Learn more about lattice field theory

#### [LaVA][lava]

[The Lattice Virtual Academy (LaVa)][lava]
 provides introductory online lectures on topics in LFT.

---

#### **Quantum Fields on a Lattice**
*István Montvay & Gernot Münster*
**ISBN-13:** 978-0521404327
A comprehensive treatment of lattice field theory, covering gauge fields, fermions, algorithms, and numerical methods.

---

#### **Lattice Gauge Theories: An Introduction**
*H. J. Rothe*
**ISBN-13:** 978-9812560629
A mathematically rigorous introduction to the foundations of lattice gauge theories, including gauge invariance, lattice actions, path integrals, and continuum limits.

---

#### **Lattice Quantum Chromodynamics: Practical Essentials**
*Carleton DeTar & Steven Gottlieb*
**ISBN-13:** 978-9402409970
A modern, concise guide to the practical and algorithmic aspects of lattice QCD simulations.

---

#### **Lattice Methods for Quantum Chromodynamics**
*Thomas DeGrand & Carleton DeTar*
**ISBN-13:** 978-9812567277
An applied introduction emphasising spectroscopy, fermion formulations, simulation workflows, and computational strategies.

---

#### **Quantum Chromodynamics on the Lattice: An Introductory Presentation**
*Christof Gattringer & Christian B. Lang*
**ISBN-13:** 978-3642018497
A pedagogical introduction to lattice QCD, covering the theoretical foundations, fermions, gauge fields, Monte Carlo methods, and hadron spectroscopy.


---

### Related organisations:

- [International Lattice Data Grid (ILDG)][ildg]:
  Defines standards for data sharing in LFT

- [USQCD Collaboration][usqcd]:
  Representing the majority of LFT research in the USA

[ildg]: https://hpc.desy.de/ildg/
[lava]: https://sites.google.com/view/lattice-virtual-academy/
[usqcd]: https://www.usqcd.org
