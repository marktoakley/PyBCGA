'''
Run the BCGA

@author: Mark Oakley
'''

from bcga.genetic_algorithm import GeneticAlgorithm
from bcga.cluster_factory import ClusterFactory
from pele.systems.ljcluster import LJCluster
from bcga.minimiser import PeleMinimiser

natoms = 13
minimiser=PeleMinimiser(LJCluster(natoms))
factory=ClusterFactory(natoms,minimiser)

myga = GeneticAlgorithm(natoms,factory,remove_duplicates=True,max_generation=10)
myga.run()
myga.write_xyz()
