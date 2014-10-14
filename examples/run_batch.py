'''
Simple BCGA run for a single-component Lennard-Jones cluster.

@author: Mark Oakley
'''

from bcga.batch_genetic_algorithm import BatchGeneticAlgorithm
from pele.systems.ljcluster import LJCluster
from bcga.minimiser import PeleMinimiser

natoms = 38
minimiser=PeleMinimiser(LJCluster(natoms))

myga = BatchGeneticAlgorithm(natoms,
                        minimiser,
                        remove_duplicates=True,
                        max_generation=100)

myga.run()
#myga.write_xyz()
