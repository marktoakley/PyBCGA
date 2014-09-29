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
    coords=np.empty(shape=(natoms,3))
    for i in range(0,cut):
        coords[i]=cluster1.get_coords(i)
    for i in range(cut,natoms):
        coords[i]=cluster2.get_coords(i)
    mycluster=Cluster(natoms,coords)
    mycluster.quenched=False
    return mycluster
