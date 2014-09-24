import unittest
from bcga.cluster_factory import ClusterFactory

class ClusterFactoryTest(unittest.TestCase):
    def setUp(self):
        natoms=10
        self.factory=ClusterFactory(natoms)
        
    def test_mutant(self):
        cluster = self.factory.get_random_cluster()
        mutant = self.factory.get_mutant(cluster)
        self.assertLess(mutant.get_energy(), 0)
        
    def test_offspring(self):
        parent0=self.factory.get_random_cluster()
        parent1=self.factory.get_random_cluster()
        offspring =self.factory.get_offspring(parent0,parent1)
        self.assertLess(offspring.get_energy(), 0)

            
if __name__ == "__main__":
    unittest.main()
