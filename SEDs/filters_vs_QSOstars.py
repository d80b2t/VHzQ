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
##   READ-IN THE DATA FILE(S)
##

##
##   FILTERS
path = '/cos_pc19a_npr/data/filter_curves/'

##   D E C a m
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

##     Pan-STARRS
infile = 'PanSTARRS/Tonry_2012_Table3.dat'
table = path+infile
PanSTARRS_bands = ascii.read(table)
PanSTARRS_wave = PanSTARRS_bands['Wave']
PanSTARRS_gp1 = PanSTARRS_bands['gp1']
PanSTARRS_rp1 = PanSTARRS_bands['rp1']
PanSTARRS_ip1 = PanSTARRS_bands['ip1']
PanSTARRS_zp1 = PanSTARRS_bands['zp1']
PanSTARRS_yp1 = PanSTARRS_bands['yp1']

## CFHT
infile= 'CFHT_WIRCam/W_8105.dat'
table = path+infile
CFHT_Wband = ascii.read(table)
CFHT_Wband_wave = CFHT_Wband['col1']
CFHT_Wband_flux = CFHT_Wband['col2']

##     2MASS
infile = '2MASS/2MASS_Ks.dat'
table = path+infile
TwoMASS_Ksband      = ascii.read(table)
TwoMASS_Ksband_wave = TwoMASS_Ksband['wavelength']
TwoMASS_Ksband_thru = TwoMASS_Ksband['throughput']

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


##  VIRCAM/VISTA  
infile = 'VIRCAM/Paranal_VISTA.Z.dat'
table = path+infile
VISTA_Zband      = ascii.read(table)
VISTA_Zband_wave = VISTA_Zband['wavelength']
VISTA_Zband_thru = VISTA_Zband['throughput']
infile = 'VIRCAM/Paranal_VISTA.Y.dat'
table = path+infile
VISTA_Yband      = ascii.read(table)
VISTA_Yband_wave = VISTA_Yband['wavelength']
VISTA_Yband_thru = VISTA_Yband['throughput']
infile = 'VIRCAM/Paranal_VISTA.J.dat'
table = path+infile
VISTA_Jband      = ascii.read(table)
VISTA_Jband_wave = VISTA_Jband['wavelength']
VISTA_Jband_thru = VISTA_Jband['throughput']
infile = 'VIRCAM/Paranal_VISTA.H.dat'
table = path+infile
VISTA_Hband      = ascii.read(table)
VISTA_Hband_wave = VISTA_Hband['wavelength']
VISTA_Hband_thru = VISTA_Hband['throughput']
infile = 'VIRCAM/Paranal_VISTA.Ks.dat'
table = path+infile
VISTA_Ksband      = ascii.read(table)
VISTA_Ksband_wave = VISTA_Ksband['wavelength']
VISTA_Ksband_thru = VISTA_Ksband['throughput']

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
##  Composite quasar spectra
##
## The Vanden Berk et al. (2001) composite
path = '/cos_pc19a_npr/data/SDSS/VdB01/'
infile = 'Vanden_Berk_2001_Table1.dat'
table = path+infile
VdB01_comp = ascii.read(table)
VdB01_wave = VdB01_comp['Wavelength']
VdB01_flux = VdB01_comp['Flux']

## The Banados et al. (2016) Table 6 composite
path = '/cos_pc19a_npr/data/highest_z_QSOs/Banados_Tables/'
infile = 'Banados_2016_Table6.dat'
table = path+infile
Banados_2016_full   = ascii.read(table)
Banados_wave        = Banados_2016_full['Wavelength']
Banados_comp_flux   = Banados_2016_full['Flux_comp']
Banados_strong_flux = Banados_2016_full['Flux_strong']
Banados_weak_flux   = Banados_2016_full['Flux_weak']

## Glikman et al. (2006) Red/NIR composite
path = '/cos_pc19a_npr/data/Glikman2006/'
infile = 'Glikman_2006_ApJ_Table3.dat'
table = path+infile
Glikman_comp = ascii.read(table)
Glik_wave = Glikman_comp['Wavelength']
Glik_flux = Glikman_comp['Flux']
Glik_flux = Glik_flux/Glik_flux.max()

