'''
WISE detections and colors of Very High redshift quasars
'''

from astropy.io import fits
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
infile = 'THE_TABLE_v0pnt97.dat'
readin = path+infile
#all_VHzQs  = ascii.read(readin, delimiter=r'\s', guess=False)
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

plt.rcParams.update({'font.size': 14})

## From
## https://jakevdp.github.io/PythonDataScienceHandbook/04.08-multiple-subplots.html
fig = plt.figure(figsize=(16, 12))
grid = plt.GridSpec(4, 4, hspace=0.00, wspace=0.00)
#grid = plt.GridSpec(4, 4)

main_ax = fig.add_subplot(grid[:-1, 1:])
y_hist  = fig.add_subplot(grid[:-1, 0], xticklabels=[], sharey=main_ax)
x_hist  = fig.add_subplot(grid[-1, 1:], yticklabels=[], sharex=main_ax)

#fig, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, gridspec_kw={'height_ratios': [7, 7, 3]}, figsize=(14.0, 16.0))


## define the colormap
#cmap = plt.cm.jet
#cmap = plt.cm.hsv
#cmap = plt.cm.gist_rainbow_r
#cmap = plt.cm.rainbow   ##  Good for  W1SNR
#cmap =  plt.cm.terrain
#cmap = plt.cm.jet ## great with 'dark_background'
#cmap = plt.cm.viridis
cmap = plt.cm.plasma  ## Good for W1-W2
##cmap = plt.cm.gnuplot
##cmap = plt.cm.coolwarm
#cmap = plt.cm.Reds_r
#cmap = plt.cm.Oranges_r

## REDSHIFT RANGE
xmin =  4.80  
xmax =  7.95

zmin = xmin
zmax = xmax

##
## TOP  PANEL
##
ls = 'solid'
lw = 1.0
ms_large = 250*1.75
ms = ms_large/3.
#main_ax.scatter(z_GTO,   w1mag_GTO,   c='r', marker="P", s=ms_large)
#hdl=main_ax.scatter(z_all, M1450_all , c=w1snr,        cmap=cmap, s=ms, alpha=0.85)
hdl=main_ax.scatter(z_all, M1450_all , c=w1_min_w2_all, cmap=cmap, s=ms, alpha=0.85)
#hdl=main_ax.scatter(z_all, M1450_all , c=w1snr, cmap=cmap, s=ms, alpha=0.85)
#main_ax.scatter(z_ATLAS, w1mag_ATLAS, c='k', marker="o", s=ms_large)

## Normally, this is:: left, bottom, width, height
## but with orientation='horizontal', then
## left, up,  length, height
#datco=[0.45, 0.775, 0.40, 0.025]   ##
#datco=[0.68, 0.80, 0.28, 0.025]     ## W1 SNR
datco=[0.76, 0.82, 0.20, 0.025]     ## W1-W2 SNR

##and finally the new colorabar axes at the right position!
cbar_ax = fig.add_axes(datco)
#the rest stays the same:
#clevs = [0,  12, 24, 36]  ## w1snr
#clevs = [0, 12, 24, 36]  ## w1snr
#clevs = [0, 15, 30] ## w1snr
#clevs = [0,  6 , 12]  ## w3snr
clevs = [0.0, 1.0]  ## W1-W2

cb1 = plt.colorbar(hdl, cax=cbar_ax, orientation='horizontal', ticks=clevs)
#cb1.set_label(r'W1 SNR', labelpad=-80, fontsize=24)
cb1.set_label(r'W1-W2',      labelpad=-80, fontsize=24)
#ax1.set_ylabel(r'W1MPRO',fontsize=22)


## Bowler et al. 2015, MNRAS, 452, 1817
## Schechter function
z_Bowler        = [5.0, 6.0, 7.0]
Mstar_Bowler    = [-21.07, -20.77, -20.56]
errMstar_Bowler = [0.09, 0.18, 0.17]
## https://matplotlib.org/examples/lines_bars_and_markers/linestyles.html
main_ax.plot(z_Bowler, Mstar_Bowler,linestyle='--', linewidth=4, color='w')
main_ax.text(7.025, -20.5, r'galaxy ${\it M}^*$', {'color': 'w', 'fontsize': 22},  weight=600)
main_ax.text(7.025, -20.0, r'Bowler et al. (2015)', {'color': 'w', 'fontsize': 14}, weight=700)


ymin = -19.5
ymax = -30.5
main_ax.set_xlim((xmin, xmax))
main_ax.set_ylim((ymin, ymax))
main_ax.tick_params('x', direction='in', which='both', bottom=True, top=True, left=True, right=True)
main_ax.tick_params('y', direction='in', which='both', bottom=True, top=True, left=True, right=True)

ax4 = main_ax.twiny()
ax4.set_xticks(ageticks)
ax4.set_xticklabels(['{:g}'.format(age) for age in ages.value])
#zmin, zmax = 0, 5.9
#ax.set_xlim(zmin, zmax)
ax4.set_xlim(zmin, zmax)
#ax4.set_xlabel('Time since Big Bang (Gyr; Flat $\Lambda$CDM, H0=67.7)')
ax4.set_xlabel('Time since Big Bang (Gyr)')
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
## color = 'azure' great for 'dark_background'
#xcolor = 'mediumaquamarine'
#xcolor='seagreen'
#xcolor = 'azure'
xcolor='darkturquoise'
x_hist.hist(z_all, bins=nxbins, label='425 quasars', alpha=1.0, color='c') 
x_hist.legend(loc='upper right')

yymin = 0.0
yymax = 40.0
x_hist.set_xlim((xmin, xmax))
x_hist.set_ylim((yymin, yymax))

#x_hist.set_ylabel('# quasars',fontsize=22)
x_hist.set_xlabel(r'$z$, redshift',fontsize=22)
x_hist.tick_params('x', direction='in', which='both', bottom=True, top=True, left=True, right=True) #,labelsize=18 )
x_hist.tick_params('y', direction='in', which='both', bottom=True, top=True, left=True, right=True)
#ax3.legend=('[All quasars]', '[WISE detected quasars]')

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

#y_hist.set_xlabel('# quasars',fontsize=22)
y_hist.set_ylabel(r'Absolute Magnitude, M$_{1450}$',fontsize=22)

y_hist.set_xlim((50, 0))
#y_hist.set_ylim((ymin, ymax))


#plt.show()
plt.savefig('VHzQ_Lz_temp.png',format='png')
plt.close(fig)
