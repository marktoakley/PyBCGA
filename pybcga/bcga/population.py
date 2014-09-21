'''
Holds a population of structures for the BCGA.
@author: Mark Oakley
'''
from bcga.cluster import Cluster

class Population:
    def __init__(self,natoms,size=10):
        self.size=10
        self.population=[]
        while self.population.__len__()<self.size:
            self.population.append(Cluster(natoms))
            
    def print_energies(self):
        for cluster in self.population:
            print(cluster.get_energy())
            
    def sort(self):
        """Sort population by energy"""
        self.population.sort(key=lambda x: x.energy, reverse=False)
            

