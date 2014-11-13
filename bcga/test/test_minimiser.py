'''
@author: Mark Oakley
'''
import unittest
from bcga.cluster import Cluster
import numpy as np
import pele.potentials.lj as lj
from bcga.minimiser import PeleMinimiser

class ClusterTest(unittest.TestCase):
    def setUp(self):
        natoms=3
        self.minimiser=PeleMinimiser(lj.LJ())
        coords=np.array(((0.,0.,0.1),
                         (1.,1.,0.3),
                         (0.,2.,0.2)))
        self.cluster = Cluster(natoms,coords,self.minimiser)
   
    def test_get_energy(self):
        self.minimiser.minimise(self.cluster)
        self.assertAlmostEquals(self.cluster.energy,-3.)