'''
@author: Mark Oakley
'''
import numpy as np
from bcga.cluster import Cluster
from bcga.composition import *
from bcga.mutator import MutateReplace
from bcga.crossover import DeavenHo

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
        self.minimiser=minimiser
        
    def get_random_cluster(self):
        '''Return a cluster with random coordinates'''
        coords=(np.random.rand(self.natoms,3) -0.5) * 1.4 * float(self.natoms)**(1./3.)
        cluster = Cluster(self.natoms,
                          coords,
                          self.minimiser,
                          atom_types=get_atom_types(self.composition),
                          labels=self.labels)
        cluster.quenched=False
        return cluster
    
    def read_xyz(self,xyz_file):
        '''Read structure from xyz file.'''
        natoms=int(xyz_file.readline())
        coords=np.empty(shape=(natoms,3))
        energy=float(xyz_file.readline().split()[1])
        for i in range(0,natoms):
            coords[i]=xyz_file.readline().split()[1:4]
        cluster=Cluster(natoms,
                        coords,
                        self.minimiser,
                        atom_types=get_atom_types(self.composition),
                        labels=self.labels)
        cluster.energy=energy
        cluster.quenched=True
        return cluster
    
    def read_db(self,minimum):
        '''Read structure from Pele minimum'''
        cluster=Cluster(self.natoms,
                        np.reshape(minimum.coords,(-1,3)),
                        self.minimiser,
                        atom_types=get_atom_types(self.composition),
                        labels=self.labels)
        cluster.energy=minimum.energy
        cluster.quenched=True
        return cluster