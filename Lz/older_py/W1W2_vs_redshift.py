'''
WISE detections and colors of Very High redshift quasars
'''

from astropy.io import fits
from astropy.table import Table
from astropy.io import ascii
from astropy.table import Table

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math

from matplotlib import colors as mcolors
from matplotlib import gridspec

from astropy.cosmology import FlatLambdaCDM
# In this case we just need to define the matter density 
# and hubble parameter at z=0.
# Note the default units for the hubble parameter H0 are km/s/Mpc. 
# You can also pass an astropy `Quantity` with the units specified. 
#cosmo = FlatLambdaCDM(H0=68, Om0=0.27)
cosmo = FlatLambdaCDM(H0=67.7, Om0=0.307)  #Banados thesis


import astropy.units as u
ages = np.array([13, 10, 8, 6, 5, 4, 3, 2, 1.5, 1.2, 1, 0.8, 0.70])*u.Gyr
from astropy.cosmology import z_at_value
ageticks = [z_at_value(cosmo.age, age) for age in ages]



## READ-IN THE DATA FILE(S)
path = '/cos_pc19a_npr/data/highest_z_QSOs/'

## na desig        ra_hms  dec_dms ra      dec     redshift        mag     M1450   errM1450        ra_WISE dec_WISE        w1mag w1err w1snr       w2mag w2err w2snr       w3mag w3err w3snr       w4mag w4err w4snr       ref
#all_VHzQs  = ascii.read(path+'THE_TABLE_byRA.dat', delimiter=r'\s', guess=False)
## Just for "clean" plotting purposes!!   (126 quasars in the full file...)
all_VHzQs  = ascii.read(path+'THE_TABLE_byRA_zge5pnt00.dat', delimiter=r'\s', guess=False)

## The four ATLAS QSOs
ATLAS = ascii.read(path+'ATLAS_Quasar_TABLE.dat', delimiter=r'\s', guess=False)

GTO =  ascii.read('JWST_GTO_VeryHighZ_Quasar_targets_byRA.dat', delimiter=r'\s', guess=False)

## Setting up the variables for easier use
w1mag = all_VHzQs['w1mag']
w2mag = all_VHzQs['w2mag']
w3mag = all_VHzQs['w3mag']
w4mag = all_VHzQs['w4mag']
w1snr   = all_VHzQs['w1snr']
w2snr   = all_VHzQs['w2snr']
w3snr   = all_VHzQs['w3snr']
w4snr   = all_VHzQs['w4snr']

z_all = all_VHzQs['redshift']
w1_min_w2_all = (w1mag-w2mag)
w2_min_w3_all = (w1mag-w2mag)
w3_min_w4_all = (w1mag-w2mag)

## ATLAS
w1mag_ATLAS = ATLAS['w1mag']
w2mag_ATLAS = ATLAS['w2mag']
w3mag_ATLAS = ATLAS['w3mag']
w4mag_ATLAS = ATLAS['w4mag']
w1snr_ATLAS   = ATLAS['w1snr']
w2snr_ATLAS   = ATLAS['w2snr']
w3snr_ATLAS   = ATLAS['w3snr']
w4snr_ATLAS   = ATLAS['w4snr']

z_ATLAS = ATLAS['redshift']
w1_min_w2_ATLAS = (w1mag_ATLAS-w2mag_ATLAS)
w2_min_w3_ATLAS = (w1mag_ATLAS-w2mag_ATLAS)
w3_min_w4_ATLAS = (w1mag_ATLAS-w2mag_ATLAS)


## GTO
w1mag_GTO = GTO['w1mag']
w2mag_GTO = GTO['w2mag']
w3mag_GTO = GTO['w3mag']
w4mag_GTO = GTO['w4mag']
w1snr_GTO   = GTO['w1snr']
w2snr_GTO   = GTO['w2snr']
w3snr_GTO   = GTO['w3snr']
w4snr_GTO   = GTO['w4snr']

z_GTO = GTO['redshift']
w1_min_w2_GTO = (w1mag_GTO-w2mag_GTO)
w2_min_w3_GTO = (w1mag_GTO-w2mag_GTO)
w3_min_w4_GTO = (w1mag_GTO-w2mag_GTO)


##
## Making the plot
##
## May fave new line ;-=)
#plt.style.use('dark_background')
#matplotlib.rc('text', usetex=True)

plt.rcParams.update({'font.size': 14})
fig, (ax1, ax2, ax3) = plt.subplots(3, sharex=True,
                               gridspec_kw={'height_ratios': [7, 7, 3]},
                               figsize=(14.0, 16.0))

