'''
@author: Mark Oakley
'''
import numpy as np
import sys
from ase.calculators.nwchem import *
from ase.optimize.bfgslinesearch import BFGSLineSearch
from bcga.composition import get_composition
    
class NWMinimiser():
    '''Adapter for GPAW minimisation.
    Takes any parameters from the NWChem class.
    If no parameters are defined, a PBE plane wave calculation is performed.'''
    def __init__(self,**GPAWargs):
        '''Set up'''
        self.GPAWargs=GPAWargs
        
    def minimise (self,cluster):
        cluster.fix_overlaps(1.5)
        atom_string=""
        for i in range(0,len(cluster.labels)):
            atom_string+=cluster.labels[i]+str(get_composition(cluster.atom_types)[i])
        print(atom_string)
        mol = Atoms(atom_string,
                      positions=cluster._coords)
        mol.center()

        calc = NWChem(**self.GPAWargs)

        mol.set_calculator(calc)
        opt = BFGSLineSearch(mol)
        try:
            opt.run(fmax=0.25)
        except:
            sys.exit()
        
        cluster.energy=mol.get_potential_energy()
        cluster.quenched=True
        return cluster
