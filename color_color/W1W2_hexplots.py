'''
Making the 'famous' W2-W3 vs. W1-W2 WISE color-color plot
'''

import numpy as np
from astropy.io    import fits
from astropy.io    import ascii
from astropy.table import Table

import matplotlib
import matplotlib.pyplot as plt
from   matplotlib.ticker import MultipleLocator, FormatStrFormatter

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
path = '/cos_pc19a_npr/programs/quasars/highest_z/data/'
filename ='VHzQs457_unWISE_v1pnt0.dat'
table=path+filename
VHzQ = ascii.read(table)


##  Making the plot(s)
## 
##     W2  vs.  W1-W2       (Assef et al. 2018 and the `R90' and `C75' samples) 
##
plt.rcParams.update({'font.size': 14})
#plt.style.use('dark_background')

## works well for xmin=13.6; xmax=16.9; ymin=-0.2; ymax=3.2:: 
#fig, ax = plt.subplots(figsize=(10, 10), num=None, dpi=80, facecolor='w', edgecolor='k')  ## works well
## works well for xmin=13.0; xmax=16.9; ymin=-0.2; ymax=3.2:: 
fig, ax = plt.subplots(figsize=(14, 10), num=None, dpi=80, facecolor='w', edgecolor='k')  ## works well

## Blain et al. (2013), Figure 1:: 
#xmin =  1.7; xmax =  4.7; ymin = -0.2; ymax =  2.0 
## Wright et al. (2010), Figure 
xmin=12.4; xmax=17.6; ymin=-0.5; ymax=2.6

## Plotting setup
cmap = plt.cm.rainbow
fontsize        = 30
ls              = fontsize
lw              = 2.0
ticklength      = 18
tickwidth       = 2.0
pointsize       = 60
pointsize_large = pointsize*1.2

##
## Plotting the   D R 1 4 Q    hexbins
##
hb = ax.hexbin( dr14q['W2MAG'], (dr14q['W1MAG'] - dr14q['W2MAG']), C=dr14q['Z'],
#            gridsize=180, mincnt=5, marginals=False, cmap=cmap, vmin=0.00, vmax=3.00)  ##works well..
            gridsize=180, mincnt=3, marginals=False, cmap=cmap, vmin=0.20, vmax=3.00)

cb = fig.colorbar(hb, ax=ax)
cb.set_label('redshift')

##
## Plotting the    V H z Q    points
##
ax.scatter( VHzQ['unW1_mag'], (VHzQ['unW1_mag'] - VHzQ['unW2_mag']), color='k', s=pointsize*2.8 )
ax.scatter( VHzQ['unW1_mag'], (VHzQ['unW1_mag'] - VHzQ['unW2_mag']), color='w', s=pointsize )
#ax.scatter(0,0, color='w', s=pointsize_large)

## ``The vertical dashed line at W2-W3=5.3 is one of the selection
## criteria for W1W2-dropouts; some are bluer than this because they
## satisfied the W2-W4>8.2 criterion.''
lw = 2.0
#ax.axvline(x=5.3, linewidth=lw,linestyle='dotted', color='k')

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

##
## Reliability
#
## Equation (4), Assef et al. 2018
## R90
alpha_R =  0.650
beta_R  =  0.153
gamma_R = 13.86

#if xx > gamma_R:
#    yy = (alpha_R)*np.exp( beta_R* ((xx - gamma_R)**2) )
#elsif:
#    xx = alpha_R

##
## Completeness
##
## W1 - W2 > delta_c 
delta_c = 0.71 ## for 75% completeness
delta_c = 0.50 ## for 90% completeness
## Horizontal lines
ax.axhline(y=delta_c, xmin=0, xmax=1, ls='--', color='w', linewidth=6.)

ax.set_xlabel(r" W2 (Vega) ",  fontsize=fontsize)
ax.set_ylabel(r" W1 - W2 ",    fontsize=fontsize)

plt.savefig('W1W2_hexplots_temp.png', format='png')
#plt.show()
#plt.close()
