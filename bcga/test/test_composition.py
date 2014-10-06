import unittest
from bcga.composition import *

class CompositionTest(unittest.TestCase):
        
    def test_get_composition(self):
        atom_types=[0,0,1]
        self.assertEqual(get_composition(atom_types)[0], 2)
        self.assertEqual(get_composition(atom_types)[1], 1)
        
    def test_get_atom_types(self):
        composition=[1,2]
        self.assertEqual(get_atom_types(composition)[0],0)
        self.assertEqual(get_atom_types(composition)[1],1)
        self.assertEqual(get_atom_types(composition)[2],1)
        
    def test_fix(self):
        composition = [5,2]
        atom_types=[0,0,0,0,0,0,0]
        fix_composition(composition, atom_types)
        self.assertEqual(get_composition(atom_types)[0], 5)
        self.assertEqual(get_composition(atom_types)[1], 2)
    
if __name__ == "__main__":
    unittest.main()