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
filename ='temp2.dat'
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
7.5400
g -1.000     -1.000
r -1.000     -1.000
i -1.000     -1.000
z -1.000     -1.000
y -1.000     -1.000

Y 20.840         0.191
J 19.816      0.108
H 18.639      0.119
K 18.132      0.123

17.471    0.146    7.400
16.769    0.295    3.700
12.834    0.498    2.200
9.256   -9.990   -1.100

(z-J) = 

'''

##  Making the plot(s)
plt.rcParams.update({'font.size': 14})
#matplotlib.rc('text', usetex=True)

## https://matplotlib.org/examples/pylab_examples/subplots_demo.html
#fig, (ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9) = plt.subplots(9, figsize=(10, 14), num=None, dpi=80, facecolor='w', edgecolor='k', sharex=True)
fig, (ax1, ax2, ax3, ax4, ax5, ax6 ) = plt.subplots(6,  figsize=(10, 14), sharex=True)

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
ms       = 120.


##  x-axis; redshift
xmin=4.8; xmax=7.7

fig.subplots_adjust(hspace=0)

ymin=-1.3; ymax=3.8
cmap = plt.cm.jet
w = VHzQ[np.where( (i_PS1 - z_PS1 != 0.00))]
ms_clrsize  = ((w['redshift']-3.9)**5.5)
ax1.axis([xmin, xmax, ymin, ymax])
#ax1.scatter( redshift, (i_PS1 - z_PS1), s=ms_clrsize, alpha=0.85)
#ax1.scatter( w['redshift'], (w['iMag'] - w['zMag']), c=w['redshift'], cmap=cmap, s=ms_clrsize, alpha=0.85)
ax1.scatter( w['redshift'], (w['iMag'] - w['zMag']), c=w['redshift'], cmap=cmap, s=ms)
#ax1.tick_params(axis='y', which='major', labelsize=ticklabelsize, top='on', right='on', direction='in', length=majorticklength, width=tickwidth)
#ax1.tick_params(axis='both', which='minor', labelsize=ticklabelsize, top='on', right='on', direction='in', length=minorticklength, width=tickwidth)
ax1.set_ylabel(r" i - z ", fontsize=labelsize)
fig.subplots_adjust(hspace=0)


ymin=-1.0; ymax=3.8
cmap = plt.cm.rainbow
ax2.axis([xmin, xmax, ymin, ymax])
w = VHzQ[np.where( (z_PS1 - Jmag != 0.00))]
ms_clrsize  = ((w['redshift']-3.9)**5.5)
#ax2.scatter(    redshift,   (z_PS1 - Jmag), s=ms, alpha=0.85)
ax2.scatter( w['redshift'], (w['zMag'] - w['Jmag']), c=w['redshift'], cmap=cmap, s=ms)
#ax2.tick_params(axis='both', which='major', labelsize=ticklabelsize, top='on', right='on', direction='in', length=majorticklength, width=tickwidth)
#ax2.tick_params(axis='both', which='minor', labelsize=ticklabelsize, top='on', right='on', direction='in', length=minorticklength, width=tickwidth)
ax2.set_ylabel(r" z - J ", fontsize=labelsize)
fig.subplots_adjust(hspace=0)


ymin=-1.5; ymax=3.8
cmap = plt.cm.rainbow
w = VHzQ[np.where( (z_PS1 - y_PS1 != 0.00))]
ms_clrsize  = ((w['redshift']-3.9)**5.5)
ax3.axis([xmin, xmax, ymin, ymax])
#ax3.scatter(redshift, (z_PS1 - y_PS1), s=ms, alpha=0.85)
ax3.scatter(w['redshift'], (w['zMag'] - w['yMag']), c=w['redshift'], cmap=cmap,  s=ms)
#ax3.tick_params(axis='both', which='major', labelsize=ticklabelsize, top='on', right='on', direction='in', length=majorticklength, width=tickwidth)
#ax3.tick_params(axis='both', which='minor', labelsize=ticklabelsize, top='on', right='on', direction='in', length=minorticklength, width=tickwidth)
ax3.set_ylabel(r" z - y ", fontsize=labelsize)
fig.subplots_adjust(hspace=0)


ymin=2.0; ymax=7.8
cmap = plt.cm.rainbow
w = VHzQ[np.where( (z_PS1 - W2mag != 0.00))]
ms_clrsize  = ((w['redshift']-3.9)**5.5)
ax4.axis([xmin, xmax, ymin, ymax])
#ax4.scatter(   redshift,   (z_PS1 - W2mag), c=redshift_clrmap, cmap=cmap, s=ms)
ax4.scatter(w['redshift'], (w['zMag'] - w['W2mag']), c=w['redshift'], cmap=cmap,  s=ms)
#ax4.tick_params(axis='both', which='major', labelsize=ticklabelsize, top='on', right='on', direction='in', length=majorticklength, width=tickwidth)
#ax4.tick_params(axis='both', which='minor', labelsize=ticklabelsize, top='on', right='on', direction='in', length=minorticklength, width=tickwidth)
ax4.set_ylabel(r" z - W2 ", fontsize=labelsize)


ymin=1.0; ymax=6.8
cmap = plt.cm.jet
w = VHzQ[np.where( (y_PS1 - W2mag != 0.00))]
ms_clrsize  = ((w['redshift']-3.9)**5.5)
ax5.axis([xmin, xmax, ymin, ymax])
#ax5.scatter(   redshift,   (y_PS1 - W1mag),          c=redshift_clrmap, cmap=cmap, s=ms)
ax5.scatter(w['redshift'], (w['yMag'] - w['W2mag']), c=w['redshift'],   cmap=cmap,  s=ms)
#ax5.tick_params(axis='both', which='major', labelsize=ticklabelsize, top='on', right='on', direction='in', length=majorticklength, width=tickwidth)
#ax5.tick_params(axis='both', which='minor', labelsize=ticklabelsize, top='on', right='on', direction='in', length=minorticklength, width=tickwidth)
ax5.set_ylabel(r" y - W2 ", fontsize=labelsize)


ymin=-0.8; ymax=1.8
cmap = plt.cm.rainbow
w = VHzQ[np.where( (Ymag - Jmag != 0.00))]
ms_clrsize  = ((w['redshift']-3.9)**5.5)
ax6.axis([xmin, xmax, ymin, ymax])
#ax6.scatter(   redshift,   (Ymag-Jmag), c=redshift_clrmap, cmap=cmap,s=ms)
ax6.scatter(w['redshift'], (w['Yapermag'] - w['Jmag']), c=w['redshift'],   cmap=cmap,  s=ms)
#ax6.tick_params(axis='both', which='major', labelsize=ticklabelsize, top='on', right='on', direction='in', length=majorticklength, width=tickwidth)
#ax6.tick_params(axis='both', which='minor', labelsize=ticklabelsize, top='on', right='on', direction='in', length=minorticklength, width=tickwidth)
ax6.set_ylabel(r" Y - J ", fontsize=labelsize)
fig.subplots_adjust(hspace=0)


'''
ymin=-1.0; ymax=6.8
cmap = plt.cm.plasma
ax7.axis([xmin, xmax, ymin, ymax])
ax7.scatter( redshift, (Ymag - W1mag), c=redshift_clrmap, cmap=cmap, s=ms, alpha=0.85)
#ax7.tick_params(axis='both', which='major', labelsize=ticklabelsize, top='on', right='on', direction='in', length=majorticklength, width=tickwidth)
#ax7.tick_params(axis='both', which='minor', labelsize=ticklabelsize, top='on', right='on', direction='in', length=minorticklength, width=tickwidth)
ax7.set_ylabel(r" $Y_{Vega}$ - $W1_{Vega}$  ", fontsize=labelsize)
fig.subplots_adjust(hspace=0)


