'''
WISE detections and colors of Very High redshift quasars
'''

from astropy.io import fits
from astropy.io import ascii
from astropy.table import Table

#import matplotlib
import matplotlib as mpl

import matplotlib.pyplot as plt
import numpy as np
import math

from matplotlib import colors as mcolors
from matplotlib import gridspec

from mpl_toolkits.axes_grid1.axes_divider  import make_axes_locatable
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, zoomed_inset_axes
from mpl_toolkits.axes_grid1.colorbar      import colorbar

## READ-IN THE DATA FILE(S)
path = '/cos_pc19a_npr/data/highest_z_QSOs/'
all_VHzQs  = ascii.read(path+'THE_TABLE_v0pnt97_WISE_coverage.dat', delimiter=r'\s', guess=False)

## Setting up the variables for easier use
w1mpro = all_VHzQs['w1mpro']
w2mpro = all_VHzQs['w2mpro']
w3mpro = all_VHzQs['w3mpro']
w4mpro = all_VHzQs['w4mpro']
w1snr = all_VHzQs['w1snr']
w2snr = all_VHzQs['w2snr']
w3snr = all_VHzQs['w3snr']
w4snr = all_VHzQs['w4snr']
w1cov = all_VHzQs['w1cov']
w2cov = all_VHzQs['w2cov']
w3cov = all_VHzQs['w3cov']
w4cov = all_VHzQs['w4cov']



##
##  Making thesplot
##
##  May fave new line ;-=)
#plt.style.use('dark_background')

## 4 plots all in (one) row
#fig, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4, figsize=(14.0, 5.0))
## If 1 by 4:: 
left   = 0.04   # the left side of the subplots of the figure
right  = 0.96   # the right side of the subplots of the figure
bottom = 0.10   # the bottom of the subplots of the figure
top    = 0.90   # the top of the subplots of the figure
wspace = 0.48   # the amount of width reserved for blank space between subplots
hspace = 0.20   # the amount of height reserved for white space between subplots

## 4 plots all 2x2 grid
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(8.4, 8.0))
left   = 0.12   # the left side of the subplots of the figure
right  = 0.92   # the right side of the subplots of the figure
bottom = 0.10   # the bottom of the subplots of the figure
top    = 0.94   # the top of the subplots of the figure
wspace = 0.44   # the amount of width reserved for blank space between subplots
hspace = 0.24   # the amount of height reserved for white space between subplots

plt.subplots_adjust(left=left, bottom=bottom, right=right, top=top, wspace=wspace, hspace=hspace)

## define the colormap
cmap = plt.cm.inferno_r

ls = 'solid'
lw = 1.0
ms = 50.
ms_large = ms*3.
fontsize=14
alpha=1.00

xmin = 13.00; xmax =  19.00; ymin =  0.00; ymax =  45.00
ax1.scatter(w1mpro, w1snr, s=ms*1.8,  alpha=1.0, color='k')
im1 = ax1.scatter(w1mpro, w1snr, s=ms,  cmap= cmap, alpha=alpha, label='424 VHzQs', c=w1cov, vmin=12, vmax=110) #, norm=mpl.colors.LogNorm())
#im1 = ax1.scatter(w1mpro, w1snr, s=ms,  cmap= cmap, alpha=0.85, label='424 VHzQs', c=w1cov, vmin=20, vmax=115) #, norm=mpl.colors.LogNorm())
#ax1.legend(loc='upper left', fontsize=fontsize/1.3, frameon='True')
ax1.set_xlim((xmin, xmax))
ax1.set_ylim((ymin, ymax))
ax1.tick_params('x', direction='in', which='both', bottom='True', top='True', left='True', right='True')
ax1.tick_params('y', direction='in', which='both', bottom='True', top='True', left='True', right='False')
ax1.set_xlabel('W1 Mag', fontsize=fontsize)
ax1.set_ylabel('W1 SNR', fontsize=fontsize)

