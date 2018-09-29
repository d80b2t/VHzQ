'''
Why doesn't matplotlib look as good as SM??!!!
http://space.mit.edu/home/turnerm/python.html
'''

import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

from matplotlib import colors as mcolors
from astropy.io import ascii
from astropy.io import fits
from pylab import plot, show

redshift = 6.3
one_plus_z = 1 #+ redshift

##
##  P h o t o m e t r y    d a t a
##
path = '/cos_pc19a_npr/programs/quasars/highest_z/LightCurves/variable_candidates/SDSSJ0100+2802/'

## 2MASS
filename = 'TWOMASS_v1.tbl'
infile = path+filename
twomass_data = ascii.read(filename)

twomass_mjd   = twomass_data['jdate']-2400000.0
twomass_JVega = twomass_data['j_m']
twomass_HVega = twomass_data['j_m']
twomass_KVega = twomass_data['j_m']

twomass_J_AB = twomass_JVega + 0.894
twomass_H_AB = twomass_HVega + 1.374
twomass_K_AB = twomass_KVega + 1.84


## UKIDSS LAS
filename = 'qsoID22_setup1_light_curve_WSERV1000.fits'
infile = path+filename

## Okay, what we really want to do... ;-)
#data_table = pyfits.getdata(infile)
wfcam      = fits.open(infile)
data_table = wfcam[1].data

## Quick check on the format/dimensions of the FITS table file...
print(type(data_table), '\n')
print('The number of rows of is.... ', data_table.shape, '\n')
print('The number of columns is...  ', len(data_table.names), '\n\n')

## Now getting into it some more...
mjd_full    = data_table.field('MJD')
WFCAM_Z     = data_table[np.where(data_table['FILTERID'] == 1)]['APERMAG3AB']
WFCAM_Y     = data_table[np.where(data_table['FILTERID'] == 2)]['APERMAG3AB']
WFCAM_J     = data_table[np.where(data_table['FILTERID'] == 3)]['APERMAG3AB']
WFCAM_H     = data_table[np.where(data_table['FILTERID'] == 4)]['APERMAG3AB']
WFCAM_K     = data_table[np.where(data_table['FILTERID'] == 5)]['APERMAG3AB']
WFCAM_Z_err = data_table[np.where(data_table['FILTERID'] == 1)]['APERMAG3ERR']
WFCAM_Y_err = data_table[np.where(data_table['FILTERID'] == 2)]['APERMAG3ERR']
WFCAM_J_err = data_table[np.where(data_table['FILTERID'] == 3)]['APERMAG3ERR']
WFCAM_H_err = data_table[np.where(data_table['FILTERID'] == 4)]['APERMAG3ERR']
WFCAM_K_err = data_table[np.where(data_table['FILTERID'] == 5)]['APERMAG3ERR']
WFCAM_Z_mjd = data_table[np.where(data_table['FILTERID'] == 1)]['MJD']
WFCAM_Y_mjd = data_table[np.where(data_table['FILTERID'] == 2)]['MJD']
WFCAM_J_mjd = data_table[np.where(data_table['FILTERID'] == 3)]['MJD']
WFCAM_H_mjd = data_table[np.where(data_table['FILTERID'] == 4)]['MJD']
WFCAM_K_mjd = data_table[np.where(data_table['FILTERID'] == 5)]['MJD']

## From Ross&Cross (2018/9)::
#ULAS_Z_AB = ULAS_Y['YAperMag3']   + 0.617
#ULAS_Y_AB = ULAS_Y['YAperMag3']   + 0.617
#ULAS_J_AB = ULAS_J['J1_AperMag3'] + 0.919
#ULAS_H_AB = ULAS_H['HAperMag3']   + 1.379
#ULAS_K_AB = ULAS_K['KAperMag3']   + 1.90	

##   
## WISE
##
data = ascii.read(path+'NEOWISER-R_slim.dat')
xx    = np.empty(8)
yy_w1 = np.empty(8)   
yy_w2 = np.empty(8)   

xx[0] = data['mjd'][0:14].mean()
xx[1] = data['mjd'][14:28].mean()
xx[2] = data['mjd'][29:42].mean()
xx[3] = data['mjd'][43:54].mean()
xx[4] = data['mjd'][55:65].mean()
xx[5] = data['mjd'][66:77].mean()
xx[6] = data['mjd'][77:88].mean()
xx[7] = data['mjd'][89:].mean()

yy_w1[0] = data['neowise_w1'][0:14].mean()
yy_w1[1] = data['neowise_w1'][14:28].mean()
yy_w1[2] = data['neowise_w1'][29:42].mean()
yy_w1[3] = data['neowise_w1'][43:54].mean()
yy_w1[4] = data['neowise_w1'][55:65].mean()
yy_w1[5] = data['neowise_w1'][66:77].mean()
yy_w1[6] = data['neowise_w1'][77:88].mean()
yy_w1[7] = data['neowise_w1'][89:].mean()

yy_w2[0] = data['neowise_w2'][0:14].mean()
yy_w2[1] = data['neowise_w2'][14:28].mean()
yy_w2[2] = data['neowise_w2'][29:42].mean()
yy_w2[3] = data['neowise_w2'][43:54].mean()
yy_w2[4] = data['neowise_w2'][55:65].mean()
yy_w2[5] = data['neowise_w2'][69:77].mean()
yy_w2[6] = data['neowise_w2'][77:88].mean()
yy_w2[7] = data['neowise_w2'][89:].mean()


## 
filename='NEOWISER-R_SingleExposure_L1bs_SDSSJ0100.tbl'
WISE_data = ascii.read(path+filename)

