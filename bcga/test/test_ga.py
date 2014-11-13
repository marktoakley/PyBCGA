'''
@author: Mark
'''
import unittest
from bcga.genetic_algorithm import GeneticAlgorithm
import pele.potentials.lj as lj
from bcga.minimiser import PeleMinimiser

class GATest(unittest.TestCase):
    def setUp(self):
        natoms=10
        minimiser=PeleMinimiser(lj.LJ())
        self.ga=GeneticAlgorithm(natoms,minimiser,max_generation=2)
        
    def test_run(self):
        #For now, just run and see that there are no exceptions.
        self.ga.run()
                    
if __name__ == "__main__":
    unittest.main()