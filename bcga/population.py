'''
Holds a population of structures for the BCGA.
@author: Mark Oakley
'''
from bcga.cluster import Cluster

class PopulationList(list):
    '''Population of clusters (subclass of List)
    Parameters:
    size- Number of clusters in population
    '''
    def __init__(self,natoms,factory,size=10):
        list.__init__([])
        #Parameters
        self.size=size
        self.natoms=natoms
        self.factory = factory
        #Initialise population
        self.fill()
        self.sort_energy()
            
    def print_energies(self):
        '''Print energies of clusters in population to std out.'''
        for i in range(0,self.size):
            print(str(i+1)+"\t"+str(self[i].get_energy()))
            
    def sort_energy(self):
        """Sort population by energy."""
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
        while i < len(self):
            diff = self[i].get_energy()-self[i-1].get_energy()
            if (diff < threshold) & (len(self)>self.size):
                self.pop(i)
            else:
                i = i +1
    
    def write_xyz(self,xyz_file):
        '''Write the coordinates of the whole population to an xyz file.'''
        for cluster in self:
            cluster.write_xyz(xyz_file)
            
    def get_energy(self,i):
        '''Return energy of cluster at position i'''
        return self[i].get_energy()
    
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
            self.append(self.factory.get_random_cluster())
            
    def mass_extinction(self,survivors=0):
        '''Mass extinction event replaces whole population.
        Optionally a few survivors remain in the population.'''
        while self.__len__() > survivors:
            self.pop()
        self.fill()

