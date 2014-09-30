'''
@author: Mark Oakley
'''
import cProfile
from bcga.genetic_algorithm import Genetic_algorithm as ga
from pele.systems.ljcluster import LJCluster
from bcga.cluster_factory import ClusterFactory

natoms=13
system = LJCluster(13)
factory=ClusterFactory(13,system)
cProfile.run('ga(13,factory).run()')