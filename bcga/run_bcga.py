'''
Run the BCGA

@author: Mark Oakley
'''

from bcga.genetic_algorithm import Genetic_algorithm as ga

natoms = 13

myga = ga(natoms,remove_duplicates=True,max_generation=5)
myga.run()
myga.write_xyz()




