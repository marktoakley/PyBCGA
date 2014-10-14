'''
@author: Mark Oakley
'''
import numpy as np
import random
from bcga.population import PopulationList
from bcga.cluster_factory import ClusterFactory
from bcga.selector import TournamentSelector

class BatchGeneticAlgorithm:
    '''The Birmingham Cluster Genetic Algorithm.
    Parameters:
    natoms- Number of atoms in cluster
    minimiser- See bcga.minimiser
    Optional parameters:
    composition- A list containing the number of atoms of each type
    labels- A list containing the names of each atom type
    pop_size- Number of clusters in population
    max_generation- Number of generations to run GA
    selector- Selection method for choosing parents (see bcga.selector)
    offspring- Number of crossover operations in each generation
    mutant_rate- Probability of any cluster producing a mutant
    remove_duplicates- Remove identical clusters from population to prevent stagnation
    restart- Read population from restart.xyz and continue a search
    '''
    def __init__(self,natoms,minimiser,
                 composition="default",labels=["X"],
                 pop_size=10,max_generation=10,
                 selector=TournamentSelector(3),
                 offspring=8,mutant_rate=0.1,remove_duplicates=False):
        #Parameters
        self.max_generation = max_generation
        self.mutant_rate = mutant_rate
        self.offspring=offspring
        self.pop_size=pop_size
        self.remove_duplicates=remove_duplicates
        self.selector=selector
        #Factory
        self.factory=ClusterFactory(natoms,minimiser,composition,labels)
        #PopulationList
        self.population = PopulationList(natoms,self.factory,pop_size)
        #Evolutionary progress
        self.mean_energy_series=[]
        self.min_energy_series=[]

    def write_xyz(self,filename="cluster.xyz"):
        '''Open an xyz file and write the current population to it (non-blocking).'''
        try:
            with open(filename,'w') as xyz_file:
                self.population.write_xyz(xyz_file)
        except IOError as err:
            print("File error: "+str(err))
            
    def read_xyz(self,filename="restart.xyz"):
        '''Read population from an xyz file (non-blocking for now).'''
        self.population.mass_extinction(0)
        try:
            with open("restart.xyz") as xyz_file:
                self.population.read_xyz(xyz_file)
        except:
            print("No restart file available.")

    def run(self):
        '''Run the GA.'''
        for generation in range(1,self.max_generation+1):
            print ("Generation "+str(generation))
            self.read_xyz("restart.xyz")
            print(len(self.population))
            if len(self.population) < self.population.size:
                cluster=self.factory.get_random_cluster()
                print("Filling population with random structure.")
            else:
                if np.random < self.mutant_rate:
                    index=np.random.randint(0,len(self.population))
                    cluster=self.factory.get_mutant(self.population[index])
                    print("Generating mutant of cluster "+str(index))
                else:
                    indices = self.selector.select(self.population)
                    cluster=self.factory.get_offspring(self.population[indices[0]],
                                                       self.population[indices[1]])
                    print("Generating offpsring of clusters "+str(indices[0])+" and "+str(indices[1]))
            cluster.minimise()
            self.read_xyz("restart.xyz")
            self.population.append(cluster)
            self.population.sort_energy()    
            if self.remove_duplicates:
                self.population.remove_duplicates()
            self.population.truncate()
            #Update time series
            self.mean_energy_series.append(self.population.get_mean_energy())
            self.min_energy_series.append(self.population.get_lowest_energy())
            print("Lowest energy: "+str(self.population.get_lowest_energy())+" Mean energy: "+str(self.population.get_mean_energy()))
            self.write_xyz("restart.xyz")
    