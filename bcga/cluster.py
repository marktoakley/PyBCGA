
'''
Atomic cluster.

@author: Mark Oakley
'''

import numpy as np
import math

class Cluster(object):
    '''An atomic cluster.'''
    def __init__(self,natoms,coords,minimiser,atom_types=None,labels=("X",)):
        '''Make a new cluster.
        In most cases, use the ClusterFactory class to make a new Cluster.
        Parameters:
        natoms- Number of atoms in cluster.
        coords- A 3*natoms numpy array containing the cluster's atomic coordinates.
        minimiser- A Minimiser object to define the energy calculation method (see bcga.minimiser)
        atom_types- Needed for binary clusters. ClusterFactory handles the generaton of this list
        labels- A list or tuple containing the atom labels (e.g. ["Au","Ag"]'''
        self.natoms=natoms
        self.quenched=False
        self._coords=coords
        self.labels=labels
        self.minimiser=minimiser
        self.energy = None
        if atom_types is None:
            atom_types=[0]*natoms
        self.atom_types=atom_types
        
    def get_energy(self):
        '''Returns energy of cluster.
        Also minimises the cluster if this has not already happened.'''
        if self.quenched is False:
            self.minimise()
            self.quenched=True
        return self.energy
    
    def minimise(self): 
        '''Perform a local minimisation onthe cluster.'''
        self.minimiser.minimise(self)
  
    def sort_type(self):
        '''Re-orders the atoms by atom type'''
        indices=sorted(range(len(self.atom_types)), key = self.atom_types.__getitem__)
        self.re_order(indices)
        
    def sort_z(self):
        '''Re-orders the atoms along the z-axis.'''
        indices=self._coords[:,2].argsort()
        self.re_order(indices)
        
    def print_coords(self):
        '''Print coordinates of cluster to std out.'''
        for i in range(0,self.natoms):
            print(str(i+1)+"\t"+str(self._coords[i]))
            
    def write_xyz(self,xyz_file):
        '''Write the cluster's coordinates to an xyz file.
        Parameters:
        xyz_file- An open file'''
        xyz_file.write(str(self.natoms)+"\n")
        xyz_file.write("Energy: "+str(self.get_energy())+"\n")
        for i in range(0,self.natoms):
            xyz_file.write(self.labels[self.atom_types[i]]+
                           " "+str(self._coords[i,0])+
                           " "+str(self._coords[i,1])+
                           " "+str(self._coords[i,2])+"\n")
            
    def centre(self):
        '''Translate cluster's centroid to the origin.
        Note that this may not be the centre of mass because different masses
        for different elements are not currently supported.'''
        com=np.mean(self._coords,axis=0)
        self._coords=(self._coords-com)
        return -com
        
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
        self._coords=np.dot(self._coords,rot)
        
    def get_coords(self,i):
        '''Return a copy of the coordinates of atom i.'''
        return self._coords[i,:].copy()
    
    def re_order(self,indices):
        '''Re-order the atoms in a cluster'''
        new_coor=np.empty(shape=(self.natoms,3))
        new_types=[0]*self.natoms
        for i in range(0,self.natoms):
            new_coor[i]=self._coords[indices[i],:]
            new_types[i]=self.atom_types[indices[i]]
        self._coords=new_coor
        self.atom_types=new_types
        
    def get_label(self,i):
        '''Return the string corresponding to the atom at index i.'''
        return self.labels[self.atom_types[i]]
    
    def fix_overlaps(self,cut_off=1.0):
        '''Fix overlapping atoms (useful for GA-DFT).
        Any pairwise distances shorter than the cut_off are expanded.'''
        converged = False
        while converged is False:
            converged=True
            moves=np.zeros(shape=(self.natoms,3))
            for i in range (0,self.natoms):
                for j in range (i+1,self.natoms):
                    vec=self._coords[i,:] - self._coords[j,:]
                    if vec.dot(vec) < cut_off**2:
                        moves[i,:]+=vec*0.1
                        moves[j,:]-=vec*0.1
                        converged=False
            self._coords+=moves
