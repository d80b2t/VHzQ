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
## FILTERS
path = '/cos_pc19a_npr/data/filter_curves/'

##
##      UKIRT
##      http://www.mso.anu.edu.au/~brad/Filters/UKIRT[ZYJHK]
##
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

##
##      UKIDSS
##      http://svo2.cab.inta-csic.es/svo/theory/fps/index.php?mode=browse&gname=UKIRT&gname2=UKIDSS
##
infile = 'UKIDSS/UKIRT_UKIDSS.Z.dat'
table = path+infile
UKIDSS_Zband      = ascii.read(table)
UKIDSS_Zband_wave = UKIDSS_Zband['wavelength']
UKIDSS_Zband_thru = UKIDSS_Zband['throughput']
infile = 'UKIDSS/UKIRT_UKIDSS.Y.dat'
table = path+infile
UKIDSS_Yband      = ascii.read(table)
UKIDSS_Yband_wave = UKIDSS_Yband['wavelength']
UKIDSS_Yband_thru = UKIDSS_Yband['throughput']
infile = 'UKIDSS/UKIRT_UKIDSS.J.dat'
table = path+infile
UKIDSS_Jband      = ascii.read(table)
UKIDSS_Jband_wave = UKIDSS_Jband['wavelength']
UKIDSS_Jband_thru = UKIDSS_Jband['throughput']
infile = 'UKIDSS/UKIRT_UKIDSS.H.dat'
table = path+infile
UKIDSS_Hband      = ascii.read(table)
UKIDSS_Hband_wave = UKIDSS_Hband['wavelength']
UKIDSS_Hband_thru = UKIDSS_Hband['throughput']
infile = 'UKIDSS/UKIRT_UKIDSS.K.dat'
table = path+infile
UKIDSS_Kband      = ascii.read(table)
UKIDSS_Kband_wave = UKIDSS_Kband['wavelength']
UKIDSS_Kband_thru = UKIDSS_Kband['throughput']

##
##    WFCAM
##    http://svo2.cab.inta-csic.es/svo/theory/fps/index.php?mode=browse&gname=UKIRT&gname2=WFCAM
##
infile = 'WFCAM/UKIRT_WFCAM.Z.dat'
table = path+infile
WFCAM_Zband      = ascii.read(table)
WFCAM_Zband_wave = WFCAM_Zband['wavelength']
WFCAM_Zband_thru = WFCAM_Zband['throughput']
infile = 'WFCAM/UKIRT_WFCAM.Y.dat'
table = path+infile
WFCAM_Yband      = ascii.read(table)
WFCAM_Yband_wave = WFCAM_Yband['wavelength']
WFCAM_Yband_thru = WFCAM_Yband['throughput']
infile = 'WFCAM/UKIRT_WFCAM.J.dat'
table = path+infile
WFCAM_Jband      = ascii.read(table)
WFCAM_Jband_wave = WFCAM_Jband['wavelength']
WFCAM_Jband_thru = WFCAM_Jband['throughput']
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





##
## Making the plot...
##
plt.rcParams.update({'font.size': 14})
#fig = plt.figure(figsize=(14, 7))
fig, ax = plt.subplots(figsize=(16, 7))

xmin =  0.78      ## um
xmax =  2.7    ## just PS1/DECam

ymin =  0.00
ymax =  1.00
#ymax =  0.275

ax.set_xscale('log')
#ax.set_yscale('log')
## if log, then...
#ymin =   0.001
#ymax =   2.30
ax.set_xlim([xmin,xmax])
ax.set_ylim([ymin, ymax])

labelsize       = 18
tickwidth       = 2.0
majorticklength = 12
minorticklength = 6
ticklabelsize   = labelsize

linewidth = 2.2
fontsize  = 22
alpha = 1.0

#ax.tick_params(axis='both', which='major', labelsize=ticklabelsize, top=True, right=True, direction='in', length=majorticklength, width=tickwidth)
#ax.tick_params(axis='both', which='minor', right=True, direction='in', width=tickwidth)

##
## Named colors from::
##    https://matplotlib.org/examples/color/named_colors.html
##
## FILTERS
##

