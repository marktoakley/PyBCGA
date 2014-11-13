'''
@author: Mark
'''
import numpy as np
import sys
from ase import *
from gpaw import *
from ase.optimize.bfgslinesearch import BFGSLineSearch
from gpaw import GPAW, PW, FermiDirac
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
    
class GPAWMinimiser():
    '''Adapter for GPAW minimisation.
    Takes any parameters from the GPAW class.
    If no parameters are defined, a PBE plane wave calculation is performed.'''
    def __init__(self,**GPAWargs):
        '''Set up'''
        if len(GPAWargs)==0:
            GPAWargs={"mode":PW(),"xc":'PBE'}
        self.GPAWargs=GPAWargs
        
    def minimise (self,cluster):
        cluster.fix_overlaps(1.5)
        atom_string=""
        for i in range(0,len(cluster.labels)):
            atom_string+=cluster.labels[i]+str(get_composition(cluster.atom_types)[i])
        print(atom_string)
        mol = Atoms(atom_string,
                      positions=cluster._coords,
                      cell=(6.0,6.0,6.0))
        mol.center()

        calc = GPAW(**self.GPAWargs)

        mol.set_calculator(calc)
        opt = BFGSLineSearch(mol)
        try:
            opt.run(fmax=0.25)
        except:
            sys.exit()
        
        cluster.energy=mol.get_potential_energy()
        cluster.quenched=True
        return cluster