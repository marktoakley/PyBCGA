'''
@author: Mark
'''
import unittest
from bcga.genetic_algorithm import Genetic_algorithm
from bcga.cluster_factory import ClusterFactory
from pele.systems.ljcluster import LJCluster

class GATest(unittest.TestCase):
    def setUp(self):
        natoms=10
        system=LJCluster(natoms)
        factory=ClusterFactory(natoms,system)
        self.ga=Genetic_algorithm(natoms,factory,max_generation=2)
        
    def test_run(self):
        #For now, just run and see that there are no exceptions.
        self.ga.run()
                    
if __name__ == "__main__":
    unittest.main()