##
##  L/T dwarf spectra; Cushing et al. (2008; ApJ, 678, 1372)
##
## 2MASS 1439+1929 (L1), 2MASS 0036+1821 (L3.5), 2MASS 1507-1627 (L5),
## DENIS 0255-4700 (L8), SDSS 1254-0122 (T2), and 2MASS 0559-1404 (T4.5) 
path = '/cos_pc19a_npr/data/MLandT_dwarfs/Cushing_2008/'

infile = '2MASS1439_L1.dat'
table = path+infile
L1_2MASS_1439 = ascii.read(table)
L1_wave = L1_2MASS_1439['wavelength']
L1_flux = L1_2MASS_1439['flux']

infile = '2MASS0036_L3pnt5.dat'
table = path+infile
L3pnt5_2MASS_0036 = ascii.read(table)
L3pnt5_wave = L3pnt5_2MASS_0036['wavelength']
L3pnt5_flux = L3pnt5_2MASS_0036['flux']

infile = '2MASS1507_L5.dat'
table = path+infile
L5_2MASS_1507 = ascii.read(table)
L5_wave = L5_2MASS_1507['wavelength']
L5_flux = L5_2MASS_1507['flux']

infile = 'DENIS0255_L8.dat'
table = path+infile
L8_DENIS_0255 = ascii.read(table)
L8_wave = L8_DENIS_0255['wavelength']
L8_flux = L8_DENIS_0255['flux']

infile = 'SDSS1254_T2.dat'
table = path+infile
T2_SDSS_1254 = ascii.read(table)
T2_wave = T2_SDSS_1254['wavelength']
T2_flux = T2_SDSS_1254['flux']

infile = '2MASS0559_T4pnt5.dat'
table = path+infile
T4pnt5_2MASS_0559 = ascii.read(table)
T4pnt5_wave = T4pnt5_2MASS_0559['wavelength']
T4pnt5_flux = T4pnt5_2MASS_0559['flux']


plot_DECam     = 'N'
plot_PanSTARRS = 'N' 
plot_UKIRT     = 'N'
plot_VISTA     = 'y'
plot_WISE      = 'y'

print()
print('plot_DECam     = ', plot_DECam)
print('plot_PanSTARRS = ', plot_PanSTARRS)
print('plot_UKIRT     = ', plot_UKIRT)
print('plot_VISTA     = ', plot_VISTA)
print('plot_WISE      = ', plot_WISE)
print()

##
## Making the plot...
##
plt.rcParams.update({'font.size': 14})
#fig = plt.figure(figsize=(14, 7))
fig, ax = plt.subplots(figsize=(16, 7))

ax.set_xscale('log')
#ax.set_yscale('log')

#xmin =   0.38   ## in um, starting with g-band
#xmin =   0.52   ## in um, starting with r-band
#xmin =   0.72   ## in um, starting with Z-band
xmin =   0.77   ## in um, starting with Z-band

xmax =  2.6    ## with K/Ks-band
#xmax =  5.5    ## with WISE W2
#xmax = 18.5    ## with WISE W3
#xmax = 28.00    ## with WISE W4

ymin =  0.00
ymax =  1.30
#ymin = 0.001   ## for y-log,
#ymax = 2.30    ## for y-log
ax.set_xlim([xmin,xmax])
ax.set_ylim([ymin, ymax])

## Some NPR plotting defaults 
alpha           = 1.0
fontsize        = 22
linewidth       = 2.4
labelsize       = 18
tickwidth       = 2.0
ticklabelsize   = labelsize
majorticklength = 12
minorticklength = 6


