'''
@author: Mark Oakley
'''
from abc import ABCMeta, abstractmethod
import numpy as np

from bcga.cluster import Cluster
from bcga.composition import fix_composition, get_composition

class Crossover():
    '''Abstract superclass for crossover.'''
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def get_offspring(self,cluster_a,cluster_b):
        '''Generate a new cluster object based on two parent cluster objects.'''
        pass

class DeavenHo(Crossover):
    '''Use the Deaven-Ho cut-and-splice method.'''
    
    def get_offspring(self,cluster_a,cluster_b):
        '''Generate an offspring structure from two parent structures.'''
        #Prepare clusters
        for cluster in [cluster_a,cluster_b]:
            cluster.centre()
            cluster.rotate_random()
            cluster.sort_z()
        #Choose cutting plane
        cut=np.random.randint(1,cluster_a.natoms)
        #Make new cluster
        coords=np.empty(shape=(cluster_a.natoms,3))
        atom_types=[]
        for i in range(0,cut):
            coords[i]=cluster_a.get_coords(i)
            atom_types.append(cluster_a.atom_types[i])
        for i in range(cut,cluster_a.natoms):
            coords[i]=cluster_b.get_coords(i)
            atom_types.append(cluster_b.atom_types[i])
            composition = get_composition(cluster_a.atom_types)
        atom_types=fix_composition(composition,atom_types)
        offspring=Cluster(cluster_a.natoms,
                          coords,
                          cluster_a.minimiser,
                          atom_types=atom_types,
                          labels=cluster_a.labels)
        offspring.quenched=False
        offspring.sort_type()
        cluster_a.sort_type()
        cluster_b.sort_type()
        return offspring