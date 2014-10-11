'''
Example input file for PyBCGA-DFT using GPAW.

@author: Mark Oakley
'''

from bcga.genetic_algorithm import GeneticAlgorithm
from bcga.minimiser import GPAWMinimiser
from gpaw import PW

natoms = 3
minimiser=GPAWMinimiser(mode=PW(),xc="PBE")
myga = GeneticAlgorithm(natoms,minimiser,
                        labels=["He"],
                        composition=[3],
                        pop_size=2,
                        offspring=1,
                        max_generation=1,
                        mutant_rate=0.0)
myga.run()
#myga.write_xyz()
