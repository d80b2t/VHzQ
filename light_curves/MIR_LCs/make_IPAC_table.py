'''
'''

from astropy.io import fits
from astropy.io import ascii
from astropy    import units as u
from astropy.coordinates import SkyCoord
from astropy.table import Table, Column, MaskedColumn

import numpy as np
import pandas as pd               

data = pd.read_csv("most_variable_v1pnt0.csv")
data

len(data)

name = np.array(data['name'])
ra   = np.array(data['ra'])
dec  = np.array(data['dec'])
print(type(ra))


d = Table([name, ra, dec], names=['name', 'ra', 'dec'])

ascii.write(d, 'forIRAC_temp.dat', format='ipac') 

