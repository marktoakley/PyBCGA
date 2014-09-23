'''
@author: Mark Oakley
'''
import numpy as np
from bcga.cluster import Cluster
def one_point(cluster1,cluster2):
    '''Perform crossover using the Deaven-Ho cut-and-splice operation.'''
    natoms=cluster1.natoms
    #Prepare clusters
    cluster1.centre()
    cluster1.rotate_random()
    cluster1.z_sort()
    cluster2.centre()
    cluster2.rotate_random()
    cluster2.z_sort()
    #Choose cutting plane
    cut=np.random.randint(1,natoms)
    #Make new cluster
    mycluster=Cluster(natoms)
    mycluster.coords[0:3*cut]=cluster1.coords[0:3*cut].copy()
    mycluster.coords[3*cut:3*natoms]=cluster2.coords[3*cut:3*natoms].copy()
    mycluster.quenched=False
#    mycluster.print_coords()
    return mycluster
