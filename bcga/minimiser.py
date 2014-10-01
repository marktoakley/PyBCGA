'''
@author: Mark
'''
import numpy as np

class PeleMinimiser():
    '''Adapter for pele minimisation'''
    def __init__(self,minimiser):
        self.system=minimiser
        
    def minimise(self,cluster):
        quench = self.system.get_minimizer()
        res = quench(cluster._coords.flatten())
        cluster.energy = res.energy
        cluster._coords=np.reshape(res.coords,(-1,3))
        return cluster