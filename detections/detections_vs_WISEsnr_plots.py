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
from mpl_toolkits.axes_grid1.axes_divider  import make_axes_locatable
from mpl_toolkits.axes_grid1.colorbar import colorbar

## READ-IN THE DATA FILE(S)
path = '/cos_pc19a_npr/data/highest_z_QSOs/'
all_VHzQs  = ascii.read(path+'THE_TABLE_v0pnt971.dat', delimiter=r'\s', guess=False)


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

redshift  = all_VHzQs['redshift']
M1450_all = all_VHzQs['M1450']


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
#fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(8.0, 8.0))
left   = 0.12   # the left side of the subplots of the figure
right  = 0.94   # the right side of the subplots of the figure
bottom = 0.10   # the bottom of the subplots of the figure
top    = 0.98   # the top of the subplots of the figure
wspace = 0.48   # the amount of width reserved for blank space between subplots
hspace = 0.24   # the amount of height reserved for white space between subplots


## 4 plots all 2 rows, 2 colun grid
## no gaps!!
#fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(8.0, 8.0), sharey=True)
left   = 0.12   # the left side of the subplots of the figure
right  = 0.94   # the right side of the subplots of the figure
bottom = 0.10   # the bottom of the subplots of the figure
top    = 0.98   # the top of the subplots of the figure
wspace = 0.00   # the amount of width reserved for blank space between subplots
hspace = 0.00   # the amount of height reserved for white space between subplots

## 6 plots all 2 rows, 3 colun grid
## no gaps!!
fig, ((ax1, ax2, ax5), (ax3, ax4, ax6)) = plt.subplots(2, 3, figsize=(12.0, 8.0))
left   = 0.08   # the left side of the subplots of the figure
right  = 0.92   # the right side of the subplots of the figure
bottom = 0.08   # the bottom of the subplots of the figure
top    = 0.98   # the top of the subplots of the figure
wspace = 0.00   # the amount of width reserved for blank space between subplots
hspace = 0.26   # the amount of height reserved for white space between subplots

plt.subplots_adjust(left=left, bottom=bottom, right=right, top=top, wspace=wspace, hspace=hspace)


## define the colormap
cmap = plt.cm.inferno_r

ls = 'solid'
lw = 1.0
ms = 100.
ms_large = ms*3.
fontsize=18
alpha=1.00
vmin=5.00
vmax=7.00

xmin1 =   -2.00; xmax1 =  40.00; ymin1 =  -2.00; ymax1 =  40.00
ax1.scatter(      w1snr, w2snr, s=ms*1.8, color='k')
im1 = ax1.scatter(w1snr, w2snr, s=ms,    c=redshift, cmap= cmap, alpha=alpha,vmin=vmin, vmax=vmax)
ax1.set_xlim((xmin1, xmax1))
ax1.set_ylim((ymin1, ymax1))
ax1.tick_params('x', direction='in', which='both', bottom='True', top='True', left='True', right='True', labelsize=fontsize)
ax1.tick_params('y', direction='in', which='both', bottom='True', top='True', left='True', right='True', labelsize=fontsize)
ax1.set_xlabel('W1 SNR', fontsize=fontsize)
ax1.set_ylabel('W2 SNR', fontsize=fontsize)
#ax1_divider = make_axes_locatable(ax1)
#cax1 = ax1_divider.append_axes("right", size="8%", pad="0%")
#cb1 = colorbar(im1, cax=cax1)

xmin2 =   -3.00; xmax2 =  12.00; ymin2 =   -2.00; ymax2 =  42.00
ax2.scatter(      w3snr, w2snr, s=ms*1.8, color='k')
im2 = ax2.scatter(w3snr, w2snr, s=ms,    c=redshift, cmap= cmap, alpha=alpha, vmin=vmin, vmax=vmax)
ax2.set_xlim((xmin2, xmax2))
ax2.set_ylim((ymin2, ymax2))
ax2.tick_params('x', direction='in', which='both', bottom='True', top='True', left='True', right='True', labelsize=fontsize)
ax2.tick_params('y', direction='in', which='both', bottom='True', top='True', left='True', right='True', labelleft='False', labelsize=fontsize)
ax2.set_xlabel('W3 SNR', fontsize=fontsize)
#ax2.set_ylabel('W2 SNR', fontsize=fontsize)
#ax2_divider = make_axes_locatable(ax2)
#cax2 = ax2_divider.append_axes("right", size="8%", pad="0%")
#cb2 = colorbar(im2, cax=cax2)