##
## Named colors from::
##    https://matplotlib.org/examples/color/named_colors.html
##
## FILTERS
##
if plot_DECam == 'y':
    ##   D E C a m
    ax.plot( (DES_gband_wave/10000.),  (DES_gband_thru/100.), color='violet',         alpha=alpha, linewidth=linewidth)
    ax.plot( (DES_rband_wave/10000.),  (DES_rband_thru/100.), color='indigo',         alpha=alpha, linewidth=linewidth)
    ax.plot( (DES_iband_wave/10000.),  (DES_iband_thru/100.), color='royalblue',      alpha=alpha, linewidth=linewidth)
    ax.plot( (DES_zband_wave/10000.),  (DES_zband_thru/100.), color='deepskyblue',    alpha=alpha, linewidth=linewidth)
    ax.plot( (DES_Yband_wave/10000.),  (DES_Yband_thru/100.), color='paleturquoise',  alpha=alpha, linewidth=linewidth)
    ax.fill( (DES_gband_wave/10000.),  (DES_gband_thru/100.), color='violet',         alpha=alpha/2)
    ax.fill( (DES_rband_wave/10000.),  (DES_rband_thru/100.), color='indigo',         alpha=alpha/2)
    ax.fill( (DES_iband_wave/10000.),  (DES_iband_thru/100.), color='royalblue',      alpha=alpha/2)
    ax.fill( (DES_zband_wave/10000.),  (DES_zband_thru/100.), color='deepskyblue',    alpha=alpha/2)
    ax.fill( (DES_Yband_wave/10000.),  (DES_Yband_thru/100.), color='paleturquoise',  alpha=alpha/2)

if plot_PanSTARRS == 'y':
    ## Pan-STARRS
    ax.plot( (PanSTARRS_wave/1000.),  (PanSTARRS_gp1/PanSTARRS_gp1.max()), color='darkviolet',      alpha=alpha, linewidth=linewidth)
    ax.fill( (PanSTARRS_wave/1000.),  (PanSTARRS_gp1/PanSTARRS_gp1.max()), color='darkviolet',      alpha=alpha/2)
    ax.plot( (PanSTARRS_wave/1000.),  (PanSTARRS_rp1/PanSTARRS_rp1.max()), color='slateblue',      alpha=alpha, linewidth=linewidth)
    ax.fill( (PanSTARRS_wave/1000.),  (PanSTARRS_rp1/PanSTARRS_rp1.max()), color='slateblue',      alpha=alpha/2)
    ax.plot( (PanSTARRS_wave/1000.),  (PanSTARRS_ip1/PanSTARRS_ip1.max()), color='dodgerblue',      alpha=alpha, linewidth=linewidth)
    ax.fill( (PanSTARRS_wave/1000.),  (PanSTARRS_ip1/PanSTARRS_ip1.max()), color='dodgerblue',      alpha=alpha/2)
    ax.plot( (PanSTARRS_wave/1000.),  (PanSTARRS_zp1/PanSTARRS_zp1.max()), color='skyblue',         alpha=alpha, linewidth=linewidth)
    ax.fill( (PanSTARRS_wave/1000.),  (PanSTARRS_zp1/PanSTARRS_zp1.max()), color='skyblue',         alpha=alpha/2)
    ax.plot( (PanSTARRS_wave/1000.),  (PanSTARRS_yp1/PanSTARRS_yp1.max()), color='mediumturquoise', alpha=alpha, linewidth=linewidth)
    ax.fill( (PanSTARRS_wave/1000.),  (PanSTARRS_yp1/PanSTARRS_yp1.max()), color='mediumturquoise', alpha=alpha/2)

    ## for xmin=0.38
    plt.text(0.460, 1.1, r'g', color ='darkviolet',      fontsize=fontsize)
    plt.text(0.570, 1.1, r'r', color ='slateblue',       fontsize=fontsize)
    plt.text(0.700, 1.1, r'i', color ='dodgerblue',      fontsize=fontsize)
    plt.text(0.800, 1.1, r'z', color ='skyblue',         fontsize=fontsize)
    plt.text(0.900, 1.1, r'y', color ='mediumturquoise', fontsize=fontsize)

## for xmin=0.52
#plt.text(0.590, 1.1, r'r', color ='slateblue',       fontsize=fontsize, style='italic', weight='bold')
#plt.text(0.710, 1.1, r'i', color ='dodgerblue',      fontsize=fontsize, style='italic', weight='bold')
#plt.text(0.840, 1.1, r'z', color ='skyblue',         fontsize=fontsize, style='italic', weight='bold')
#plt.text(0.910, 1.1, r'y', color ='mediumturquoise', fontsize=fontsize, style='italic', weight='bold')

## CFHT
#ax.plot( (CFHT_Wband_wave/1000.),  (CFHT_Wband_flux/CFHT_Wband_flux.max()), color='silver',   alpha=alpha, linewidth=linewidth)
#ax.fill( (CFHT_Wband_wave/1000.),  (CFHT_Wband_flux/CFHT_Wband_flux.max()), color='silver',   alpha=alpha/2)
#plt.text(1.400, 1.1, r'W', color ='silver', fontsize=fontsize)

