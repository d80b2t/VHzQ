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
from matplotlib import gridspec
from astropy.io import ascii
from astropy.io import fits
from pylab import plot, show

redshift = 6.3
one_plus_z = 1 #+ redshift

mjd_offset = 50000  ## for 2MASS
#mjd_offset = 55000  ## for 2MASS

##
##  P h o t o m e t r y    d a t a
##
path = '/cos_pc19a_npr/programs/quasars/highest_z/LightCurves/variable_candidates/SDSSJ0100+2802/'

## 2MASS
filename = 'TWOMASS_v1.tbl'
infile = path+filename
twomass_data = ascii.read(filename)

## 2MASS J, H and Ks bands with Vega magnitudes of 17.00 6 0.20, 15.98 6 0.19 and 15.20 6 0.16,
## J2MASS = JAB − 0.894
twomass_mjd   = twomass_data['jdate']-2400000.0
twomass_JVega = twomass_data['j_m']
twomass_HVega = twomass_data['h_m']
twomass_KVega = twomass_data['k_m']
twomass_Jerr  = twomass_data['j_cmsig']
twomass_Herr  = twomass_data['h_cmsig']
twomass_Kerr  = twomass_data['k_cmsig']

twomass_J_AB  = twomass_JVega + 0.894
twomass_H_AB  = twomass_HVega + 1.374
twomass_K_AB  = twomass_KVega + 1.84


##
## UKIDSS LAS
##
filename   = 'qsoID22_setup1_light_curve_WSERV1000.fits'
infile     = path+filename
wfcam      = fits.open(infile)
data_table = wfcam[1].data

## Quick check on the format/dimensions of the FITS table file...
print(type(data_table), '\n')
print('The number of rows of is.... ', data_table.shape, '\n')
print('The number of columns is...  ', len(data_table.names), '\n\n')

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



##   
##   W I S E      reading-in the data...
##
## All-Sky
infile= 'WISE_AllSky_SourceCatalog_SDSSJ0100.tbl'
AllSky = ascii.read(path+infile)
AllSky_W1    = AllSky['w1mpro']
AllSky_W2    = AllSky['w2mpro']
AllSky_W3    = AllSky['w3mpro']
AllSky_W4    = AllSky['w4mpro']
AllSky_W1err = AllSky['w1sigmpro']
AllSky_W2err = AllSky['w2sigmpro']
AllSky_W3err = AllSky['w3sigmpro']
AllSky_W4err = AllSky['w4sigmpro']

AllSky_W1_AB = AllSky_W1 + 2.699
AllSky_W2_AB = AllSky_W2 + 3.339
AllSky_W3_AB = AllSky_W3 + 5.174
AllSky_W4_AB = AllSky_W4 + 6.60

AllSky_W1mjd =  AllSky['w1mjdmean']
AllSky_W2mjd =  AllSky['w2mjdmean']
AllSky_W3mjd =  AllSky['w3mjdmean']
AllSky_W4mjd =  AllSky['w4mjdmean']


## All-Sky  L1bs
infile='WISE_AllSky_SingleExposure_L1bs_SDSSJ0100.tbl'
AllSky_L1bs =  ascii.read(path+infile)
AllSky_w1_L1bs =  AllSky_L1bs['w1mpro']
AllSky_w2_L1bs =  AllSky_L1bs['w2mpro']
AllSky_w3_L1bs =  AllSky_L1bs['w3mpro']
AllSky_w4_L1bs =  AllSky_L1bs['w4mpro']
AllSky_w1_L1bs_AB =  AllSky_L1bs['w1mpro'] + 2.699
AllSky_w2_L1bs_AB =  AllSky_L1bs['w2mpro'] + 3.339
AllSky_w3_L1bs_AB =  AllSky_L1bs['w3mpro'] + 5.174
AllSky_w4_L1bs_AB =  AllSky_L1bs['w4mpro'] + 6.60

AllSky_L1bs_mjd = AllSky_L1bs['mjd']


## ALLWISE
infile='WISE_ALLWISE_SourceCatalog_SDSSJ0100.tbl'
ALLWISE =  ascii.read(path+infile)
ALLWISE_W1 = ALLWISE['w1mpro']
ALLWISE_W2 = ALLWISE['w2mpro']
ALLWISE_W3 = ALLWISE['w3mpro']
ALLWISE_W4 = ALLWISE['w4mpro']

ALLWISE_W1_AB = ALLWISE_W1 + 2.699
ALLWISE_W2_AB = ALLWISE_W2 + 3.339
ALLWISE_W3_AB = ALLWISE_W3 + 5.174
ALLWISE_W4_AB = ALLWISE_W4 + 6.66

