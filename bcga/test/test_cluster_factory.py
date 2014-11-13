import unittest
from bcga.cluster_factory import ClusterFactory
import pele.potentials.lj as lj
from pele.systems.bljcluster import BLJCluster
from bcga.minimiser import PeleMinimiser

class ClusterFactoryTest(unittest.TestCase):
    def setUp(self):
        natoms=10
        minimiser=PeleMinimiser(lj.LJ())
        self.factory=ClusterFactory(natoms,minimiser)
        
    def test_mutant(self):
        cluster = self.factory.get_random_cluster()
        mutant = self.factory.get_mutant(cluster)
        self.assertLess(mutant.get_energy(), 0)
        
    def test_offspring(self):
        parent0=self.factory.get_random_cluster()
        parent1=self.factory.get_random_cluster()
        offspring =self.factory.get_offspring(parent0,parent1)
        self.assertLess(offspring.get_energy(), 0)
        
class BinaryFactoryTest(unittest.TestCase):
    def setUp(self):
        natoms=10
        minimiser=PeleMinimiser(BLJCluster(natoms,5))
        self.factory=ClusterFactory(natoms,minimiser,
                                    composition=[5,5],
                                    labels=["A","B"])
        
    def test_label(self):
        cluster = self.factory.get_random_cluster()
        self.assertEquals(cluster.get_label(0),"A")
        self.assertEquals(cluster.get_label(5),"B")

            
if __name__ == "__main__":
    unittest.main()
