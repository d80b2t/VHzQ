'''
Why doesn't matplotlib look as good as SM??!!!
http://space.mit.edu/home/turnerm/python.html
'''
import os
import math
import numpy as np
import matplotlib.pyplot as plt

from astropy.io import ascii
from matplotlib import colors as mcolors
from matplotlib.font_manager import FontProperties

## Setting up the path for the input data
path = os.path.join(os.path.dirname(os.getcwd()),'data/light_curves/individual_objects/')

choice = '1'
## Ordered by qsoID number. 
print()
print('  1)   MMTJ0215-0529      (qsoID  54)')
print('  2)   CFHQSJ0216-045     (qsoID  56; faint)')
print('  3)   SHELLQsJ0220-0432  (qsoID  59; faint)') 
print('  4)   SDSSJ0836+0054     (qsoID 121)')
print('  5)   SDSSJ0959+0227     (qsoID 162; faint)')
print('  6)   SDSSJ1000+0234     (qsoID 164; faint)')
print('  7)   SHELLQsJ1146+0124  (qsoID 206)')
print('  8)   VIKJ1148+0056      (qsoID 214)')
print('  9)   SDSSJ2216+0013     (qsoID 337)')
print()
choice = input('Which object? ')

inputQuasar = None
if choice == '1' : inputQuasar = 'MMTJ0215-0529'
if choice == '2' : inputQuasar = 'CFHQSJ0216-0455'
if choice == '3' : inputQuasar = 'SHELLQsJ0220-0432'
if choice == '4' : inputQuasar = 'SDSSJ0836+0054'
if choice == '5' : inputQuasar = 'SDSSJ0959+0227'
if choice == '6' : inputQuasar = 'SDSSJ1000+0234'
if choice == '7' : inputQuasar = 'SHELLQsJ1146+0124'
if choice == '8' : inputQuasar = 'VIKJ1148+0056'
if choice == '9' : inputQuasar = 'SDSSJ2216+0013'
    

print
print(" Plotting W/VSA light curve for ", inputQuasar)
print

##
##  P h o t o m e t r y    d a t a
##
## all: all the photometric data
## 30d: photometry averaged over a 30 MJD period

##  WSA  - WFCAM Science Archive
WSA_data_all = ascii.read(os.path.join(path,inputQuasar,'WSA_lc_all.dat'))
WSA_data_30d = ascii.read(os.path.join(path,inputQuasar,'WSA_lc_30d.dat'))

## VSA - VISTA Science Archive
VSA_data_all = ascii.read(os.path.join(path,inputQuasar,'VSA_lc_all.dat'))
VSA_data_30d = ascii.read(os.path.join(path,inputQuasar,'VSA_lc_30d.dat'))

## NEOWISE-R
if (choice != '7' and choice !='5'):
    NEOWISER =  ascii.read(os.path.join(path,inputQuasar,'NEOWISER-R_SingleExp_L1b.dat'))
#WISE_W1 = ascii.read(path+'WISE_W1_LC.dat')
#WISE_W2 = ascii.read(path+'WISE_W2_LC.dat')
#WISE_L1bs = ascii.read(path+'J110057_l1b.tbl')


##  Assigned in WSA: 1=Z,2=Y,3=J,4=H,5=K,6=H2,7=Br,8=blank)
Z_WFCAM_all = WSA_data_all[(WSA_data_all['filterID'] == 1) & (WSA_data_all['aperMag3AverAB']>0)]
Y_WFCAM_all = WSA_data_all[(WSA_data_all['filterID'] == 2) & (WSA_data_all['aperMag3AverAB']>0)]
J_WFCAM_all = WSA_data_all[(WSA_data_all['filterID'] == 3) & (WSA_data_all['aperMag3AverAB']>0)]
H_WFCAM_all = WSA_data_all[(WSA_data_all['filterID'] == 4) & (WSA_data_all['aperMag3AverAB']>0)]
K_WFCAM_all = WSA_data_all[(WSA_data_all['filterID'] == 5) & (WSA_data_all['aperMag3AverAB']>0)]

