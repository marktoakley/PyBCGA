'''
Simple BCGA run for a single-component Lennard-Jones cluster.

@author: Mark Oakley
'''

from bcga.batch_genetic_algorithm import BatchGeneticAlgorithm
from bcga.pele_interface import PeleMinimiser
import pele.potentials.lj as lj

natoms = 38
minimiser=PeleMinimiser(lj.LJ())

myga = BatchGeneticAlgorithm(natoms,
                        minimiser,
                        remove_duplicates=True,
                        max_generation=5)

myga.run()
#myga.write_xyz()
