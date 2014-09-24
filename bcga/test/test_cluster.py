import unittest
from bcga.cluster import Cluster

class ClusterTest(unittest.TestCase):
    def setUp(self):
        self.natoms=10
        self.cluster = Cluster(self.natoms)
        
    def test_z_sort(self):
        self.cluster.z_sort()
        for i in range(1,self.natoms):
            self.assertGreater(self.cluster.coords[i,2],self.cluster.coords[i-1,2])
            
if __name__ == "__main__":
    unittest.main()
