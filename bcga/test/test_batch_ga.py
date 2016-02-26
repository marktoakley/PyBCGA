'''
@author: Mark
'''
import unittest
import os

from bcga.batch_genetic_algorithm import BatchGeneticAlgorithm
import pele.potentials.lj as lj
from bcga.pele_interface import PeleMinimiser

class GATest(unittest.TestCase):
    def setUp(self):
        natoms=10
        minimiser=PeleMinimiser(lj.LJ())
        self.ga=BatchGeneticAlgorithm(natoms,minimiser,max_generation=20)
        
    def tearDown(self):
        os.remove("mydatabase.sqlite")
        
    def test_run(self):
        #For now, just run and see that there are no exceptions.
        self.ga.run()
        
    
                    
if __name__ == "__main__":
    unittest.main()