if plot_UKIRT== 'y':
    ##  UKIRT
    ax.plot( (UKIRT_Zband_wave/10000.),  (UKIRT_Zband_thru/UKIRT_Zband_thru.max()), color='olive',         alpha=alpha, linewidth=linewidth)
    ax.fill( (UKIRT_Zband_wave/10000.),  (UKIRT_Zband_thru/UKIRT_Zband_thru.max()), color='olive',         alpha=alpha/2)
    ax.plot( (UKIRT_Yband_wave/10000.),  (UKIRT_Yband_thru/UKIRT_Yband_thru.max()), color='darkgoldenrod', alpha=alpha, linewidth=linewidth)
    ax.fill( (UKIRT_Yband_wave/10000.),  (UKIRT_Yband_thru/UKIRT_Yband_thru.max()), color='darkgoldenrod', alpha=alpha/2)
    ax.plot( (UKIRT_Jband_wave/10000.),  (UKIRT_Jband_thru/UKIRT_Jband_thru.max()), color='orange',        alpha=alpha, linewidth=linewidth)
    ax.fill( (UKIRT_Jband_wave/10000.),  (UKIRT_Jband_thru/UKIRT_Jband_thru.max()), color='orange',        alpha=alpha/2)
    ax.plot( (UKIRT_Hband_wave/10000.),  (UKIRT_Hband_thru/UKIRT_Hband_thru.max()), color='gold',          alpha=alpha, linewidth=linewidth)
    ax.fill( (UKIRT_Hband_wave/10000.),  (UKIRT_Hband_thru/UKIRT_Hband_thru.max()), color='gold',          alpha=alpha/2)
    ax.plot( (UKIRT_Kband_wave/10000.),  (UKIRT_Kband_thru/UKIRT_Kband_thru.max()), color='yellow',        alpha=alpha, linewidth=linewidth)
    ax.fill( (UKIRT_Kband_wave/10000.),  (UKIRT_Kband_thru/UKIRT_Kband_thru.max()), color='yellow',        alpha=alpha/2)
    
    plt.text(0.870, 1.1, r'Z', color ='olive',        fontsize=fontsize,     weight='bold')
    plt.text(1.000, 1.1, r'Y', color ='darkgoldenrod', fontsize=fontsize,     weight='bold')
    plt.text(1.280, 1.1, r'J', color ='orange',        fontsize=fontsize,     weight='bold')
    plt.text(1.600, 1.1, r'H', color ='gold',          fontsize=fontsize,     weight='bold')
    #plt.text(2.020, 1.1, r'K', color ='k',            fontsize=fontsize*1.2, weight='bold')
    plt.text(2.020, 1.1, r'K', color ='yellow',        fontsize=fontsize,     weight='bold')

