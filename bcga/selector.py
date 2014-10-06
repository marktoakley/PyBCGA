'''
@author: Mark Oakley
'''
import numpy as np

class TournamentSelector():
    def __init__(self,tournament_size=3):
        '''Select parents for crossover by tournament selection.'''
        self.tournament_size=tournament_size
        
    def select(self,population):
        a = np.arange(population.size)
        np.random.shuffle(a)
        a=sorted(a[:3])
        return (a[:2])