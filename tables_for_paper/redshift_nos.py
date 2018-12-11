'''
A simple little bit of code to give the number of quasars
above given redshifts

v1.00    Wed Dec  5 19:14:34 GMT 2018
'''

import numpy as np
import pandas as pd

from astropy.io    import fits
from astropy.io    import ascii
from astropy.table import Table

##
##  V H z Q    data
##
path     = '../data/'
filename = 'LIST_OF_VHzQs.dat'
table    = path+filename

VHzQs = ascii.read(table)

## Just a little bit of info 
print('type(VHzQs)', type(VHzQs))
print('len(VHzQs)',   len(VHzQs))
VHzQs.colnames

zgt5pnt00 = np.where(VHzQs['redshift'] > 5.00)
zgt5pnt70 = np.where(VHzQs['redshift'] > 5.00)
zgt5pnt00 = np.where(VHzQs['redshift'] > 5.00)
zgt5pnt00 = np.where(VHzQs['redshift'] > 5.00)
zgt5pnt00 = np.where(VHzQs['redshift'] > 5.00)


print('\hline \hline' )
print('Number of objects with $z$>7.00 ', len(
print()
