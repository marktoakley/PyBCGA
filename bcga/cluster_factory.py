'''
@author: Mark Oakley
'''
import numpy as np
from bcga.cluster import Cluster
import pele.potentials.lj as lj

class ClusterFactory:
    '''Builds clusters.
    Parameters:
    natoms- Number of atoms in cluster.
    composition- List containing number of atoms of each type.
    labels- List containing names of each atom type.'''
    def __init__(self,natoms,minimiser,composition=[],labels=["X"]):
        self.natoms=natoms
        if composition==[]:
            self.composition=[natoms]
        else:
            self.composition=composition
        self.labels=labels
        self.system=minimiser
        
    def get_random_cluster(self):
        '''Return a cluster with random coordinates'''
        coords=(np.random.rand(self.natoms,3) -0.5) * 1.4 * float(self.natoms)
        cluster = Cluster(self.natoms,
                          coords,
                          self.system,
                          atom_types=self.get_atom_types(),
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
        atom_types=self.fix_composition(atom_types)
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
    
    def get_atom_types(self):
        '''
        Return an atom_types array (needed for creation of new random clusters).
        '''
        atom_types=[]
        for i in range(0,len(self.composition)):
            for j in range(0,self.composition[i]):
                atom_types.append(i)
        return atom_types
    
    def fix_composition(self,in_types):
        '''Returns an atom_types array with the correct composition'''
        wrong_composition = True
        while wrong_composition:
            if self.get_composition(in_types)[0]==self.composition[0]:
                wrong_composition=False
            if self.get_composition(in_types)[0]>self.composition[0]:
                in_types[np.random.randint(0,self.natoms)]=1
            if self.get_composition(in_types)[0]<self.composition[0]:
                in_types[np.random.randint(0,self.natoms)]=0
        return in_types
    
    def get_composition(self,atom_types):
        '''Return a list containing the number of atoms of each type.'''
        composition = [0] *len(self.labels)
        for i in atom_types:
            composition[i]+=1
        return composition
            
        