ALLWISE_W1mjd =  ALLWISE['w1mjdmean']
ALLWISE_W2mjd =  ALLWISE['w2mjdmean']
ALLWISE_W3mjd =  ALLWISE['w3mjdmean']
ALLWISE_W4mjd =  ALLWISE['w4mjdmean']

##
## NEOWISER-R_SingleExposure_L1bs
##
filename='NEOWISER-R_SingleExposure_L1bs_SDSSJ0100.tbl'
NEOWISER_data = ascii.read(path+filename)
NEOWISER_data_mjd = NEOWISER_data['mjd']

## For WISE, we adopt 2.699 and 3.339 as the conversions to AB from W1 and W2 Vega magnitudes,
NEOWISER_W1_AB = NEOWISER_data['w1mpro']  + 2.699
NEOWISER_W2_AB = NEOWISER_data['w2mpro']  + 3.339


## NEOWISE-R averages...
data = ascii.read(path+'NEOWISER-R_slim.dat')
xx       = np.empty(8)
yy_w1    = np.empty(8)
yy_w1err = np.empty(8)   
yy_w2    = np.empty(8)
yy_w2err = np.empty(8)   


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

yy_w1err[0] = data['neowise_w1'][0:14].std()
yy_w1err[1] = data['neowise_w1'][14:28].std()
yy_w1err[2] = data['neowise_w1'][29:42].std()
yy_w1err[3] = data['neowise_w1'][43:54].std()
yy_w1err[4] = data['neowise_w1'][55:65].std()
yy_w1err[5] = data['neowise_w1'][66:77].std()
yy_w1err[6] = data['neowise_w1'][77:88].std()
yy_w1err[7] = data['neowise_w1'][89:].std()

yy_w2[0] = data['neowise_w2'][0:14].mean()
yy_w2[1] = data['neowise_w2'][14:28].mean()
yy_w2[2] = data['neowise_w2'][29:42].mean()
yy_w2[3] = data['neowise_w2'][43:54].mean()
yy_w2[4] = data['neowise_w2'][55:65].mean()
yy_w2[5] = data['neowise_w2'][69:77].mean()
yy_w2[6] = data['neowise_w2'][77:88].mean()
yy_w2[7] = data['neowise_w2'][89:].mean()

yy_w2err[0] = data['neowise_w2'][0:14].std()
yy_w2err[1] = data['neowise_w2'][14:28].std()
yy_w2err[2] = data['neowise_w2'][29:42].std()
yy_w2err[3] = data['neowise_w2'][43:54].std()
yy_w2err[4] = data['neowise_w2'][55:65].std()
yy_w2err[5] = data['neowise_w2'][66:77].std()
yy_w2err[6] = data['neowise_w2'][77:88].std()
yy_w2err[7] = data['neowise_w2'][89:].std()


##
##   Making the plot
##
plt.rcParams.update({'font.size': 14})
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(12.0, 8.0))

##  `Default' style choices
ls       = 'solid'
lw       = 2.0
s        = 60.
s_large  = s*5.
ms       = 6.0
fontsize = 24
alpha    = 1.00


## MJD ranges
#xmin = 50000 - mjd_offset   # 
xmin = 55000 - mjd_offset   #  No 2MASS
xmax = 56000 - mjd_offset   #  Just ALLWISE
xmax = 58250 - mjd_offset   #  
xmin_rest = (xmin/one_plus_z)
xmax_rest = (xmax/one_plus_z)
ymin = 17.70      # 18.20 with 2MASS
ymax = 16.70   
##
## PLOTTING    2 M A S S
##
#ax.scatter((twomass_mjd-mjd_offset)/one_plus_z, twomass_J_AB, s=ms*60*1.8, color='k',      label='')
#ax.scatter((twomass_mjd-mjd_offset)/one_plus_z, twomass_J_AB, s=ms*60.,    color='orange', label="2MASSS J")
#ax.scatter((twomass_mjd-mjd_offset)/one_plus_z, twomass_H_AB, s=ms*60*1.8, color='k',      label='')
#ax.scatter((twomass_mjd-mjd_offset)/one_plus_z, twomass_H_AB, s=ms*60.,    color='gold',   label="2MASSS H")
#ax.scatter((twomass_mjd-mjd_offset)/one_plus_z, twomass_K_AB, s=ms*60*1.8, color='k',      label='')
#ax.scatter((twomass_mjd-mjd_offset)/one_plus_z, twomass_K_AB, s=ms*60.,    color='yellow', label="2MASSS Ks")
##
ms=12
ax.errorbar((twomass_mjd-mjd_offset)/one_plus_z, twomass_J_AB, yerr=twomass_Jerr, ms=ms*1.4, marker="o", color='k',      label=''     )
ax.errorbar((twomass_mjd-mjd_offset)/one_plus_z, twomass_J_AB, yerr=twomass_Jerr, ms=ms,     marker="o", color='orange', label="2MASSS J")
ax.errorbar((twomass_mjd-mjd_offset)/one_plus_z, twomass_H_AB, yerr=twomass_Herr, ms=ms*1.4, marker="o", color='k',      label='')
ax.errorbar((twomass_mjd-mjd_offset)/one_plus_z, twomass_H_AB, yerr=twomass_Herr, ms=ms,     marker="o", color='gold',   label="2MASSS H")
ax.errorbar((twomass_mjd-mjd_offset)/one_plus_z, twomass_K_AB, yerr=twomass_Kerr, ms=ms*1.4, marker="o", color='k',      label='')
ax.errorbar((twomass_mjd-mjd_offset)/one_plus_z, twomass_K_AB, yerr=twomass_Kerr, ms=ms,     marker="o", color='yellow', label="2MASSS Ks")


