'''
Example input file for PyBCGA-DFT using GPAW.

@author: Mark Oakley
'''

from bcga.genetic_algorithm import GeneticAlgorithm
from bcga.gpaw_interface import GPAWMinimiser
from gpaw import PW

natoms = 4
minimiser=GPAWMinimiser(mode=PW(),xc="PBE")
myga = GeneticAlgorithm(natoms,minimiser,
                        labels=["Ag","Au"],
                        composition=[2,2],
                        pop_size=10,
                        offspring=8,
                        max_generation=1,
                        mutant_rate=0.1)
myga.run()
#myga.write_xyz()
