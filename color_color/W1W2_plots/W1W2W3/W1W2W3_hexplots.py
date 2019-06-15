'''
Making the 'famous' W2-W3 vs. W1-W2 WISE color-color plot
e.g. Figure 12 of Wright et al. (2010) and lots of other
places too...

Good links::
 http://www.sc.eso.org/~bdias/pycoffee/codes/20160407/gridspec_demo.html
 https://stackoverflow.com/questions/33737427/top-label-for-matplotlib-colorbars/33740567
 https://pythonmatplotlibtips.blogspot.com/2018/10/combine-two-contourf-and-two-colorbar-in-one-figure-matplotlib.html
 https://jakevdp.github.io/PythonDataScienceHandbook/04.07-customizing-colorbars.html
 https://jdhao.github.io/2017/06/11/mpl_multiplot_one_colorbar/
'''

import numpy as np
from astropy.io    import fits
from astropy.io    import ascii
from astropy.table import Table

import fitsio
from fitsio import FITS,FITSHDR

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

##
## DR14Q
##
path      = '/cos_pc19a_npr/data/SDSS/DR14Q/'
filename  ='DR14Q_v4_4.fits'
#filename ='DR14Q_v4_4_W4good.fits'
infile    = path+filename
#data      = fits.getdata(infile, 1)
data      = fitsio.read(infile,1)
dr14q     = Table(data)

## Vega to AB conversion
dr14q['W1MAG'] =  dr14q['W1MAG'] + 2.673
dr14q['W2MAG'] =  dr14q['W2MAG'] + 3.313
dr14q['W3MAG'] =  dr14q['W3MAG'] + 5.148
dr14q['W4MAG'] =  dr14q['W4MAG'] + 6.66

dr14q_W1minW2 = (dr14q['W1MAG'] - dr14q['W2MAG'])
dr14q_W2minW3 = (dr14q['W2MAG'] - dr14q['W3MAG'])


##
##  V H z Q    data
##
path      = '/cos_pc19a_npr/programs/quasars/highest_z/data/'
filename  = 'VHzQs_ZYJHK_WISE.dat'
table     = path+filename
VHzQ_full = ascii.read(table)

## Vega to AB conversion
VHzQ_full['unW1mag'] = VHzQ_full['unW1mag'] - 0.004 + 2.673
VHzQ_full['unW2mag'] = VHzQ_full['unW2mag'] - 0.032 + 3.313
VHzQ_full['w3mpro']  = VHzQ_full['w3mpro'] + 5.148
VHzQ_full['w4mpro']  = VHzQ_full['w4mpro'] + 6.66


## in case you want to select on e.g. snr
VHzQ        = VHzQ_full
VHzQ_goodW3 = VHzQ_full[np.where(VHzQ_full['w3snr'] >3.0)]


##  Making the plot(s)
## 
##  W2-W3  vs.  W1-W2 
##
plt.rcParams.update({'font.size': 14})
fig, ax = plt.subplots(figsize=(10, 10), num=None, dpi=80, facecolor='w', edgecolor='k')

## Blain et al. (2013), Figure 1::
## with VEGA mags
#xmin =  1.7; xmax =  5.4; ymin = -0.8;  ymax =  2.1
## with AB mags
xmin =  -0.85; xmax =  3.8; ymin = -1.2;  ymax =  1.4

## Wright et al. (2010), Figure 
#xmin = -1.0; xmax=7.0;    ymin=-0.5; ymax=4.0

## Some plotting defaults
ls              = 28
ticklength      = 18
tickwidth       = 2.0
pointsize       = 100
pointsize_large = pointsize*2.2
fontsize        = 28

##
##   Plotting the   D R 1 4 Q    hexbins
##
cmap = plt.cm.Greys
hb = ax.hexbin( dr14q_W2minW3, 
                dr14q_W1minW2,
                C=dr14q['Z'],
#                gridsize=180, mincnt=25, marginals=False, cmap=cmap, vmin=0.00, vmax=3.00)
                 gridsize=220, mincnt=10, marginals=False, cmap=cmap, vmin=0.00, vmax=3.00)

