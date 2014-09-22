'''
@author: Mark Oakley
'''
import numpy as np
import random
from bcga.population import Population
import crossover

class Genetic_algorithm:
    def __init__(self,natoms,pop_size=10,max_generation=10,mutant_rate=0.2,offspring=8,remove_duplicates=False):
        #Parameters
        self.max_generation = max_generation
        self.mutant_rate = mutant_rate
        self.offspring=offspring
        self.pop_size=pop_size
        self.remove_duplicates=remove_duplicates
        #Population
        self.mypop = Population(natoms,pop_size)
        #Evolutionary progress
        self.mean_energy_series=[]
        self.mean_energy_series.append(self.mypop.get_mean_energy())
        self.min_energy_series=[]
        self.min_energy_series.append(self.mypop.get_lowest_energy())
    

    def make_offspring(self):
        '''Add offspring clusters to population'''
        for i in range(0, self.offspring):
            indices = random.sample(xrange(0, self.pop_size), 2)
            cluster1=self.mypop.population[indices[0]]
            cluster2=self.mypop.population[indices[1]]
            mycluster=crossover.one_point(cluster1,cluster2)
            self.mypop.population.append(mycluster)


    def make_mutants(self):
        '''Add mutant clusters to population'''
        for mycluster in self.mypop.population:
            if np.random.uniform(0, 1) < self.mutant_rate:
                self.mypop.population.append(mycluster.mutate_replace())
                
    def write_xyz(self,filename="cluster.xyz"):
        '''Open an xyz file and write the current population to it'''
        try:
            xyz_file = open(filename,'w')
            self.mypop.write_xyz(xyz_file)
        except IOError as err:
            print("File error: "+str(err))
        finally:
            xyz_file.close()

    def run(self):
        for generation in range(1,self.max_generation+1):
            print ("Generation "+str(generation))
            self.make_offspring()
            self.make_mutants()
            if self.remove_duplicates:
                self.mypop.remove_duplicates()
            self.mypop.truncate()
            #Update time series
            self.mean_energy_series.append(self.mypop.get_mean_energy())
            self.min_energy_series.append(self.mypop.get_lowest_energy())
            print("Lowest energy: "+str(self.mypop.get_lowest_energy()))
            print("Mean energy: "+str(self.mypop.get_mean_energy()))
    