Z_WFCAM_30d = WSA_data_30d[(WSA_data_30d['filterID'] == 1) & (WSA_data_30d['aperMag3Ab']>0)]
Y_WFCAM_30d = WSA_data_30d[(WSA_data_30d['filterID'] == 2) & (WSA_data_30d['aperMag3Ab']>0)]
J_WFCAM_30d = WSA_data_30d[(WSA_data_30d['filterID'] == 3) & (WSA_data_30d['aperMag3Ab']>0)]
H_WFCAM_30d = WSA_data_30d[(WSA_data_30d['filterID'] == 4) & (WSA_data_30d['aperMag3Ab']>0)]
K_WFCAM_30d = WSA_data_30d[(WSA_data_30d['filterID'] == 5) & (WSA_data_30d['aperMag3Ab']>0)]

##  UID of combined filter (assigned in WSA: 1=Z,2=Y,3=J,4=H,5=K,6=H2,7=Br,8=blank)
Z_VIRCAM_all  = VSA_data_all[(VSA_data_all['filterID'] == 1) & (VSA_data_all['aperMag3AverAB']>0)]
Y_VIRCAM_all  = VSA_data_all[(VSA_data_all['filterID'] == 2) & (VSA_data_all['aperMag3AverAB']>0)]
J_VIRCAM_all  = VSA_data_all[(VSA_data_all['filterID'] == 3) & (VSA_data_all['aperMag3AverAB']>0)]
H_VIRCAM_all  = VSA_data_all[(VSA_data_all['filterID'] == 4) & (VSA_data_all['aperMag3AverAB']>0)]
Ks_VIRCAM_all = VSA_data_all[(VSA_data_all['filterID'] == 5) & (VSA_data_all['aperMag3AverAB']>0)]

Z_VIRCAM_30d  = VSA_data_30d[(VSA_data_30d['filterID'] == 1) & (VSA_data_30d['aperMag3Ab']>0)]
Y_VIRCAM_30d  = VSA_data_30d[(VSA_data_30d['filterID'] == 2) & (VSA_data_30d['aperMag3Ab']>0)]
J_VIRCAM_30d  = VSA_data_30d[(VSA_data_30d['filterID'] == 3) & (VSA_data_30d['aperMag3Ab']>0)]
H_VIRCAM_30d  = VSA_data_30d[(VSA_data_30d['filterID'] == 4) & (VSA_data_30d['aperMag3Ab']>0)]
Ks_VIRCAM_30d = VSA_data_30d[(VSA_data_30d['filterID'] == 5) & (VSA_data_30d['aperMag3Ab']>0)]

## For WISE, we adopt 2.699 and 3.339 as the conversions to AB from W1 and W2 Vega magnitudes,
#if choice != '7' & choice !='5':
if choice !='5':
    WISE_W1_AB = NEOWISER['w1mpro'] + 2.699
    WISE_W2_AB = NEOWISER['w2mpro'] + 3.339



##
## Making the plot
##
## http://matplotlib.org/examples/statistics/errorbar_limits.html
## http://matplotlib.org/examples/color/named_colors.html
fig, ax = plt.subplots(figsize=(8.0, 6.0))

## Adjusting the Whitespace for the plots
left   = 0.14   # the left side of the subplots of the figure
right  = 0.98   # the right side of the subplots of the figure
bottom = 0.12   # the bottom of the subplots of the figure
top    = 0.92   # the top of the subplots of the figure
wspace = 0.22   # the amount of width reserved for blank space between subplots
hspace = 0.04   # the amount of height reserved for white space between subplots
plt.subplots_adjust(left=left, bottom=bottom, right=right, top=top, wspace=wspace, hspace=hspace)

## Some NPR defaults
ls              = 'solid'
lw              = 1.0  # 2.4
alpha           = 1.0
fontsize        = 14
labelsize       = 14
tickwidth       = 2.0
ticklength      = 6.0
ticklabelsize   = labelsize
majorticklength = 12
minorticklength = 6
markeredgewidth = 1.5

print('Creating plot ...WSA labels...')
## WSA
ms = 3.
ax.scatter(Z_WFCAM_all['mjdObs'], Z_WFCAM_all['aperMag3AverAB'], label='', s=ms, color='olive'             )
ax.scatter(Y_WFCAM_all['mjdObs'], Y_WFCAM_all['aperMag3AverAB'], label='', s=ms, color='orange'             )
ax.scatter(J_WFCAM_all['mjdObs'], J_WFCAM_all['aperMag3AverAB'], label='', s=ms, color='goldenrod'    )
ax.scatter(H_WFCAM_all['mjdObs'], H_WFCAM_all['aperMag3AverAB'], label='', s=ms, color='y' )
ax.scatter(K_WFCAM_all['mjdObs'], K_WFCAM_all['aperMag3AverAB'], label='', s=ms, color='yellow'    )

