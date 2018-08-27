'''
WISE detections and colors of Very High redshift quasars
'''

from astropy.io import fits
from astropy.io import ascii
from astropy.table import Table
from matplotlib.ticker import AutoMinorLocator

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
cosmo = FlatLambdaCDM(H0=67.7, Om0=0.307)  #Banados thesis

import astropy.units as u
ages = np.array([13, 10, 8, 6, 5, 4, 3, 2, 1.5, 1.2, 1, 0.8, 0.70])*u.Gyr
from astropy.cosmology import z_at_value
ageticks = [z_at_value(cosmo.age, age) for age in ages]


## READ-IN THE DATA FILE(S)
path = '/cos_pc19a_npr/data/highest_z_QSOs/'
infile = 'THE_TABLE_v0pnt97.dat'
readin = path+infile
all_VHzQs  = ascii.read(readin, delimiter=r'\s')

## The four ATLAS QSOs
#ATLAS = ascii.read(path+'ATLAS_Quasar_TABLE.dat', delimiter=r'\s', guess=False)
#GTO =  ascii.read('JWST_GTO_VeryHighZ_Quasar_targets_byRA.dat', delimiter=r'\s', guess=False)

## Setting up the variables for easier use
w1mag = all_VHzQs['w1mag']
w2mag = all_VHzQs['w2mag']
w3mag = all_VHzQs['w3mag']
w4mag = all_VHzQs['w4mag']
w1snr   = all_VHzQs['w1snr']
w2snr   = all_VHzQs['w2snr']
w3snr   = all_VHzQs['w3snr']
w4snr   = all_VHzQs['w4snr']
w1_min_w2_all = (w1mag-w2mag)
w2_min_w3_all = (w1mag-w2mag)
w3_min_w4_all = (w1mag-w2mag)

z_all = all_VHzQs['redshift']
M1450_all = all_VHzQs['M1450']

## ATLAS QSOs
#z_ATLAS = ATLAS['redshift']
## GTO
#z_GTO = GTO['redshift']


##
## Making the plot
##
## May fave new line ;-=)
#plt.style.use('dark_background')
#matplotlib.rc('text', usetex=True)

#plt.rcParams.update({'font.size': 14})
minorLocator = AutoMinorLocator()

fontsize        = 36
labelsize       = fontsize
tickwidth       = 2.0
majorticklength = 14
minorticklength = majorticklength/2.
ticklabelsize   = labelsize

ls       = 'solid'
lw       = 1.0
ms       = 240.
ms_large = ms*3.
ms_small = ms/10.


## From
## https://jakevdp.github.io/PythonDataScienceHandbook/04.08-multiple-subplots.html
#fig, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, gridspec_kw={'height_ratios': [7, 7, 3]}, figsize=(14.0, 16.0))
fig = plt.figure(figsize=(16, 12))
grid = plt.GridSpec(4, 4, hspace=0.00, wspace=0.00)
#grid = plt.GridSpec(4, 4)

main_ax = fig.add_subplot(grid[:-1, 1:])
y_hist  = fig.add_subplot(grid[:-1, 0], xticklabels=[], sharey=main_ax)
x_hist  = fig.add_subplot(grid[-1, 1:], yticklabels=[], sharex=main_ax)


## define the colormap
#cmap = plt.cm.rainbow   ##  Good for  W1SNR
#cmap = plt.cm.jet       ## great with 'dark_background'
cmap = plt.cm.plasma  ## Good for W1-W2

## REDSHIFT RANGE
xmin =  4.80  
xmax =  7.95

zmin = xmin
zmax = xmax

##
## TOP  PANEL
##
hdl=main_ax.scatter(z_all, M1450_all, c=w1_min_w2_all, cmap=cmap, s=ms, alpha=0.85)

## Normally, this is:: left, bottom, width, height
## but with orientation='horizontal', then
## left, up,  length, height
datco=[0.68, 0.80, 0.20, 0.025]     ## W1-W2 SNR

##and finally the new colorabar axes at the right position!
cbar_ax = fig.add_axes(datco)
cbar_min = 0.0
cbar_max = 1.0
cbar_step = 0.25
#clevs = [0, 15, 30] ## w1snr
#clevs = [0,  6 , 12]  ## w3snr
clevs = [cbar_min, cbar_max]  ## W1-W2


cb1 = plt.colorbar(hdl, cax=cbar_ax, orientation='horizontal', ticks=clevs)
#cb1.set_label(r'W1 SNR', labelpad=-80, fontsize=fontsize)
cb1.set_label(r'W1-W2',  labelpad=-80, fontsize=fontsize/1.4)
cb1.ax.tick_params(labelsize=fontsize/1.4)

#ax1.set_ylabel(r'W1MPRO',fontsize=fontsize)
#cb1.set_yticklabels(['{:.0f}'.format(x) for x in np.arange(cbar_min, cbar_max+cbar_step, cbar_step)], fontsize=32, weight='bold')


