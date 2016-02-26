import unittest
import numpy as np
from math import sqrt

import pele.potentials.lj as lj
from pele.potentials import BLJCut

from bcga.cluster import Cluster
from bcga.pele_interface import PeleMinimiser

class ClusterTest(unittest.TestCase):
    def setUp(self):
        self.natoms=3
        minimiser=PeleMinimiser(lj.LJ())
        coords=np.array(((0.,0.,0.1),
                         (1.,1.,0.3),
                         (0.,2.,0.2)))
        self.cluster = Cluster(self.natoms,coords,minimiser)
        
    def test_z_sort(self):
        self.cluster.sort_z()
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
        
class OverlapTest(unittest.TestCase):
    def setUp(self):
        self.natoms=3
        minimiser=PeleMinimiser(lj.LJ())
        coords=np.array(((0.  ,0.  ,0.1),
                         (0.1 ,0.1 ,0.1),
                         (0.  ,0.2 ,0.2)))
        self.cluster = Cluster(self.natoms,coords,minimiser)
        
    def test_cutoff_default(self):
        self.cluster.fix_overlaps()
        self.assertGreaterEqual(min_dist(self.cluster._coords), 1.0)
        
    def test_cutoff_2(self):
        self.cluster.fix_overlaps(2.0)
        self.assertGreaterEqual(min_dist(self.cluster._coords), 2.0)

def min_dist(coords):
    min_r = 1e6
    for i in range (0,len(coords)):
        for j in range (i+1,len(coords)):
            vec=coords[i,:] - coords[j,:]
            r = vec.dot(vec) 
            if r < min_r:
                min_r = r
    return sqrt(min_r)
        
class BinaryClusterTest(unittest.TestCase):
    def setUp(self):
        self.natoms=3
        minimiser=PeleMinimiser(BLJCut(3,1))
        coords=np.array(((0.,0.,0.1),
                         (1.,1.,0.3),
                         (0.,2.,0.2)))
        types=[0,1,0]
        labels=["X","Y"]
        self.cluster = Cluster(self.natoms,coords,minimiser,
                               atom_types=types,labels=labels)
    
    def test_labels(self):
        self.assertEquals(self.cluster.get_label(0),"X")
        self.assertEquals(self.cluster.get_label(1),"Y")
        self.assertEquals(self.cluster.get_label(2),"X")

    def test_sort_labels(self):
        self.cluster.sort_z()
        self.assertEquals(self.cluster.get_label(0),"X")
        self.assertEquals(self.cluster.get_label(1),"X")
        self.assertEquals(self.cluster.get_label(2),"Y")    

if __name__ == "__main__":
    unittest.main()