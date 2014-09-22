
'''
Atomic cluster.

@author: Mark Oakley
'''

import numpy as np
import pele.potentials.lj as lj
import pele.basinhopping as bh
from pele.takestep import displace

class Cluster:
    def __init__(self,natoms):
        '''Generate a random cluster and minimise it'''
        self.natoms=natoms
        self.coords = np.random.uniform(-1, 1, [3*natoms]) * 0.7 * float(natoms)**(1./3)
#        self.coords=(np.random.rand(natoms,3) -0.5) * 1.4 * float(natoms)
        '''This is a really slow implementation, but it works for now.'''
        potential = lj.LJ()
        step = displace.RandomDisplacement(stepsize=0.5)
        opt = bh.BasinHopping(self.coords, potential, takeStep=step)
        opt.run(0)
        self.energy = opt.markovE
        
    def get_energy(self):
        """Energy of minimised cluster"""
        return self.energy
    
    def mutate_replace(self):
        return Cluster(self.natoms)