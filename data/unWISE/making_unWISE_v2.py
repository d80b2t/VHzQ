'''
This wee script combines, or simply makes, the unWISE files for the VHzQs.

v1.0::
Starting with 'just' the original 424 VHzQs and then added
the "Halloween" 2018 Oct objects from arXiv:1810.11924-27v1.
Tidied up version of the Jupyter notebook making_unWISE_W1s.ipynb

v2.0::
Takes now *both* the W1 and W2 unWISE input files (e.g. from
Aaron Meisner and the official DR1 of the

''' 

import numpy as np
from astropy.io import ascii
from astropy.io import fits

## http://docs.astropy.org/en/stable/io/fits/index.html
## Reading in the unWISE W1 and W2 files::
december_w1_hdu = fits.open("high_z_qsos_03Dec18-w1.fits")  
december_w2_hdu = fits.open("high_z_qsos_03Dec18-w2.fits")  

print('december_w1_hdu', december_w1_hdu)

## Assuming (correctly) the first extension is a table
december_w1 = december_w1_hdu[1].data
december_w2 = december_w2_hdu[1].data

## Can look at the columns of said files.
## Should be very similiar (!!), even identical to that
## of the offical unWISE DR1, Meisner & Schlafly (2019)
december_w1.columns


print("type(december_w1['RA']), len(december_w1['RA'])", type(december_w1['RA']), len(december_w1['RA']))
print("type(december_w2['RA']), len(december_w2['RA'])", type(december_w2['RA']), len(december_w2['RA']))
print()

## Setting up the variables for flux -> magnitude (and flux error to mag error) conversions
unWISE_W1_RA    = december_w1['RA']
unWISE_W2_RA    = december_w2['RA']
unWISE_W1_DEC   = december_w1['DEC']
unWISE_W2_DEC   = december_w2['DEC']
unWISE_W1_FLUX  = december_w1['FLUX']
unWISE_W2_FLUX  = december_w2['FLUX']
unWISE_W1_DFLUX = december_w1['DFLUX']
unWISE_W2_DFLUX = december_w2['DFLUX']


## From http://astrometry.net/svn/tags/sequels-fp-1/wisecheck.py
def fluxtomag(nmgy):
    return -2.5 * (np.log10(np.maximum(1e-3, nmgy)) - 9.)

def dfluxtodmag(nmgy, dnmgy):
    return np.abs(-2.5 * (np.log10(1. + dnmgy / nmgy)))

## Calculating the magnitude, magnitude errors and SNRs
unWISE_W1_mag    = fluxtomag(unWISE_W1_FLUX)
unWISE_W1_magerr = dfluxtodmag(unWISE_W1_FLUX, unWISE_W1_DFLUX)
unWISE_W1_SNR    = unWISE_W1_FLUX/unWISE_W1_DFLUX

unWISE_W2_mag    = fluxtomag(unWISE_W2_FLUX)
unWISE_W2_magerr = dfluxtodmag(unWISE_W2_FLUX, unWISE_W2_DFLUX)
unWISE_W2_SNR    = unWISE_W2_FLUX/unWISE_W2_DFLUX

## To check what these mags look like
#for x, y, z in zip(unWISE_W1_mag, unWISE_W1_magerr,unWISE_W1_SNR ):
#    print(x, y, z)

# Creating the output variable
data_W1_out = [unWISE_W1_RA, unWISE_W1_DEC, unWISE_W1_mag, unWISE_W1_magerr, unWISE_W1_SNR]
data_W2_out = [unWISE_W2_RA, unWISE_W2_DEC, unWISE_W2_mag, unWISE_W2_magerr, unWISE_W2_SNR]

type(data_W1_out)
ascii.write(data_W1_out, 'unWISE_W1_temp.dat', names=['ra', 'dec', ' w1mpro', 'w1sigmpro', 'w1snr'], overwrite=True)
ascii.write(data_W2_out, 'unWISE_W2_temp.dat', names=['ra', 'dec', ' w2mpro', 'w2sigmpro', 'w2snr'], overwrite=True)

