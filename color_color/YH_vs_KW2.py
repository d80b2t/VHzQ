'''
 Y-H vs. K-W2
   
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
path = '/cos_pc19a_npr/programs/quasars/highest_z/data/'
filename ='VHzQs_ZYJHK_WISE.dat'
table=path+filename
VHzQ = ascii.read(table)
#VHzQ = VHzQ[np.where( (VHzQ['redshift'] >= 5.7) & (VHzQ['redshift'] <= 6.7))]

redshift = VHzQ['redshift']
Zmag  = VHzQ['Z']
Ymag  = VHzQ['Y']
Jmag  = VHzQ['J']
Hmag  = VHzQ['H']
Kmag  = VHzQ['K']
W1mag = VHzQ['unW1mag']
W2mag = VHzQ['unW2mag']
W3mag = VHzQ['w3mpro']
W4mag = VHzQ['w4mpro']


##
## Late Type stellar colours
##
## spider.ipac.caltech.edu/staff/davy/ARCHIVE/index.shtml
##
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

fig, ax1 = plt.subplots(1, figsize=(10, 10), num=None, dpi=80, facecolor='w', edgecolor='k')

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
##    (Y - H)   vs.  (K - W2)
##   
xmin=-0.5; xmax=3.5; ymin=1.5; ymax=5.2

cmap = plt.cm.jet
ax1.axis([xmin, xmax, ymin, ymax])

ax1.scatter( (Ldwarfs['yMag']-Ldwarfs['Hmag']),  (Ldwarfs['Kmag']-Ldwarfs['W2mag']), c='k', s=ms_small*1.7)
ax1.scatter( (Tdwarfs['yMag']-Tdwarfs['Hmag']),  (Tdwarfs['Kmag']-Tdwarfs['W2mag']), c='k', s=ms_small*1.7)
ax1.scatter( (Ldwarfs['yMag']-Ldwarfs['Hmag']),  (Ldwarfs['Kmag']-Ldwarfs['W2mag']), c='orangered', s=ms_small, label='L dwarfs')
ax1.scatter( (Tdwarfs['yMag']-Tdwarfs['Hmag']),  (Tdwarfs['Kmag']-Tdwarfs['W2mag']), c='darkred',   s=ms_small, label='T dwarfs')

ax1.scatter( (VHzQ['Y'] - VHzQ['H']), (VHzQ['K'] - VHzQ['unW2mag']), c='k', s=ms*1.7)
ax1.scatter( (VHzQ['Y'] - VHzQ['H']), (VHzQ['K'] - VHzQ['unW2mag']), c=redshift_clrmap, s=ms)

              
ax1.tick_params(axis='both', which='major', labelsize=ticklabelsize, top='on', right='on', direction='in', length=majorticklength, width=tickwidth)
ax1.tick_params(axis='both', which='minor', labelsize=ticklabelsize, top='on', right='on', direction='in', length=minorticklength, width=tickwidth)

ax1.set_xlabel(r" $Y_{AB}$ - $H_{AB}$  ",  fontsize=labelsize)
ax1.set_ylabel(r" $K_{AB}$ - $W2_{AB}$ ",  fontsize=labelsize)

plt.savefig('YH_vs_KW2_temp.png', format='png')
plt.close(fig)

#plt.show()
