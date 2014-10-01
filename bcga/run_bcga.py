'''
Run the BCGA

@author: Mark Oakley
'''

from bcga.genetic_algorithm import GeneticAlgorithm
from bcga.cluster_factory import ClusterFactory
from pele.systems.ljcluster import LJCluster

natoms = 13
system=LJCluster(natoms)
factory=ClusterFactory(natoms,system)

myga = GeneticAlgorithm(natoms,factory,remove_duplicates=True,max_generation=10)
myga.run()
myga.write_xyz()