xmin5 = -0.60; xmax5 =  1.60; ymin5 =   -2.00; ymax5 =  40.00
ax5.scatter(    (w1mag-w2mag), w2snr, s=ms*1.8, color='k')
im5=ax5.scatter((w1mag-w2mag), w2snr, s=ms, c=redshift,  cmap= cmap,alpha=alpha, vmin=vmin, vmax=vmax)
#ax5.legend(loc='upper left', fontsize=fontsize/1.3, frameon='True')
ax5.set_xlim((xmin5, xmax5))
ax5.set_ylim((ymin5, ymax5))
ax5.tick_params('x', direction='in', which='both', bottom='True', top='True', left='True', right='True', labelsize=fontsize)
ax5.tick_params('y', direction='in', which='major', bottom='True', top='True', left='True', right='False', labelleft='False', labelsize=fontsize)
ax5.tick_params('y', direction='in', which='minor', bottom='True', top='True', left='True', right='False', labelsize=fontsize)
ax5.set_xlabel('(W1 - W2)', fontsize=fontsize)
#ax5.set_ylabel('W3 SNR', fontsize=fontsize)
ax5_divider = make_axes_locatable(ax5)
cax5 = ax5_divider.append_axes("right", size="8%", pad="0%")
cb5 = colorbar(im5, cax=cax5)
cb5.ax.set_ylabel('redshiftt', rotation='270', fontsize=fontsize, labelpad=20, position=[2.60, 0.50])
cb5.ax.tick_params(labelsize=fontsize) 




xmin3 = -2.00; xmax3 = 42.00; ymin3 =   -3.00; ymax3 = 14.00
ax3.scatter(    w1snr, w3snr, s=ms*1.8, color='k')
im3=ax3.scatter(w1snr, w3snr, s=ms, c=redshift,  cmap= cmap,alpha=alpha, vmin=vmin, vmax=vmax)
ax3.set_xlim((xmin3, xmax3))
ax3.set_ylim((ymin3, ymax3))
ax3.tick_params('x', direction='in', which='both', bottom='True', top='True', left='True', right='True', labelsize=fontsize)
ax3.tick_params('y', direction='in', which='both', bottom='True', top='True', left='True', right='True', labelsize=fontsize)
ax3.set_xlabel('W1 SNR', fontsize=fontsize)
ax3.set_ylabel('W3 SNR', fontsize=fontsize)
#ax3_divider = make_axes_locatable(ax3)
#cax3 = ax3_divider.append_axes("right", size="8%", pad="0%")
#cb3 = colorbar(im3, cax=cax3)

xmin4 = -3.00; xmax4 =  12.00; ymin4 =   -3.00; ymax4 = 14.00
ax4.scatter(    w4snr, w3snr, s=ms*1.8, color='k')
im4=ax4.scatter(w4snr, w3snr, s=ms, c=redshift,  cmap= cmap, alpha=alpha, vmin=vmin, vmax=vmax)
ax4.set_xlim((xmin4, xmax4))
ax4.set_ylim((ymin4, ymax4))
ax4.tick_params('x', direction='in', which='major', bottom='True', top='True', left='True', right='True', labelsize=fontsize)
ax4.tick_params('x', direction='in', which='minor', bottom='True', top='True', left='True', right='True', labelsize=fontsize)
ax4.tick_params('y', direction='in', which='major', bottom='True', top='True', left='True', right='True',labelleft='False', labelsize=fontsize)
ax4.tick_params('y', direction='in', which='minor', bottom='True', top='True', left='True', right='True', labelsize=fontsize)
ax4.set_xlabel('W4 SNR', fontsize=fontsize)
#ax4.set_ylabel('W3 SNR', fontsize=fontsize)
#ax4_divider = make_axes_locatable(ax4)
#cax4        = ax4_divider.append_axes("right", size="8%", pad="0%")
#cb4         = colorbar(im4, cax=cax4)

xmin6 = -0.60; xmax6 = 1.60; ymin6 =   -3.00; ymax6 = 14.00
ax6.scatter(    (w1mag-w2mag), w3snr, s=ms*1.8, color='k')
im6=ax6.scatter((w1mag-w2mag), w3snr, s=ms, c=redshift,  cmap= cmap, alpha=alpha, vmin=vmin, vmax=vmax)
#ax6.legend(loc='upper left', fontsize=fontsize/1.3, frameon='True')
ax6.set_xlim((xmin6, xmax6))
ax6.set_ylim((ymin6, ymax6))
ax6.tick_params('x', direction='in', which='major', bottom='True', top='True', left='True', right='True', labelsize=fontsize)
ax6.tick_params('x', direction='in', which='minor', bottom='True', top='True', left='True', right='True', labelsize=fontsize)
ax6.tick_params('y', direction='in', which='major', bottom='True', top='True', left='True', right='True',labelleft='False', labelsize=fontsize)
ax6.tick_params('y', direction='in', which='minor', bottom='True', top='True', left='True', right='True', labelsize=fontsize)
ax6.set_xlabel('(W1 - W2)', fontsize=fontsize)
#ax6.set_ylabel('W3 SNR', fontsize=fontsize)
ax6_divider = make_axes_locatable(ax6)
cax6        = ax6_divider.append_axes("right", size="8%", pad="0%")
cb6         = colorbar(im6, cax=cax6)
cb6.ax.set_ylabel('redshiftt', rotation='270', fontsize=fontsize, labelpad=20, position=[2.60, 0.50])
cb6.ax.tick_params(labelsize=fontsize) 


#plt.show()
plt.savefig('WISEsnrW1W2W3_temp.png', format='png')
plt.savefig('WISEsnrW1W2W3_temp.pdf', format='pdf')
plt.close(fig)






