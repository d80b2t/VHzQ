'''
So, some more wee bits of code that is just investigating the detection rates for 
the unWISE and AllWISE VHzQ data, this time as a function of redshift. 

unWISE both    matched ::  304 
unWISE just W1 matched ::  58
unWISE just W2 matched ::  4
unWISE matched in W1   ::  362
unWISE matched in W2   ::  308
unWISE neither matched ::  97

Total matched   =  463 
'''

import numpy as np

from astropy.io    import fits
from astropy.io    import ascii
from astropy.table import Table

## Data files and path
#path     = '/cos_pc19a_npr/programs/quasars/highest_z/data/AllWISE/'
#filename = 'VHzQs463_UNvALL_WISE_temp.dat'
path     = '/cos_pc19a_npr/programs/quasars/highest_z/data/'
filename = 'VHzQs_ZYJHK_WISE.dat'
VHzQs    = ascii.read(path+filename)

## just a quick wee check
len(VHzQs)

## Setting up the variables just for me to use a bit easier
unW1           = VHzQs[np.where( VHzQs['unW1mag']>-1)]
unW1_just      = VHzQs[np.where((VHzQs['unW1mag']>-1) & (VHzQs['unW2mag']<-1))]

unW2           = VHzQs[np.where( VHzQs['unW2mag']>-1)]
unW2_just      = VHzQs[np.where((VHzQs['unW2mag']>-1) & (VHzQs['unW1mag']<-1))]

## Wee bit out .tex outputting...
## also see, 
print('\hline \hline')
print('Detection band & No. of objects')
print('\hline')
print('unWISE W1                 & ', len(unW1),             ' \\\ ')
print('unWISE W1     !unWISE W2  & ', len(unW1_just),        '  \\\ ')
#print('unWISE W1 and !AllWISE W1 & ', len(unW1_not_AllW1),   '  \\\ ')
print()
print('unWISE W2                 & ', len(unW2),             ' \\\ ')
print('unWISE W2     !unWISE W1  & ', len(unW2_just),        '   \\\ ')
#print('unWISE W2 and !AllWISE W1 & ', len(unW2_not_AllW2),   '  \\\ ')
print('\hline \hline')


## By redshift
redshift_array = np.array([5.00, 5.70, 6.00, 6.19, 6.50, 6.78, 7.00, 7.50])

## How many of the VHzQs are above a given redshift 
N_zgt5pnt00 = np.count_nonzero(VHzQs['redshift'] >= redshift_array[0]) 
N_zgt5pnt70 = np.count_nonzero(VHzQs['redshift'] >= redshift_array[1]) 
N_zgt6pnt00 = np.count_nonzero(VHzQs['redshift'] >= redshift_array[2]) 
N_zgt6pnt19 = np.count_nonzero(VHzQs['redshift'] >= redshift_array[3]) 
N_zgt6pnt50 = np.count_nonzero(VHzQs['redshift'] >= redshift_array[4]) 
N_zgt6pnt78 = np.count_nonzero(VHzQs['redshift'] >= redshift_array[5]) 
N_zgt7pnt00 = np.count_nonzero(VHzQs['redshift'] >= redshift_array[6]) 
N_zgt7pnt50 = np.count_nonzero(VHzQs['redshift'] >= redshift_array[7]) 

## How many of the VHzQs, with unWISE W1 detections are above a given redshift 
N_zgt5pnt00_unW1 = np.count_nonzero((VHzQs['redshift'] >= redshift_array[0]) & (VHzQs['unW1mag']>-1))
N_zgt5pnt70_unW1 = np.count_nonzero((VHzQs['redshift'] >= redshift_array[1]) & (VHzQs['unW1mag']>-1))
N_zgt6pnt00_unW1 = np.count_nonzero((VHzQs['redshift'] >= redshift_array[2]) & (VHzQs['unW1mag']>-1))
N_zgt6pnt19_unW1 = np.count_nonzero((VHzQs['redshift'] >= redshift_array[3]) & (VHzQs['unW1mag']>-1))
N_zgt6pnt50_unW1 = np.count_nonzero((VHzQs['redshift'] >= redshift_array[4]) & (VHzQs['unW1mag']>-1))
N_zgt6pnt78_unW1 = np.count_nonzero((VHzQs['redshift'] >= redshift_array[5]) & (VHzQs['unW1mag']>-1))
N_zgt7pnt00_unW1 = np.count_nonzero((VHzQs['redshift'] >= redshift_array[6]) & (VHzQs['unW1mag']>-1))
N_zgt7pnt50_unW1 = np.count_nonzero((VHzQs['redshift'] >= redshift_array[7]) & (VHzQs['unW1mag']>-1))

print('$z \geq $ ')
print(' 5.00   {:5d} ({:6.2f}\%)'.format(N_zgt5pnt00_unW1,    ((N_zgt5pnt00_unW1/N_zgt5pnt00)*100)))
print(' 5.70   {:5d} ({:6.2f}\%)'.format(N_zgt5pnt70_unW1,    ((N_zgt5pnt70_unW1/N_zgt5pnt70)*100)))
print(' 6.00   {:5d} ({:6.2f}\%)'.format(N_zgt6pnt00_unW1,    ((N_zgt6pnt00_unW1/N_zgt6pnt00)*100)))
print(' 6.19   {:5d} ({:6.2f}\%)'.format(N_zgt6pnt19_unW1,    ((N_zgt6pnt19_unW1/N_zgt6pnt19)*100)))
print(' 6.50   {:5d} ({:6.2f}\%)'.format(N_zgt6pnt50_unW1,    ((N_zgt6pnt50_unW1/N_zgt6pnt50)*100)))
print(' 6.78   {:5d} ({:6.2f}\%)'.format(N_zgt6pnt78_unW1,    ((N_zgt6pnt78_unW1/N_zgt6pnt78)*100)))
print(' 7.00   {:5d} ({:6.2f}\%)'.format(N_zgt7pnt00_unW1,    ((N_zgt7pnt00_unW1/N_zgt7pnt00)*100)))
print(' 7.50   {:5d} ({:6.2f}\%)'.format(N_zgt7pnt50_unW1,    ((N_zgt7pnt50_unW1/N_zgt7pnt50)*100)))


