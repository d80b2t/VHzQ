'''
A wavelength vs. wide-area survey filters plot.
For e.g. Pan-STARRS, UKIRT/UKIDSS, VISTA/VHS and WISE.

To reproduce something akin to the Spectral Bands plot at::
https://blog.backyardworlds.org/2018/04/24/guest-blog-post-by-peter-jalowiczor/

Filter curves from e.g.
http://www.mso.anu.edu.au/~brad/filters.html
'''

import matplotlib
import math
import numpy as np
import matplotlib.pyplot as plt

from matplotlib import colors as mcolors
from matplotlib import gridspec
from astropy.io import fits
from astropy.io import ascii
from astropy.table import Table


##
## READ-IN THE DATA FILE(S)
##

##
## FILTERS
path = '/cos_pc19a_npr/data/filter_curves/'

##     D E C a m
infile = 'DECam/DES_uband.dat'
table = path+infile
DES_uband      = ascii.read(table)
DES_uband_wave = DES_uband['wavelength']
DES_uband_thru = DES_uband['throughput']
infile = 'DECam/DES_gband.dat'
table = path+infile
DES_gband      = ascii.read(table)
DES_gband_wave = DES_gband['wavelength']
DES_gband_thru = DES_gband['throughput']
infile = 'DECam/DES_rband.dat'
table = path+infile
DES_rband      = ascii.read(table)
DES_rband_wave = DES_rband['wavelength']
DES_rband_thru = DES_rband['throughput']
infile = 'DECam/DES_iband.dat'
table = path+infile
DES_iband      = ascii.read(table)
DES_iband_wave = DES_iband['wavelength']
DES_iband_thru = DES_iband['throughput']
infile = 'DECam/DES_zband.dat'
table = path+infile
DES_zband      = ascii.read(table)
DES_zband_wave = DES_zband['wavelength']
DES_zband_thru = DES_zband['throughput']
infile = 'DECam/DES_Yband.dat'
table = path+infile
DES_Yband      = ascii.read(table)
DES_Yband_wave = DES_Yband['wavelength']
DES_Yband_thru = DES_Yband['throughput']

##   Pan-STARRS
infile = 'PanSTARRS/Tonry_2012_Table3.dat'
table = path+infile
PanSTARRS_bands = ascii.read(table)
PanSTARRS_wave = PanSTARRS_bands['Wave']
PanSTARRS_gp1 = PanSTARRS_bands['gp1']
PanSTARRS_rp1 = PanSTARRS_bands['rp1']
PanSTARRS_ip1 = PanSTARRS_bands['ip1']
PanSTARRS_zp1 = PanSTARRS_bands['zp1']
PanSTARRS_yp1 = PanSTARRS_bands['yp1']

##  CFHT
infile= 'CFHT_WIRCam/W_8105.dat'
table = path+infile
CFHT_Wband = ascii.read(table)
CFHT_Wband_wave = CFHT_Wband['col1']
CFHT_Wband_flux = CFHT_Wband['col2']


##  WFACM
infile = 'WFCAM/UKIRT_WFCAM.Y.dat'
table = path+infile
WFCAM_Yband      = ascii.read(table)
WFCAM_Yband_wave = WFCAM_Yband['wavelength']
WFCAM_Yband_thru = WFCAM_Yband['throughput']
infile = 'WFCAM/UKIRT_WFCAM.J.dat'
table = path+infile
WFCAM_Jband      = ascii.read(table)
WFCAM_Jband_wave = WFCAM_Yband['wavelength']
WFCAM_Jband_thru = WFCAM_Yband['throughput']
infile = 'WFCAM/UKIRT_WFCAM.H.dat'
table = path+infile
WFCAM_Hband      = ascii.read(table)
WFCAM_Hband_wave = WFCAM_Hband['wavelength']
WFCAM_Hband_thru = WFCAM_Hband['throughput']
infile = 'WFCAM/UKIRT_WFCAM.K.dat'
table = path+infile
WFCAM_Kband      = ascii.read(table)
WFCAM_Kband_wave = WFCAM_Kband['wavelength']
WFCAM_Kband_thru = WFCAM_Kband['throughput']


