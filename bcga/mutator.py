'''
@author: Mark Oakley
'''
from bcga.cluster import Cluster
import numpy as np
from bcga.composition import get_composition
from abc import ABCMeta, abstractmethod

class Mutate():
    '''Abstract superclass for mutators.'''
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def get_mutant(self,cluster):
        '''Generate a new cluster object based on a parent cluster object.'''
        pass

class MutateExchange(Mutate):
    '''Mutate by exchanging pairs of atoms of different types.'''
    
    def get_mutant(self,cluster):
        cluster.sort_type()
        atom_types=list(cluster.atom_types)
        swap0=np.random.randint(0,
                                get_composition(atom_types)[0])
        swap1=np.random.randint(get_composition(atom_types)[0],
                                cluster.natoms)
        atom_types[swap0]=1
        atom_types[swap1]=0
        mutant=Cluster(cluster.natoms,
                        np.array(cluster._coords),
                        cluster.minimiser,
                        atom_types=atom_types,
                        labels=cluster.labels)
        mutant.sort_type()
        return mutant
    
class MutateReplace(Mutate):
    '''Mutate by randomising positions of all atoms.'''
    
    def get_mutant(self,cluster):
        coords=(np.random.rand(cluster.natoms,3) -0.5) * 1.4 * float(cluster.natoms)**(1./3.)
        mutant=Cluster(cluster.natoms,
                        coords,
                        cluster.minimiser,
                        atom_types=list(cluster.atom_types),
                        labels=cluster.labels)
        return mutant