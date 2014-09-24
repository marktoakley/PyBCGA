
'''
Atomic cluster.

@author: Mark Oakley
'''

import numpy as np
import pele.potentials.lj as lj
from pele.optimize import mylbfgs
import math

class Cluster:
    '''An atomic cluster.
    (Only single-component clusters are currently implemented).
    Parameters:
    natoms- Number of atoms in cluster.'''
    def __init__(self,natoms):
        '''Use the ClusterFactory class to make a new Cluster.
        This method returns an empty cluster with no atomic coordinates.'''
        self.natoms=natoms
        self.quenched=False
        
    def get_energy(self):
        '''Returns energy of minimised cluster'''
        if self.quenched==False:
            self.minimise()
            self.quenched=True
        return self.energy
    
    def minimise(self): 
        '''Minimise a Lennard-Jones cluster with the LBFGS minimiser.
        (Eventually, other potentials will be available.)'''
        potential = lj.LJ()
        quench = lambda coords : mylbfgs(self.coords.flatten(), potential)
        res = quench(self.coords.flatten())
        self.energy = res.energy
        self.coords=np.reshape(res.coords,(-1,3))
        
    def z_sort(self):
        '''Re-orders the atoms in a cluster along the z-axis.'''
        self.coords=self.coords[np.lexsort(self.coords.T)]
        
    def print_coords(self):
        '''Print coordinates of cluster to std out.'''
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
            
    def centre(self):
        '''Translate cluster's centre of mass to origin.'''
        com=np.mean(self.coords,axis=0)
        self.coords=(self.coords-com)
        
    def rotate_random(self):
        '''Rotate cluster to random orientation.
        
        This implementation is copied from the BCGA fortran code.'''
        theta=np.random.rand()*math.pi*2.
        phi= np.random.rand()*math.pi
        rot=np.empty(shape=(3,3))
        rot[0,0] = math.cos(phi)
        rot[0,1] = 0.
        rot[0,2] = -math.sin(phi)
        rot[1,0] = math.sin(theta)*math.sin(phi)
        rot[1,1] = math.cos(theta)
        rot[1,2] = math.sin(theta)*math.cos(phi)
        rot[2,0] = math.cos(theta)*math.sin(phi)
        rot[2,1] = -math.sin(theta)
        rot[2,2] = math.cos(theta)*math.cos(phi)
        self.coords=np.dot(self.coords,rot)
        
        