'''
Pretty simple wee bit of code to look at the N(z) of the VHzQs.
   h/t to https://towardsdatascience.com/histograms-and-density-plots-in-python-f6bda88f5ac0
          https://towardsdatascience.com/histograms-and-density-plots-in-python-f6bda88f5ac0
          https://github.com/WillKoehrsen/Data-Analysis/blob/master/univariate_dist/Histogram%20and%20Density%20Plot.ipynb
''' 

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from matplotlib.patches import Rectangle
from matplotlib         import colors as mcolors

from astropy.io import ascii
from astropy.io import fits


datapath = '/cos_pc19a_npr/programs/quasars/highest_z/data/'
datafile = 'LIST_OF_VHzQs.dat'
VHzQs = ascii.read(datapath+datafile)

'''
ATLAS   &    4     CFHQS   &   20     DELS    &   16 
ELAIS   &    1     FIRST   &    1     HSC     &    8
IMS     &    5     MMT     &   12     NDWFS   &    1
PSO     &   83     RD      &    1     SDSS    &  170
SDWISE  &   27     SHELLQs &   55     SUV     &   20     
UHS     &    1     ULAS    &   10     VDES    &   17
VHS     &    1     VIK     &    9     VIMOS   &    1
'''

## Make a separate list for each astro survey
HSC    = list(VHzQs[(VHzQs['na'] == 'HSC')  | (VHzQs['na'] == 'SHELLQs')]['redshift'])    ## 63
PSO    = list(VHzQs[VHzQs['na'] == 'PSO']['redshift'])        
SDSS   = list(VHzQs[VHzQs['na'] == 'SDSS']['redshift'])
ULASES = list(VHzQs[(VHzQs['na'] == 'ULAS') | (VHzQs['na'] == 'SUV')]['redshift']) 

## ELAIS+FIRST+NDWFS+RD+UHS+VHS+VIMOS
others = list(VHzQs[ (VHzQs['na'] == 'ATLAS') | (VHzQs['na'] == 'CFHQS')  | (VHzQs['na'] == 'DELS')  |
                     (VHzQs['na'] == 'ELAIS') | (VHzQs['na'] == 'FIRST')  |
                     (VHzQs['na'] == 'IMS')   | (VHzQs['na'] == 'MMT')    | (VHzQs['na'] == 'NDWFS') |
                     (VHzQs['na'] == 'RD')    | (VHzQs['na'] == 'SDWISE') |
                     (VHzQs['na'] == 'UHS')   | (VHzQs['na'] == 'VDES')   | (VHzQs['na'] == 'VHS')   |
                     (VHzQs['na'] == 'VIK')   | (VHzQs['na'] == 'VIMOS') ] ['redshift'])

##  Assign colors for each survey
cmap = plt.get_cmap('plasma')  ## rainbow Actually works pretty well for 6 datasets

#names  = ['ATLAS', 'CFHQS',  'DELS', 'HSC', 'IMS', 'MMT',   'PSO',    'SDSS', 'SDUV', 'SDWISE', 'ULAS', 'VDES',  'VIK',  'others']
names  = ['CFHQS',  'DELS', 'HSC', 'PSO',  'SDSS', 'SDUV', 'SDWISE','ULAS', 'VDES',  'others']
clrlevs = 9.
#colors = [ cmap(0/clrlevs),  cmap(1/clrlevs),  cmap(2/clrlevs), cmap(3/clrlevs),   cmap(4/clrlevs),  cmap(5/clrlevs),
 #          cmap(6/clrlevs),  cmap(7/clrlevs),  cmap(8/clrlevs), cmap(9/clrlevs),  cmap(10/clrlevs),  cmap(11/clrlevs),
  #        cmap(12/clrlevs),  cmap(13/clrlevs)]
colors = [ cmap(0/clrlevs),  cmap(1/clrlevs),  cmap(2/clrlevs), cmap(3/clrlevs),   cmap(4/clrlevs),  cmap(5/clrlevs),
           cmap(6/clrlevs),  cmap(7/clrlevs),  cmap(8/clrlevs), cmap(9/clrlevs)]
    
## Setting up the plot
fig, ax = plt.subplots(figsize=(5, 3), dpi=280, facecolor='w', edgecolor='k')

## Adjusting the Whitespace for the plots
left   = 0.18   # the left side of the subplots of the figure
right  = 0.98   # the right side of the subplots of the figure
bottom = 0.18   # the bottom of the subplots of the figure
top    = 0.96   # the top of the subplots of the figure
wspace = 0.26   # the amount of width reserved for blank space between subplots
hspace = 0.06   # the amount of height reserved for white space between subplots
plt.subplots_adjust(left=left, bottom=bottom, right=right, top=top, wspace=wspace, hspace=hspace)
 

## Some NPR defaults
alpha           = 1.0
fontsize        = 12
labelsize       = fontsize
tickwidth       = 2.0
linewidth       = 2.4
tickwidth       = 2.0
ticklength      = 6.0
ticklabelsize   = labelsize
majorticklength = 12
minorticklength = 6

## Setting up the N(z) binning..
binwidth = 0.075
bins = int((VHzQs['redshift'].max()-VHzQs['redshift'].min())/binwidth +2)
print('No. of bins... ', bins)

## matplotlib histogram
#ax.hist(VHzQs['redshift'], color = 'blue', bins = bins, range=[5.0,7.6])

## Make stacked histogram with multiple airlines
ax.hist([SDSS, others, PSO, HSC, ULASES],
  #    color = (cmap(0/5), cmap(1/5), cmap(2/5), cmap(3/5), cmap(4/5), cmap(5/5)) ,
        color = ('r', 'orange',  'green', 'blue', 'violet'), 
       bins = bins, range=[5.0,7.6], alpha=alpha, histtype='barstacked')

print()
## Create legend
## https://stackoverflow.com/questions/43872450/matplotlib-histogram-with-legend
#handles = [Rectangle((0,0),1,1,color=c,ec="k") for c in names]
labels  = names
ax.legend(['SDSS    (170)',
           'various (117)',
           'PSO       (83)',
           'HSC       (63)',
           'w/ULAS (30)'],
#           'wULAS+SUV  (30)'],
           loc='upper right', fontsize=fontsize/1.2)


## Axes limits
xmin =  4.90
xmax =  7.65
ymin =  0.0
#ymax = 38.0 ## 0.05 bins
ymax = 54.0 ## 0.075 bins
#ymax = 66.0 ## 0.10 bins
ax.set_xlim([xmin,xmax])
ax.set_ylim([ymin, ymax])

## Axes labels
ax.set_xlabel(r'$z$, redshift',  fontsize=labelsize)
ax.set_ylabel(r'No. of objects', fontsize=labelsize)

## Axes style
ax.tick_params(axis='both', which='major', labelsize=labelsize, top=True, right=True, direction='in', length=ticklength,   width=tickwidth)
ax.tick_params(axis='both', which='minor', labelsize=labelsize, top=True, right=True, direction='in', length=ticklength/2, width=tickwidth)


#plt.savefig('Nofz_temp.png', format='png')
plt.savefig('Nofz_temp.pdf', format='pdf')
plt.close(fig)

