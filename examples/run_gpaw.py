'''
Run the BCGA

@author: Mark Oakley
'''

from bcga.genetic_algorithm import GeneticAlgorithm
from bcga.cluster_factory import ClusterFactory
from bcga.minimiser import GPAWMinimiser

natoms = 3
minimiser=GPAWMinimiser()
myga = GeneticAlgorithm(natoms,minimiser,
                        labels=["He"],
                        pop_size=2,
                        max_generation=1)
myga.run()
myga.write_xyz()
