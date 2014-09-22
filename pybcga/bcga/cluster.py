
'''
Atomic cluster.

@author: Mark Oakley
'''

import numpy as np
class Cluster:
    def __init__(self,natoms):
        self.natoms=natoms
        self.coords = np.random.uniform(-1, 1, [3*natoms]) * 0.7 * float(natoms)**(1./3)
        self.energy = self.get_energy()
        
    def get_energy(self):
        """Dummy energy calculation routine"""
        return sum(self.coords)
    
    def mutate_replace(self):
        return Cluster(self.natoms)