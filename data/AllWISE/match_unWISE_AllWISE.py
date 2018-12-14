'''
Comparing the unWISE and the AllWISE detections.
Takes advatage of the fact that the AllWISE catalogs
return a number list of objects, missing out those
non-detections. 

'''


import numpy as np
from astropy.io import ascii
from astropy.io import fits

## `Super-set' of VHzQs, and not of these will be unWISE detections
VHzQs = ascii.read("VHzQs463_unWISE_v1pnt00.dat")

## AllWISE data.
allwise = ascii.read("VHzQs463_AllWISE_W1234.tbl")


f = open('output_temp.dat', 'w')

print('#RA           Dec   redshift  unW1_mag unW1_magerr unW1_snr  w1mpro w1sigmpro  w1snr  ', file=f)
## loop over the full VHzQs list...
for ii in range(len(VHzQs['count'])):
    #print(VHzQs['RA'][ii])
    #print('unw, {: 4d} {: 14.8f} {: 14.8f}'.format(VHzQs['count'][ii], VHzQs['RA'][ii], VHzQs['Dec'][ii]))

    matched = 0
    ## Now loop over the list of AllWISE objects
    for jj in range(len(allwise['cntr_01'])):

        ## Check to see if List 1 = List 2...
        if VHzQs['count'][ii] == allwise['cntr_01'][jj]:
            print('{:11.7f} {:11.7f} {: 5.3f}   {:8.4f} {:8.4f} {:8.4f}  {: 8.3f} {: 7.2f} {: 6.1f}'.format(
                VHzQs['RA'][ii], VHzQs['Dec'][ii], VHzQs['redshift'][ii],
                VHzQs['unW1_mag'][ii], VHzQs['unW1_magerr'][ii], VHzQs['unW1_snr'][ii], 
                allwise['w1mpro'][jj], allwise['w1sigmpro'][jj], allwise['w1snr'][jj]), 
                file=f)
            matched = 1

    if matched == 0:
        print('{:11.7f} {:11.7f} {: 5.3f}   {:8.4f} {:8.4f} {:8.4f}  {:8.3f} {:7.2f} {:6.1f}'.format(
                VHzQs['RA'][ii], VHzQs['Dec'][ii], VHzQs['redshift'][ii], 
                VHzQs['unW1_mag'][ii], VHzQs['unW1_magerr'][ii], VHzQs['unW1_snr'][ii], 
                -9.99, -9.99, -9.9), file=f)
                

f.close() 
