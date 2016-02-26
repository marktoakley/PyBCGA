import unittest
from bcga.cluster_factory import ClusterFactory
import pele.potentials.lj as lj
from pele.systems.bljcluster import BLJCluster
from bcga.pele_interface import PeleMinimiser

class ClusterFactoryTest(unittest.TestCase):
    def setUp(self):
        natoms=10
        minimiser=PeleMinimiser(lj.LJ())
        self.factory=ClusterFactory(natoms,minimiser)
        
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
