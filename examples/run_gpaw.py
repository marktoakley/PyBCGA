'''
Example input file for PyBCGA-DFT using GPAW.

@author: Mark Oakley
'''

from bcga.genetic_algorithm import GeneticAlgorithm
from bcga.minimiser import GPAWMinimiser

natoms = 3
minimiser=GPAWMinimiser()
myga = GeneticAlgorithm(natoms,minimiser,
                        labels=["He","Ne"],
                        composition=[2,1],
                        pop_size=2,
                        max_generation=1)
myga.run()
myga.write_xyz()
