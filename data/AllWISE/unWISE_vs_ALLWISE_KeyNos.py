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

print('No. of quasars with unWISE W1 detections and redshift z>=7.00 is:: ', np.count_nonzero((VHzQs['unW1mag']>0) & (VHzQs['redshift'] >= 7.00)), ' out of ', np.count_nonzero((VHzQs['redshift'] >= 7.00)))

print('No. of quasars with unWISE W1 detections and redshift z>=6.70 is:: ', np.count_nonzero((VHzQs['unW1mag']>0) & (VHzQs['redshift'] >= 6.70)), ' out of ', np.count_nonzero((VHzQs['redshift'] >= 6.70)))


