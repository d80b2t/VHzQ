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


## READ-IN THE DATA FILE(S)
path = '/cos_pc19a_npr/data/highest_z_QSOs/'
infile = 'THE_TABLE_v0pnt97.dat'
readin= path+infile
all_VHzQs  = ascii.read(readin, delimiter=r'\s')

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


##
## May fave new line ;-=)
#plt.style.use('dark_background')
matplotlib.rc('text', usetex=True)

plt.rcParams.update({'font.size': 14})
fig, ax = plt.subplots(figsize=(8.0, 8.0))


## define the colormap
#cmap = plt.cm.viridis
cmap = plt.cm.plasma_r  ## Good for W1-W2


##  
xmin =   -5.0   ## -11.2  
xmax =   42.0
ymin =    -5.0    ## -11.2
ymax =   42.0

ls = 'solid'
lw = 1.0
ms_large = 250*1.75
ms = ms_large/3.
fontsize=22

#main_ax.scatter(z_GTO,   w1mag_GTO,   c='r', marker="P", s=ms_large)
#hdl=main_ax.scatter(z_all, M1450_all , c=w1snr,        cmap=cmap, s=ms, alpha=0.85)
#ax.scatter(w1mag_limit, w1mag_percent, s=ms, alpha=0.85)
ax.scatter(w1snr, w2snr, s=ms,    alpha=0.45, marker="P", label='W2 SNR') #, c=w2snr, cmap=cmap)
ax.scatter(w1snr, w3snr, s=ms,    alpha=0.45, marker="s", label='W3 SNR') #, c=w2snr, cmap=cmap)
ax.scatter(w1snr, w4snr, s=ms*2., alpha=0.45, marker=".", label='W4 SNR') #, c=w2snr, cmap=cmap)

#ax.scatter(w2snr, w2snr, s=ms, alpha=0.55, marker="P", label='W2 SNR', c=M1450_all, cmap=cmap)
#ax.scatter(w2snr, w3snr, s=ms, alpha=0.55, marker="s", label='W3 SNR', c=w1snr, cmap=cmap)
#ax.scatter(w2snr, w4snr, s=ms, alpha=0.55, marker=".", label='W4 SNR', c=w1snr, cmap=cmap)


xmin = -5.0; xmax =   45.0
ymin = -5.0; ymax =   45.0
## log scales
#xmin =   0.9; xmax =   82.0
#ymin =   0.9; ymax =   82.0
#ax.set_xscale('log'); ax.set_yscale('log')

ax.set_xlim((xmin, xmax))
ax.set_ylim((ymin, ymax))

ax.tick_params('x', direction='in', which='both', bottom=True, top=True, left=True, right=True)
ax.tick_params('y', direction='in', which='both', bottom=True, top=True, left=True, right=True)

ax.legend(loc='upper left', fontsize=fontsize, frameon='True')
ax.set_xlabel(r" W1   SNR ")
ax.set_ylabel(r" W2/3/4   SNR ");


#plt.show()
plt.savefig('detections_vs_SNR_temp.png',format='png')
plt.close(fig)
