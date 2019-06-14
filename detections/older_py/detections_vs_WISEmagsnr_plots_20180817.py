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

z_all = all_VHzQs['redshift']
M1450_all = all_VHzQs['M1450']


##
no_bins = 101
w1mag_limit   = np.empty(no_bins)
w2mag_limit   = np.empty(no_bins)
w3mag_limit   = np.empty(no_bins)
w4mag_limit   = np.empty(no_bins)

w1mag_percent = np.empty(no_bins)
w2mag_percent = np.empty(no_bins)
w3mag_percent = np.empty(no_bins)
w4mag_percent = np.empty(no_bins)

w1snr_limit   = np.empty(no_bins)
w2snr_limit   = np.empty(no_bins)
w3snr_limit   = np.empty(no_bins)
w4snr_limit   = np.empty(no_bins)

w1snr_percent = np.empty(no_bins)
w2snr_percent = np.empty(no_bins)
w3snr_percent = np.empty(no_bins)
w4snr_percent = np.empty(no_bins)

snr_limit = 2.0

for i in range(no_bins):
    w1mag_limit[i] = 14.0+(0.05*i)
    w2mag_limit[i] = 14.0+(0.05*i)
    w3mag_limit[i] = 10.0+(0.05*i)
    w4mag_limit[i] =  6.0+(0.05*i)

    w1snr_limit[i] =  0.0+(0.5*i)
    w2snr_limit[i] =  0.0+(0.5*i)
    w3snr_limit[i] =  0.0+(0.5*i)
    w4snr_limit[i] =  0.0+(0.5*i)
    
    w_forw1 = w1mag[np.where((w1mag > 0) & (w1mag < w1mag_limit[i]))]
    w_forw2 = w2mag[np.where((w2mag > 0) & (w2mag < w2mag_limit[i]))]
    w_forw3 = w3mag[np.where((w3mag > 0) & (w3mag < w3mag_limit[i]))]
    w_forw4 = w4mag[np.where((w4mag > 0) & (w4mag < w4mag_limit[i]))]

    ww_forw1 = w1snr[np.where((w1snr > snr_limit) & (w1snr < w1snr_limit[i]))]
    ww_forw2 = w2snr[np.where((w2snr > snr_limit) & (w2snr < w2snr_limit[i]))]
    ww_forw3 = w3snr[np.where((w3snr > snr_limit) & (w3snr < w3snr_limit[i]))]
    ww_forw4 = w4snr[np.where((w4snr > snr_limit) & (w4snr < w4snr_limit[i]))]
    
    w1mag_percent[i] = (len(w_forw1)/len(w1mag)*100)
    w2mag_percent[i] = (len(w_forw2)/len(w2mag)*100)
    w3mag_percent[i] = (len(w_forw3)/len(w3mag)*100)
    w4mag_percent[i] = (len(w_forw4)/len(w4mag)*100)
    #print('W1', i, w1mag_limit[i], len(w_forw1), len(w1mag), len(w_forw1)/len(w1mag)*100, w1mag_percent[i]  )
    #print('W2', i, w2mag_limit[i], len(w_forw2), len(w2mag), len(w_forw2)/len(w2mag)*100, w2mag_percent[i]  )
    #print('W3', i, w3mag_limit[i], len(w_forw3), len(w3mag), len(w_forw3)/len(w3mag)*100, w3mag_percent[i]  )
    #print('W4', i, w4mag_limit[i], len(w_forw4), len(w4mag), len(w_forw4)/len(w4mag)*100, w4mag_percent[i]  )

    w1snr_percent[i] = (len(ww_forw1)/len(w1snr)*100)
    w2snr_percent[i] = (len(ww_forw2)/len(w2snr)*100)
    w3snr_percent[i] = (len(ww_forw3)/len(w3snr)*100)
    w4snr_percent[i] = (len(ww_forw4)/len(w4snr)*100)
    print('W1', i, w1snr_limit[i], len(ww_forw1), len(w1snr), len(ww_forw1)/len(w1snr)*100, w1snr_percent[i]  )
    print('W2', i, w2snr_limit[i], len(ww_forw2), len(w2snr), len(ww_forw2)/len(w2snr)*100, w2snr_percent[i]  )
    print('W3', i, w3snr_limit[i], len(ww_forw3), len(w3snr), len(ww_forw3)/len(w3snr)*100, w3snr_percent[i]  )
    print('W4', i, w4snr_limit[i], len(ww_forw4), len(w4snr), len(ww_forw4)/len(w4snr)*100, w4snr_percent[i]  )

   
