'''
Very simple, but pretty useful wee script that runs some 

'''
import numpy as np

from astropy.table import Table
from astropy.io import ascii

## Data files and path
#path     = '/cos_pc19a_npr/programs/quasars/highest_z/data/WISE/'
#filename = 'VHzQs_ZYJHK_WISE.dat'
#VHzQs = ascii.read(path+filename)
VHzQs = ascii.read("VHzQs463_unWISE_vs_ALLWISE_v1.dat")



## Setting up the variables just for me to use a bit easier
unW1           = VHzQs[np.where( VHzQs['unW1mag']>-1)]
unW1_just      = VHzQs[np.where((VHzQs['unW1mag']>-1) & (VHzQs['unW2mag']<-1))]
#unW1_not_AllW1 = VHzQs[np.where((VHzQs['unW1mag']>-1) & (VHzQs['w1mpro']<-1))]

unW2           = VHzQs[np.where( VHzQs['unW2mag']>-1)]
unW2_just      = VHzQs[np.where((VHzQs['unW2mag']>-1) & (VHzQs['unW1mag']<-1))]
unW2_not_AllW2 = VHzQs[np.where((VHzQs['unW2mag']>-1) & (VHzQs['w2mpro']<-1))]


## Wee bit out .tex outputting...
print('\hline \hline')
print('Detection band & No. of objects')
print('\hline')
print('unWISE W1                 & ', len(unW1),             ' \\\ ')
print('unWISE W1     ! unWISE W2 & ', len(unW1_just),        '  \\\ ')
print('unWISE W1 and !AllWISE W1 & ', len(unW1_not_AllW1),   '  \\\ ')
print()
print('unWISE W2                 & ', len(unW2),             ' \\\ ')
print('unWISE W2     ! unWISE W1  & ', len(unW2_just),        '   \\\ ')
print('unWISE W2 and !AllWISE W1 & ', len(unW2_not_AllW2),   '  \\\ ')
print('\hline \hline')
print()



print('Number of objects with unWISE W1 detections (unW1mag>0)', np.count_nonzero(VHzQs['unW1mag']>0))
print('Number of objects with unWISE W2 detections (unW1mag>0)', np.count_nonzero(VHzQs['unW2mag']>0))
print()
print('Number of objects with ALLWISE W1 detections (unW1mag>0)', np.count_nonzero(VHzQs['w1mpro']>0))
print('Number of objects with ALLWISE W2 detections (unW1mag>0)', np.count_nonzero(VHzQs['w2mpro']>0))

print()
print('No. of quasars with unWISE W1 detections and redshift z>=7.50 is:: ', np.count_nonzero((VHzQs['unW1mag']>0) & (VHzQs['redshift'] >= 7.50)), ' out of ', np.count_nonzero((VHzQs['redshift'] >= 7.50)))
print('No. of quasars with unWISE W1 detections and redshift z>=7.00 is:: ', np.count_nonzero((VHzQs['unW1mag']>0) & (VHzQs['redshift'] >= 7.00)), ' out of ', np.count_nonzero((VHzQs['redshift'] >= 7.00)))
print('No. of quasars with unWISE W1 detections and redshift z>=6.78 is:: ', np.count_nonzero((VHzQs['unW1mag']>0) & (VHzQs['redshift'] >= 6.78)), ' out of ', np.count_nonzero((VHzQs['redshift'] >= 6.78)))
#print('No. of quasars with unWISE W1 detections and redshift z>=6.70 is:: ', np.count_nonzero((VHzQs['unW1mag']>0) & (VHzQs['redshift'] >= 6.70)), ' out of ', np.count_nonzero((VHzQs['redshift'] >= 6.70)))
print('No. of quasars with unWISE W1 detections and redshift z>=6.50 is:: ', np.count_nonzero((VHzQs['unW1mag']>0) & (VHzQs['redshift'] >= 6.50)), ' out of ', np.count_nonzero((VHzQs['redshift'] >= 6.50)))
print('No. of quasars with unWISE W1 detections and redshift z>=6.19 is:: ', np.count_nonzero((VHzQs['unW1mag']>0) & (VHzQs['redshift'] >= 6.19)), ' out of ', np.count_nonzero((VHzQs['redshift'] >= 6.19)))
print('No. of quasars with unWISE W1 detections and redshift z>=6.00 is:: ', np.count_nonzero((VHzQs['unW1mag']>0) & (VHzQs['redshift'] >= 6.00)), ' out of ', np.count_nonzero((VHzQs['redshift'] >= 6.00)))
print('No. of quasars with unWISE W1 detections and redshift z>=5.70 is:: ', np.count_nonzero((VHzQs['unW1mag']>0) & (VHzQs['redshift'] >= 5.70)), ' out of ', np.count_nonzero((VHzQs['redshift'] >= 5.70)))
print('No. of quasars with unWISE W1 detections and redshift z>=5.00 is:: ', np.count_nonzero((VHzQs['unW1mag']>0) & (VHzQs['redshift'] >= 5.00)), ' out of ', np.count_nonzero((VHzQs['redshift'] >= 5.00)))

print()
