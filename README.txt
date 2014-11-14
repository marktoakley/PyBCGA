PyBCGA
++++++

Description
===========

A Python version of the Birmingham Cluster Genetic Algorithm.
The BCGA is decribed in Roy L. Johnston, Dalton Transactions, 2003, 4193-4207 (http://dx.doi.org/10.1039/b305686d).

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
