'''
@author: Mark Oakley
'''
import numpy as np
import random
from bcga.population import PopulationList
from bcga.cluster_factory import ClusterFactory
from bcga.selector import TournamentSelector

class GeneticAlgorithm:
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
    mass_extinction- Re-set population if population stagnates
    epoch_threshold- Mean population energy change that initiates mass extinction
    restart- Read population from restart.xyz and continue a search
    '''
    def __init__(self,natoms,minimiser,
                 composition="default",labels=["X"],
                 pop_size=10,max_generation=10,
                 selector=TournamentSelector(3),
                 offspring=8,mutant_rate=0.1,remove_duplicates=False,
                 mass_extinction=False,epoch_thresh=1.e-6,
                 restart=False):
        #Parameters
        self.max_generation = max_generation
        self.mutant_rate = mutant_rate
        self.offspring=offspring
        self.pop_size=pop_size
        self.remove_duplicates=remove_duplicates
        self.mass_extinction=mass_extinction
        self.epoch_thresh=epoch_thresh
        self.selector=selector
        #Factory
        self.factory=ClusterFactory(natoms,minimiser,composition,labels)
        #PopulationList
        self.population = PopulationList(natoms,self.factory,pop_size)
        if restart==False:
            while len(self.population) < self.population.size:
                self.population.append(self.factory.get_random_cluster())
            self.population.sort_energy()
        else:
            with open("restart.xyz",'r') as xyz_file:
                self.population.read_xyz(xyz_file)
        #Evolutionary progress
        self.mean_energy_series=[]
        self.mean_energy_series.append(self.population.get_mean_energy())
        self.min_energy_series=[]
        self.min_energy_series.append(self.population.get_lowest_energy())

    def make_offspring(self):
        '''Add offspring clusters to population'''
        for i in range(0, self.offspring):
            indices = self.selector.select(self.population)
            mycluster=self.factory.get_offspring(self.population[indices[0]],
                                                 self.population[indices[1]])
            self.population.append(mycluster)

    def make_mutants(self):
        '''Add mutant clusters to population'''
        for mycluster in self.population:
            if np.random.uniform(0, 1) < self.mutant_rate:
                self.population.append(self.factory.get_mutant(mycluster))
                
    def write_xyz(self,filename="cluster.xyz"):
        '''Open an xyz file and write the current population to it'''
        try:
            with open(filename,'w') as xyz_file:
                self.population.write_xyz(xyz_file)
        except IOError as err:
            print("File error: "+str(err))

    def run(self):
        '''Run the GA.'''
        for generation in range(1,self.max_generation+1):
            print ("Generation "+str(generation))
            self.make_offspring()
            self.make_mutants()
            if self.remove_duplicates:
                self.population.remove_duplicates()
            self.population.truncate()
            #Update time series
            self.mean_energy_series.append(self.population.get_mean_energy())
            self.min_energy_series.append(self.population.get_lowest_energy())
            print("Lowest energy: "+str(self.population.get_lowest_energy())+" Mean energy: "+str(self.population.get_mean_energy()))
            if self.mass_extinction:
                diff = self.mean_energy_series[-2]-self.mean_energy_series[-1]
                if 0 < diff < self.epoch_thresh:
                    print("New epoch. Energy change = "+str(diff))
                    self.population.mass_extinction()
                    while len(self.population) < self.population.size:
                        self.population.append(self.factory.get_random_cluster())
            self.population.sort_energy()
            self.write_xyz("restart.xyz")
    