## Just moving back the MJDs
WISE_data_mjd = WISE_data['mjd'] -56000 

## For WISE, we adopt 2.699 and 3.339 as the conversions to AB from W1 and W2 Vega magnitudes,
NEOWISER_W1_AB = WISE_data['w1mpro']         + 2.699
NEOWISER_W2_AB = WISE_data['w2mpro']         + 3.339
ALLWISE_W1_AB  = WISE_data['w1mpro_allwise'] + 2.699
ALLWISE_W2_ABs = WISE_data['w2mpro_allwise'] + 3.339



##
##   Making the plot
##
plt.rcParams.update({'font.size': 14})
fig, ax = plt.subplots(figsize=(12.0, 8.0))

##  `Default' style choices
ls       = 'solid'
lw       = 2.0
s        = 60.
s_large  = s*5.
ms       = 6.0
fontsize = 24
alpha    = 1.00

mjd_offset = 50000
## MJD ranges
xmin = 50000 - mjd_offset   #  WISE_data['mjd'].min(), No 2MASS,
#xmin = 56000 - 56000   #  WISE_data['mjd'].min(), No 2MASS,
xmax = 58250 - mjd_offset   #  WISE_data['mjd'].min()
xmin_rest = (xmin/one_plus_z)
xmax_rest = (xmax/one_plus_z)
ymin = 19.00   
ymax = 16.80   


## PLOTTING  2MASS 
ax.scatter((twomass_mjd-mjd_offset)/one_plus_z, twomass_J_AB, s=ms*60*1.8, color='k')
ax.scatter((twomass_mjd-mjd_offset)/one_plus_z, twomass_J_AB, s=ms*60.,    color='yellow')
ax.scatter((twomass_mjd-mjd_offset)/one_plus_z, twomass_H_AB, s=ms*60*1.8, color='k')
ax.scatter((twomass_mjd-mjd_offset)/one_plus_z, twomass_H_AB, s=ms*60.,    color='goldenrod')
ax.scatter((twomass_mjd-mjd_offset)/one_plus_z, twomass_K_AB, s=ms*60*1.8, color='k')
ax.scatter((twomass_mjd-mjd_offset)/one_plus_z, twomass_K_AB, s=ms*60.,    color='orangered')


## PLOTTING  UKIDSS LAS
ms = 15
#ax.errorbar(WFCAM_Z_mjd, WFCAM_Z,  yerr=WFCAM_Z_err,   fmt='h', linestyle=ls, linewidth=lw, color='y', ms=ms)
#ax.errorbar(WFCAM_Y_mjd, WFCAM_Y,  yerr=WFCAM_Y_err,   fmt='h', linestyle=ls, linewidth=lw, color='y', ms=ms)
ax.errorbar((WFCAM_J_mjd-mjd_offset)/one_plus_z, WFCAM_J, yerr=WFCAM_J_err, fmt='h', linestyle=ls, linewidth=lw, color='k', ms=ms*1.8)
ax.errorbar((WFCAM_J_mjd-mjd_offset)/one_plus_z, WFCAM_J, yerr=WFCAM_J_err, fmt='h', linestyle=ls, linewidth=lw, color='yellow', ms=ms)
ax.errorbar((WFCAM_H_mjd-mjd_offset)/one_plus_z, WFCAM_H, yerr=WFCAM_H_err, fmt='h', linestyle=ls, linewidth=lw, color='k', ms=ms*1.8)
ax.errorbar((WFCAM_H_mjd-mjd_offset)/one_plus_z, WFCAM_H, yerr=WFCAM_H_err, fmt='h', linestyle=ls, linewidth=lw, color='goldenrod', ms=ms)
#ax.errorbar(WFCAM_K_mjd, WFCAM_K,  yerr=WFCAM_K_err,   fmt='h', linestyle=ls, linewidth=lw, color='k', ms=ms*1.8)
#ax.errorbar(WFCAM_K_mjd, WFCAM_K,  yerr=WFCAM_K_err,   fmt='h', linestyle=ls, linewidth=lw, color='orangered', ms=ms)

##  PLOTTING  WISE 
ms=5.5
#ax.errorbar(WISE_data_mjd, NEOWISER_W1_AB, yerr=WISE_data['w1sigmpro'], fmt='o', ms=ms, color='indigo')
#ax.errorbar(WISE_data_mjd, NEOWISER_W2_AB, yerr=WISE_data['w2sigmpro'], fmt='o', ms=ms, color='brown')
#ax.errorbar(WISE_L1bs['mjd'], WISE_W1_ABs, yerr=WISE_L1bs['w1sigmpro'], fmt='o', ms=ms, color='indigo')
#ax.errorbar(WISE_L1bs['mjd'], WISE_W2_ABs, yerr=WISE_L1bs['w2sigmpro'], fmt='o', ms=ms, color='brown')

## NEOWISE averages
ax.scatter((xx-mjd_offset)/one_plus_z, (yy_w1 + 2.699), s=ms*60., color='indigo')
ax.scatter((xx-mjd_offset)/one_plus_z, (yy_w2 + 3.339) , s=ms*60., color='brown')

ax.set_xlim((xmin, xmax))
#ax.set_xlim((xmin_rest, xmax_rest))
ax.set_ylim((ymin, ymax))
ax.tick_params('x', direction='in')
ax.tick_params('y', direction='in')

plt.xlabel('MJD-50000')
#plt.xlabel('Days in the rest-frame')
plt.ylabel('magnitude (AB)')


plt.savefig('J0100_lc_temp.pdf', format='pdf')
plt.close(fig)

