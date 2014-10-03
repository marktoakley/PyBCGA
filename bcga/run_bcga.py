'''
Run the BCGA

@author: Mark Oakley
'''

from bcga.genetic_algorithm import GeneticAlgorithm
from pele.systems.ljcluster import LJCluster
from bcga.minimiser import PeleMinimiser

natoms = 13
minimiser=PeleMinimiser(LJCluster(natoms))

myga = GeneticAlgorithm(natoms,minimiser,remove_duplicates=True,max_generation=10)
myga.run()
myga.write_xyz()
