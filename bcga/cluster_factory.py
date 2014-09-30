'''
@author: Mark Oakley
'''
import numpy as np
from bcga.cluster import Cluster

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
        '''Generate an offspring structure from two parent structures.
        This uses the Deaven-Ho cut-and-splice method.'''
        #Prepare clusters
        for cluster in [cluster0,cluster1]:
            cluster.centre()
            cluster.rotate_random()
            cluster.z_sort()
        #Choose cutting plane
        cut=np.random.randint(1,self.natoms)
        #Make new cluster
        coords=np.empty(shape=(self.natoms,3))
        atom_types=[]
        for i in range(0,cut):
            coords[i]=cluster0.get_coords(i)
            atom_types.append(cluster0.atom_types[i])
        for i in range(cut,self.natoms):
            coords[i]=cluster1.get_coords(i)
            atom_types.append(cluster1.atom_types[i])
        offspring=Cluster(self.natoms,coords,atom_types=atom_types,labels=self.labels)
        offspring.quenched=False
        return offspring
        
