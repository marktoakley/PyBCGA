'''
@author: Mark
'''
import unittest
import os

from bcga.genetic_algorithm import GeneticAlgorithm
import pele.potentials.lj as lj
from bcga.pele_interface import PeleMinimiser

class GATest(unittest.TestCase):
    def setUp(self):
        natoms=10
        minimiser=PeleMinimiser(lj.LJ())
        self.ga=GeneticAlgorithm(natoms,minimiser,max_generation=2)
        
    def tearDown(self):
        os.remove("restart.xyz")
        
    def test_run(self):
        #For now, just run and see that there are no exceptions.
        self.ga.run()
                    
if __name__ == "__main__":
    unittest.main()