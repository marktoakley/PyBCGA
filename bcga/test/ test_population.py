import unittest
from bcga.population import PopulationList
from bcga.cluster_factory import ClusterFactory
from pele.systems.ljcluster import LJCluster
from bcga.minimiser import PeleMinimiser

class ClusterTest(unittest.TestCase):
    def setUp(self):
        natoms=10
        minimiser=PeleMinimiser(LJCluster(natoms))
        factory=ClusterFactory(natoms,minimiser)
        self.population=PopulationList(natoms,factory,size=5)
        
    def test_energy_sort(self):
        self.population.sort_energy()
        for i in range(1,self.population.size):
            self.assertGreater(self.population.get_energy(i),
                               self.population.get_energy(i-1))
            
if __name__ == "__main__":
    unittest.main()
