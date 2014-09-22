
'''
Atomic cluster.

@author: Mark Oakley
'''

import numpy as np
import pele.potentials.lj as lj
from pele.optimize import mylbfgs

class Cluster:
    def __init__(self,natoms):
        '''Generate a random cluster and minimise it'''
        self.natoms=natoms
        self.coords = np.random.uniform(-1, 1, [3*natoms]) * 0.7 * float(natoms)**(1./3)
#        self.coords=(np.random.rand(natoms,3) -0.5) * 1.4 * float(natoms)
        self.minimise()
        
    def get_energy(self):
        """Energy of minimised cluster"""
        return self.energy
    
    def mutate_replace(self):
        return Cluster(self.natoms)
    
    def minimise(self): 
        '''Minimise a Lennard-Jones cluster with the LBFGS minimiser.
        Eventually, potential should be user-defined.'''
        potential = lj.LJ()
        quench = lambda coords : mylbfgs(self.coords, potential)
        res = quench(self.coords)
        self.energy = res.energy
        