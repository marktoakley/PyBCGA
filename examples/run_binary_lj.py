'''
Example PyBCGA input for a binary Lennard-Jones cluster.

@author: Mark Oakley
'''

from bcga.genetic_algorithm import GeneticAlgorithm
from pele.potentials import BLJCut
from bcga.pele_interface import PeleMinimiser

natoms = 13
ntypea = 5
ntypeb = 8
myga = GeneticAlgorithm(natoms=natoms,
                        minimiser=PeleMinimiser(BLJCut(natoms,ntypea)),
                        composition=[ntypea,ntypeb],
                        labels=["A","B"],
                        remove_duplicates=True,
                        max_generation=50)
myga.run()
