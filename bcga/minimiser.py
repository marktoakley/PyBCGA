'''
@author: Mark Oakley
'''
from abc import ABCMeta, abstractmethod

class Minimiser():
    '''Abstract superclass for minimisers.
    The interface to the energy evaluation method (e.g. Lennard-Jones or DFT).
    This should optimise a cluster object to the nearest local minimum.'''
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def minimise(self,cluster): pass