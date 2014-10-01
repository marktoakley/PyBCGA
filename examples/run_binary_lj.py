'''
Run the BCGA

@author: Mark Oakley
'''

from bcga.genetic_algorithm import GeneticAlgorithm
from bcga.cluster_factory import ClusterFactory
from pele.systems.bljcluster import BLJCluster
from bcga.minimiser import PeleMinimiser

natoms = 13
minimiser=PeleMinimiser(BLJCluster(13,5))
factory=ClusterFactory(natoms,minimiser,
                       composition=[5,8],
                       labels=["A","B"])

myga = GeneticAlgorithm(natoms,factory,remove_duplicates=True,max_generation=50)
myga.run()
myga.write_xyz()
