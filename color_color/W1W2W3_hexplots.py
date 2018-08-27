import numpy as np
from astropy.io import fits
from astropy.io import ascii

from astropy.table import Table

import matplotlib
import matplotlib.pyplot as plt

##
## DR14Q
##
path = '/cos_pc19a_npr/data/SDSS/DR14Q/'
filename ='DR14Q_v4_4.fits'
#filename ='DR14Q_v4_4_W4good.fits'
infile = path+filename
data = fits.getdata(infile, 1)
dr14q = Table(data)

##
##  V H z Q    data
##
path = '/cos_pc19a_npr/data/highest_z_QSOs/'
filename ='THE_TABLE_v0pnt96.dat'
table=path+filename
VHzQ = ascii.read(table)



##  Making the plot(s)
## 
##  W2-W3  vs.  W1-W2 
##
plt.rcParams.update({'font.size': 14})
fig, ax = plt.subplots(figsize=(10, 7), num=None, dpi=80, facecolor='w', edgecolor='k')

## Blain et al. (2013), Figure 1
ymin = -0.2
ymax =  2.0 
## W2-W3 vs. W1-W2
xmin =  1.7   
xmax =  4.7
##    W2 vs. W1-W2
#xmin =  10.0   
#xmax =  17.3

xmin=1.0; xmax=6.0; ymin=-0.5; ymax=2.5

#cmap = plt.cm.RdBu_r
#cmap = plt.cm.inferno
cmap = plt.cm.rainbow

ax.axis([xmin, xmax, ymin, ymax])

hb = ax.hexbin( (dr14q['W2MAG']- dr14q['W3MAG']), (dr14q['W1MAG'] - dr14q['W2MAG']), C=dr14q['Z'],
            gridsize=180, mincnt=25, marginals=False, cmap=cmap, vmin=0.00, vmax=3.00)
cb = fig.colorbar(hb, ax=ax)
cb.set_label('redshift')

ax.scatter((VHzQ['w2mag'] -  VHzQ['w3mag']),  (VHzQ['w1mag'] - VHzQ['w2mag']), color='k')

## The vertical dashed line at W 2 − W3 = 5.3 is one of the selection
## criteria for W1W2-dropouts; some are bluer than this because they
## satisfied the W2 − W4 > 8.2 criterion.
lw = 2.0
ax.axvline(x=5.3, linewidth=lw,linestyle='dotted', color='k')

ax.tick_params(axis='both', which='major', labelsize=24, top='on', right='on', direction='in', length=12, width=2)
ax.tick_params(axis='both', which='minor', labelsize=24, top='on', right='on', direction='in', length=6,  width=2)

ax.set_xlabel(r" W2 - W3 ", fontsize=24)
ax.set_ylabel(r" W1 - W2 ", fontsize=24)

#plt.savefig('W1W2W3_hexplots_temp.png', format='png')
plt.show()
#plt.close()