##
## PLOTTING   W F C A M 
##
ms = 20
ax.errorbar((WFCAM_J_mjd-mjd_offset)/one_plus_z, WFCAM_J, yerr=WFCAM_J_err, fmt='h', linestyle=ls, linewidth=lw, color='k',      ms=ms*1.4,  label='')
ax.errorbar((WFCAM_J_mjd-mjd_offset)/one_plus_z, WFCAM_J, yerr=WFCAM_J_err, fmt='h', linestyle=ls, linewidth=lw, color='orange', ms=ms, label="WFCAM J")
ax.errorbar((WFCAM_H_mjd-mjd_offset)/one_plus_z, WFCAM_H, yerr=WFCAM_H_err, fmt='h', linestyle=ls, linewidth=lw, color='k',      ms=ms*1.4,  label='')
ax.errorbar((WFCAM_H_mjd-mjd_offset)/one_plus_z, WFCAM_H, yerr=WFCAM_H_err, fmt='h', linestyle=ls, linewidth=lw, color='gold',   ms=ms, label="WFCAM H")


##
##  P L O T T I N G     W  I  S  E
##
##  PLOTTING  AllSky
ms=6.0
#ax.scatter(AllSky_W1mjd-mjd_offset, AllSky_W1_AB, s=ms*60*1.8, color='k',         label='')
#ax.scatter(AllSky_W2mjd-mjd_offset, AllSky_W2_AB, s=ms*60*1.8, color='k',         label='')
#ax.scatter(AllSky_W3mjd-mjd_offset, AllSky_W3_AB, s=ms*60*1.8, color='k')
#ax.scatter(AllSky_W4mjd-mjd_offset, AllSky_W4_AB, s=ms*60*1.8, color='k')
#ax.scatter(AllSky_W1mjd-mjd_offset, AllSky_W1_AB, s=ms*60,     color='peru',      label='WISE AllSky')
#ax.scatter(AllSky_W2mjd-mjd_offset, AllSky_W2_AB, s=ms*60,     color='orangered', label='WISE AllSky')
#ax.scatter(AllSky_W3mjd-mjd_offset, AllSky_W3_AB, s=ms*60,     color='red')
#ax.scatter(AllSky_W4mjd-mjd_offset, AllSky_W4_AB, s=ms*60,     color='darkred')
ms=12
ax.errorbar(AllSky_W1mjd-mjd_offset, AllSky_W1_AB, ms=ms*1.4, marker="o", color='k',         label='')
ax.errorbar(AllSky_W2mjd-mjd_offset, AllSky_W2_AB, ms=ms*1.4, marker="o", color='k',         label='')
ax.errorbar(AllSky_W1mjd-mjd_offset, AllSky_W1_AB, ms=ms,     marker="o", color='peru',      label='')
ax.errorbar(AllSky_W2mjd-mjd_offset, AllSky_W2_AB, ms=ms,     marker="o", color='orangered', label='')

##  PLOTTING  AllSky  L1bs
ms=1.5
#ax.scatter(AllSky_L1bs_mjd-mjd_offset, AllSky_w1_L1bs_AB, s=ms*60*1.8, color='k')
#ax.scatter(AllSky_L1bs_mjd-mjd_offset, AllSky_w2_L1bs_AB, s=ms*60*1.8, color='k')
#ax.scatter(AllSky_L1bs_mjd-mjd_offset, AllSky_w3_L1bs_AB, s=ms*60*1.8, color='k')
#ax.scatter(AllSky_L1bs_mjd-mjd_offset, AllSky_w4_L1bs_AB, s=ms*60*1.8, color='k')
#ax.scatter(AllSky_L1bs_mjd-mjd_offset, AllSky_w1_L1bs_AB, s=ms*60,     color='peru')
#ax.scatter(AllSky_L1bs_mjd-mjd_offset, AllSky_w2_L1bs_AB, s=ms*60,     color='orangered')
#ax.scatter(AllSky_L1bs_mjd-mjd_offset, AllSky_w3_L1bs_AB, s=ms*60,     color='red')
#ax.scatter(AllSky_L1bs_mjd-mjd_offset, AllSky_w4_L1bs_AB, s=ms*60,     color='darkred')