##      UKIRT
infile = 'UKIRT/UKIRT_Z.dat'
table = path+infile
UKIRT_Zband      = ascii.read(table)
UKIRT_Zband_wave = UKIRT_Zband['wavelength']
UKIRT_Zband_thru = UKIRT_Zband['throughput']
infile = 'UKIRT/UKIRT_Y.dat'
table = path+infile
UKIRT_Yband      = ascii.read(table)
UKIRT_Yband_wave = UKIRT_Yband['wavelength']
UKIRT_Yband_thru = UKIRT_Yband['throughput']
infile = 'UKIRT/UKIRT_J.dat'
table = path+infile
UKIRT_Jband      = ascii.read(table)
UKIRT_Jband_wave = UKIRT_Jband['wavelength']
UKIRT_Jband_thru = UKIRT_Jband['throughput']
infile = 'UKIRT/UKIRT_H.dat'
table = path+infile
UKIRT_Hband      = ascii.read(table)
UKIRT_Hband_wave = UKIRT_Hband['wavelength']
UKIRT_Hband_thru = UKIRT_Hband['throughput']
infile = 'UKIRT/UKIRT_K.dat'
table = path+infile
UKIRT_Kband      = ascii.read(table)
UKIRT_Kband_wave = UKIRT_Kband['wavelength']
UKIRT_Kband_thru = UKIRT_Kband['throughput']

##     2MASS
infile = '2MASS/2MASS_Ks.dat'
table = path+infile
TwoMASS_Ksband      = ascii.read(table)
TwoMASS_Ksband_wave = TwoMASS_Ksband['wavelength']
TwoMASS_Ksband_thru = TwoMASS_Ksband['throughput']


##     WISE
infile = 'WISE/RSR-W1.txt'
table = path+infile
W1_band      = ascii.read(table)
W1_band_wave = W1_band['W1']
W1_band_thru = W1_band['RSR']
infile = 'WISE/RSR-W2.txt'
table = path+infile
W2_band      = ascii.read(table)
W2_band_wave = W2_band['W2']
W2_band_thru = W2_band['RSR']
infile = 'WISE/RSR-W3.txt'
table = path+infile
W3_band      = ascii.read(table)
W3_band_wave = W3_band['W3']
W3_band_thru = W3_band['RSR']
infile = 'WISE/RSR-W4.txt'
table = path+infile
W4_band      = ascii.read(table)
W4_band_wave = W4_band['W4']
W4_band_thru = W4_band['RSR']

## 
## Composite quasar spectra
##
## The Vanden Berk et al. (2001) composite
path = '/cos_pc19a_npr/data/SDSS/VdB01/'
infile = 'Vanden_Berk_2001_Table1.dat'
table = path+infile
VdB01_comp = ascii.read(table)
VdB01_wave = VdB01_comp['Wavelength']
VdB01_flux = VdB01_comp['Flux']

## The Banados_2016_Table6 composite
path = '/cos_pc19a_npr/data/highest_z_QSOs/Banados_Tables/'
infile = 'Banados_2016_Table6.dat'
table = path+infile
Banados_2016_full   = ascii.read(table)
Banados_wave        = Banados_2016_full['Wavelength']
Banados_comp_flux   = Banados_2016_full['Flux_comp']
Banados_strong_flux = Banados_2016_full['Flux_strong']
Banados_weak_flux   = Banados_2016_full['Flux_weak']
##
path = '/cos_pc19a_npr/data/Glikman2006/'
infile = 'Glikman_2006_ApJ_Table3.dat'
table = path+infile
Glikman_comp = ascii.read(table)
Glik_wave = Glikman_comp['Wavelength']
Glik_flux = Glikman_comp['Flux']
Glik_flux = Glik_flux/Glik_flux.max()


