'''
Example PyBCGA input for a binary Lennard-Jones cluster.

@author: Mark Oakley
'''

from bcga.genetic_algorithm import GeneticAlgorithm
from bcga.cluster_factory import ClusterFactory
from pele.potentials import BLJCut
from bcga.minimiser import PeleMinimiser

natoms = 13
ntypea = 5
ntypeb = 8
minimiser=PeleMinimiser(BLJCut(natoms,ntypea))
myga = GeneticAlgorithm(natoms,minimiser,
                        composition=[ntypea,ntypeb],
                        labels=["A","B"],
                        remove_duplicates=True,
                        max_generation=50)
myga.run()
#myga.write_xyz()
