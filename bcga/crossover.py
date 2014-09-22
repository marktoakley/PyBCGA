'''
@author: Mark Oakley
'''
import numpy as np
from bcga.cluster import Cluster
def one_point(cluster1,cluster2):
    natoms=cluster1.natoms
    cluster1.z_sort()
    cluster2.z_sort()
#    print("Cluster1")
#    cluster1.print_coords()
#    print("Cluster2")
#    cluster2.print_coords()
    cut=np.random.randint(1,natoms)
#    print(cut)
    mycluster=Cluster(natoms)
    mycluster.coords[0:3*cut]=cluster1.coords[0:3*cut].copy()
    mycluster.coords[3*cut:3*natoms]=cluster2.coords[3*cut:3*natoms].copy()
    mycluster.quenched=False
#    mycluster.print_coords()
    return mycluster
