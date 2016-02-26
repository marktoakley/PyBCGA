import unittest
import os

from pele.systems.ljcluster import LJCluster

from bcga.pele_interface import PeleMinimiser
from bcga.cluster_factory import ClusterFactory
from bcga.population import PopulationList

class ClusterTest(unittest.TestCase):
    def setUp(self):
        try:
            with open("restart.xyz",'w') as xyz_file:
                #Large negative energies to ensure that we're getting them from the file rather than calculating them.
                xyz_file.write("3\nEnergy -5.00\n")
                xyz_file.write("X 0.0 0.0 0.0\n")
                xyz_file.write("X 0.0 0.0 1.0\n")
                xyz_file.write("Y 0.0 1.0 0.0\n")
                xyz_file.write("3\nEnergy -4.00\n")
                xyz_file.write("X 0.0 0.0 0.0\n")
                xyz_file.write("X 0.0 1.0 1.0\n")
                xyz_file.write("Y 0.0 1.0 0.0\n")
        except IOError as err:
            print("File error: "+str(err))
            
    def tearDown(self):
        os.remove("restart.xyz")
            
    def test_cluster(self):
        natoms=3
        minimiser=PeleMinimiser(LJCluster(natoms))
        factory=ClusterFactory(natoms,minimiser)
        with open("restart.xyz",'r') as xyz_file:
            cluster=factory.read_xyz(xyz_file)
        self.assertEquals(-5.,cluster.get_energy())
        
    def test_population(self):
        natoms=3
        minimiser=PeleMinimiser(LJCluster(natoms))
        factory=ClusterFactory(natoms,minimiser)
        with open("restart.xyz",'r') as xyz_file:
            population=PopulationList(natoms,factory)
            population.read_xyz(xyz_file)
        self.assertEquals(-5.,population[0].get_energy())
        self.assertEquals(-4.,population[1].get_energy())

if __name__ == "__main__":
    unittest.main()