'''
Run the BCGA

@author: Mark Oakley
'''

from bcga.genetic_algorithm import Genetic_algorithm as ga
from bcga.cluster_factory import ClusterFactory
from pele.systems.bljcluster import BLJCluster
from pele.systems.ljcluster import LJCluster

natoms = 13
system=BLJCluster(13,5)
factory=ClusterFactory(natoms,system,
                       composition=[5,8],
                       labels=["A","B"])

myga = ga(natoms,factory,remove_duplicates=True,max_generation=50)
myga.run()
myga.write_xyz()
