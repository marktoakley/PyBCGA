.. image:: https://travis-ci.org/marktoakley/PyBCGA.svg?branch=master
    :target: https://travis-ci.org/marktoakley/PyBCGA

.. image:: https://coveralls.io/repos/github/marktoakley/PyBCGA/badge.svg?branch=master
    :target: https://coveralls.io/github/marktoakley/PyBCGA?branch=master

PyBCGA
++++++

Description
===========

A Python version of the Birmingham Cluster Genetic Algorithm.

The original methodology of the BCGA is described in Roy L. Johnston, Dalton Transactions, 2003, 4193-4207 (http://dx.doi.org/10.1039/b305686d).

The most recent version of the BCGA is available at https://bitbucket.org/JBADavis/bpga and presented in Jack B. A. Davis, Armin Shayeghi, Sarah L. Horswell, Roy L. Johnston, Nanoscale, 7, 2015, 14032-14038 (http://dx.doi.org/10.1039/c5nr03774c).

Installation
============

PyBCGA requires these Python packages:

numpy

pele (https://github.com/pele-python/pele)

gpaw (https://wiki.fysik.dtu.dk/gpaw/)

ase (https://wiki.fysik.dtu.dk/ase/)

numpy is available in the Ubuntu package repositories and can be installed with:

 $ sudo apt-get install python-numpy

Compile with:

  $ python setup.py build
  
Then add the installation directory to your PYTHONPATH environment variable.

Usage
=====

The examples directory contains a some examples of setting up and running the BCGA.
