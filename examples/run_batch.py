'''
The batch GA is designed to be used in conjunction with a task arrays on a
scheduling system. The population of structures is stored in an SQL database
that can be accessed by several instances of the GA at the same time.

For this example, we use a simple Lennard-Jones potential. However, the batch
GA is designed to be most useful for very expensive energy calculations (e.g.
DFT).

Use the read_database script to view the database in a human-readable format.

@author: Mark Oakley
'''

from bcga.batch_genetic_algorithm import BatchGeneticAlgorithm
from bcga.pele_interface import PeleMinimiser
import pele.potentials.lj as lj

natoms = 38
minimiser=PeleMinimiser(lj.LJ())

myga = BatchGeneticAlgorithm(natoms,
                        minimiser,
                        remove_duplicates=True,
                        max_generation=20)

myga.run()
