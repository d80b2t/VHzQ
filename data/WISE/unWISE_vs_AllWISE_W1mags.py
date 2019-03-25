'''
WISE detections and colors of Very High redshift quasars
'''
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from astropy.io import ascii

from matplotlib import colors as mcolors
from matplotlib import gridspec
from matplotlib.ticker import AutoMinorLocator

## READ-IN THE DATA FILE(S)
path = '/cos_pc19a_npr/programs/quasars/highest_z/data/AllWISE/'
infile = 'VHzQs463_UNvALL_WISE_temp.dat'
readin = path+infile
VHzQs  = ascii.read(readin, delimiter=r'\s')

unW1mag = VHzQs[np.where(VHzQs['unW1mag'] > -1)]['unW1mag']
w1mpro  = VHzQs[np.where(VHzQs['w1mpro'] > -1)]['w1mpro']

##
## Making the plot
##
## May fave new line ;-=)
plt.style.use('dark_background')
#matplotlib.rc('text', usetex=True)

#plt.rcParams.update({'font.size': 14})
minorLocator = AutoMinorLocator()

ls              = 'solid'
lw              = 1.0
ms              = 240.
ms_large        = ms*3.
ms_small        = ms/10.
alpha           =0.85
fontsize        = 36
labelsize       = fontsize
tickwidth       = 2.0
ticklabelsize   = labelsize
majorticklength = 14
minorticklength = majorticklength/2.

## From::  https://jakevdp.github.io/PythonDataScienceHandbook/04.08-multiple-subplots.html
fig = plt.figure(figsize=(16, 12))
grid = plt.GridSpec(4, 4, hspace=0.00, wspace=0.00)

main_ax = fig.add_subplot(grid[:-1, 1:])
y_hist  = fig.add_subplot(grid[:-1, 0], xticklabels=[], sharey=main_ax)
x_hist  = fig.add_subplot(grid[-1, 1:], yticklabels=[], sharex=main_ax)

## Adjusting the Whitespace for the plots
left   = 0.08   # the left side of the subplots of the figure
right  = 0.98   # the right side of the subplots of the figure
bottom = 0.12   # the bottom of the subplots of the figure
top    = 0.96   # the top of the subplots of the figure
wspace = 0.26   # the amount of width reserved for blank space between subplots
hspace = 0.06   # the amount of height reserved for white space between subplots
plt.subplots_adjust(left=left, bottom=bottom, right=right, top=top, wspace=wspace, hspace=hspace)


## define the colormap
cmap = plt.cm.plasma    ## Good for W1-W2

## REDSHIFT RANGE
xmin =  13.20  
xmax =  19.25

ymin = xmin
ymax = xmax

##
## TOP  PANEL
##
main_ax.scatter(VHzQs['unW1mag'], VHzQs['w1mpro'],
                c=VHzQs['unW1snr'], #   c=(VHzQs['unW1magerr']*1000),
                cmap=cmap, s=ms, alpha=alpha)

main_ax.set_xlim((xmin, xmax))
main_ax.set_ylim((ymin, ymax))
main_ax.tick_params('both', direction='in', which='major', bottom=True, top=True, left=True, right=True,  length=majorticklength, width=tickwidth)

## KEY LINE!!
fig.subplots_adjust(hspace=0)


##
##  B O T T O M     P A N E L
##
ms = 4
#min_x_data, max_x_data = np.min(VHzQs['unW1mag'], np.max(VHzQs['unW1mag']))
min_x_data, max_x_data = xmin, xmax
xbinsize = 0.25 
nxbins = int(np.floor((max_x_data - min_x_data) / xbinsize))
xcolor='darkturquoise'

x_hist.hist(unW1mag, bins=nxbins, label=' ', alpha=1.0, color='c') 
x_hist.legend(loc='upper right', fontsize=fontsize/1.4)

x_hist.set_xlim((xmin, xmax))
x_hist.set_ylim((0, 40))

minorLocator = AutoMinorLocator()
#x_hist.xaxis.set_minor_locator(minorLocator)
minorLocator = AutoMinorLocator()
#x_hist.yaxis.set_minor_locator(minorLocator)
x_hist.tick_params('both', direction='in', which='major', bottom=True, top=True, left=True,
                   right=True, length=majorticklength, width=tickwidth, labelsize=fontsize/1.2)
x_hist.set_xlabel(r'unWISE W1 mag',fontsize=fontsize)

## KEY LINE!!
fig.subplots_adjust(hspace=0)


##
##  LEFT HAND SIDE   P A N E L
##
min_y_data, max_y_data = ymin, ymax
ybinsize = 0.25 
nybins = int(np.floor((max_y_data - min_y_data) / ybinsize))

#ycolor='mediumturquoise'
ycolor='c'
y_hist.hist(w1mpro, bins=nybins, alpha=1.0, orientation='horizontal', color=ycolor)
y_hist.invert_xaxis()

minorLocator = AutoMinorLocator()
#y_hist.xaxis.set_minor_locator(minorLocator)
minorLocator = AutoMinorLocator()
#y_hist.yaxis.set_minor_locator(minorLocator)
y_hist.tick_params('both', direction='in', which='major', bottom=True, top=True, left=True,
                   right=True, length=majorticklength, width=tickwidth, labelsize=fontsize/1.2)
y_hist.set_ylabel(r'w1mpro', fontsize=fontsize)

y_hist.set_xlim((40, 0))
#y_hist.set_ylim((ymin, ymax))

#plt.show()
plt.savefig('VHzQ_UNvALL_temp.png',format='png')
plt.close(fig)
