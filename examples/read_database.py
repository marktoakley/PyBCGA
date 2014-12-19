'''
Created on 16 Nov 2014

@author: mark
'''
import numpy as np
from pele.storage.database import *
db = Database(db="mydatabase.sqlite")
min=db.minima()
print(db.number_of_minima())
for i in min:
    print(i.energy)
    print(np.reshape(i.coords,(-1,3)))