##
## Making the plot...
##
plt.rcParams.update({'font.size': 14})
#fig = plt.figure(figsize=(14, 7))
fig, ax = plt.subplots(figsize=(10, 5))

xmin =   1000.    ## Angstroms
xmax =   2000.    ## Angstroms

ymin =   0.00
ymax =   1.30

#ax.set_xscale('log')
#ax.set_yscale('log')
## if log, then...
#ymin =   0.001
#ymax =   2.30
ax.set_xlim([xmin,xmax])
ax.set_ylim([ymin, ymax])

alpha           = 0.5
fontsize        = 16
labelsize       = fontsize
tickwidth       = 2.0
linewidth       = 2.4
ticklabelsize   = labelsize
majorticklength = 12
minorticklength = 6

## filter   lambda_eff  lambda_min  lambda_max  Weff
## J_WFCAM  12483       11690       13280       1590

#redshift_range = (np.arange(5)*.15)+6.57
redshift_range = (np.arange(4)*.25)+6.40

    
for ii in range(len(redshift_range)):
    ## Pan-STARRS
    #ax.plot( (PanSTARRS_wave/(1+redshift_range[ii])),  (PanSTARRS_gp1/PanSTARRS_gp1.max()), color='darkviolet',     alpha=alpha, linewidth=linewidth)
    #ax.fill( (PanSTARRS_wave/(1+redshift_range[ii])),  (PanSTARRS_gp1/PanSTARRS_gp1.max()), color='darkviolet',     alpha=alpha/2)
    #ax.plot( (PanSTARRS_wave/(1+redshift_range[ii])),  (PanSTARRS_rp1/PanSTARRS_rp1.max()), color='slateblue',      alpha=alpha, linewidth=linewidth)
    #ax.fill( (PanSTARRS_wave/(1+redshift_range[ii])),  (PanSTARRS_rp1/PanSTARRS_rp1.max()), color='slateblue',      alpha=alpha/2)
    #ax.plot( (PanSTARRS_wave/(1+redshift_range[ii])),  (PanSTARRS_ip1/PanSTARRS_ip1.max()), color='dodgerblue',     alpha=alpha, linewidth=linewidth)
    #ax.fill( (PanSTARRS_wave/(1+redshift_range[ii])),  (PanSTARRS_ip1/PanSTARRS_ip1.max()), color='dodgerblue',     alpha=alpha/2)
    #ax.plot( (PanSTARRS_wave/(1+redshift_range[ii])),  (PanSTARRS_zp1/PanSTARRS_zp1.max()), color='skyblue',        alpha=alpha, linewidth=linewidth)
    #ax.fill( (PanSTARRS_wave/(1+redshift_range[ii])),  (PanSTARRS_zp1/PanSTARRS_zp1.max()), color='skyblue',        alpha=alpha/2)
    #ax.plot( (PanSTARRS_wave/(1+redshift_range[ii])),  (PanSTARRS_yp1/PanSTARRS_yp1.max()), color='mediumturquoise',alpha=alpha, linewidth=linewidth)
    #ax.fill( (PanSTARRS_wave/(1+redshift_range[ii])),  (PanSTARRS_yp1/PanSTARRS_yp1.max()), color='mediumturquoise', alpha=alpha/2)
    
    #plt.text(0.460, 1.1, r'g', color ='darkviolet', fontsize=fontsize)
    #plt.text(0.570, 1.1, r'r', color ='slateblue', fontsize=fontsize)
    #plt.text(0.700, 1.1, r'i', color ='dodgerblue', fontsize=fontsize)
    #plt.text(0.800, 1.1, r'z', color ='skyblue', fontsize=fontsize)
    #plt.text(0.900, 1.1, r'y', color ='mediumturquoise', fontsize=fontsize)
    
    ## UKIRT
    #ax.plot( (UKIRT_Zband_wave/(1+redshift_range[ii])),  (UKIRT_Zband_thru/UKIRT_Zband_thru.max()), color='olive',         alpha=alpha, linewidth=linewidth)
    #ax.fill( (UKIRT_Zband_wave/(1+redshift_range[ii])),  (UKIRT_Zband_thru/UKIRT_Zband_thru.max()), color='olive',         alpha=alpha/2)
    ax.plot( (UKIRT_Yband_wave/(1+redshift_range[ii])),  (UKIRT_Yband_thru/UKIRT_Yband_thru.max()), color='darkgoldenrod', alpha=alpha, linewidth=linewidth)
    #ax.fill( (UKIRT_Yband_wave/(1+redshift_range[ii])),  (UKIRT_Yband_thru/UKIRT_Yband_thru.max()), color='darkgoldenrod', alpha=alpha/2)
    #ax.plot( (UKIRT_Jband_wave/(1+redshift_range[ii])),  (UKIRT_Jband_thru/UKIRT_Jband_thru.max()), color='orange',  alpha=alpha, linewidth=linewidth)
  #  ax.fill( (UKIRT_Jband_wave/(1+redshift_range[ii])),  (UKIRT_Jband_thru/UKIRT_Jband_thru.max()), color='orange',  alpha=alpha/2)
    #ax.plot( (UKIRT_Hband_wave/(1+redshift_range[ii])),  (UKIRT_Hband_thru/UKIRT_Hband_thru.max()), color='gold',          alpha=alpha, linewidth=linewidth)
    #ax.fill( (UKIRT_Hband_wave/(1+redshift_range[ii])),  (UKIRT_Hband_thru/UKIRT_Hband_thru.max()), color='gold',          alpha=alpha/2)
    #ax.plot( (UKIRT_Kband_wave/(1+redshift_range[ii])),  (UKIRT_Kband_thru/UKIRT_Kband_thru.max()), color='yellow',        alpha=alpha, linewidth=linewidth)
    #ax.fill( (UKIRT_Kband_wave/(1+redshift_range[ii])),  (UKIRT_Kband_thru/UKIRT_Kband_thru.max()), color='yellow',        alpha=alpha/2)

    ## WFCAM
    #ax.plot( (WFCAM_Jband_wave/(1+redshift_range[ii])),  (WFCAM_Jband_thru/WFCAM_Jband_thru.max()), color='orange',  alpha=alpha, linewidth=linewidth)
    ax.fill( (WFCAM_Jband_wave/(1+redshift_range[ii])),  (WFCAM_Jband_thru/WFCAM_Jband_thru.max()), color='orange',  alpha=alpha)

    
