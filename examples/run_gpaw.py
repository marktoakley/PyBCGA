'''
Run the BCGA

@author: Mark Oakley
'''

from bcga.genetic_algorithm import GeneticAlgorithm
from bcga.cluster_factory import ClusterFactory
from bcga.minimiser import GPAWMinimiser

natoms = 3
minimiser=GPAWMinimiser()
factory=ClusterFactory(natoms,minimiser,
                       labels=["He"])

myga = GeneticAlgorithm(natoms,factory,pop_size=2,max_generation=1)
myga.run()
myga.write_xyz()