## How many of the VHzQs, with unWISE W2 detections are above a given redshift 
N_zgt5pnt00_unW2 = np.count_nonzero((VHzQs['redshift'] >= redshift_array[0]) & (VHzQs['unW2mag']>-1))
N_zgt5pnt70_unW2 = np.count_nonzero((VHzQs['redshift'] >= redshift_array[1]) & (VHzQs['unW2mag']>-1))
N_zgt6pnt00_unW2 = np.count_nonzero((VHzQs['redshift'] >= redshift_array[2]) & (VHzQs['unW2mag']>-1))
N_zgt6pnt19_unW2 = np.count_nonzero((VHzQs['redshift'] >= redshift_array[3]) & (VHzQs['unW2mag']>-1))
N_zgt6pnt50_unW2 = np.count_nonzero((VHzQs['redshift'] >= redshift_array[4]) & (VHzQs['unW2mag']>-1))
N_zgt6pnt78_unW2 = np.count_nonzero((VHzQs['redshift'] >= redshift_array[5]) & (VHzQs['unW2mag']>-1))
N_zgt7pnt00_unW2 = np.count_nonzero((VHzQs['redshift'] >= redshift_array[6]) & (VHzQs['unW2mag']>-1))
N_zgt7pnt50_unW2 = np.count_nonzero((VHzQs['redshift'] >= redshift_array[7]) & (VHzQs['unW2mag']>-1))

print('$z \geq $ ')
print(' 5.00   {:5d} ({:6.2f}\%)'.format(N_zgt5pnt00_unW2,    ((N_zgt5pnt00_unW2/N_zgt5pnt00)*100)))
print(' 5.70   {:5d} ({:6.2f}\%)'.format(N_zgt5pnt70_unW2,    ((N_zgt5pnt70_unW2/N_zgt5pnt70)*100)))
print(' 6.00   {:5d} ({:6.2f}\%)'.format(N_zgt6pnt00_unW2,    ((N_zgt6pnt00_unW2/N_zgt6pnt00)*100)))
print(' 6.19   {:5d} ({:6.2f}\%)'.format(N_zgt6pnt19_unW2,    ((N_zgt6pnt19_unW2/N_zgt6pnt19)*100)))
print(' 6.50   {:5d} ({:6.2f}\%)'.format(N_zgt6pnt50_unW2,    ((N_zgt6pnt50_unW2/N_zgt6pnt50)*100)))
print(' 6.78   {:5d} ({:6.2f}\%)'.format(N_zgt6pnt78_unW2,    ((N_zgt6pnt78_unW2/N_zgt6pnt78)*100)))
print(' 7.00   {:5d} ({:6.2f}\%)'.format(N_zgt7pnt00_unW2,    ((N_zgt7pnt00_unW2/N_zgt7pnt00)*100)))
print(' 7.50   {:5d} ({:6.2f}\%)'.format(N_zgt7pnt50_unW2,    ((N_zgt7pnt50_unW2/N_zgt7pnt50)*100)))

print()
print()

print(' 5.00   {:5d} ({:6.2f}\%) {:5d} ({:6.2f}\%)'.format(N_zgt5pnt00_unW1, ((N_zgt5pnt00_unW1/N_zgt5pnt00)*100), N_zgt5pnt00_unW2, ((N_zgt5pnt00_unW2/N_zgt5pnt00)*100))          )
print(' 5.70   {:5d} ({:6.2f}\%)'.format(N_zgt5pnt70_unW2, ((N_zgt5pnt70_unW2/N_zgt5pnt70)*100)))
print(' 6.00   {:5d} ({:6.2f}\%)'.format(N_zgt6pnt00_unW2, ((N_zgt6pnt00_unW2/N_zgt6pnt00)*100)))
print(' 6.19   {:5d} ({:6.2f}\%)'.format(N_zgt6pnt19_unW2, ((N_zgt6pnt19_unW2/N_zgt6pnt19)*100)))
print(' 6.50   {:5d} ({:6.2f}\%)'.format(N_zgt6pnt50_unW2, ((N_zgt6pnt50_unW2/N_zgt6pnt50)*100)))
print(' 6.78   {:5d} ({:6.2f}\%)'.format(N_zgt6pnt78_unW2, ((N_zgt6pnt78_unW2/N_zgt6pnt78)*100)))
print(' 7.00   {:5d} ({:6.2f}\%)'.format(N_zgt7pnt00_unW2, ((N_zgt7pnt00_unW2/N_zgt7pnt00)*100)))
print(' 7.50   {:5d} ({:6.2f}\%)'.format(N_zgt7pnt50_unW2,  ((N_zgt7pnt50_unW2/N_zgt7pnt50)*100)))

