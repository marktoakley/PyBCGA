import unittest
from bcga.population import PopulationList
from bcga.cluster_factory import ClusterFactory
from pele.systems.ljcluster import LJCluster
from bcga.minimiser import PeleMinimiser
from bcga.selector import TournamentSelector

class ClusterTest(unittest.TestCase):
    def setUp(self):
        natoms=10
        minimiser=PeleMinimiser(LJCluster(natoms))
        factory=ClusterFactory(natoms,minimiser)
        self.population=PopulationList(natoms,factory,size=5)
        
    def test_tournament(self):
        selector=TournamentSelector(3)
        ls=selector.select(self.population)
        self.assertEquals(len(ls),2)
        self.assertNotEqual(ls[0],ls[1])
            
if __name__ == "__main__":
    unittest.main()
