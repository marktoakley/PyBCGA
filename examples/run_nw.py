'''
Example input file for PyBCGA-DFT using NWChem.

@author: Mark Oakley
'''

from bcga.genetic_algorithm import GeneticAlgorithm
from bcga.nwchem_interface import NWMinimiser

natoms = 3
minimiser=NWMinimiser()
myga = GeneticAlgorithm(natoms,minimiser,
                        labels=["He"],
                        pop_size=3,
                        offspring=1,
                        max_generation=1,
                        mutant_rate=0.0)
myga.run()
#myga.write_xyz()
