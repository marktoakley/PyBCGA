'''
Run the BCGA

@author: Mark Oakley
'''

from bcga.genetic_algorithm import Genetic_algorithm as ga
from bcga.cluster_factory import ClusterFactory

natoms = 13
atom_types=[0,0,0,0,0,1,1,1,1,1,1,1,1]
labels=["A","B"]
factory=ClusterFactory(natoms,atom_types,labels)

myga = ga(natoms,factory,remove_duplicates=True,max_generation=10)
myga.run()
myga.write_xyz()