##
##  Making thesplot
##
##  May fave new line ;-=)
#plt.style.use('dark_background')
from matplotlib import rc
#rc('text', usetex=True)

#matplotlib.rc('text', usetex=True)
#plt.rcParams.update({'font.size': 14})

fig, ax = plt.subplots(figsize=(8.0, 8.0))

## define the colormap
cmap = plt.cm.jet

## MAGNITUDE RANGE
xmin =   5.50  
xmax =  19.00
ymin =    0.0
ymax =  100.

ls = 'solid'
lw = 1.0
ms = 150.
ms_large = ms*3.
fontsize=26

#main_ax.scatter(z_GTO,   w1mag_GTO,   c='r', marker="P", s=ms_large)
#hdl=main_ax.scatter(z_all, M1450_all , c=w1snr,        cmap=cmap, s=ms, alpha=0.85)
#ax.scatter(w1mag_limit, w1mag_percent, s=ms, alpha=0.85)
ax.scatter(w1mag_limit, w1mag_percent, s=ms, alpha=0.85, label='W1 mag')
ax.scatter(w2mag_limit, w2mag_percent, s=ms, alpha=0.85, label='W2 mag')
ax.scatter(w3mag_limit, w3mag_percent, s=ms, alpha=0.85, label='W3 mag')
ax.scatter(w4mag_limit, w4mag_percent, s=ms, alpha=0.85, label='W4 mag')

ax.set_xlim((xmin, xmax))
ax.set_ylim((ymin, ymax))
ax.tick_params('x', direction='in', which='both', bottom='True', top='True', left='True', right='True')
ax.tick_params('y', direction='in', which='both', bottom='True', top='True', left='True', right='True')

ax.legend(loc='upper left', fontsize=fontsize/1.3, frameon='True')

#plt.show()
plt.savefig('detections_vs_WISEmag_temp.png', format='png')
plt.close(fig)


##
## Making the    S N R   plot
##
fig, ax = plt.subplots(figsize=(8.0, 8.0))
## define the colormap
cmap = plt.cm.jet

xmin =   0.00  ## 0.90
xmax =  45.00
ymin =   0.00  ## 0.90
ymax = 100.00

ax.scatter(w1snr_limit, w1snr_percent, s=ms, alpha=0.85, label='W1 SNR')
ax.scatter(w2snr_limit, w2snr_percent, s=ms, alpha=0.85, label='W2 SNR')
ax.scatter(w3snr_limit, w3snr_percent, s=ms/2, alpha=0.85, label='W3 SNR')
ax.scatter(w4snr_limit, w4snr_percent, s=ms/3, alpha=0.85, label='W4 SNR')

ax.legend(loc='upper left', fontsize=fontsize/1.3, frameon='True')

ax.set_xlim((xmin, xmax))
ax.set_ylim((ymin, ymax))
ax.tick_params('x', direction='in', which='both', bottom='True', top='True', left='True', right='True')
ax.tick_params('y', direction='in', which='both', bottom='True', top='True', left='True', right='True')

#ax.set_xscale("log", nonposx='clip')
#ax.set_yscale("log", nonposy='clip')

ax.set_xlabel('SNR')
ax.set_ylabel(r'% of all VH$z$Qs detected')

axins = zoomed_inset_axes(ax, 2.0,  loc='lower right')
# sub region of the original image
x1, x2, y1, y2 = 0.0, 8., 0.0, 25.0
axins.set_xlim(x1, x2)
axins.set_ylim(y1, y2)
axins.scatter(w3snr_limit, w3snr_percent, s=ms, alpha=0.85, label='W3 SNR', color='green')
axins.scatter(w4snr_limit, w4snr_percent, s=ms, alpha=0.85, label='W4 SNR', color='red')

#handles, labels = ax.get_legend_handles_labels()
#handles = [handles[0], handles[1], handles[2], handles[3] ]
#labels  = [labels[0],  labels[1],  labels[2],  labels[3]]
#ax.legend(handles,labels,loc=2)
#axins.legend(loc='upper left', fontsize=fontsize/1.3, frameon='True')


#plt.show()
plt.savefig('detections_vs_WISEsnr_temp.png', format='png')
plt.close(fig)






