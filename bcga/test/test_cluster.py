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
            self.assertGreater(self.cluster.get_coords(i)[2],
                               self.cluster.get_coords(i-1)[2])
   
    def test_get_energy(self):
        self.assertAlmostEquals(self.cluster.get_energy(),-3.)
        
    def test_centre(self):
        self.assertEquals(self.cluster.centre()[1],-1.)
    
    def test_get_atom(self):
        self.assertEquals(self.cluster.get_coords(0)[0],0.0)
        self.assertEquals(self.cluster.get_coords(0)[1],0.0)
        self.assertEquals(self.cluster.get_coords(0)[2],0.1)
        
    def test_get_label(self):
        self.assertEquals(self.cluster.get_label(2),"X")
        
class BinaryClusterTest(unittest.TestCase):
    def setUp(self):
        self.natoms=3
        coords=np.array(((0.,0.,0.1),
                         (1.,1.,0.3),
                         (0.,2.,0.2)))
        types=[0,1,0]
        labels=["X","Y"]
        self.cluster = Cluster(self.natoms,coords,atom_types=types,labels=labels)
    
    def test_labels(self):
        self.assertEquals(self.cluster.get_label(0),"X")
        self.assertEquals(self.cluster.get_label(1),"Y")
        self.assertEquals(self.cluster.get_label(2),"X")

    def test_sort_labels(self):
        self.cluster.z_sort()
        self.assertEquals(self.cluster.get_label(0),"X")
        self.assertEquals(self.cluster.get_label(1),"X")
        self.assertEquals(self.cluster.get_label(2),"Y")    

if __name__ == "__main__":
    unittest.main()