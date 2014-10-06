'''
Methods to process atom_types and composition arrays.

@author: Mark Oakley
'''

import numpy as np

def get_composition(atom_types):
    '''Return a list containing the number of atoms of each type.'''
    composition = [0] * (max(atom_types)+1)
    for i in atom_types:
        composition[i]+=1
    return composition
    
def get_atom_types(composition):
    '''
    Return an atom_types array (needed for creation of new random clusters).
    '''
    atom_types=[]
    for i in range(0,len(composition)):
        for j in range(0,composition[i]):
            atom_types.append(i)
    return atom_types

def fix_composition(composition,atom_types):
    '''Fixes an atom_types array so that it matches the target composition'''
    wrong_composition = True
    natoms = len(atom_types)
    while wrong_composition:
        if get_composition(atom_types)[0]==composition[0]:
            wrong_composition=False
        if get_composition(atom_types)[0]>composition[0]:
            atom_types[np.random.randint(0,natoms)]=1
        if get_composition(atom_types)[0]<composition[0]:
            atom_types[np.random.randint(0,natoms)]=0
    return atom_types