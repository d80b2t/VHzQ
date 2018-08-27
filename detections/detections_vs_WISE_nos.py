'''
WISE detections and colors of Very High redshift quasars
'''

from astropy.io import fits
from astropy.io import ascii
from astropy.table import Table

import numpy as np
import math

## READ-IN THE DATA FILE(S)
path = '/cos_pc19a_npr/data/highest_z_QSOs/'
#all_VHzQs  = ascii.read(path+'THE_TABLES/v0pnt97/THE_TABLE_v0pnt97.dat', delimiter=r'\s', guess=False)
all_VHzQs  = ascii.read(path+'THE_TABLE_v0pnt971.dat', delimiter=r'\s', guess=False)

## Setting up the variables for easier use
w1mag = all_VHzQs['w1mag']
w2mag = all_VHzQs['w2mag']
w3mag = all_VHzQs['w3mag']
w4mag = all_VHzQs['w4mag']
w1snr   = all_VHzQs['w1snr']
w2snr   = all_VHzQs['w2snr']
w3snr   = all_VHzQs['w3snr']
w4snr   = all_VHzQs['w4snr']
w1_min_w2_all = (w1mag-w2mag)
w2_min_w3_all = (w1mag-w2mag)
w3_min_w4_all = (w1mag-w2mag)

z_all = all_VHzQs['redshift']
M1450_all = all_VHzQs['M1450']

snr_limit = 2.0

## Some conditions, values etc.
w_forw1 = all_VHzQs[np.where((w1snr > snr_limit))]
w_forw2 = all_VHzQs[np.where((w2snr > snr_limit))]
w_forw3 = all_VHzQs[np.where((w3snr > snr_limit))]
w_forw4 = all_VHzQs[np.where((w4snr > snr_limit))]

w_forw1w2 = all_VHzQs[np.where((w1snr > snr_limit)  & (w2snr > snr_limit  ))]
w_forw1w3 = all_VHzQs[np.where((w1snr > snr_limit)  & (w3snr > snr_limit  ))]
w_forw2w3 = all_VHzQs[np.where((w2snr > snr_limit)  & (w3snr > snr_limit  ))]

w_notw1w2       = all_VHzQs[np.where((w1snr < snr_limit)  & (w2snr < snr_limit  ) )   ]
w_notw1w2forw3  = all_VHzQs[np.where((w1snr < snr_limit)  & (w2snr < snr_limit  ) & (w3snr > snr_limit)  )   ]

print()
print('Total number of quasars in data file...', len(all_VHzQs) )
print(' all_VHzQs[np.where((w1snr > snr_limit))]', len(w_forw1), 'i.e. ', ( len(w_forw1) / len(all_VHzQs) )*100, '%')
print(' all_VHzQs[np.where((w2snr > snr_limit))]', len(w_forw2), 'i.e. ', ( len(w_forw2) / len(all_VHzQs) )*100, '%') 
print(' all_VHzQs[np.where((w3snr > snr_limit))]', len(w_forw3), 'i.e. ', ( len(w_forw3) / len(all_VHzQs) )*100, '%') 
print(' all_VHzQs[np.where((w4snr > snr_limit))]', len(w_forw4), 'i.e. ', ( len(w_forw4) / len(all_VHzQs) )*100, '%')
print()

print(' (w1snr > snr_limit)  & (w2snr > snr_limit )', len(w_forw1w2),      'i.e. ', ( len(w_forw1w2) / len(all_VHzQs) )*100, '%')
print(' (w1snr > snr_limit)  & (w3snr > snr_limit )', len(w_forw1w3),      'i.e. ', ( len(w_forw1w3) / len(all_VHzQs) )*100, '%')
print(' (w2snr > snr_limit)  & (w3snr > snr_limit )', len(w_forw2w3),      'i.e. ', ( len(w_forw2w3) / len(all_VHzQs) )*100, '%')

print(' (w1snr < snr_limit)  & (w2snr < snr_limit) ',                        len(w_notw1w2),      'i.e. ', ( len(w_notw1w2) / len(all_VHzQs) )*100, '%')
print(' (w1snr < snr_limit)  & (w2snr < snr_limit) & (w3snr > snr_limit)',   len(w_notw1w2forw3), 'i.e. ', ( len(w_notw1w2forw3) / len(all_VHzQs) )*100, '%')


print()
