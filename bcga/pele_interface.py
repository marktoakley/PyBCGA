'''
@author: Mark Oakley
'''
import numpy as np
from pele.optimize import mylbfgs
from bcga.minimiser import Minimiser

class PeleMinimiser(Minimiser):
    '''Adapter for pele minimisation
    Parameters:
    potential- a pele potential object(see pele documentation)'''
    def __init__(self,potential):
        self.potential=potential
        
    def minimise(self,cluster):
        '''Minimise a cluster
        parameters:
        cluster- a Cluster object from bcga.cluster
        
        Using this method will overwrite the coordinates and energy of the
        supplied Cluster object.'''
        # Set up pele minimiser
        coords = cluster._coords.flatten()
        quench = lambda coords : mylbfgs(coords, self.potential)
        # Minimise
        res = quench(coords)
        # Get cluster properties back from pele
        cluster.energy = res.energy
        cluster._coords=np.reshape(res.coords,(-1,3))
        cluster.quenched = True
        return cluster
    
