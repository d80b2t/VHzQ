'''
This wee script combines the unWISE files for the VHzQs. 
Starting with 'just' the original 424 VHzQs and then added
the "Halloween" 2018 Oct objects from arXiv:1810.11924-27v1.

v1.0::
Starting with 'just' the original 424 VHzQs and then added
the "Halloween" 2018 Oct objects from arXiv:1810.11924-27v1.
Tidied up version of the Jupyter notebook making_unWISE_W1s.ipynb

Copy of making_unWISE_W2s.py, but needed since unWISE W2 catalog
and unWISE W2 catalogs are separate
''' 

import numpy as np
from astropy.io import ascii
from astropy.io import fits

## http://docs.astropy.org/en/stable/io/fits/index.html
## Reading in the unWISE W2 files::
fourhundered_w2_hdu = fits.open("VHzQ_w2-unwise_source_catalog.fits")  
halloween_w2_hdu    = fits.open("halloween_quasars-w2.fits")

print(fourhundered_w2_hdu)

## Assuming (correctly) the first extension is a table
fourhundered_w2 = fourhundered_w2_hdu[1].data
halloween_w2    = halloween_w2_hdu[1].data

#fourhundered_w2.columns
#halloween_w2.columns      ##   Doesn't have OBJID, NM

print(type(fourhundered_w2['RA']), len(fourhundered_w2['RA']))
print(type(halloween_w2['RA'])   , len(halloween_w2['RA']))

## Combining the W2 arrays
unWISE_W2_RA    = np.concatenate((fourhundered_w2['RA'], halloween_w2['RA']), axis=0)
unWISE_W2_DEC   = np.concatenate((fourhundered_w2['DEC'], halloween_w2['DEC']), axis=0)
unWISE_W2_FLUX  = np.concatenate((fourhundered_w2['FLUX'], halloween_w2['FLUX']), axis=0)
unWISE_W2_DFLUX = np.concatenate((fourhundered_w2['DFLUX'], halloween_w2['DFLUX']), axis=0)

print('len(unWISE_W2_RA)', len(unWISE_W2_RA))

## From http://astrometry.net/svn/tags/sequels-fp-1/wisecheck.py
def fluxtomag(nmgy):
    return -2.5 * (np.log10(np.maximum(1e-3, nmgy)) - 9.)

def dfluxtodmag(nmgy, dnmgy):
    return np.abs(-2.5 * (np.log10(1. + dnmgy / nmgy)))

## Calculating the magnitude, magnitude errors and SNRs
unWISE_W2_mag    = fluxtomag(unWISE_W2_FLUX)
unWISE_W2_magerr = dfluxtodmag(unWISE_W2_FLUX, unWISE_W2_DFLUX)
unWISE_W2_SNR    = unWISE_W2_FLUX/unWISE_W2_DFLUX

## To check what these mags look like
#for x, y, z in zip(unWISE_W2_mag, unWISE_W2_magerr,unWISE_W2_SNR ):
#    print(x, y, z)

# Creating the output variable
data_out = [unWISE_W2_RA, unWISE_W2_DEC, unWISE_W2_mag, unWISE_W2_magerr, unWISE_W2_SNR]
type(data_out)
ascii.write(data_out, 'unWISE_W2_temp.dat', names=['ra', 'dec', ' w2mpro', 'w2sigmpro', 'w2snr'], overwrite=True)

