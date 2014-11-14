import unittest

from bcga.pele_interface import PeleMinimiser
from pele.systems.bljcluster import BLJCluster
from bcga.cluster_factory import ClusterFactory
from bcga.mutator import MutateExchange

class ClusterTest(unittest.TestCase):
        
    def test_exchange(self):
        natoms=20
        minimiser=PeleMinimiser(BLJCluster(natoms,10))
        factory=ClusterFactory(natoms,minimiser,
                                    composition=[10,10],
                                    labels=["A","B"])
        cluster = factory.get_random_cluster()
        mutator = MutateExchange()
        for i in range(0,50):
            mutant=mutator.get_mutant(cluster)
            self.assertEquals(mutant.atom_types[9],0)
            self.assertEquals(mutant.atom_types[10],1)
            
if __name__ == "__main__":
    unittest.main()
