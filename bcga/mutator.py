'''
@author: Mark Oakley
'''

from bcga.cluster import Cluster
import numpy as np
from bcga.composition import *

class MutateExchange():
    '''Mutate by exchanging pairs of atoms of different types'''
    
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