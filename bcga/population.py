'''
Holds a population of structures for the BCGA.
@author: Mark Oakley
'''
from bcga.cluster import Cluster

class PopulationList(list):
    def __init__(self,natoms,size=10):
        list.__init__([])
        self.size=size
        self.natoms=natoms
        self.fill()
        self.sort_energy()
            
    def print_energies(self):
        for i in range(0,self.size):
            print(str(i+1)+"\t"+str(self[i].get_energy()))
            
    def sort_energy(self):
        """Sort population by energy"""
        self.sort(key=lambda x: x.get_energy(), reverse=False)
        
    def truncate(self):
        """Remove worst clusters from population until population is below maximum size"""
        self.sort_energy()
        while self.__len__() > self.size:
            self.pop()
            
    def remove_duplicates(self,threshold=1e-6):
        '''Duplicate predator deletes duplicate structures (defined by energy difference below threshold).'''
        self.sort_energy()
        i=1
        while i < self.__len__():
            diff = self[i].get_energy()-self[i-1].get_energy()
            if diff < threshold:
                self.pop(i)
            else:
                i = i +1
    
    def write_xyz(self,xyz_file):
        '''Write the coordinates of the whole population to an xyz file.'''
        for cluster in self:
            cluster.write_xyz(xyz_file)
            
    def get_lowest_energy(self):
        '''Return the energy of the most stable structure in the population.'''
        self.sort_energy()
        return self[0].get_energy()
    
    def get_mean_energy(self):
        '''Return the mean energy of all structures in the population.'''
        e_sum=0
        for cluster in self[0:self.size]:
            e_sum += cluster.get_energy()
        return e_sum/float(self.size)

    def fill(self):
        '''Fill population with random structures'''
        while self.__len__() < self.size:
            self.append(Cluster(self.natoms))
            
    def mass_extinction(self,survivors=0):
        '''Mass extinction event replaces whole population. Optionally a few survivors remain in the population'''
        while self.__len__() > survivors:
            self.pop()
        self.fill()

