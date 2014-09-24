import unittest
from bcga.population import PopulationList

class ClusterTest(unittest.TestCase):
    def setUp(self):
        self.natoms=10
        self.population=PopulationList(self.natoms,size=5)
        
    def test_energy_sort(self):
        self.population.sort_energy()
        for i in range(1,self.population.size):
            self.assertGreater(self.population.get_energy(i),
                               self.population.get_energy(i-1))
            
if __name__ == "__main__":
    unittest.main()
