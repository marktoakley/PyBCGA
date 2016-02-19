'''
Example input file for PyBCGA-DFT using NWChem.

Note that this is a very short run on a trivially small system because DFT
calculations are computationally expensive.

@author: Mark Oakley
'''

from bcga.genetic_algorithm import GeneticAlgorithm
from bcga.nwchem_interface import NWMinimiser

myga = GeneticAlgorithm(natoms=3,
                        minimiser=NWMinimiser(basis='6-31G',xc='b3lyp'),
                        labels=["He"],
                        pop_size=3,
                        offspring=1,
                        max_generation=1,
                        mutant_rate=0.0)
myga.run()
