'''
The python/matplotlib code to make the MJD vs. (NIR) band coverage
figure in Ross & Cross, (2019).

Requires the WSA SQL data file.
''' 

from astropy.io    import fits
from astropy.io    import ascii
from astropy.table import Table

import numpy as np

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

## Input path and file
path = '/cos_pc19a_npr/programs/quasars/highest_z/data/WSA/'
filename = 'results16_20_2_38_44430.fits'
fits_table=path+filename

## open a FITS file
hdul = fits.open(fits_table)  

## assume the first extension is a table
data = hdul[1].data 

print('The data columns are:: ') 
print(data.columns)
print()

## show the first two rows
first_two_rows = data[:2]
first_two_rows  
## show the last two rows
last_two_rows = data[-2:]
last_two_rows  

##
## Making the figure
##
fig, ax = plt.subplots(figsize=(12, 8), num=None, dpi=80

# Some general style and size optopn
cmap       = plt.cm.rainbow
fontsize   = 30
ls         = fontsize
lw         = 2.0
ticklength = 18
tickwidth  = 2.0
pnts       = 60
pnts_large = pointsize*1.2

## Plotting it up...
ax.scatter(data.MJDOBS, data.FILTERID)

## axis label
ax.set_xlabel(r" MJD ",  fontsize=fontsize)
ax.set_ylabel(r" NIR band ",    fontsize=fontsize)

plt.savefig('MJD_vs_band_coverage_temp.png', format='png')
