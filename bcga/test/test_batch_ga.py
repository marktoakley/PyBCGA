'''
@author: Mark
'''
import unittest
from bcga.batch_genetic_algorithm import BatchGeneticAlgorithm
from pele.systems.ljcluster import LJCluster
from bcga.minimiser import PeleMinimiser

class GATest(unittest.TestCase):
    def setUp(self):
        natoms=10
        minimiser=PeleMinimiser(LJCluster(natoms))
        self.ga=BatchGeneticAlgorithm(natoms,minimiser,max_generation=20)
        
    def test_run(self):
        #For now, just run and see that there are no exceptions.
        self.ga.run()
                    
if __name__ == "__main__":
    unittest.main()