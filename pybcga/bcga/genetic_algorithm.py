'''
@author: mark
'''
import numpy as np
import random
from bcga.population import Population
import crossover

class Genetic_algorithm:
    def __init__(self,natoms,pop_size=10,max_generation=10,mutant_rate=0.2,offspring=8):
        self.max_generation = max_generation
        self.mutant_rate = mutant_rate
        self.mypop = Population(natoms,pop_size)
        self.offspring=offspring
        self.pop_size=pop_size
    

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

    def run(self):
        self.mypop.print_energies()
        for generation in range(1,self.max_generation+1):
            print ("Generation "+str(generation))
            self.make_offspring()
            self.make_mutants()
            self.mypop.truncate()
            self.mypop.print_energies()
    