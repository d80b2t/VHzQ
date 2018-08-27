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

from mpl_toolkits.axes_grid1.inset_locator import inset_axes, zoomed_inset_axes
from mpl_toolkits.axes_grid1.colorbar import colorbar

## READ-IN THE DATA FILE(S)
path = '/cos_pc19a_npr/data/highest_z_QSOs/'
all_VHzQs  = ascii.read(path+'THE_TABLE_v0pnt97.dat', delimiter=r'\s', guess=False)


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

redshift = all_VHzQs['redshift']
M1450_all = all_VHzQs['M1450']


##
##  Making thesplot
##
##  May fave new line ;-=)
#plt.style.use('dark_background')

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(8.0, 8.0))

## define the colormap
cmap = plt.cm.inferno

ls = 'solid'
lw = 1.0
ms = 100.
ms_large = ms*3.
fontsize=26

xmin =   0.00; xmax =  40.00; ymin = -21.00; ymax =  40.00
ax1.scatter(w1snr, M1450_all, s=ms, c=redshift, cmap= cmap, alpha=0.85, label='237 VHzQs')
#ax1.legend(loc='upper left', fontsize=fontsize/1.3, frameon='True')
ax1.set_xlim((xmin, xmax))
ax1.set_ylim((ymin, ymax))
ax1.tick_params('x', direction='in', which='both', bottom='True', top='True', left='True', right='True')
ax1.tick_params('y', direction='in', which='both', bottom='True', top='True', left='True', right='True')
ax1.set_xlabel('W1 SNR')
ax1.set_ylabel('W2 SNR')

xmin =   0.00; xmax =  40.00; ymin =   0.00; ymax =  40.00
ax1.scatter(w2snr, M1450_all, s=ms, c=redshift, cmap= cmap, alpha=0.85, label='237 VHzQs')
#ax1.legend(loc='upper left', fontsize=fontsize/1.3, frameon='True')
ax1.set_xlim((xmin, xmax))
ax1.set_ylim((ymin, ymax))
ax1.tick_params('x', direction='in', which='both', bottom='True', top='True', left='True', right='True')
ax1.tick_params('y', direction='in', which='both', bottom='True', top='True', left='True', right='True')
ax1.set_xlabel('W1 SNR')
ax1.set_ylabel('W2 SNR')

xmin =   0.00; xmax =  40.00; ymin =   0.00; ymax =  12.00
ax3.scatter(w3snr, M1450_all, s=ms, c=redshift,  cmap= cmap,alpha=0.85, label='237 VHzQs')
#ax3.legend(loc='upper left', fontsize=fontsize/1.3, frameon='True')
ax3.set_xlim((xmin, xmax))
ax3.set_ylim((ymin, ymax))
ax3.tick_params('x', direction='in', which='both', bottom='True', top='True', left='True', right='True')
ax3.tick_params('y', direction='in', which='both', bottom='True', top='True', left='True', right='True')
ax3.set_xlabel('W1 SNR')
ax3.set_ylabel('W3 SNR')

xmin =   0.00; xmax =  40.00; ymin =   0.00; ymax =  12.00
ax4.scatter(w4snr, M1450_all, s=ms, c=redshift,  cmap= cmap, alpha=0.85, label='2?? VHzQs')
#ax4.legend(loc='upper left', fontsize=fontsize/1.3, frameon='True')
ax4.set_xlim((xmin, xmax))
ax4.set_ylim((ymin, ymax))
ax4.tick_params('x', direction='in', which='major', bottom='True', top='True', left='True', right='True')
ax4.tick_params('x', direction='in', which='minor', bottom='True', top='True', left='True', right='True')
ax4.tick_params('y', direction='in', which='major', bottom='True', top='True', left='True', right='True')
ax4.tick_params('y', direction='in', which='minor', bottom='True', top='True', left='True', right='True')
ax4.set_xlabel('W2 SNR')
ax4.set_ylabel('W3 SNR')


#plt.show()
plt.savefig('WISEmag_vs_M1450_temp.png', format='png')
plt.close(fig)