## Bowler et al. 2015, MNRAS, 452, 1817
## Schechter function
z_Bowler        = [5.0, 6.0, 7.0]
Mstar_Bowler    = [-21.07, -20.77, -20.56]
errMstar_Bowler = [0.09, 0.18, 0.17]
## https://matplotlib.org/examples/lines_bars_and_markers/linestyles.html
gal_color = 'k' 
main_ax.plot(z_Bowler, Mstar_Bowler,linestyle='--', linewidth=4, color=gal_color)
main_ax.text(7.025, -20.5, r'galaxy ${\it M}^*$', color=gal_color, fontsize=22,  weight=600)
main_ax.text(7.025, -20.0, r'Bowler et al. (2015)', color=gal_color, fontsize=14, weight=700)

ymin = -19.5
ymax = -31.0
main_ax.set_xlim((xmin, xmax))
main_ax.set_ylim((ymin, ymax))

#minorLocator = AutoMinorLocator()
#main_ax.xaxis.set_minor_locator(minorLocator)
#minorLocator = AutoMinorLocator()
#main_ax.yaxis.set_minor_locator(minorLocator)
main_ax.tick_params('both', direction='in', which='major', bottom=True, top=True, left=True, right=True,  length=majorticklength, width=tickwidth)
#main_ax.tick_params('both', direction='in', which='minor', bottom=True, top=True, left=True, right=True,  length=minorticklength, width=tickwidth)

ax4 = main_ax.twiny()
ax4.set_xticks(ageticks)
ax4.set_xticklabels(['{:g}'.format(age) for age in ages.value], fontsize=fontsize/1.2)
#zmin, zmax = 0, 5.9
#ax.set_xlim(zmin, zmax)
ax4.set_xlim(zmin, zmax)
#ax4.set_xlabel('Time since Big Bang (Gyr; Flat $\Lambda$CDM, H0=67.7)')
ax4.set_xlabel('Time since Big Bang (Gyr)', fontsize=fontsize)
ax4.xaxis.set_label_coords(0.50, 1.10)

## KEY LINE!!
fig.subplots_adjust(hspace=0)


##
##  B O T T O M     P A N E L
##
ms = 4
min_x_data, max_x_data = np.min(z_all), np.max(z_all)
xbinsize = 0.05 
nxbins = int(np.floor((max_x_data - min_x_data) / xbinsize))
xcolor='darkturquoise'
x_hist.hist(z_all, bins=nxbins, label='424 quasars', alpha=1.0, color='c') 
x_hist.legend(loc='upper right', fontsize=fontsize/1.4)

yymin = 0.0
yymax = 40.0
x_hist.set_xlim((xmin, xmax))
x_hist.set_ylim((yymin, yymax))

minorLocator = AutoMinorLocator()
#x_hist.xaxis.set_minor_locator(minorLocator)
minorLocator = AutoMinorLocator()
#x_hist.yaxis.set_minor_locator(minorLocator)
x_hist.tick_params('both', direction='in', which='major', bottom=True, top=True, left=True,
                   right=True, length=majorticklength, width=tickwidth, labelsize=fontsize/1.2)
#x_hist.tick_params('both', direction='in', which='minor', bottom=True, top=True, left=True,                   right=True, length=minorticklength, width=tickwidth)

x_hist.set_xlabel(r'$z$, redshift',fontsize=fontsize)
#x_hist.set_ylabel('# quasars',fontsize=22)

## KEY LINE!!
fig.subplots_adjust(hspace=0)


##
##  LEFT HAND SIDE   P A N E L
##
min_y_data, max_y_data = ymax, ymin
ybinsize = 0.05 
nybins = int(np.floor((max_y_data - min_y_data) / ybinsize))

#ycolor='mediumturquoise'
ycolor='c'
y_hist.hist(M1450_all, bins=nybins, alpha=1.0, orientation='horizontal', color=ycolor)
y_hist.invert_xaxis()
#y_hist.legend(loc='upper right')

minorLocator = AutoMinorLocator()
#y_hist.xaxis.set_minor_locator(minorLocator)
minorLocator = AutoMinorLocator()
#y_hist.yaxis.set_minor_locator(minorLocator)
y_hist.tick_params('both', direction='in', which='major', bottom=True, top=True, left=True,
                   right=True, length=majorticklength, width=tickwidth, labelsize=fontsize/1.2)
#y_hist.tick_params('both', direction='in', which='minor', bottom=True, top=True, left=True,                   right=True, length=minorticklength, width=tickwidth)
#y_hist.set_xlabel('# quasars', fontsize=fontsize)
y_hist.set_ylabel(r'Absolute Magnitude, M$_{1450}$', fontsize=fontsize)

y_hist.set_xlim((50, 0))
#y_hist.set_ylim((ymin, ymax))


#plt.show()
plt.savefig('VHzQ_Lz_temp.png',format='png')
plt.savefig('VHzQ_Lz_temp.pdf',format='pdf')

plt.close(fig)