ms = 7.
ax.errorbar(Z_WFCAM_30d['mjd'], Z_WFCAM_30d['aperMag3Ab'],  yerr=Z_WFCAM_30d['aperMag3Err'],
            label='WFCAM Z', fmt='o', markeredgecolor ='black', markeredgewidth = markeredgewidth, color='olive', ms=ms)
ax.errorbar(Y_WFCAM_30d['mjd'], Y_WFCAM_30d['aperMag3Ab'],  yerr=Y_WFCAM_30d['aperMag3Err'],
            label='WFCAM Y', fmt='o', markeredgecolor ='black', markeredgewidth = markeredgewidth, color='orange', ms=ms)
ax.errorbar(J_WFCAM_30d['mjd'], J_WFCAM_30d['aperMag3Ab'],  yerr=J_WFCAM_30d['aperMag3Err'],
            label='WFCAM J', fmt='o', markeredgecolor ='black', markeredgewidth = markeredgewidth, color='goldenrod',     ms=ms)
ax.errorbar(H_WFCAM_30d['mjd'], H_WFCAM_30d['aperMag3Ab'],  yerr=H_WFCAM_30d['aperMag3Err'],
            label='WFCAM H', fmt='o', markeredgecolor ='black', markeredgewidth = markeredgewidth, color='y',   ms=ms)
ax.errorbar(K_WFCAM_30d['mjd'], K_WFCAM_30d['aperMag3Ab'],  yerr=K_WFCAM_30d['aperMag3Err'],
            label='WFCAM K', fmt='o', markeredgecolor ='black', markeredgewidth = markeredgewidth, color='yellow',       ms=ms)

print('Creating plot, ...VSA labels...')

## VSA
ms = 3.
ax.scatter( Z_VIRCAM_all['mjdObs'],  Z_VIRCAM_all['aperMag3AverAB'], label='', s=ms, color='olive')
ax.scatter( Y_VIRCAM_all['mjdObs'],  Y_VIRCAM_all['aperMag3AverAB'], label='', s=ms, color='orange')
ax.scatter( J_VIRCAM_all['mjdObs'],  J_VIRCAM_all['aperMag3AverAB'], label='', s=ms, color='goldenrod')
ax.scatter( H_VIRCAM_all['mjdObs'],  H_VIRCAM_all['aperMag3AverAB'], label='', s=ms, color='y')
ax.scatter(Ks_VIRCAM_all['mjdObs'], Ks_VIRCAM_all['aperMag3AverAB'], label='', s=ms, color='yellow')

ms = 7.
ax.errorbar(Y_VIRCAM_30d['mjd'],  Y_VIRCAM_30d['aperMag3Ab'],  yerr=Y_VIRCAM_30d['aperMag3Err'],
            markeredgecolor ='black', markeredgewidth = markeredgewidth, fmt='h', label='VIRCAM Z',  color='olive',     ms=ms*1.4)
ax.errorbar(Y_VIRCAM_30d['mjd'],  Y_VIRCAM_30d['aperMag3Ab'],  yerr=Y_VIRCAM_30d['aperMag3Err'],
            markeredgecolor ='black', markeredgewidth = markeredgewidth, fmt='h', label='VIRCAM Y',  color='orange',    ms=ms*1.4)
ax.errorbar(J_VIRCAM_30d['mjd'],  J_VIRCAM_30d['aperMag3Ab'],  yerr=J_VIRCAM_30d['aperMag3Err'],
            markeredgecolor ='black', markeredgewidth = markeredgewidth, fmt='h', label='VIRCAM J',  color='goldenrod', ms=ms*1.4)
ax.errorbar(H_VIRCAM_30d['mjd'],  H_VIRCAM_30d['aperMag3Ab'],  yerr=H_VIRCAM_30d['aperMag3Err'],
            markeredgecolor ='black', markeredgewidth = markeredgewidth, fmt='h', label='VIRCAM H',  color='y',         ms=ms*1.4)
