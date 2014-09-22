'''
Run the BCGA

@author: Mark Oakley
'''

from bcga.genetic_algorithm import Genetic_algorithm as ga

natoms = 13

myga = ga(natoms)
myga.run()




