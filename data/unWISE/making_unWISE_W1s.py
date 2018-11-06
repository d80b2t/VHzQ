'''
This wee script combines the unWISE files for the VHzQs. 
Starting with 'just' the original 424 VHzQs and then added
the "Halloween" 2018 Oct objects from arXiv:1810.11924-27v1.
Tidied up version of the Jupyter notebook making_unWISE_W1s.ipynb
''' 

import numpy as np
from astropy.io import ascii
from astropy.io import fits

## http://docs.astropy.org/en/stable/io/fits/index.html
## Reading in the unWISE W1 files::
fourhundered_w1_hdu = fits.open("VHzQ_w1-unwise_source_catalog.fits")  
halloween_w1_hdu    = fits.open("halloween_quasars-w1.fits")

print(fourhundered_w1_hdu)

## Assuming (correctly) the first extension is a table
fourhundered_w1 = fourhundered_w1_hdu[1].data
halloween_w1    = halloween_w1_hdu[1].data

#fourhundered_w1.columns
#halloween_w1.columns      ##   Doesn't have OBJID, NM

print(type(fourhundered_w1['RA']), len(fourhundered_w1['RA']))
print(type(halloween_w1['RA'])   , len(halloween_w1['RA']))

## Combining the W1 arrays
unWISE_W1_RA    = np.concatenate((fourhundered_w1['RA'], halloween_w1['RA']), axis=0)
unWISE_W1_DEC   = np.concatenate((fourhundered_w1['DEC'], halloween_w1['DEC']), axis=0)
unWISE_W1_FLUX  = np.concatenate((fourhundered_w1['FLUX'], halloween_w1['FLUX']), axis=0)
unWISE_W1_DFLUX = np.concatenate((fourhundered_w1['DFLUX'], halloween_w1['DFLUX']), axis=0)

print('len(unWISE_W1_RA)', len(unWISE_W1_RA))

## From http://astrometry.net/svn/tags/sequels-fp-1/wisecheck.py
def fluxtomag(nmgy):
    return -2.5 * (np.log10(np.maximum(1e-3, nmgy)) - 9.)

def dfluxtodmag(nmgy, dnmgy):
    return np.abs(-2.5 * (np.log10(1. + dnmgy / nmgy)))

## Calculating the magnitude, magnitude errors and SNRs
unWISE_W1_mag    = fluxtomag(unWISE_W1_FLUX)
unWISE_W1_magerr = dfluxtodmag(unWISE_W1_FLUX, unWISE_W1_DFLUX)
unWISE_W1_SNR    = unWISE_W1_FLUX/unWISE_W1_DFLUX

## To check what these mags look like
#for x, y, z in zip(unWISE_W1_mag, unWISE_W1_magerr,unWISE_W1_SNR ):
#    print(x, y, z)

# Creating the output variable
data_out = [unWISE_W1_RA, unWISE_W1_DEC, unWISE_W1_mag, unWISE_W1_magerr, unWISE_W1_SNR]
type(data_out)
ascii.write(data_out, 'unWISE_W1_temp.dat', names=['ra', 'dec', ' w1mpro', 'w1sigmpro', 'w1snr'], overwrite=True)