if plot_VISTA == 'y':
    ##  VISTA
    ax.plot( (VISTA_Zband_wave/10000.), (VISTA_Zband_thru/VISTA_Zband_thru.max()), color='olive',         alpha=alpha, linewidth=linewidth)
    ax.fill( (VISTA_Zband_wave/10000.), (VISTA_Zband_thru/VISTA_Zband_thru.max()), color='olive',         alpha=alpha/2)
    ax.plot( (VISTA_Yband_wave/10000.), (VISTA_Yband_thru/VISTA_Yband_thru.max()), color='darkgoldenrod', alpha=alpha, linewidth=linewidth)
    ax.fill( (VISTA_Yband_wave/10000.), (VISTA_Yband_thru/VISTA_Yband_thru.max()), color='darkgoldenrod', alpha=alpha/2)
    ax.plot( (VISTA_Jband_wave/10000.), (VISTA_Jband_thru/VISTA_Jband_thru.max()), color='orange',        alpha=alpha, linewidth=linewidth)
    ax.fill( (VISTA_Jband_wave/10000.), (VISTA_Jband_thru/VISTA_Jband_thru.max()), color='orange',        alpha=alpha/2)
    ax.plot( (VISTA_Hband_wave/10000.), (VISTA_Hband_thru/VISTA_Hband_thru.max()), color='gold',          alpha=alpha, linewidth=linewidth)
    ax.fill( (VISTA_Hband_wave/10000.), (VISTA_Hband_thru/VISTA_Hband_thru.max()), color='gold',          alpha=alpha/2)
    ax.plot( (VISTA_Ksband_wave/10000.), (VISTA_Ksband_thru/VISTA_Ksband_thru.max()), color='yellow',        alpha=alpha, linewidth=linewidth)
    ax.fill( (VISTA_Ksband_wave/10000.), (VISTA_Ksband_thru/VISTA_Ksband_thru.max()), color='yellow',        alpha=alpha/2)

    plt.text(0.870, 1.1, r'Z', color ='olive',        fontsize=fontsize,     weight='bold')
    plt.text(1.000, 1.1, r'Y', color ='darkgoldenrod', fontsize=fontsize,     weight='bold')
    plt.text(1.280, 1.1, r'J', color ='orange',        fontsize=fontsize,     weight='bold')
    plt.text(1.600, 1.1, r'H', color ='gold',          fontsize=fontsize,     weight='bold')
    #plt.text(2.020, 1.1, r'K', color ='k',            fontsize=fontsize*1.2, weight='bold')
    plt.text(2.020, 1.1, r'Ks', color ='yellow',        fontsize=fontsize,     weight='bold')

## 2MASS
#ax.plot( (TwoMASS_Ksband_wave/10000.), (TwoMASS_Ksband_thru/TwoMASS_Ksband_thru.max()), color='khaki', alpha=alpha, linewidth=linewidth, linestyle='-')
#ax.fill( (TwoMASS_Ksband_wave/10000.), (TwoMASS_Ksband_thru/TwoMASS_Ksband_thru.max()), color='khaki', alpha=alpha/2.)
#
#plt.text(2.200, 1.1, r'K$_{s}$', color ='khaki', fontsize=fontsize, style='italic', weight='bold')

## WISE
if plot_WISE  == 'y': 
    ax.plot( (W1_band_wave),  (W1_band_thru/W1_band_thru.max()), color='peru',      alpha=0.85, linewidth=linewidth)
    ax.fill( (W1_band_wave),  (W1_band_thru/W1_band_thru.max()), color='peru',      alpha=alpha/2)
    ax.plot( (W2_band_wave),  (W2_band_thru/W2_band_thru.max()), color='orangered', alpha=0.85, linewidth=linewidth)
    ax.fill( (W2_band_wave),  (W2_band_thru/W2_band_thru.max()), color='orangered', alpha=alpha/2)
    ax.plot( (W3_band_wave),  (W3_band_thru/W3_band_thru.max()), color='red',       alpha=0.85, linewidth=linewidth)
    ax.fill( (W3_band_wave),  (W3_band_thru/W3_band_thru.max()), color='red',       alpha=alpha/2)
    ax.plot( (W4_band_wave),  (W4_band_thru/W4_band_thru.max()), color='darkred',   alpha=0.85, linewidth=linewidth)
    ax.fill( (W4_band_wave),  (W4_band_thru/W4_band_thru.max()), color='darkred',   alpha=alpha/2)
    
    plt.text( 3.280, 1.1, r'W1', color ='peru',      fontsize=fontsize, weight='bold')
    plt.text( 4.200, 1.1, r'W2', color ='orangered', fontsize=fontsize, weight='bold')
    plt.text(10.120, 1.1, r'W3', color ='red',       fontsize=fontsize, weight='bold')
    plt.text(19.120, 1.1, r'W4', color ='darkred',   fontsize=fontsize, weight='bold')
    

##
## L/T spectra
##
L1_flux = L1_flux/ np.nanmax(L1_flux)
#ax.plot(L1_wave[0::5],  L1_flux[0::5], color='r', alpha=1.0, linewidth=linewidth/2.)
ax.plot(L1_wave[0::20],  L1_flux[0::20], color='r', alpha=1.0, linewidth=linewidth, linestyle='--')

L3pnt5_flux = L3pnt5_flux/ np.nanmax(L3pnt5_flux)
##ax.plot(L3pnt5_wave,  L3pnt5_flux, color='firebrick', alpha=1.0, linewidth=linewidth/10.)
#ax.plot(L3pnt5_wave[0::20],  L3pnt5_flux[0::20], color='indianred', alpha=1.0, linewidth=linewidth)

