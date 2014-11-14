'''
@author: Mark
'''
import numpy as np
import sys
from bcga.composition import get_composition
from pele.optimize import mylbfgs


class PeleMinimiser():
    '''Adapter for pele minimisation'''
    def __init__(self,potential):
        self.potential=potential
        
    def minimise(self,cluster):
        coords = cluster._coords.flatten()
        quench = lambda coords : mylbfgs(coords, self.potential)
        res = quench(coords)
        cluster.energy = res.energy
        cluster._coords=np.reshape(res._coords,(-1,3))
        cluster.quenched = True
        return cluster
    