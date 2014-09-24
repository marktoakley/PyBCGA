'''
@author: Mark Oakley
'''
import cProfile
from bcga.genetic_algorithm import Genetic_algorithm as ga

cProfile.run('ga(13).run()')