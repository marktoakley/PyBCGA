import unittest
from bcga.population import PopulationList
from bcga.cluster_factory import ClusterFactory
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
        
    def test_energy_sort(self):
        self.population.sort_energy()
        for i in range(1,self.population.max_size):
            self.assertGreater(self.population.get_energy(i),
                               self.population.get_energy(i-1))
            
if __name__ == "__main__":
    unittest.main()
