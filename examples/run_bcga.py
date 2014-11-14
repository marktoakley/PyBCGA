'''
Simple BCGA run for a single-component Lennard-Jones cluster.

@author: Mark Oakley
'''

from bcga.genetic_algorithm import GeneticAlgorithm
import pele.potentials.lj as lj
from bcga.pele_interface import PeleMinimiser

natoms = 38
minimiser=PeleMinimiser(lj.LJ())

myga = GeneticAlgorithm(natoms,minimiser,remove_duplicates=True,max_generation=10)
myga.run()
#myga.write_xyz()
