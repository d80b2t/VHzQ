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

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

##
## DR14Q
##
path       = '/cos_pc19a_npr/data/SDSS/DR14Q/'
filename   ='DR14Q_v4_4.fits'
#filename  ='DR14Q_v4_4_W4good.fits'
infile     = path+filename
data       = fits.getdata(infile, 1)
#dr14q_full = Table(data)
dr14q      = Table(data)
## in case you want to select on e.g. SDSS survey
#dr14q      = dr14q_full

## Splitting up the DR14Q by intergral survey
##   from the DR12Q,  MJD.min() = 55176 and MJD.max() = 56837
## SDSS-I/II
sdss  = dr14q[np.where( dr14q['MJD'] < 55176  )]
## BOSS
boss  = dr14q[np.where((dr14q['MJD'] > 55176) & (dr14q['MJD'] < 56837))  ]
## SDSS-IV
eboss = dr14q[np.where( dr14q['MJD'] > 56837  )]  

## Should be:
##   79,487 for SDSS-I/II;
##  286,686 for BOSS;
##  159,981 for SDSS-IV
dr14q_W1minW2 = (dr14q['W1MAG'] - dr14q['W2MAG'])
dr14q_W2minW3 = (dr14q['W2MAG'] - dr14q['W3MAG'])
##
sdss_W1minW2  = (sdss['W1MAG'] - sdss['W2MAG'])
sdss_W2minW3  = (sdss['W2MAG'] - sdss['W3MAG'])
boss_W1minW2  = (boss['W1MAG'] - boss['W2MAG'])
boss_W2minW3  = (boss['W2MAG'] - boss['W3MAG'])
eboss_W1minW2 = (eboss['W1MAG'] - eboss['W2MAG'])
eboss_W2minW3 = (eboss['W2MAG'] - eboss['W3MAG'])


##
##  V H z Q    data
##
path = '/cos_pc19a_npr/programs/quasars/highest_z/data/'
filename = 'VHzQs_ZYJHK_WISE.dat'
table=path+filename
VHzQ_full = ascii.read(table)
## in case you want to select on e.g. snr
VHzQ = VHzQ_full
#VHzQ = VHzQ_full[np.where(VHzQ_full['w3snr'] >3.0)]



##  Making the plot(s)
## 
##  W2-W3  vs.  W1-W2 
##
plt.rcParams.update({'font.size': 14})
fig, ax = plt.subplots(figsize=(14, 8), num=None, dpi=80, facecolor='w', edgecolor='k')

## redshif on the x-axis
xmin =  -0.1; xmax =  7.7;  ymin = -0.8;  ymax =  2.1 

## Some plotting defaults
ls              = 28
ticklength      = 18
tickwidth       = 2.0
pointsize       = 100
pointsize_large = pointsize*2.2
fontsize        = 28


vmin = 2.2
vmax = 4.25
##
##   Plotting the   D R 1 4 Q    hexbins
##
cmap = plt.cm.Greys
hb = ax.hexbin(dr14q['Z'],
               dr14q_W1minW2,
             C=dr14q_W2minW3,
             gridsize=220, mincnt=10, marginals=False, cmap=cmap,
             vmin=vmin, vmax=vmax)
## Making the colorbar
cbaxes = fig.add_axes([0.2, 0.20,  0.36, 0.025]) 
cb = fig.colorbar(hb, ax=ax, cax=cbaxes, orientation='horizontal', ticklocation = 'top')
cb.ax.set_xticklabels([''])
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
hb_VHzQ = ax.scatter(  VHzQ['redshift'], 
                      (VHzQ['unW1mag'] - VHzQ['unW2mag']),
                     s=pointsize_large, c='k')

hb_VHzQ = ax.scatter(VHzQ['redshift'], 
                    (VHzQ['unW1mag'] - VHzQ['unW2mag']),
                  c=(VHzQ['unW2mag'] - VHzQ['w3mpro']),
                  vmin=vmin, vmax=vmax, 
                  s=pointsize, cmap=cmap)

## need this just for the objects that have e.g. null detections
xxx = np.full((len(VHzQ['redshift'])), 0)
ax.scatter(VHzQ['redshift'], xxx, color='w', s=pointsize_large)

cbaxes = fig.add_axes([0.2, 0.24,  0.36, 0.025])
cb = fig.colorbar(hb_VHzQ,  ax=ax, cax=cbaxes, orientation='horizontal',ticklocation = 'top')
cb.set_label('W2-W3', labelpad=16)

## The vertical dashed line at W 2 − W3 = 5.3 is one of the selection
## criteria for W1W2-dropouts; some are bluer than this because they
## satisfied the W2 − W4 > 8.2 criterion.
lw = 2.0
#ax.axvline(x=5.3, linewidth=lw,linestyle='dotted', color='k')

ax.axis([xmin, xmax, ymin, ymax])
ax.tick_params(axis='both', which='major', labelsize=ls, top='on', right='on', direction='in', length=ticklength,   width=tickwidth)
ax.tick_params(axis='both', which='minor', labelsize=ls, top='on', right='on', direction='in', length=ticklength/2, width=tickwidth)

majorLocator = MultipleLocator(2.0)
minorLocator = MultipleLocator(0.5)
ax.xaxis.set_major_locator(majorLocator)
ax.xaxis.set_minor_locator(minorLocator)

majorLocator = MultipleLocator(1.0)
minorLocator = MultipleLocator(0.1)
ax.yaxis.set_major_locator(majorLocator)
ax.yaxis.set_minor_locator(minorLocator)


## Grid lines to compare with Wright et al. (2010) Fig. 12
## Vertical lines
for x in range(8): 
    ax.axvline(x=(x-1.0), ymin=0, ymax=1, ls=':', color='grey')
## Horizontal lines
for y in range(9):
    ax.axhline(y=((y*.5)-1.0), xmin=0, xmax=1, ls=':', color='grey')

ax.set_xlabel(r"$z$, redshift", fontsize=fontsize)
ax.set_ylabel(r" W1 - W2 ", fontsize=fontsize)

plt.savefig('redshift_vs_W1W2_temp.png', format='png')
#plt.show()
plt.close()





###################################
##
##   S D S S
##
plt.rcParams.update({'font.size': 14})
fig, ax1 = plt.subplots(figsize=(14, 8), num=None, dpi=80, facecolor='w', edgecolor='k')
##
cmap = plt.cm.Greys
hb = ax1.hexbin(sdss['Z'], sdss_W1minW2,
             C=sdss_W2minW3,
             gridsize=220, mincnt=10, marginals=False, cmap=cmap,  vmin=vmin, vmax=vmax)

## Making the colorbar
cbaxes = fig.add_axes([0.2, 0.20,  0.36, 0.025]) 
cb = fig.colorbar(hb, ax=ax, cax=cbaxes, orientation='horizontal', ticklocation = 'top')
cb.ax.set_xticklabels([''])

ax1.set_xlabel(r"$z$, redshift", fontsize=fontsize)
ax1.set_ylabel(r" W1 - W2 ", fontsize=fontsize)

plt.savefig('redshift_vs_W1W2_sdss_temp.png', format='png')
#plt.show()
plt.close()
