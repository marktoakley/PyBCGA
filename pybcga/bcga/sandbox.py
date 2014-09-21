'''
Run the BCGA

@author: Mark Oakley
'''

from bcga.population import Population


natoms = 6
mypop = Population(natoms,10)
mypop.print_energies()
mypop.sort()
print("")
mypop.print_energies()
