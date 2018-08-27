'''
   Carnall z-W1, W1-W2 (1)
'''
from astropy.io import fits
from astropy.io import ascii
from astropy.table import Table

from time import sleep

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math

from matplotlib import colors as mcolors
from matplotlib import gridspec

##
##  V H z Q    data
##
path = '/cos_pc19a_npr/data/highest_z_QSOs/'
#filename ='THE_TABLE_v0pnt96.dat'
filename ='THE_TABLE_v0pnt97x_PS1_ULAS_VHS_photom_v2.dat'
table=path+filename
VHzQ = ascii.read(table)
#VHzQ = VHzQ[np.where( (VHzQ['redshift'] >= 5.7) & (VHzQ['redshift'] <= 6.7))]


redshift = VHzQ['redshift']
g_PS1 = VHzQ['gMag']
r_PS1 = VHzQ['rMag']
i_PS1 = VHzQ['iMag']
z_PS1 = VHzQ['zMag']
y_PS1 = VHzQ['yMag']
Ymag  = VHzQ['Yapermag']
Jmag  = VHzQ['Jmag']
Hmag  = VHzQ['Hmag']
Kmag  = VHzQ['Kmag']
W1mag = VHzQ['W1mag']
W2mag = VHzQ['W2mag']
W3mag = VHzQ['W3mag']
W4mag = VHzQ['W4mag']

'''
https://blog.backyardworlds.org/page/2/
'''
path = '/cos_pc19a_npr/data/highest_z_QSOs/LT_dwarfs/'
filename ='Ldwarfs_photom_v1pnt00.dat'
table=path+filename
Ldwarfs = ascii.read(table)
#Ldwarfs = Ldwarfs[np.where( (Ldwarfs['W3snr'] > 3.0))]

path = '/cos_pc19a_npr/data/highest_z_QSOs/LT_dwarfs/'
filename ='Tdwarfs_photom_v1pnt00.dat'
table=path+filename
Tdwarfs = ascii.read(table)
#Tdwarfs = Ldwarfs[np.where( (Ldwarfs['W3snr'] > 3.0))]

##
##  Making the plot(s)
##
plt.rcParams.update({'font.size': 14})
#matplotlib.rc('text', usetex=True)

## https://matplotlib.org/examples/pylab_examples/subplots_demo.html
fig, ax1 = plt.subplots(1, figsize=(10, 10), num=None, dpi=80, facecolor='w', edgecolor='k')
#plt.tight_layout()


redshift_clrmap = (10**(redshift-5.15))
redshift_clrmap = redshift
ms_clrsize  = ((redshift-3.9)**5.5)

labelsize       = 28
tickwidth       = 2.0
majorticklength = 12
minorticklength = 6
ticklabelsize   = labelsize

ls       = 'solid'
lw       = 1.0
ms_large = 360.
ms       = 100.
ms_small = 8.

##
##    W1 - W2    vs.    z - W2  
##   
xmin=-0.5; xmax=2.5; ymin=2.0; ymax=8.2
cmap = plt.cm.jet
ax1.axis([xmin, xmax, ymin, ymax])

ax1.scatter( (Ldwarfs['W1mag']-Ldwarfs['W2mag']), (Ldwarfs['zMag']-Ldwarfs['W2mag']), c='k', s=ms_small*1.7)
ax1.scatter( (Tdwarfs['W1mag']-Tdwarfs['W2mag']), (Tdwarfs['zMag']-Tdwarfs['W2mag']), c='k', s=ms_small*1.7)
ax1.scatter( (Ldwarfs['W1mag']-Ldwarfs['W2mag']), (Ldwarfs['zMag']-Ldwarfs['W2mag']), c='orangered', s=ms_small, label='L dwarfs')
ax1.scatter( (Tdwarfs['W1mag']-Tdwarfs['W2mag']), (Tdwarfs['zMag']-Tdwarfs['W2mag']), c='darkred',   s=ms_small, label='T dwarfs')

zbin_size = 0.2
#for ii in range(20):
#    redshift_min = 5.0 + (0.0*ii)
#redshift_min = 5.0 + (zbin_size*(ii-1))
#redshift_max = 5.0 + (zbin_size*ii)
redshift_min = 5.0 
redshift_max = 5.2 
VHzQ_zslice = VHzQ[np.where( (VHzQ['redshift'] >= redshift_min) & (VHzQ['redshift'] <= redshift_max))]

#print(ii, redshift_min,redshift_max, len(VHzQ_zslice))
print(redshift_min,redshift_max, len(VHzQ_zslice))
ax1.scatter(       (VHzQ_zslice['W1mag'] - VHzQ_zslice['W2mag']), (VHzQ_zslice['zMag'] - VHzQ_zslice['W2mag']), c='k', s=ms*1.7)
ax1.scatter( (VHzQ_zslice['W1mag'] - VHzQ_zslice['W2mag']), (VHzQ_zslice['zMag'] - VHzQ_zslice['W2mag']), c='blue', s=ms)
#hdl = ax1.scatter( (VHzQ_zslice['W1mag'] - VHzQ_zslice['W2mag']), (VHzQ_zslice['zMag'] - VHzQ_zslice['W2mag']), c=VHzQ_zslice['redshift'], cmap=cmap, s=ms)
#sleep(0.1)


## Normally, this is:: left, bottom, width, height
## but with orientation='horizontal', then
## left, up,  length, height
datco   = [0.56, 0.28, 0.20, 0.025]     ## W1-W2 SNR
#cbar_ax = fig.add_axes(datco)
##clevs   = [5.2, 6.3, 7.4]  ## redshift
#clevs   = [redshift_min, redshift_max]  ## redshift
#cb1     = plt.colorbar(hdl, cax=cbar_ax, orientation='horizontal', ticks=clevs)
#cb1.set_label(r'redshift', labelpad=0, fontsize=16)

#ax1.legend(['','', 'L dwarfs', 'T dwarfs', '', ''],loc="lower left", ncol=1, fontsize=16)

              
ax1.tick_params(axis='both', which='major', labelsize=ticklabelsize, top='on', right='on', direction='in', length=majorticklength, width=tickwidth)
ax1.tick_params(axis='both', which='minor', labelsize=ticklabelsize, top='on', right='on', direction='in', length=minorticklength, width=tickwidth)

ax1.set_xlabel(r" $W1_{Vega}$   - $W1_{Vega}$  ", fontsize=labelsize)
ax1.set_ylabel(r" $z_{AB}$ - $W2_{Vega}$ ", fontsize=labelsize)

plt.savefig('W1W2_vs_zW2_Carnall_temp.png', format='png')
plt.close(fig)

#plt.show()