ms=6.0
##  PLOTTING  ALLWISE
#ax.scatter(ALLWISE_W1mjd-mjd_offset, ALLWISE_W1_AB, s=ms*60*1.8, color='k')
#ax.scatter(ALLWISE_W2mjd-mjd_offset, ALLWISE_W2_AB, s=ms*60*1.8, color='k')
#ax.scatter(ALLWISE_W3mjd-mjd_offset, ALLWISE_W3_AB, s=ms*60*1.8, color='k')
#ax.scatter(ALLWISE_W4mjd-mjd_offset, ALLWISE_W4_AB, s=ms*60*1.8, color='k')
#ax.scatter(ALLWISE_W1mjd-mjd_offset, ALLWISE_W1_AB, s=ms*60, color='peru')
#ax.scatter(ALLWISE_W2mjd-mjd_offset, ALLWISE_W2_AB, s=ms*60, color='orangered')
#ax.scatter(ALLWISE_W3mjd-mjd_offset, ALLWISE_W3_AB, s=ms*60, color='red')
#ax.scatter(ALLWISE_W4mjd-mjd_offset, ALLWISE_W4_AB, s=ms*60, color='darkred')
ms=12.
ax.errorbar(ALLWISE_W1mjd-mjd_offset, ALLWISE_W1_AB, yerr=ALLWISE['w1sigmpro'], ms=ms*1.4, color='k',         marker="o", label='')
ax.errorbar(ALLWISE_W2mjd-mjd_offset, ALLWISE_W2_AB, yerr=ALLWISE['w2sigmpro'], ms=ms*1.4, color='k',         marker="o", label='')
ax.errorbar(ALLWISE_W1mjd-mjd_offset, ALLWISE_W1_AB, yerr=ALLWISE['w1sigmpro'], ms=ms,     color='peru',      marker="o", label='WISE W1')  #label='ALLWISE W1' 
ax.errorbar(ALLWISE_W2mjd-mjd_offset, ALLWISE_W2_AB, yerr=ALLWISE['w2sigmpro'], ms=ms,     color='orangered', marker="o", label='WISE W2')


## NEOWISE averages
ms=6.0
#ax.scatter((xx-mjd_offset)/one_plus_z, (yy_w1 + 2.699), s=ms*60.*1.8, color='k')
#ax.scatter((xx-mjd_offset)/one_plus_z, (yy_w2 + 3.339), s=ms*60.*1.8, color='k')
#ax.scatter((xx-mjd_offset)/one_plus_z, (yy_w1 + 2.699), s=ms*60.,     color='peru')
#ax.scatter((xx-mjd_offset)/one_plus_z, (yy_w2 + 3.339), s=ms*60.,     color='orangered')
ms=8.0
ax.errorbar((xx-mjd_offset)/one_plus_z, (yy_w1 + 2.699), yerr=yy_w1err, ms=ms*1.4,  color='k',         marker="o", label='')
ax.errorbar((xx-mjd_offset)/one_plus_z, (yy_w1 + 2.699), yerr=yy_w1err, ms=ms,      color='peru',      marker="o", label='')  # label='NEOWISE W1'
ax.errorbar((xx-mjd_offset)/one_plus_z, (yy_w2 + 3.339), yerr=yy_w2err, ms=ms*1.4,  color='k',         marker="o", label='')
ax.errorbar((xx-mjd_offset)/one_plus_z, (yy_w2 + 3.339), yerr=yy_w2err, ms=ms,      color='orangered', marker="o", label='')

## Plotting the SPECTRA as vertical lines
## Wu et al., 2015, Nature, 518, 512
lw = 5.0
plt.axvline(x=56655-mjd_offset, linewidth=lw, color='b')


ax.set_xlim((xmin, xmax))
#ax.set_xlim((xmin_rest, xmax_rest))
ax.set_ylim((ymin, ymax))
ax.tick_params('x', direction='in')
ax.tick_params('y', direction='in')

plt.xlabel('MJD-50000')
#plt.xlabel('Days in the rest-frame')
plt.ylabel('magnitude (AB)')

plt.legend(loc="lower right", ncol=1,
#plt.legend(loc="lower center", ncol=3, 
           shadow=True, fancybox=False,frameon=True, 
           fontsize=fontsize/2.)


plt.savefig('J0100_lc_temp.pdf', format='pdf')
plt.close(fig)

