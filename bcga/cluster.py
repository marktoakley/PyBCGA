
'''
Atomic cluster.

@author: Mark Oakley
'''

import numpy as np
import pele.potentials.lj as lj
from pele.optimize import mylbfgs

class Cluster:
    def __init__(self,natoms):
        '''Generate a random cluster'''
        self.natoms=natoms
#        self.coords = np.random.uniform(-1, 1, [3*natoms]) * 0.7 * float(natoms)**(1./3)
        self.coords=(np.random.rand(natoms,3) -0.5) * 1.4 * float(natoms)
        self.quenched=False
        
    def get_energy(self):
        """Energy of minimised cluster"""
        if self.quenched==False:
            self.minimise()
            self.quenched=True
        return self.energy
    
    def mutate_replace(self):
        return Cluster(self.natoms)
    
    def minimise(self): 
        '''Minimise a Lennard-Jones cluster with the LBFGS minimiser.
        Eventually, potential should be user-defined.'''
        potential = lj.LJ()
        quench = lambda coords : mylbfgs(self.coords.flatten(), potential)
        res = quench(self.coords.flatten())
        self.energy = res.energy
        self.coords=np.reshape(res.coords,(-1,3))
        
    def z_sort(self):
        '''Re-orders the atoms in a cluster along the z-axis'''
        self.coords=self.coords[np.lexsort(self.coords.T)]
        self.print_coords()
        
    def print_coords(self):
        '''Print coordinates of cluster to std out'''
        for i in range(0,self.natoms):
            print(str(i+1)+"\t"+str(self.coords[i]))
            
    def write_xyz(self,xyz_file):
        '''Write the cluster's coordinates to an xyz file.'''
        xyz_file.write(str(self.natoms)+"\n")
        xyz_file.write("Energy: "+str(self.get_energy())+"\n")
        for i in range(0,self.natoms):
            xyz_file.write("X "+str(self.coords[i,0])+
                       " "+str(self.coords[i,1])+
                       " "+str(self.coords[i,2])+"\n")

        
        