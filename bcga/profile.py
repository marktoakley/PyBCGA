'''
@author: Mark Oakley
'''
import cProfile
from bcga.genetic_algorithm import GeneticAlgorithm
from pele.systems.ljcluster import LJCluster
from bcga.cluster_factory import ClusterFactory
from bcga.pele_interface import PeleMinimiser

natoms=13
minimiser = PeleMinimiser(LJCluster(13))
cProfile.run('GeneticAlgorithm(13,minimiser).run()')