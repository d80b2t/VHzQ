'''
Very simple, but pretty useful wee script that runs some 

'''
import numpy as np

from astropy.table import Table
from astropy.io import ascii



VHzQs = ascii.read("VHzQs463_unWISE_vs_ALLWISE_v1.dat")


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
