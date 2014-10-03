'''
@author: Mark
'''
import numpy as np
import sys
from ase import *
from gpaw import *
from ase.optimize.bfgslinesearch import BFGSLineSearch
from gpaw import GPAW, PW, FermiDirac

class PeleMinimiser():
    '''Adapter for pele minimisation'''
    def __init__(self,system):
        self.system=system
        
    def minimise(self,cluster):
        quench = self.system.get_minimizer()
        res = quench(cluster._coords.flatten())
        cluster.energy = res.energy
        cluster._coords=np.reshape(res.coords,(-1,3))
        cluster.quenched = True
        return cluster
    
class GPAWMinimiser():
    '''Adapter for GPAW minimisation.'''
    def __init__(self):
        '''Set up'''
        
    def minimise (self,cluster):
        cluster.fix_overlaps()
        print("Before")
        cluster.print_coords()
        atom_string="He"+str(cluster.natoms)
        mol = Atoms(atom_string,
                      positions=cluster._coords,
                      cell=(6.0,6.0,6.0))
        mol.center()

        calc = GPAW(mode=PW(), 
                    xc='PBE', 
                    eigensolver='rmm-diis',
                    occupations=FermiDirac(0.0, fixmagmom=True))

        mol.set_calculator(calc)
        opt = BFGSLineSearch(mol)
        try:
            opt.run(fmax=0.25)
        except:
            sys.exit()
        
        cluster.energy=mol.get_potential_energy()
        cluster.quenched=True
        print("After")
        cluster.print_coords()
        return cluster