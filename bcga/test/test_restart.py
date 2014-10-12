import unittest
from bcga.cluster import Cluster
import numpy as np
from pele.systems.ljcluster import LJCluster
from pele.systems.bljcluster import BLJCluster
from bcga.minimiser import PeleMinimiser
from bcga.cluster_factory import ClusterFactory

class ClusterTest(unittest.TestCase):
    def setUp(self):
        try:
            with open("restart.xyz",'w') as xyz_file:
                #Dummy geometry
                xyz_file.write("3\nEnergy -3.00\n")
                xyz_file.write("X 0.0 0.0 0.0\n")
                xyz_file.write("X 0.0 0.0 1.0\n")
                xyz_file.write("Y 0.0 1.0 0.0\n")
                xyz_file.write("3\nEnergy-2.00\n")
                xyz_file.write("X 0.0 0.0 0.0\n")
                xyz_file.write("X 0.0 1.0 1.0\n")
                xyz_file.write("Y 0.0 1.0 0.0\n")
        except IOError as err:
            print("File error: "+str(err))
            
    def test_cluster(self):
        natoms=3
        minimiser=PeleMinimiser(LJCluster(natoms))
        factory=ClusterFactory(natoms,minimiser)
        with open("restart.xyz",'r') as xyz_file:
            cluster=factory.read_xyz(xyz_file)
        self.assertEquals(-3.,cluster.get_energy())

if __name__ == "__main__":
    unittest.main()