#plt.text(0.870, 1.1, r'Z', color ='olive', fontsize=fontsize)
#plt.text(1.000, 1.1, r'Y', color ='darkgoldenrod', fontsize=fontsize)
plt.text(1.280, 1.1, r'J', color ='orange', fontsize=fontsize)
plt.text(1.600, 1.1, r'H', color ='gold',   fontsize=fontsize)
#plt.text(2.020, 1.1, r'K', color ='k',      fontsize=fontsize*1.2)
plt.text(2.020, 1.1, r'K', color ='yellow', fontsize=fontsize)

## 2MASS
#ax.plot( (TwoMASS_Ksband_wave/10000.), (TwoMASS_Ksband_thru/TwoMASS_Ksband_thru.max()), color='khaki', alpha=alpha, linewidth=linewidth, linestyle='-')
#ax.fill( (TwoMASS_Ksband_wave/10000.), (TwoMASS_Ksband_thru/TwoMASS_Ksband_thru.max()), color='khaki', alpha=alpha/2.)
#plt.text(2.200, 1.1, r'K$_{s}$', color ='khaki', fontsize=fontsize)

## WISE
#ax.plot( (W1_band_wave),  (W1_band_thru/W1_band_thru.max()), color='peru',      alpha=0.85, linewidth=linewidth)
#ax.fill( (W1_band_wave),  (W1_band_thru/W1_band_thru.max()), color='peru',      alpha=alpha/2)
#ax.plot( (W2_band_wave),  (W2_band_thru/W2_band_thru.max()), color='orangered', alpha=0.85, linewidth=linewidth)
#ax.fill( (W2_band_wave),  (W2_band_thru/W2_band_thru.max()), color='orangered', alpha=alpha/2)
#ax.plot( (W3_band_wave),  (W3_band_thru/W3_band_thru.max()), color='red',       alpha=0.85, linewidth=linewidth)
#ax.fill( (W3_band_wave),  (W3_band_thru/W3_band_thru.max()), color='red',       alpha=alpha/2)
#ax.plot( (W4_band_wave),  (W4_band_thru/W4_band_thru.max()), color='darkred',   alpha=0.85, linewidth=linewidth)
#ax.fill( (W4_band_wave),  (W4_band_thru/W4_band_thru.max()), color='darkred',   alpha=alpha/2)
#plt.text( 3.280, 1.1, r'W1', color ='peru',      fontsize=fontsize)
#plt.text( 4.200, 1.1, r'W2', color ='orangered', fontsize=fontsize)
#plt.text(10.120, 1.1, r'W3', color ='red',       fontsize=fontsize)
#plt.text(19.120, 1.1, r'W4', color ='darkred',   fontsize=fontsize)