##  U K I R T  
##ax.plot( (UKIRT_Zband_wave/10000.),  (UKIRT_Zband_thru/UKIRT_Zband_thru.max()), color='olive',         alpha=alpha, linewidth=linewidth)
##ax.plot( (UKIRT_Yband_wave/10000.),  (UKIRT_Yband_thru/UKIRT_Yband_thru.max()), color='darkgoldenrod', alpha=alpha, linewidth=linewidth)
##ax.plot( (UKIRT_Jband_wave/10000.),  (UKIRT_Jband_thru/UKIRT_Jband_thru.max()), color='orange',        alpha=alpha, linewidth=linewidth)
##ax.plot( (UKIRT_Hband_wave/10000.),  (UKIRT_Hband_thru/UKIRT_Hband_thru.max()), color='red',          alpha=alpha, linewidth=linewidth)
##ax.plot( (UKIRT_Kband_wave/10000.),  (UKIRT_Kband_thru/UKIRT_Kband_thru.max()), color='firebrick',        alpha=alpha, linewidth=linewidth)
##ax.fill( (UKIRT_Zband_wave/10000.),  (UKIRT_Zband_thru/UKIRT_Zband_thru.max()), color='olive',         alpha=alpha/2)
##ax.fill( (UKIRT_Yband_wave/10000.),  (UKIRT_Yband_thru/UKIRT_Yband_thru.max()), color='darkgoldenrod', alpha=alpha/2)
##ax.fill( (UKIRT_Jband_wave/10000.),  (UKIRT_Jband_thru/UKIRT_Jband_thru.max()), color='orange',        alpha=alpha/2)
##ax.fill( (UKIRT_Hband_wave/10000.),  (UKIRT_Hband_thru/UKIRT_Hband_thru.max()), color='red',          alpha=alpha/2)
##ax.fill( (UKIRT_Kband_wave/10000.),  (UKIRT_Kband_thru/UKIRT_Kband_thru.max()), color='firebrick',        alpha=alpha/2)

#ax.plot( (UKIDSS_Zband_wave/10000.),  (UKIDSS_Zband_thru), color='olive',  alpha=alpha,           linewidth=linewidth, ls='--')
#ax.plot( (UKIDSS_Yband_wave/10000.),  (UKIDSS_Yband_thru), color='darkgoldenrod', alpha=alpha,    linewidth=linewidth, ls='--')
#ax.plot( (UKIDSS_Jband_wave/10000.),  (UKIDSS_Jband_thru), color='orange',        alpha=alpha,    linewidth=linewidth, ls='--')
#ax.plot( (UKIDSS_Hband_wave/10000.),  (UKIDSS_Hband_thru), color='red',          alpha=alpha,     linewidth=linewidth, ls='--')
#ax.plot( (UKIDSS_Kband_wave/10000.),  (UKIDSS_Kband_thru), color='firebrick',        alpha=alpha, linewidth=linewidth, ls='--')
#ax.plot( (UKIDSS_Zband_wave/10000.),  (UKIDSS_Zband_thru), color='k',  linewidth=linewidth/1.4)
#ax.plot( (UKIDSS_Yband_wave/10000.),  (UKIDSS_Yband_thru), color='k',  linewidth=linewidth/1.4)
#ax.plot( (UKIDSS_Jband_wave/10000.),  (UKIDSS_Jband_thru), color='k',  linewidth=linewidth/1.4)
#ax.plot( (UKIDSS_Hband_wave/10000.),  (UKIDSS_Hband_thru), color='k',   linewidth=linewidth/1.4)
#ax.plot( (UKIDSS_Kband_wave/10000.),  (UKIDSS_Kband_thru), color='k',  linewidth=linewidth/1.4)

ax.plot( (UKIDSS_Zband_wave/10000.),  (UKIDSS_Zband_thru/UKIDSS_Zband_thru.max()), color='k',  alpha=alpha, linewidth=linewidth/1.4)
ax.plot( (UKIDSS_Yband_wave/10000.),  (UKIDSS_Yband_thru/UKIDSS_Yband_thru.max()), color='k',  alpha=alpha, linewidth=linewidth/1.4)
ax.plot( (UKIDSS_Jband_wave/10000.),  (UKIDSS_Jband_thru/UKIDSS_Jband_thru.max()), color='k',  alpha=alpha, linewidth=linewidth/1.4)
ax.plot( (UKIDSS_Hband_wave/10000.),  (UKIDSS_Hband_thru/UKIDSS_Hband_thru.max()), color='k',  alpha=alpha, linewidth=linewidth/1.4)
ax.plot( (UKIDSS_Kband_wave/10000.),  (UKIDSS_Kband_thru/UKIDSS_Kband_thru.max()), color='k',  alpha=alpha, linewidth=linewidth/1.4)
##ax.fill( (UKIDSS_Zband_wave/10000.),  (UKIDSS_Zband_thru/UKIDSS_Zband_thru.max()), color='olive', alpha=alpha/2)
##ax.fill( (UKIDSS_Yband_wave/10000.),  (UKIDSS_Yband_thru/UKIDSS_Yband_thru.max()), color='darkgoldenrod', alpha=alpha/2)
##ax.fill( (UKIDSS_Jband_wave/10000.),  (UKIDSS_Jband_thru/UKIDSS_Jband_thru.max()), color='orange',        alpha=alpha/2)
##ax.fill( (UKIDSS_Hband_wave/10000.),  (UKIDSS_Hband_thru/UKIDSS_Hband_thru.max()), color='red',          alpha=alpha/2)
##ax.fill( (UKIDSS_Kband_wave/10000.),  (UKIDSS_Kband_thru/UKIDSS_Kband_thru.max()), color='firebrick',        alpha=alpha/2)

