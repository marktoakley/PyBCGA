'''
@author: Mark Oakley
'''
import numpy as np
from bcga.cluster import Cluster
from bcga.composition import *

class ClusterFactory:
    '''Builds clusters.
    Parameters:
    natoms- Number of atoms in cluster.
    composition- List containing number of atoms of each type.
    labels- List containing names of each atom type.'''
    def __init__(self,natoms,minimiser,composition="default",labels=["X"]):
        self.natoms=natoms
        if composition=="default":
            self.composition=[natoms]
        else:
            self.composition=composition
        self.labels=labels
        self.system=minimiser
        
    def get_random_cluster(self):
        '''Return a cluster with random coordinates'''
        coords=(np.random.rand(self.natoms,3) -0.5) * 1.4 * float(self.natoms)**(1./3.)
        cluster = Cluster(self.natoms,
                          coords,
                          self.system,
                          atom_types=get_atom_types(self.composition),
                          labels=self.labels)
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
            cluster.sort_z()
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
        atom_types=fix_composition(self.composition,atom_types)
        offspring=Cluster(self.natoms,
                          coords,
                          self.system,
                          atom_types=atom_types,
                          labels=self.labels)
        offspring.quenched=False
        offspring.sort_type()
        cluster0.sort_type()
        cluster1.sort_type()
        return offspring
    
    def read_xyz(self,xyz_file):
        '''Read structure from xyz file.'''
        natoms=int(xyz_file.readline())
        coords=np.empty(shape=(natoms,3))
        energy=float(xyz_file.readline().split()[1])
        for i in range(0,natoms):
            coords[i]=xyz_file.readline().split()[1:4]
        cluster=Cluster(natoms,
                        coords,
                        self.system,
                        atom_types=get_atom_types(self.composition),
                        labels=self.labels)
        cluster.energy=energy
        cluster.quenched=True
        return cluster