##
## QSO template
##
## len(Banados_comp_flux)) = 960.

## VdB01 is every 1.0Ang; Banados is every 0.5Ang.
## Therefore need every *second* line of Banados to match VdB01
quasar_template_flux          = VdB01_flux/2.6
quasar_template_flux[200:680] = (Banados_comp_flux[::2]*3.4)
quasar_template_flux[0:199]   = 0.0

VdB01_flux           = VdB01_flux           / VdB01_flux.max()
quasar_template_flux = quasar_template_flux / quasar_template_flux.max()
Banados_comp_flux    = Banados_comp_flux    / Banados_comp_flux.max()
Banados_strong_flux  = Banados_strong_flux  / Banados_strong_flux.max()
Banados_weak_flux    = Banados_weak_flux    / Banados_weak_flux.max()

#ax.plot(VdB01_wave,   quasar_template_flux, color='k',alpha=1.0, linewidth=linewidth)
ax.plot(VdB01_wave,   VdB01_flux, color='k',alpha=1.0, linewidth=linewidth)
ax.plot(Banados_wave, Banados_comp_flux,    color='b', alpha=0.85)
#ax.plot(Glik_wave     Glik_flux,            color='dimgray', alpha=1.0, linewidth=linewidth/2)
#ax.plot(VdB01_wave    VdB01_flux,           color='g',alpha=0.85)
#ax.plot(Banados_wave  Banados_strong_flux,  color='b', alpha=0.85)
#ax.plot(Banados_wave  Banados_weak_flux,    color='b', alpha=0.85)

font = {'color': 'k',     'weight': 'normal', 'size':  20, }
##plt.text( 5.5, (ymax*0.72), r'z='+str(redshift)+' quasar', fontdict=font)

## "Somehow", these three lines convert the
## 10^-1, 10^0 and 10^1 x-axis lables to 0.1, 1, 10...
from matplotlib.ticker import ScalarFormatter
for axis in [ax.xaxis, ax.yaxis]:
    axis.set_major_formatter(ScalarFormatter())

ax.set_xlabel(r"Wavelength / Angstrom", fontsize=fontsize)
ax.set_ylabel("Normalised Transmission", fontsize=fontsize)
ax.tick_params(axis='both', which='major', labelsize=fontsize)

plt.savefig('filters_for_M1450_temp.png', format='png')
##plt.savefig('filters_for_M1450_temp.pdf', format='pdf')
plt.close(fig)
#plt.show()