ax.errorbar(Ks_VIRCAM_30d['mjd'], Ks_VIRCAM_30d['aperMag3Ab'],  yerr=Ks_VIRCAM_30d['aperMag3Err'],
            markeredgecolor ='black', markeredgewidth = markeredgewidth, fmt='h', label='VIRCAM Ks', color='yellow',    ms=ms*1.4)

print('Creating plot, ...WISE labels...')
if choice != '5' :
    ## WISE W1/W2
    ms = 6.
    ax.errorbar(NEOWISER['mjd'], WISE_W1_AB, yerr=NEOWISER['w1sigmpro'], fmt='o', ms=ms, label='NEOWISE-R W1',
            markeredgecolor ='black', markeredgewidth = markeredgewidth, color='peru') #linestyle=ls, linewidth=lw*2.5, 
    ax.errorbar(NEOWISER['mjd'], WISE_W2_AB, yerr=NEOWISER['w2sigmpro'], fmt='o', ms=ms, label='NEOWISE-R W2', 
           markeredgecolor ='black', markeredgewidth = markeredgewidth, color='orangered') #linestyle=ls, linewidth=lw*2.5,
    ax.errorbar(NEOWISER['mjd'], WISE_W1_AB, yerr=NEOWISER['w1sigmpro'], fmt='o', ms=ms, label='',
            markeredgecolor ='black', markeredgewidth = markeredgewidth, color='peru') #linestyle=ls, linewidth=lw*2.5, 
    ax.errorbar(NEOWISER['mjd'], WISE_W2_AB, yerr=NEOWISER['w2sigmpro'], fmt='o', ms=ms, label='', 
           markeredgecolor ='black', markeredgewidth = markeredgewidth, color='orangered') #linestyle=ls, linewidth=lw*2.5,
    ax.errorbar(NEOWISER['mjd'], WISE_W1_AB, yerr=NEOWISER['w1sigmpro'], fmt='o', ms=ms, label='',
            markeredgecolor ='black', markeredgewidth = markeredgewidth, color='peru') #linestyle=ls, linewidth=lw*2.5, 
           
print('Tidying up figure...')

 ## Tidy up the figure
mjd_offset = 50.
xmin = min(min(WSA_data_all['mjdObs']), min(VSA_data_all['mjdObs'])) - mjd_offset
xmax = max(min(WSA_data_all['mjdObs']), max(VSA_data_all['mjdObs'])) + mjd_offset
xmax = 58484 ## 2019-Jan-01
mag_offset = 0.5
ymin = max(max(WSA_data_all['aperMag3AverAB']), max(VSA_data_all['aperMag3AverAB'])) + (mag_offset*1.00)
ymax = min(max(WSA_data_all['aperMag3AverAB']), min(VSA_data_all['aperMag3AverAB'])) - (mag_offset*2.25)
#ymin = 27.4
ymax = 16.8

print('Set axes limits...')

ax.set_xlim((xmin, xmax))
ax.set_ylim((ymin, ymax))
ax.tick_params('x', direction='in', labelsize=ticklabelsize )
ax.tick_params('y', direction='in', labelsize=ticklabelsize)
#ax.minorticks_on('x', direction='in')
#ay.minorticks_on()
#ax.get_xaxis().set_tick_params(which='both', direction='out')
#ax.get_yaxis().set_tick_params(which='both', direction='out')
#ax.grid(True)

print('Adding legends...')
## https://matplotlib.org/api/legend_api.html
plt.legend(loc="upper left", ncol=2, fontsize=labelsize/1.4, frameon=True)

plt.title(inputQuasar,         fontsize=fontsize)
plt.xlabel('MJD',              fontsize=fontsize)
plt.ylabel('magnitude (AB)',   fontsize=fontsize)

##plt.show()
#fig.savefig("plot.pdf",)
#fig.savefig("plot.eps",format='eps')
print('Saving figure to ',inputQuasar+'LC_temp.png')
plt.savefig(inputQuasar+'LC_temp.png', format='png')
#plt.savefig(inputQuasar+'LC_temp.pdf', format='pdf')
#plt.savefig('bias_with_redshift_temp.png',format='png')
plt.show()

plt.close(fig)

print('Complete.')