## Making the colorbar,
cbaxes = fig.add_axes([0.18, 0.24,  0.34, 0.025]) 
cb = fig.colorbar(hb, ax=ax, cax=cbaxes, orientation='horizontal', ticklocation = 'top')
#cb.set_label('')

w = dr14q[np.where( (dr14q_W2minW3 >= xmin)  &
                    (dr14q_W2minW3 <= xmax)  &
                    (dr14q_W1minW2 >= ymin)  &
                    (dr14q_W1minW2 <= ymax) )]
print()
print('Number of DR14Q objects plotted:: ', len(w))
print()


##
##  Plotting the   V H z Q    points
##
#cmap = plt.cm.inferno
cmap = plt.cm.seismic

ax.scatter((VHzQ['unW2mag'] - VHzQ['w3mpro']),
           (VHzQ['unW1mag'] - VHzQ['unW2mag']),
           s=pointsize_large/2.5, c='k')
ax.scatter((VHzQ['unW2mag'] - VHzQ['w3mpro']),
           (VHzQ['unW1mag'] - VHzQ['unW2mag']),
           c=VHzQ['redshift'],
           s=pointsize/2.5, cmap=cmap)

## Good W3 detections
hb_VHzQ = ax.scatter((VHzQ_goodW3['unW2mag'] - VHzQ_goodW3['w3mpro']),
                     (VHzQ_goodW3['unW1mag'] - VHzQ_goodW3['unW2mag']),
                     s=pointsize_large, c='k')

hb_VHzQ = ax.scatter((VHzQ_goodW3['unW2mag'] - VHzQ_goodW3['w3mpro']),
                     (VHzQ_goodW3['unW1mag'] - VHzQ_goodW3['unW2mag']),
                     c=VHzQ_goodW3['redshift'],
                     s=pointsize, cmap=cmap)

## need this just for the objects that have e.g. null detections
ax.scatter(0,0, color='w', s=pointsize_large)

cbaxes = fig.add_axes([0.18, 0.32, 0.34, 0.025])
cb = fig.colorbar(hb_VHzQ,  ax=ax, cax=cbaxes, orientation='horizontal', ticklocation = 'top')
#cb.set_label('redshift            ', labelpad=14)
ax.text(0.00, -1.0, 'redshift', size=fontsize/1.2)


## The vertical dashed line at W 2 − W3 = 5.3 is one of the selection
## criteria for W1W2-dropouts; some are bluer than this because they
## satisfied the W2 − W4 > 8.2 criterion.
lw = 2.0
#ax.axvline(x=5.3, linewidth=lw,linestyle='dotted', color='k')

ax.axis([xmin, xmax, ymin, ymax])

ax.tick_params(axis='both', which='major', labelsize=ls, top='on', right='on', direction='in', length=ticklength,   width=tickwidth)
ax.tick_params(axis='both', which='minor', labelsize=ls, top='on', right='on', direction='in', length=ticklength/2, width=tickwidth)

majorLocator_x = MultipleLocator(2.0)
minorLocator_x = MultipleLocator(0.5)
majorLocator_y = MultipleLocator(1.0)
minorLocator_y = MultipleLocator(0.1)

ax.xaxis.set_major_locator(majorLocator_x)
ax.xaxis.set_minor_locator(minorLocator_x)
ax.yaxis.set_major_locator(majorLocator_y)
ax.yaxis.set_minor_locator(minorLocator_y)

## Grid lines to compare with Wright et al. (2010) Fig. 12
## Vertical lines
for x in range(8): 
    ax.axvline(x=(x-1.0), ymin=0, ymax=1, ls=':', color='grey')
## Horizontal lines
for y in range(9):
    ax.axhline(y=((y*.5)-1.0), xmin=0, xmax=1, ls=':', color='grey')

ax.set_xlabel(r" W2 - W3 ", fontsize=fontsize)
ax.set_ylabel(r" W1 - W2 ", fontsize=fontsize)

plt.savefig('W1W2W3_hexplots_temp.png', format='png')
#plt.show()
#plt.close()
