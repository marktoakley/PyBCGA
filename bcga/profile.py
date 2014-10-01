'''
@author: Mark Oakley
'''
import cProfile
from bcga.genetic_algorithm import GeneticAlgorithm
from pele.systems.ljcluster import LJCluster
from bcga.cluster_factory import ClusterFactory

natoms=13
minimiser = LJCluster(13)
factory=ClusterFactory(13,minimiser)
cProfile.run('GeneticAlgorithm(13,factory).run()')