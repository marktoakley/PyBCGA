import unittest
from bcga.cluster import Cluster
import numpy as np

class ClusterTest(unittest.TestCase):
    def setUp(self):
        self.natoms=3
        coords=np.array(((0.,0.,0.1),
                         (1.,1.,0.3),
                         (0.,2.,0.2)))
        self.cluster = Cluster(self.natoms,coords)
        
    def test_z_sort(self):
        self.cluster.z_sort()
        for i in range(1,self.natoms):
            self.assertGreater(self.cluster.coords[i,2],self.cluster.coords[i-1,2])
   
    def test_get_energy(self):
        self.assertAlmostEquals(self.cluster.get_energy(),-3.)
                
if __name__ == "__main__":
    unittest.main()
