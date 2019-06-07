'''
  Banados 2016 figures (3)
  Carnall z-W1, W1-W2 (1)
  W123 (1) 
  HSC SHELLQS plots (??)
  In the ‘exact’ style of the Banado2016 figures...
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


##
##  V H z Q    data
##
path = '/cos_pc19a_npr/data/highest_z_QSOs/'
#filename ='THE_TABLE_v0pnt96.dat'
filename  ='THE_TABLE_v0pnt97x_PS1_ULAS_VHS_photom_v2.dat'
table=path+filename
VHzQ = ascii.read(table)

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
Ldwarfs = Ldwarfs[np.where( (Ldwarfs['W3snr'] > 3.0))]

path = '/cos_pc19a_npr/data/highest_z_QSOs/LT_dwarfs/'
filename ='Tdwarfs_photom_v1pnt00.dat'
table=path+filename
Tdwarfs = ascii.read(table)
#Tdwarfs = Ldwarfs[np.where( (Tdwarfs['W3snr'] > 3.0))]


## 
##  Making the plot(s)
##
plt.rcParams.update({'font.size': 14})
#matplotlib.rc('text', usetex=True)

## https://matplotlib.org/examples/pylab_examples/subplots_demo.html
fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(18, 7), sharey=True, num=None, dpi=80, facecolor='w', edgecolor='k')


redshift_clrmap = (10**(redshift-5.15))
redshift_clrmap = redshift
ms_clrsize  = ((redshift-3.9)**5.5)

labelsize       = 20
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
##  ...  vs. W1-W2
##
ymin=-1.0; ymax=4.0


xmin=-0.5; xmax=4.0 
cmap = plt.cm.jet
ax1.axis([xmin, xmax, ymin, ymax])

ax1.scatter((Ldwarfs['yMag']-Ldwarfs['W1mag']), (Ldwarfs['W1mag']-Ldwarfs['W2mag']), c='k', s=ms_small*1.7)
ax1.scatter((Tdwarfs['yMag']-Tdwarfs['W1mag']), (Tdwarfs['W1mag']-Tdwarfs['W2mag']), c='k', s=ms_small*1.7)
ax1.scatter((Ldwarfs['yMag']-Ldwarfs['W1mag']), (Ldwarfs['W1mag']-Ldwarfs['W2mag']), c='orangered', s=ms_small)
ax1.scatter((Tdwarfs['yMag']-Tdwarfs['W1mag']), (Tdwarfs['W1mag']-Tdwarfs['W2mag']), c='darkred',   s=ms_small)
ax1.scatter( (y_PS1 - W1mag), (W1mag - W2mag), c='k',     s=ms*1.7)
ax1.scatter( (y_PS1 - W1mag), (W1mag - W2mag), c=redshift, cmap=cmap, s=ms)
ax1.plot(0.00, 0.00, marker='o', markersize=30, color="white")

ax1.tick_params(axis='both', which='major', labelsize=ticklabelsize, top='on', right='on', direction='in', length=majorticklength, width=tickwidth)
ax1.tick_params(axis='both', which='minor', labelsize=ticklabelsize, top='on', right='on', direction='in', length=minorticklength, width=tickwidth)
ax1.set_xlabel(r" $y_{AB}$ - $W1_{Vega}$  ", fontsize=labelsize)
ax1.set_ylabel(r" $W1_{Vega}$ - $W2_{Vega}$ ", fontsize=labelsize)


## ymin=-0.5; ymax=4.0; xmin=-1.0; xmax=7.0  in Wright et al. (2010)
xmin=-1.5; xmax=7.1
cmap = plt.cm.rainbow
ax2.axis([xmin, xmax, ymin, ymax])

ax2.scatter((Ldwarfs['W2mag']-Ldwarfs['W3mag']), (Ldwarfs['W1mag']-Ldwarfs['W2mag']), c='k', s=ms_small*1.7)
ax2.scatter((Tdwarfs['W2mag']-Tdwarfs['W3mag']), (Tdwarfs['W1mag']-Tdwarfs['W2mag']), c='k', s=ms_small*1.7)
ax2.scatter((Ldwarfs['W2mag']-Ldwarfs['W3mag']), (Ldwarfs['W1mag']-Ldwarfs['W2mag']), c='orangered', s=ms_small)
ax2.scatter((Tdwarfs['W2mag']-Tdwarfs['W3mag']), (Tdwarfs['W1mag']-Tdwarfs['W2mag']), c='darkred',   s=ms_small)
ax2.scatter( (W2mag - W3mag), (W1mag - W2mag), c='k',     s=ms*1.7)
ax2.scatter( (W2mag - W3mag), (W1mag - W2mag), c=redshift, cmap=cmap, s=ms)
ax2.plot(0.00, 0.00, marker='o', markersize=30, color="white")

ax2.tick_params(axis='x', which='major', labelsize=ticklabelsize, top='on', right='on', direction='in', length=majorticklength, width=tickwidth)
ax2.tick_params(axis='x', which='minor', labelsize=ticklabelsize, top='on', right='on', direction='in', length=minorticklength, width=tickwidth)
ax2.set_xlabel(r" $W2_{Vega}$ - $W3_{Vega}$ ", fontsize=labelsize)



xmin=-1.0; xmax=7.0
cmap = plt.cm.rainbow
ax3.axis([xmin, xmax, ymin, ymax])

ax3.scatter((Ldwarfs['zMag']-Ldwarfs['W2mag']), (Ldwarfs['W1mag']-Ldwarfs['W2mag']), c='k', s=ms_small*1.7)
ax3.scatter((Tdwarfs['zMag']-Tdwarfs['W2mag']), (Tdwarfs['W1mag']-Tdwarfs['W2mag']), c='k', s=ms_small*1.7)
ax3.scatter((Ldwarfs['zMag']-Ldwarfs['W2mag']), (Ldwarfs['W1mag']-Ldwarfs['W2mag']), c='orangered', s=ms_small)
ax3.scatter((Tdwarfs['zMag']-Tdwarfs['W2mag']), (Tdwarfs['W1mag']-Tdwarfs['W2mag']), c='darkred',   s=ms_small)
ax3.scatter( (z_PS1 - W2mag), (W1mag - W2mag), c='k',     s=ms*1.7)
ax3.scatter( (z_PS1 - W2mag), (W1mag - W2mag), c=redshift, cmap=cmap, s=ms)
ax3.plot(0.00, 0.00, marker='o', markersize=30, color="white")

ax3.tick_params(axis='x', which='major', labelsize=ticklabelsize, top='on', right='on', direction='in', length=majorticklength, width=tickwidth)
ax3.tick_params(axis='x', which='minor', labelsize=ticklabelsize, top='on', right='on', direction='in', length=minorticklength, width=tickwidth)
ax3.set_xlabel(r" $z_{AB}$ - $W2_{Vega}$  ", fontsize=labelsize)


plt.savefig('W1W2_colors_temp.png', format='png')
plt.close(fig)

#plt.show()

