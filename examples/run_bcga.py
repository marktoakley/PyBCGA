'''
Simple BCGA run for a single-component Lennard-Jones cluster.

@author: Mark Oakley
'''

from bcga.genetic_algorithm import GeneticAlgorithm
from pele.systems.ljcluster import LJCluster
from bcga.minimiser import PeleMinimiser

natoms = 38
minimiser=PeleMinimiser(LJCluster(natoms))

myga = GeneticAlgorithm(natoms,minimiser,remove_duplicates=True,max_generation=100)
myga.run()
myga.write_xyz()
