'''
A simple little bit of code to give the number of quasars
above given redshifts

v1.00    Wed Dec  5 19:14:34 GMT 2018
'''

import numpy as np
import pandas as pd
import astropy.units as u

from astropy.io    import fits
from astropy.io    import ascii
from astropy.table import Table
from astropy.cosmology import FlatLambdaCDM
from astropy.cosmology import z_at_value

## Setting up the cosmology, using the values in Banados thesis
cosmo = FlatLambdaCDM(H0=67.7, Om0=0.307)
'''
z_at_value(Planck13.age, 1 * u.Gyr)
 5.676612956824678
z_at_value(Planck13.age, 0.9 * u.Gyr)
 6.162712171507278
z_at_value(Planck13.age, 0.8 * u.Gyr)
 6.747787512646126
z_at_value(Planck13.age, 0.7 * u.Gyr)
 7.468681984034107
z_at_value(Planck13.age, 0.6 * u.Gyr)
 8.384171561487875
'''

redshift_array = np.array([5.00, 5.70, 6.00, 6.19, 6.50, 6.78, 7.00, 7.50])
#given_redshifts = np.array([5.00, 5.50, 5.70, 6.00, 6.30, 6.50, 6.80, 7.00])
given_redshifts = redshift_array
given_age = (cosmo.age(given_redshifts).value)*1e3   #From Gyr into Myr

print()
print(redshift_array, '\n')

##
##  V H z Q    data
##
path     = '../data/'
filename = 'LIST_OF_VHzQs_v2.dat'
table    = path+filename

VHzQs = ascii.read(table)

## Just a little bit of info 
print('type(VHzQs)', type(VHzQs))
print('len(VHzQs)',   len(VHzQs))
VHzQs.colnames

N_zgt5pnt00 = np.count_nonzero(VHzQs['redshift'] >= redshift_array[0])
N_zgt5pnt50 = np.count_nonzero(VHzQs['redshift'] >= redshift_array[1])
N_zgt5pnt70 = np.count_nonzero(VHzQs['redshift'] >= redshift_array[2])
N_zgt6pnt00 = np.count_nonzero(VHzQs['redshift'] >= redshift_array[3])
N_zgt6pnt30 = np.count_nonzero(VHzQs['redshift'] >= redshift_array[4])
N_zgt6pnt50 = np.count_nonzero(VHzQs['redshift'] >= redshift_array[5])
N_zgt6pnt80 = np.count_nonzero(VHzQs['redshift'] >= redshift_array[6])
N_zgt7pnt00 = np.count_nonzero(VHzQs['redshift'] >= redshift_array[7])

print()
print('\hline \hline' )
print('Number of objects with $z \geq$ 7.50  (', given_age[7],')', N_zgt7pnt00, '  \\')
print('         ``            $z \geq$ 7.00  (', given_age[6],')', N_zgt6pnt80, '  \\')
print('         ``            $z \geq$ 6.78  (', given_age[5],')', N_zgt6pnt50, '  \\')
print('         ``            $z \geq$ 6.50  (', given_age[4],')', N_zgt6pnt30, '  \\')
print('         ``            $z \geq$ 6.19  (', given_age[3],')', N_zgt6pnt00, '  \\')
print('         ``            $z \geq$ 6.00  (', given_age[2],')', N_zgt5pnt70, '  \\')
print('         ``            $z \geq$ 5.70  (', given_age[1],')', N_zgt5pnt50, '  \\')
print('         ``            $z \geq$ 5.00  (', given_age[0],')', N_zgt5pnt00, '  \\')
print('\hline \hline' )
print()
