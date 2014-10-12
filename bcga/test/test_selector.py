import unittest
from bcga.population import PopulationList
from bcga.cluster_factory import ClusterFactory
from pele.systems.ljcluster import LJCluster
from bcga.minimiser import PeleMinimiser
from bcga.selector import *

class ClusterTest(unittest.TestCase):
    def setUp(self):
        natoms=10
        minimiser=PeleMinimiser(LJCluster(natoms))
        factory=ClusterFactory(natoms,minimiser)
        self.population=PopulationList(natoms,factory,size=5)
        self.population.fill()
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