#im1 = ax1.imshow([[1, 2], [3, 4]])
ax1_divider = make_axes_locatable(ax1)
cax1 = ax1_divider.append_axes("right", size="8%", pad="0%")
cb1 = colorbar(im1, cax=cax1)


xmin = 13.00;  xmax =  19.00; ymin = -5.00; ymax = 40.00
ax2.scatter(w2mpro, w2snr, s=ms*2.0,  alpha=1.0, color='k')
im2 = ax2.scatter(w2mpro, w2snr, s=ms,  cmap=cmap, alpha=alpha, label='237 VHzQs', c=w2cov, vmin=12, vmax=110)
#ax1.legend(loc='upper left', fontsize=fontsize/1.3, frameon='True')
ax2.set_xlim((xmin, xmax))
ax2.set_ylim((ymin, ymax))
ax2.tick_params('x', direction='in', which='both', bottom='True', top='True', left='True', right='True')
ax2.tick_params('y', direction='in', which='both', bottom='True', top='True', left='True', right='True')
ax2.set_xlabel('W2 Mag', fontsize=fontsize)
ax2.set_ylabel('W2 SNR', fontsize=fontsize)

ax2_divider = make_axes_locatable(ax2)
cax2 = ax2_divider.append_axes("right", size="8%", pad="0%")
cb2 = colorbar(im2, cax=cax2)
cb2.ax.set_ylabel('number of exposures', rotation='270', fontsize=fontsize, labelpad=10)
cb2.ax.tick_params(labelsize=fontsize) 


xmin =   10.25; xmax =  14.00; ymin =  -4.00; ymax =  12.00
ax3.scatter(w3mpro, w3snr, s=ms*2.2,  alpha=1.0, color='k')
im3 = ax3.scatter(w3mpro, w3snr, s=ms,  cmap= cmap,alpha=alpha, label='237 VHzQs', c=w3cov, vmin=6, vmax=60)
ax3.set_xlim((xmin, xmax))
ax3.set_ylim((ymin, ymax))
ax3.tick_params('x', direction='in', which='both', bottom='True', top='True', left='True', right='True')
ax3.tick_params('y', direction='in', which='both', bottom='True', top='True', left='True', right='False')
ax3.set_xlabel('W3 Mag', fontsize=fontsize)
ax3.set_ylabel('W3 SNR', fontsize=fontsize)

ax3_divider = make_axes_locatable(ax3)
cax3 = ax3_divider.append_axes("right", size="8%", pad="0%")
cb3 = colorbar(im3, cax=cax3)


xmin =   7.50; xmax =  10.00; ymin =   -4.00; ymax =  7.30
ax4.scatter(w4mpro, w4snr, s=ms*2.4,  alpha=1.0, color='k')
im4 = ax4.scatter(w4mpro, w4snr, s=ms,   cmap= cmap, alpha=alpha, label='2?? VHzQs',  c=w4cov, vmin=6, vmax=60)
ax4.set_xlim((xmin, xmax))
ax4.set_ylim((ymin, ymax))
ax4.tick_params('x', direction='in', which='major', bottom='True', top='True', left='True', right='True')
ax4.tick_params('x', direction='in', which='minor', bottom='True', top='True', left='True', right='True')
ax4.tick_params('y', direction='in', which='major', bottom='True', top='True', left='True', right='False')
ax4.tick_params('y', direction='in', which='minor', bottom='True', top='True', left='True', right='False')
ax4.set_xlabel('W4 Mag', fontsize=fontsize)
ax4.set_ylabel('W4 SNR', fontsize=fontsize)

ax4_divider = make_axes_locatable(ax4)
cax4 = ax4_divider.append_axes("right", size="10%", pad="0%")
cb4 = colorbar(im4, cax=cax4)
cb4.ax.set_ylabel('number of exposures', rotation='270', fontsize=fontsize, labelpad=16)
cb4.ax.tick_params(labelsize=fontsize) 



#plt.show()
plt.savefig('WISEmag_vs_coverage_temp.png', format='png')
plt.savefig('WISEmag_vs_coverage_temp.pdf', format='pdf')
plt.close(fig)






