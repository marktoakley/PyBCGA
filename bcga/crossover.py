'''
@author: Mark Oakley
'''
import numpy as np
from bcga.cluster import Cluster
def one_point(cluster1,cluster2):
    '''Perform crossover using the Deaven-Ho cut-and-splice operation.
    Parameters:
    Two Cluster objects.
    Returns:
    A Cluster object derived from the two parents.'''
    natoms=cluster1.natoms
    #Prepare clusters
    for cluster in [cluster1,cluster2]:
        cluster.centre()
        cluster.rotate_random()
        cluster.z_sort()
    #Choose cutting plane
    cut=np.random.randint(1,natoms)
    #Make new cluster
    mycluster=Cluster(natoms)
    mycluster.coords=np.empty(shape=(natoms,3))
    mycluster.coords[0:3*cut]=cluster1.coords[0:3*cut].copy()
    mycluster.coords[3*cut:3*natoms]=cluster2.coords[3*cut:3*natoms].copy()
    mycluster.quenched=False
#    mycluster.print_coords()
    return mycluster
