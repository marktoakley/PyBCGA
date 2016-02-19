'''
@author: Mark Oakley
'''
import sys
from ase.calculators.nwchem import NWChem, Atoms
from ase.optimize.lbfgs import LBFGSLineSearch
from bcga.composition import get_composition
from bcga.minimiser import Minimiser
    
class NWMinimiser(Minimiser):
    '''Adapter for NWChem minimisation.
    Provides minimisation using the NWChem 
    Parameters:
    temp_files- directory for NWChem temporary files
    **GPAWargs- NWChem parameters
    
    See the NWChem class in ASE documentation for available **GPAWargs
    '''
    def __init__(self,temp_files="/tmp/nw",**GPAWargs):
        '''Set up'''
        self.GPAWargs=GPAWargs
        self.temp_files=temp_files
        
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
        # Set up an ASE Atoms object for the cluster
        mol = Atoms(atom_string,
                      positions=cluster._coords)
        mol.center()
        # Set up and runNWChem minimise
        calc = NWChem(label=self.temp_files,**self.GPAWargs)
        mol.set_calculator(calc)
        opt = LBFGSLineSearch(mol)
        try:
            opt.run(fmax=0.25)
        except:
            sys.exit()
        # Get back results from ASE
        cluster.energy=mol.get_potential_energy()
        cluster.quenched=True
        return cluster
