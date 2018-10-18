'''
Making the 'famous' W2-W3 vs. W1-W2 WISE color-color plot
'''

import numpy as np
from astropy.io    import fits
from astropy.io    import ascii
from astropy.table import Table

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

##
##  V H z Q    data
##
path = '/cos_pc19a_npr/programs/quasars/highest_z/data/'
filename ='THE_TABLE_v0pnt981_temp.ascii'
table=path+filename
VHzQ = ascii.read(table)

redshift = VHzQ['redshift']
w1mag    = VHzQ['w1mag']
w2mag    = VHzQ['w2mag']
unWISE_W1 = (-2.5)*(np.log10(VHzQ['FLUX_1']))+22.5
unWISE_W2 = (-2.5)*(np.log10(VHzQ['FLUX_2']))+22.5


##
##  Making the plot(s)
## 
##     W2  vs.  W1-W2      Assef  R90  and  C75
##
plt.rcParams.update({'font.size': 14})
plt.style.use('dark_background')

## works well for xmin=13.6; xmax=16.9; ymin=-0.2; ymax=3.2:: 
fig, ax = plt.subplots(figsize=(14, 10), num=None, dpi=80, facecolor='w', edgecolor='k')  ## works well

## Setting the x-, y-axis ranges
xmin=4.9; xmax=7.7; ymin=12.5; ymax=19.6   # Good for redshift vs. W1/2 mags
xmin=4.9; xmax=7.7; ymin=-2.05; ymax=2.05   # Good for redshift vs. W1/2 mags

#cmap = plt.cm.RdBu_r
#cmap = plt.cm.inferno
cmap = plt.cm.rainbow
fontsize        = 30
ls              = fontsize
lw              = 2.0
ticklength      = 18
tickwidth       = 2.0
pointsize       = 60
pointsize_large = pointsize*1.8
alpha           = 1.00

##
## Plotting the    V H z Q    points
##
##   Redshift vs. color
#ax.scatter( redshift, VHzQ['w1mag'], color='k', alpha=alpha, s=pointsize_large, label='')
#ax.scatter( redshift, VHzQ['w1mag'], color='r', alpha=alpha, s=pointsize, label='ALLWISE W1')
#ax.scatter( redshift, VHzQ['w2mag'], color='k', alpha=alpha, s=pointsize_large, label='')
#ax.scatter( redshift, VHzQ['w2mag'], color='c', alpha=alpha, s=pointsize, label='ALLWISE W2')
#
#ax.scatter( redshift, unWISE_W1, color='k', alpha=alpha, s=pointsize_large,   label='')
#ax.scatter( redshift, unWISE_W1, color='orangered', alpha=alpha, s=pointsize, label='unWISE W1')
#ax.scatter( redshift, unWISE_W2, color='k', alpha=alpha, s=pointsize_large,   label='')
#ax.scatter( redshift, unWISE_W2, color='cyan', alpha=alpha, s=pointsize,      label='unWISE W2')

## looking at the differences in W1/2 mags
#ax.scatter( redshift, (unWISE_W1-VHzQ['w1mag']), color='k', alpha=alpha, s=pointsize_large,   label='')
#ax.scatter( redshift, (unWISE_W1-VHzQ['w1mag']), color='orangered', alpha=alpha, s=pointsize, label='W1 band')
#ax.scatter( redshift, (unWISE_W2-VHzQ['w2mag']), color='k', alpha=alpha, s=pointsize_large,   label='')
#ax.scatter( redshift, (unWISE_W2-VHzQ['w2mag']), color='cyan', alpha=alpha, s=pointsize,      label='W2 band')


ax.axis([xmin, xmax, ymin, ymax])
ax.tick_params(axis='both', which='major', labelsize=ls, top=True, right=True, direction='in', length=ticklength,   width=tickwidth)
ax.tick_params(axis='both', which='minor', labelsize=ls, top=True, right=True, direction='in', length=ticklength/2, width=tickwidth)
#ax.tick_params(axis='x', which='minor', bottom=True)
#ax.tick_params(axis='y', which='minor', bottom=True)

majorLocator = MultipleLocator(1.0)
minorLocator = MultipleLocator(0.2)
ax.xaxis.set_major_locator(majorLocator)
ax.xaxis.set_minor_locator(minorLocator)
#ax.xaxis.set_major_formatter(majorFormatter)

majorLocator = MultipleLocator(1.0)
minorLocator = MultipleLocator(0.2)
ax.yaxis.set_major_locator(majorLocator)
ax.yaxis.set_minor_locator(minorLocator)

legend = ax.legend(loc='lower right', shadow=True, fontsize='xx-large', frameon='True')
#legend.get_frame().set_facecolor('C2')
legend.get_frame().set_edgecolor('w')

ax.set_xlabel(r" redshift ",    fontsize=fontsize)
#ax.set_ylabel(r"unWISE - ALLWISE", fontsize=fontsize)
ax.set_ylabel(r" W1/W2 mag  (Vega) ", fontsize=fontsize)

plt.savefig('ALLvUnWISE_redshiftmag_temp.png', format='png')
#plt.show()
#plt.close()