#ax.plot( (WFCAM_Zband_wave/10000.),  (WFCAM_Zband_thru), color='olive',         alpha=alpha, linewidth=linewidth)
#ax.plot( (WFCAM_Yband_wave/10000.),  (WFCAM_Yband_thru), color='darkgoldenrod', alpha=alpha, linewidth=linewidth)
#ax.plot( (WFCAM_Jband_wave/10000.),  (WFCAM_Jband_thru), color='orange',        alpha=alpha, linewidth=linewidth)
#ax.plot( (WFCAM_Hband_wave/10000.),  (WFCAM_Hband_thru), color='red',           alpha=alpha, linewidth=linewidth)
#ax.plot( (WFCAM_Kband_wave/10000.),  (WFCAM_Kband_thru), color='firebrick',     alpha=alpha, linewidth=linewidth)
ax.plot( (WFCAM_Zband_wave/10000.),  (WFCAM_Zband_thru/WFCAM_Zband_thru.max()), color='olive',         alpha=alpha, linewidth=linewidth)
ax.plot( (WFCAM_Yband_wave/10000.),  (WFCAM_Yband_thru/WFCAM_Yband_thru.max()), color='darkgoldenrod', alpha=alpha, linewidth=linewidth)
ax.plot( (WFCAM_Jband_wave/10000.),  (WFCAM_Jband_thru/WFCAM_Jband_thru.max()), color='orange',        alpha=alpha, linewidth=linewidth)
ax.plot( (WFCAM_Hband_wave/10000.),  (WFCAM_Hband_thru/WFCAM_Hband_thru.max()), color='red',           alpha=alpha, linewidth=linewidth)
ax.plot( (WFCAM_Kband_wave/10000.),  (WFCAM_Kband_thru/WFCAM_Kband_thru.max()), color='firebrick',     alpha=alpha, linewidth=linewidth)
##ax.fill( (WFCAM_Zband_wave/10000.),  (WFCAM_Zband_thru/WFCAM_Zband_thru.max()), color='olive',         alpha=alpha/2)
##ax.fill( (WFCAM_Yband_wave/10000.),  (WFCAM_Yband_thru/WFCAM_Yband_thru.max()), color='darkgoldenrod', alpha=alpha/2)
##ax.fill( (WFCAM_Jband_wave/10000.),  (WFCAM_Jband_thru/WFCAM_Jband_thru.max()), color='orange',        alpha=alpha/2)
##ax.fill( (WFCAM_Hband_wave/10000.),  (WFCAM_Hband_thru/WFCAM_Hband_thru.max()), color='red',          alpha=alpha/2)
##ax.fill( (WFCAM_Kband_wave/10000.),  (WFCAM_Kband_thru/WFCAM_Kband_thru.max()), color='firebrick',        alpha=alpha/2)


plt.text(0.870, ymax*0.55, r'Z', color ='olive',          fontsize=fontsize*1.30)
plt.text(1.020, ymax*0.55, r'Y', color ='darkgoldenrod', fontsize=fontsize*1.30)
plt.text(1.240, ymax*0.55, r'J', color ='orange',        fontsize=fontsize*1.30)
plt.text(1.620, ymax*0.55, r'H', color ='red',           fontsize=fontsize*1.30)
#plt.text(2.020, 1.1, r'K', color ='k',                 fontsize=fontsize*1.2)
plt.text(2.190, ymax*0.55, r'K', color ='firebrick',     fontsize=fontsize*1.30)

#plt.text(0.870, ymax*0.20, r'Z', color ='k',          fontsize=fontsize*1.30)
#plt.text(1.020, ymax*0.20, r'Y', color ='k', fontsize=fontsize*1.30)
#plt.text(1.240, ymax*0.20, r'J', color ='k',        fontsize=fontsize*1.30)
#plt.text(1.620, ymax*0.20, r'H', color ='k',           fontsize=fontsize*1.30)
#plt.text(2.190, ymax*0.20, r'K', color ='k',     fontsize=fontsize*1.30)



## "Somehow", these three lines convert the
## 10^-1, 10^0 and 10^1 x-axis lables to 0.1, 1, 10...
from matplotlib.ticker import ScalarFormatter
for axis in [ax.xaxis, ax.yaxis]:
    axis.set_major_formatter(ScalarFormatter())

ax.set_xlabel(r"Observed wavelength / $\mu$m")
#ax.set_ylabel("Normalised Transmission");
ax.set_ylabel("Transmission")


plt.savefig('filters_UKIRT-WFCAM_temp.png', format='png')
plt.savefig('filters_UKIRT-WFCAM_temp.pdf', format='pdf')
plt.close(fig)
#plt.show()


