import unittest
from bcga.cluster_factory import ClusterFactory

class ClusterTest(unittest.TestCase):
    def setUp(self):
        self.natoms=10
        factory =ClusterFactory(self.natoms)
        self.cluster = factory.get_random_cluster()
        
    def test_z_sort(self):
        self.cluster.z_sort()
        for i in range(1,self.natoms):
            self.assertGreater(self.cluster.coords[i,2],self.cluster.coords[i-1,2])
            
if __name__ == "__main__":
    unittest.main()
