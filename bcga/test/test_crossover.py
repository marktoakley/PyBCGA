'''
@author: Mark Oakley
'''
import unittest

import pele.potentials.lj as lj

from bcga.cluster_factory import ClusterFactory
from bcga.pele_interface import PeleMinimiser
from bcga.crossover import DeavenHo

class CrossoverTest(unittest.TestCase):
    def test_mutant(self):
        natoms=10
        minimiser=PeleMinimiser(lj.LJ())
        factory=ClusterFactory(natoms,minimiser)
        parent_a = factory.get_random_cluster()   
        parent_b = factory.get_random_cluster() 
        crossover = DeavenHo()
        offspring = crossover.get_offspring(parent_a, parent_b)
        self.assertLess(offspring.get_energy(), 0)
         
if __name__ == "__main__":
    unittest.main()