'''
@author: Mark Oakley
'''
import sys
from ase import Atoms
from ase.optimize.bfgslinesearch import BFGSLineSearch
from gpaw import GPAW, PW
from bcga.composition import get_composition
from bcga.minimiser import Minimiser
    
class GPAWMinimiser(Minimiser):
    '''Adapter for GPAW minimisation.
    Provides minimisation using the GPAW 
    Parameters:
    **GPAWargs- GPAW parameters
    
    See the GPAW class in ASE documentation for available **GPAWargs
    If no **GPAWargs are defined, a PBE plane wave calculation is performed.'''
    def __init__(self,**GPAWargs):
        '''Set up'''
        if len(GPAWargs)==0:
            GPAWargs={"mode":PW(),"xc":'PBE'}
        self.GPAWargs=GPAWargs
        
    def minimise (self,cluster):
        '''Minimise a cluster
        parameters:
        cluster- a Cluster object from bcga.cluster
        
        Using this method will overwrite the coordinates and energy of the
        supplied Cluster object.'''
        # Fix overlapping atoms to avoid NWChem errors
        cluster.fix_overlaps(1.5)
        # Set up element labels for NWChem
        atom_string=""
        for i in range(0,len(cluster.labels)):
            atom_string+=cluster.labels[i]+str(get_composition(cluster.atom_types)[i])
        print(atom_string)
        mol = Atoms(atom_string,
                      positions=cluster._coords,
                      cell=(6.0,6.0,6.0))
        mol.center()
        # Run GPAW calculation
        calc = GPAW(**self.GPAWargs)
        mol.set_calculator(calc)
        opt = BFGSLineSearch(mol)
        try:
            opt.run(fmax=0.25)
        except:
            sys.exit()
        # Get back cluster properties from GPAW
        cluster.energy=mol.get_potential_energy()
        cluster.quenched=True
        return cluster