ymin=-0.5; ymax=1.8
cmap = plt.cm.cool
ax8.axis([xmin, xmax, ymin, ymax])
ax8.scatter( redshift, (W1mag - W2mag), c=redshift_clrmap, cmap=cmap, s=ms, alpha=0.85)
#ax8.tick_params(axis='both', which='major', labelsize=ticklabelsize, top='on', right='on', direction='in', length=majorticklength, width=tickwidth)
#ax8.tick_params(axis='both', which='minor', labelsize=ticklabelsize, top='on', right='on', direction='in', length=minorticklength, width=tickwidth)
ax8.set_ylabel(r" $W1_{Vega}$ - $W2_{Vega}$  ", fontsize=labelsize)
fig.subplots_adjust(hspace=0)


ymin=-0.5; ymax=2.5
cmap = plt.cm.rainbow
ax9.axis([xmin, xmax, ymin, ymax])
ax9.scatter(redshift, (W2mag-W3mag), s=ms, alpha=0.85)
ax9.tick_params(axis='x', which='major', labelsize=ticklabelsize, top='on', right='on', direction='in', length=majorticklength, width=tickwidth)
#ax9.tick_params(axis='x', which='minor', labelsize=ticklabelsize, top='on', right='on', direction='in', length=minorticklength, width=tickwidth)
ax9.set_ylabel(r" $W2_{Vega}$ - $W3_{Vega}$  ", fontsize=labelsize)
fig.subplots_adjust(hspace=0)
'''

ax6.set_xlabel(r" redshift ", fontsize=labelsize)

plt.show()

