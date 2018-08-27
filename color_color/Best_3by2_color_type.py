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
7.5400
g -1.000     -1.000
r -1.000     -1.000
i -1.000     -1.000
z -1.000     -1.000
y -1.000     -1.000

Y 20.840      0.191
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
fig, ((ax1, ax2), (ax4, ax5), (ax7, ax8)) = plt.subplots(3, 2, figsize=(14, 16), num=None, dpi=80, facecolor='w', edgecolor='k')
#fig, ((ax1, ax2, ax3), (ax4, ax5, ax6), (ax7, ax8, ax9)) = plt.subplots(3, 3, figsize=(10, 10), num=None, dpi=80, facecolor='w', edgecolor='k')

cmap = plt.cm.plasma
#cmap = plt.cm.rainbow

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


##
##  T O P    R O W
##
##  z-J vs.J - W1 
xmin=0.05; xmax=3.8; ymin=-0.1; ymax=4.2
cmap = plt.cm.jet
ax1.axis([xmin, xmax, ymin, ymax])
ax1.scatter( (z_PS1 - Jmag), (Jmag - W1mag), c=redshift, cmap=cmap, s=ms_clrsize, alpha=0.85)
ax1.tick_params(axis='both', which='major', labelsize=ticklabelsize, top='on', right='on', direction='in', length=majorticklength, width=tickwidth)
ax1.tick_params(axis='both', which='minor', labelsize=ticklabelsize, top='on', right='on', direction='in', length=minorticklength, width=tickwidth)
ax1.set_xlabel(r" $z_{AB}$   - $J_{Vega}$  ", fontsize=labelsize)
ax1.set_ylabel(r" $J_{Vega}$ - $W1_{Vega}$ ", fontsize=labelsize)

xmin=-0.1; xmax=3.1; ymin=-1.0; ymax=4.0
cmap = plt.cm.rainbow
ax2.axis([xmin, xmax, ymin, ymax])
ax2.scatter((z_PS1-y_PS1), (y_PS1 - Jmag), c=redshift_clrmap, cmap=cmap, s=ms, alpha=0.85)
ax2.plot(0.00, 0.00, marker='o', markersize=30, color="white")

ax2.tick_params(axis='both', which='major', labelsize=ticklabelsize, top='on', right='on', direction='in', length=majorticklength, width=tickwidth)
ax2.tick_params(axis='both', which='minor', labelsize=ticklabelsize, top='on', right='on', direction='in', length=minorticklength, width=tickwidth)
ax2.set_xlabel(r" $z_{AB}$  - $y_{AB}$  ", fontsize=labelsize)
ax2.set_ylabel(r" $y_{AB}$ - $J_{Vega}$ ", fontsize=labelsize)


'''
xmin=10.0; xmax=20.0; ymin=-0.5; ymax=2.5
cmap = plt.cm.rainbow
ax3.axis([xmin, xmax, ymin, ymax])
ax3.scatter(w2mag, (w1mag-w2mag), s=ms, alpha=0.85)
ax3.tick_params(axis='both', which='major', labelsize=ticklabelsize, top='on', right='on', direction='in', length=majorticklength, width=tickwidth)
ax3.tick_params(axis='both', which='minor', labelsize=ticklabelsize, top='on', right='on', direction='in', length=minorticklength, width=tickwidth)
ax3.set_xlabel(r" W2 - W3 ", fontsize=labelsize)
ax3.set_ylabel(r" W1 - W2 ", fontsize=labelsize)
'''


##
##   M I D D L E   R O W
##
xmin=-0.5; xmax=4.3; ymin=-0.5; ymax=2.8
cmap = plt.cm.rainbow
ax4.axis([xmin, xmax, ymin, ymax])
ax4.scatter( (i_PS1-z_PS1), (z_PS1 - y_PS1), c=redshift_clrmap, cmap=cmap, s=ms, alpha=0.85)
ax4.plot(0.00, 0.00, marker='o', markersize=30, color="white")

ax4.tick_params(axis='both', which='major', labelsize=ticklabelsize, top='on', right='on', direction='in', length=majorticklength, width=tickwidth)
ax4.tick_params(axis='both', which='minor', labelsize=ticklabelsize, top='on', right='on', direction='in', length=minorticklength, width=tickwidth)
ax4.set_xlabel(r" $i_{AB}$  - $z_{AB}$  ", fontsize=labelsize)
ax4.set_ylabel(r" $z_{AB}$  - $y_{AB}$  ", fontsize=labelsize)

