'''
@author: Mark Oakley
'''
import numpy as np
from bcga.cluster import Cluster
from bcga.crossover import one_point

class ClusterFactory:
    '''Builds clusters.
    Parameters:
    natoms- Number of atoms in cluster.'''
    def __init__(self,natoms,atom_types=[],labels=["X"]):
        self.natoms=natoms
        self.atom_types=atom_types
        self.labels=labels
        #self.potential = lj.LJ()
        
    def get_random_cluster(self):
        '''Return a cluster with random coordinates'''
        coords=(np.random.rand(self.natoms,3) -0.5) * 1.4 * float(self.natoms)
        cluster = Cluster(self.natoms,coords,self.atom_types,self.labels)
        cluster.quenched=False
        return cluster
    
    def get_mutant(self,cluster):
        '''Generate a mutant structure from a parent structure.
        Currently, this randomises all of the coordinates in the mutant.'''
        mutant=self.get_random_cluster()
        return mutant
    
    def get_offspring(self,cluster0,cluster1):
        '''Generate an offspring structure from two parent structures.'''
        offspring=one_point(cluster0,cluster1)
        offspring.labels=self.labels
        return offspring
        
