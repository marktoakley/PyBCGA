'''
A simple GA run. We use a 38 atom Lennard-Jones in this example.

The natoms argument defines the number of atoms in the cluster and is required for all GA searchs.
The minimiser object is also needed to perform the energy evaluations. This example uses a simple
Lennard-Jones minimiser. Other examples show how to set up minimisers for more complicated potentials.

@author: Mark Oakley
'''

from bcga.genetic_algorithm import GeneticAlgorithm
import pele.potentials.lj as lj
from bcga.pele_interface import PeleMinimiser

myga = GeneticAlgorithm(natoms=38, # Number of atoms
                        minimiser=PeleMinimiser(lj.LJ())) #Energy minimisation method
myga.run()
