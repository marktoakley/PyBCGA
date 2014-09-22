'''
@author: mark
'''
import numpy as np
from bcga.population import Population

class Genetic_algorithm:
    def __init__(self,natoms,pop_size=10,max_generation=10,mutant_rate=0.2):
        self.max_generation = max_generation
        self.mutant_rate = mutant_rate
        self.mypop = Population(natoms,pop_size)
    
    def run(self):
        self.mypop.print_energies()
        for generation in range(1,self.max_generation+1):
            print ("Generation "+str(generation))
            for mycluster in self.mypop.population:
                if np.random.uniform(0,1) <self.mutant_rate:
                    self.mypop.population.append(mycluster.mutate_replace())
            self.mypop.truncate()
            self.mypop.print_energies()
    