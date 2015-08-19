'''
@author: Mark Oakley
'''
import numpy as np

class TournamentSelector():
    '''Select parents for crossover by tournament selection.'''
    def __init__(self,tournament_size=3):
        self.tournament_size=tournament_size
        
    def select(self,population):
        a = np.arange(population.max_size)
        np.random.shuffle(a)
        a=sorted(a[:3])
        return (a[:2])
    
class RouletteSelector():
    '''Select parents for crossover using roulette wheel method.'''
        
    def select(self,population):    
        best = population[0].get_energy()
        erange=population[population.max_size-1].get_energy()-population[0].get_energy()
        #Calculate fitness
        fit=[]
        for i in range(0,population.max_size):
            fit.append(1-0.7*(population[i].get_energy()-best)/erange)
        pair=[]
        while len(pair)<2:
            index=np.random.randint(0,population.max_size)
            if (index not in pair) and (np.random.random()<fit[index]):
                pair.append(index)
        return pair
    