L5_flux = L5_flux/ np.nanmax(L5_flux)
##ax.plot(L5_wave,        L5_flux, color='maroon', alpha=1.0, linewidth=linewidth/10.)
#ax.plot(L5_wave[0::20], L5_flux[0::20], color='firebrick', alpha=1.0, linewidth=linewidth)

L8_flux = L8_flux/ np.nanmax(L8_flux)
##ax.plot(L8_wave,        L8_flux, color='maroon', alpha=1.0, linewidth=linewidth/10.)
#ax.plot(L8_wave[0::20], L8_flux[0::20], color='maroon', alpha=1.0, linewidth=linewidth)

## T's... 
T2_flux = T2_flux/ np.nanmax(T2_flux)
##ax.plot(T2_wave,  T2_flux, color='brown', alpha=1.0, linewidth=linewidth/10.)
#ax.plot(T2_wave[0::20],  T2_flux[0::20], color='darkred', alpha=1.0, linewidth=linewidth)

T4pnt5_flux = T4pnt5_flux/ np.nanmax(T4pnt5_flux)
##ax.plot(T2_wave,  T2_flux, color='brown', alpha=1.0, linewidth=linewidth/10.)
ax.plot(T4pnt5_wave[0::20],  T4pnt5_flux[0::20], color='brown', alpha=1.0, linewidth=linewidth)


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

## Plot a redshifted quasar spectrum
print()
#redshift_in = float(input("What redshift is the quasar? "))
redshift_in = 6.7
redshift = redshift_in

ax.plot( ((VdB01_wave/10000.)*(1.0+redshift)),  (quasar_template_flux), color='k',alpha=1.0, linewidth=linewidth)
#ax.plot( ((Banados_wave/10000.)*(1.0+redshift)), (Banados_comp_flux), color='b', alpha=0.85)
##ax.plot( ((Glik_wave/10000.0)*(1.0+redshift)),  (Glik_flux), color='dimgray', alpha=1.0, linewidth=linewidth/2)
##ax.plot( ((VdB01_wave/10000.)*(1.0+redshift)),  (VdB01_flux), color='g',alpha=0.85)
##ax.plot( ((Banados_wave/10000.)*(1.0+redshift)), (Banados_strong_flux), color='b', alpha=0.85)
##ax.plot( ((Banados_wave/10000.)*(1.0+redshift)), (Banados_weak_flux), color='b', alpha=0.85)


## Labels
#size=18   ## 18 if between K  and W1; 
size=22    ## 22 if between W2 and W3. 
#x_placement = 2.40    ## Stopping at W2
x_placement = 5.5      ## With W4
plt.text(x_placement, (ymax*0.72), r'$z$='+str(redshift)+' quasar', color='k',     weight='bold', size=size)
plt.text(x_placement, (ymax*0.64), r'L1 dwarf',                     color='r',     weight='bold', size=size)
plt.text(x_placement, (ymax*0.56), r'T4.5 dwarf',                   color='brown', weight='bold', size=size)


## Axes parameters
#ax.tick_params(axis='both', which='major', labelsize=ticklabelsize, top=True, right=True, direction='in', length=majorticklength, width=tickwidth)
#ax.tick_params(axis='both', which='minor', right=True, direction='in', width=tickwidth)

## "Somehow", these three lines convert the
## 10^-1, 10^0 and 10^1 x-axis lables to 0.1, 1, 10...
from matplotlib.ticker import ScalarFormatter
for axis in [ax.xaxis, ax.yaxis]:
    axis.set_major_formatter(ScalarFormatter())

ax.set_xlabel(r"Observed wavelength / $\mu$m")
ax.set_ylabel("Normalised Transmission");

## Save the figure
plt.savefig('filters_vs_QSOstars_temp.png', format='png')
plt.savefig('filters_vs_QSOstars_temp.pdf', format='pdf')
plt.close(fig)
#plt.show()

## Write out the SED::
#ascii.write([VdB01_wave, quasar_template_flux], 'quasar_SED_temp.dat', names=['wavelength', 'flux'], overwrite=True)     
