'''
@author: Mark Oakley
'''
import numpy as np
import random
from bcga.population import PopulationList
from bcga.cluster_factory import ClusterFactory

class Genetic_algorithm:
    '''The Birmingham Cluster Genetic Algorithm.
    Parameters:
    natoms- Number of atoms in cluster
    Optional parameters:
    pop_size- Number of clusters in population
    max_generation- Number of generations to run GA
    offspring- Number of crossover operations in each generation
    mutant_rate- Probability of any cluster producing a mutant
    remove_duplicates- Remove identical clusters from population to prevent stagnation
    mass_extinction- Re-set population if population stagnates
    epoch_threshold- Mean population energy change that initiates mass extinction
    '''
    def __init__(self,natoms,pop_size=10,max_generation=10,
                 offspring=8,mutant_rate=0.2,remove_duplicates=False,
                 mass_extinction=False,epoch_thresh=1.e-6):
        #Parameters
        self.max_generation = max_generation
        self.mutant_rate = mutant_rate
        self.offspring=offspring
        self.pop_size=pop_size
        self.remove_duplicates=remove_duplicates
        self.mass_extinction=mass_extinction
        self.epoch_thresh=epoch_thresh
        self.factory=ClusterFactory(natoms)
        #PopulationList
        self.mypop = PopulationList(natoms,self.factory,pop_size)
        #Evolutionary progress
        self.mean_energy_series=[]
        self.mean_energy_series.append(self.mypop.get_mean_energy())
        self.min_energy_series=[]
        self.min_energy_series.append(self.mypop.get_lowest_energy())
    

    def make_offspring(self):
        '''Add offspring clusters to population'''
        for i in range(0, self.offspring):
            indices = random.sample(xrange(0, self.pop_size), 2)
            cluster1=self.mypop[indices[0]]
            cluster2=self.mypop[indices[1]]
            mycluster=self.factory.get_offspring(cluster1,cluster2)
            self.mypop.append(mycluster)


    def make_mutants(self):
        '''Add mutant clusters to population'''
        for mycluster in self.mypop:
            if np.random.uniform(0, 1) < self.mutant_rate:
                self.mypop.append(self.factory.get_mutant(mycluster))
                
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
        '''Run the GA.'''
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
            print("Lowest energy: "+str(self.mypop.get_lowest_energy())+" Mean energy: "+str(self.mypop.get_mean_energy()))
            if self.mass_extinction:
                diff = self.mean_energy_series[-2]-self.mean_energy_series[-1]
                if 0 < diff < self.epoch_thresh:
                    print("New epoch. Energy change = "+str(diff))
                    self.mypop.mass_extinction()
    