## define the colormap
#cmap = plt.cm.jet
#cmap = plt.cm.hsv
#cmap = plt.cm.gist_rainbow
#cmap = plt.cm.jet ## great with 'dark_background'
cmap = plt.cm.viridis

## REDSHIFT RANGE
xmin =  4.80  
xmax =  7.9

zmin = xmin
zmax = xmax

##
## TOP  PANEL
##
ls = 'solid'
lw = 1.0
ms_large = 250
ms = ms_large/3.
ax1.scatter(z_GTO,   w1mag_GTO,   c='r', marker="P", s=ms_large)
hdl=ax1.scatter(z_all, w1mag , c=w3snr, cmap=cmap, s=ms, alpha=0.85,) 
ax1.scatter(z_ATLAS, w1mag_ATLAS, c='k', marker="o", s=ms_large)

## Normally, this is:: left, bottom, width, height
## but with orientation='horizontal', then
## left, up,  length, height
datco=[0.45,0.775,0.40,0.025]
#and finally the new colorabar axes at the right position!
cbar_ax = fig.add_axes(datco)
#the rest stays the same:
clevs = [0,  6 , 12]  ## w3snr
cb1 = plt.colorbar(hdl, cax=cbar_ax, orientation='horizontal', ticks=clevs, )
cb1.set_label(r'W3 SNR', labelpad=-80)
ax1.set_ylabel(r'W1MPRO',fontsize=22)

ymin =  18.4
ymax =  13.5
ax1.set_xlim((xmin, xmax))
ax1.set_ylim((ymin, ymax))
ax1.tick_params('x', direction='in', which='both', bottom='on', top='on', left='on', right='on')
ax1.tick_params('y', direction='in', which='both', bottom='on', top='on', left='on', right='on')

ax4 = ax1.twiny()
ax4.set_xticks(ageticks)
ax4.set_xticklabels(['{:g}'.format(age) for age in ages.value])
#zmin, zmax = 0, 5.9
#ax.set_xlim(zmin, zmax)
ax4.set_xlim(zmin, zmax)
ax4.set_xlabel('Time since Big Bang (Gyr; Flat $\Lambda$CDM, H0=67.7)')
ax4.xaxis.set_label_coords(0.50, 1.10)

## KEY LINE!!
fig.subplots_adjust(hspace=0)


##
##  M I D D L E     P A N E L
##
ax2.scatter(z_GTO,   w3snr_GTO,   c='r', marker="P", s=ms_large, label="GTO targets")
hdl=ax2.scatter(z_all, w3snr , c=w1_min_w2_all, cmap=cmap, s=ms, alpha=0.85, label="All z>5 quasars")
ax2.scatter(z_ATLAS, w3snr_ATLAS, c='k', marker="o", s=ms_large, label="ATLAS quasars")

datco=[0.45,0.775,0.40,0.025]
#and finally the new colorabar axes at the right position!
cbar_ax = fig.add_axes(datco)
#the rest stays the same:
clevs = [0,  1 , 2]
cb2 = plt.colorbar(hdl, cax=cbar_ax, orientation='horizontal', ticks=clevs, )
cb2.set_label(r'W1-W2 colour', labelpad=-80)
ax2.set_ylabel(r'W3 SNR',fontsize=22)

ymin = -3.0
ymax =  13.0
ax2.set_xlim((xmin, xmax))
ax2.set_ylim((ymin, ymax))
ax2.tick_params('x', direction='in', which='both', bottom='on', top='on', left='on', right='on')
ax2.tick_params('y', direction='in', which='both', bottom='on', top='on', left='on', right='on')

ax2.legend(loc='upper right', fontsize=26)

## KEY LINE!!
fig.subplots_adjust(hspace=0)


##
##  B O T T O M     P A N E L
##
ms = 4
min_x_data, max_x_data = np.min(z_all), np.max(z_all)
binsize = 0.05 
nbins = int(np.floor((max_x_data - min_x_data) / binsize))
## color = 'azure' great for 'dark_background'
ax3.hist(z_all, bins=nbins, label='All quasars (517)', alpha=1.0) 
ax3.legend(loc='upper right')

ymin = 0.0
ymax = 50.0
ax3.set_xlim((xmin, xmax))
ax3.set_ylim((ymin, ymax))

ax3.set_ylabel('# quasars',fontsize=22)
ax3.set_xlabel(r'$z$, redshift',fontsize=22)
ax3.tick_params('x', direction='in', which='both', bottom='on', top='on', left='on', right='on') #,labelsize=18 )
ax3.tick_params('y', direction='in', which='both', bottom='on', top='on', left='on', right='on')
#ax3.legend=('[All quasars]', '[WISE detected quasars]')

#plt.show()
plt.savefig('W1W2_vs_redshift_temp.png',format='png')
plt.close(fig)
