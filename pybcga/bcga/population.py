'''
Holds a population of structures for the BCGA.
@author: Mark Oakley
'''
from bcga.cluster import Cluster

class Population:
    def __init__(self,natoms,size=10):
        self.size=size
        self.population=[]
        while self.population.__len__()<self.size:
            self.population.append(Cluster(natoms))
        self.sort_energy()
            
    def print_energies(self):
        for i in range(0,self.size):
            print(str(i+1)+"\t"+str(self.population[i].get_energy()))
            
    def sort_energy(self):
        """Sort population by energy"""
        self.population.sort(key=lambda x: x.get_energy(), reverse=False)
        
    def truncate(self):
        """Remove worst clusters from population until population is below maximum size"""
        self.sort_energy()
        while self.population.__len__() > self.size:
            self.population.pop()
            

