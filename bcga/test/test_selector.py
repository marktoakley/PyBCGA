import unittest
from bcga.population import PopulationList
from bcga.cluster_factory import ClusterFactory
from bcga.selector import *
import pele.potentials.lj as lj
from bcga.pele_interface import PeleMinimiser

class ClusterTest(unittest.TestCase):
    def setUp(self):
        natoms=10
        minimiser=PeleMinimiser(lj.LJ())
        factory=ClusterFactory(natoms,minimiser)
        self.population=PopulationList(natoms,factory,max_size=5)
        while len(self.population) < self.population.max_size:
            self.population.append(factory.get_random_cluster())
        self.population.sort_energy()
        
    def test_tournament(self):
        selector=TournamentSelector(3)
        pair=selector.select(self.population)
        self.assertEquals(len(pair),2)
        self.assertNotEqual(pair[0],pair[1])
        
    def test_roulette(self):
        selector=RouletteSelector()
        for _ in range (0,50):#Repeat for several random selections
            pair=selector.select(self.population)
            self.assertEquals(len(pair),2)
            self.assertNotEqual(pair[0],pair[1])
            
if __name__ == "__main__":
    unittest.main()
