'''
@author: Mark Oakley
'''
import cProfile
from bcga.genetic_algorithm import GeneticAlgorithm
from pele.systems.ljcluster import LJCluster
from bcga.cluster_factory import ClusterFactory

natoms=13
system = LJCluster(13)
factory=ClusterFactory(13,system)
cProfile.run('GeneticAlgorithm(13,factory).run()')