xmin=-0.75; xmax=1.6; ymin=-0.4; ymax=4.2
cmap = plt.cm.jet
ax5.axis([xmin, xmax, ymin, ymax])
ax5.scatter( (z_PS1 - y_PS1), (i_PS1-z_PS1), c=redshift_clrmap, cmap=cmap, s=ms, alpha=0.85)
ax5.plot(0.00, 0.00, marker='o', markersize=30, color="white")
ax5.tick_params(axis='both', which='major', labelsize=ticklabelsize, top='on', right='on', direction='in', length=majorticklength, width=tickwidth)
ax5.tick_params(axis='both', which='minor', labelsize=ticklabelsize, top='on', right='on', direction='in', length=minorticklength, width=tickwidth)
ax5.set_xlabel(r" $z_{AB}$  - $y_{AB}$  ", fontsize=labelsize)
ax5.set_ylabel(r" $i_{AB}$  - $z_{AB}$  ", fontsize=labelsize)

'''
xmin=10.0; xmax=20.0; ymin=-0.5; ymax=2.5
cmap = plt.cm.rainbow
ax6.axis([xmin, xmax, ymin, ymax])
ax6.scatter(w2mag, (w1mag-w2mag), s=ms, alpha=0.85)
ax6.tick_params(axis='both', which='major', labelsize=ticklabelsize, top='on', right='on', direction='in', length=majorticklength, width=tickwidth)
ax6.tick_params(axis='both', which='minor', labelsize=ticklabelsize, top='on', right='on', direction='in', length=minorticklength, width=tickwidth)
ax6.set_xlabel(r" W2 - W3 ", fontsize=labelsize)
ax6.set_ylabel(r" W1 - W2 ", fontsize=labelsize)
'''


##
##  B O T T O M   R O W 
##
xmin=-0.4; xmax=2.3; ymin=-0.5; ymax=2.5
cmap = plt.cm.plasma
ax7.axis([xmin, xmax, ymin, ymax])
ax7.scatter( (y_PS1 - Jmag), (Ymag - Jmag), c=redshift_clrmap, cmap=cmap, s=ms, alpha=0.85)
ax7.plot(0.00, 0.00, marker='o', markersize=30, color="white")
ax7.tick_params(axis='both', which='major', labelsize=ticklabelsize, top='on', right='on', direction='in', length=majorticklength, width=tickwidth)
ax7.tick_params(axis='both', which='minor', labelsize=ticklabelsize, top='on', right='on', direction='in', length=minorticklength, width=tickwidth)
ax7.set_xlabel(r" $y_{AB}$   - $J_{Vega}$  ", fontsize=labelsize)
ax7.set_ylabel(r" $Y_{Vega}$ - $J_{Vega}$  ", fontsize=labelsize)

xmin=-0.9; xmax=1.8; ymin=-0.5; ymax=1.8
cmap = plt.cm.cool
ax8.axis([xmin, xmax, ymin, ymax])
ax8.scatter( (y_PS1 - Ymag), (Ymag - Jmag), c=redshift_clrmap, cmap=cmap, s=ms, alpha=0.85)
ax8.plot(0.00, 0.00, marker='o', markersize=30, color="white")
ax8.tick_params(axis='both', which='major', labelsize=ticklabelsize, top='on', right='on', direction='in', length=majorticklength, width=tickwidth)
ax8.tick_params(axis='both', which='minor', labelsize=ticklabelsize, top='on', right='on', direction='in', length=minorticklength, width=tickwidth)
ax8.set_xlabel(r" $y_{AB}$   - $Y_{Vega}$  ", fontsize=labelsize)
ax8.set_ylabel(r" $Y_{Vega}$ - $J_{Vega}$  ", fontsize=labelsize)

'''
xmin=10.0; xmax=20.0; ymin=-0.5; ymax=2.5
cmap = plt.cm.rainbow
ax9.axis([xmin, xmax, ymin, ymax])
ax9.scatter(w2mag, (w1mag-w2mag), s=ms, alpha=0.85)
ax9.tick_params(axis='both', which='major', labelsize=ticklabelsize, top='on', right='on', direction='in', length=majorticklength, width=tickwidth)
ax9.tick_params(axis='both', which='minor', labelsize=ticklabelsize, top='on', right='on', direction='in', length=minorticklength, width=tickwidth)
ax9.set_xlabel(r" W2 - W3 ", fontsize=labelsize)
ax9.set_ylabel(r" W1 - W2 ", fontsize=labelsize)
'''


plt.show()

