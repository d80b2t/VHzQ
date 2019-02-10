'''
Why doesn't matplotlib look as good as SM??!!!
http://space.mit.edu/home/turnerm/python.html
'''

import math
import numpy as np
import inquirer
import matplotlib.pyplot as plt

from matplotlib import colors as mcolors
from astropy.io import ascii

path = '/cos_pc19a_npr/programs/quasars/highest_z/data/LightCurves/'


choice = '4'
## Ordered by qsoID number. 
print()
print('  1)   MMTJ0215-0529      (qsoID  54)')
print('  2)   CFHQSJ0216-045     (qsoID  56; faint)')
print('  3)   SHELLQsJ0220-0432  (qsoID  59; faint)') 
print('  4)   SDSSJ0836+0054     (qsoID 121)')
print('  5)   SDSSJ0959+0227     (qsoID 162; faint)')
print()
#choice = input('Which object? ')

if choice == '1' : inputQuasar = 'MMTJ0215-0529'
if choice == '2' : inputQuasar = 'CFHQSJ0216-0455'
if choice == '3' : inputQuasar = 'SHELLQsJ0220-0432'
if choice == '4' : inputQuasar = 'SDSSJ0836+0054'
if choice == '5' : inputQuasar = 'SDSSJ0959+0227'

print
print(" Plotting W/VSA light curve for ", inputQuasar)
print

##
##  P h o t o m e t r y    d a t a
##

##  WSA  - WFCAM Science Archive
WSA_data = ascii.read(path+inputQuasar+'/WSA_lc.dat')

## VSA - VISTA Science Archive
VSA_data = ascii.read(path+inputQuasar+'/VSA_lc.dat')


##  UID of combined filter (assigned in WSA: 1=Z,2=Y,3=J,4=H,5=K,6=H2,7=Br,8=blank)
Z_WFCAM = WSA_data[(WSA_data['filterID'] == 1) & (WSA_data['aperMag3AverAB']>0)]
Y_WFCAM = WSA_data[(WSA_data['filterID'] == 2) & (WSA_data['aperMag3AverAB']>0)]
J_WFCAM = WSA_data[(WSA_data['filterID'] == 3) & (WSA_data['aperMag3AverAB']>0)]
H_WFCAM = WSA_data[(WSA_data['filterID'] == 4) & (WSA_data['aperMag3AverAB']>0)]
K_WFCAM = WSA_data[(WSA_data['filterID'] == 5) & (WSA_data['aperMag3AverAB']>0)]


##  UID of combined filter (assigned in WSA: 1=Z,2=Y,3=J,4=H,5=K,6=H2,7=Br,8=blank)
Z_VIRCAM  = VSA_data[(VSA_data['filterID'] == 1) & (VSA_data['aperMag3AverAB']>0)]
Y_VIRCAM  = VSA_data[(VSA_data['filterID'] == 2) & (VSA_data['aperMag3AverAB']>0)]
J_VIRCAM  = VSA_data[(VSA_data['filterID'] == 3) & (VSA_data['aperMag3AverAB']>0)]
H_VIRCAM  = VSA_data[(VSA_data['filterID'] == 4) & (VSA_data['aperMag3AverAB']>0)]
Ks_VIRCAM = VSA_data[(VSA_data['filterID'] == 5) & (VSA_data['aperMag3AverAB']>0)]


##  From the Ross&Cross appendix
##  WFCAM
Z_ABw = Z_WFCAM['aperMag3AverAB'] + 0.514
Y_ABw = Y_WFCAM['aperMag3AverAB'] + 0.617
J_ABw = J_WFCAM['aperMag3AverAB'] + 0.919 
H_ABw = H_WFCAM['aperMag3AverAB'] + 1.379
K_AB  = K_WFCAM['aperMag3AverAB'] + 1.900   

## VIRCAM
Z_ABv = Z_VIRCAM['aperMag3AverAB']  + 0.513 
Y_ABv = Y_VIRCAM['aperMag3AverAB']  + 0.601
J_ABv = J_VIRCAM['aperMag3AverAB']  + 0.921
H_ABv = H_VIRCAM['aperMag3AverAB']  + 1.368
Ks_AB = Ks_VIRCAM['aperMag3AverAB'] + 1.83

  
## WISE
#WISE_W1 = ascii.read(path+'WISE_W1_LC.dat')
#WISE_W2 = ascii.read(path+'WISE_W2_LC.dat')
#WISE_L1bs = ascii.read(path+'J110057_l1b.tbl')

## For WISE, we adopt 2.699 and 3.339 as the conversions to AB from W1 and W2 Vega magnitudes,
#WISE_W1_ABave = WISE_W1['W1_vega'] + 2.699
#WISE_W2_ABave = WISE_W2['W2_vega'] + 3.339
#WISE_W1_ABs   = WISE_L1bs['w1mpro'] + 2.699
#WISE_W2_ABs   = WISE_L1bs['w2mpro'] + 3.339



##
## Making the plot
##
## http://matplotlib.org/examples/statistics/errorbar_limits.html
## http://matplotlib.org/examples/color/named_colors.html
plt.rcParams.update({'font.size': 14})

# 17.0 and 8.0 for paper
#fig, ax = plt.subplots(figsize=(17.0, 8.0))
# 12.0 and 8.0 for job app figure
fig, ax = plt.subplots(figsize=(10.0, 6.0))


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
fontsize        = 16
labelsize       = fontsize
tickwidth       = 2.0
tickwidth       = 2.0
ticklength      = 6.0
ticklabelsize   = labelsize
majorticklength = 12
minorticklength = 6

## WSA
ms = 6.
#ax.scatter(Y_WFCAM['mjdObs'], Y_WFCAM['aperMag3AverAB'],   color='y'             )
#ax.scatter(J_WFCAM['mjdObs'], J_WFCAM['aperMag3AverAB'],    color='goldenrod'    )
#ax.scatter(H_WFCAM['mjdObs'], H_WFCAM['aperMag3AverAB'],   color='darkgoldenrod' )
#ax.scatter(K_WFCAM['mjdObs'], K_WFCAM['aperMag3AverAB'],   color='orangered'    )

ms = 6.
ax.errorbar(Y_WFCAM['mjdObs'], Y_WFCAM['aperMag3AverAB'],  yerr=Y_WFCAM['aperMag3Err'], fmt='h',  color='y',             ms=ms)
ax.errorbar(J_WFCAM['mjdObs'], J_WFCAM['aperMag3AverAB'],  yerr=J_WFCAM['aperMag3Err'], fmt='h',  color='goldenrod',     ms=ms)
ax.errorbar(H_WFCAM['mjdObs'], H_WFCAM['aperMag3AverAB'],  yerr=H_WFCAM['aperMag3Err'], fmt='h',  color='darkgoldenrod', ms=ms)
ax.errorbar(K_WFCAM['mjdObs'], K_WFCAM['aperMag3AverAB'],  yerr=K_WFCAM['aperMag3Err'], fmt='h',  color='orangered',     ms=ms)


## VSA
ms = 6.
#ax.scatter(Y_VIRCAM['mjdObs'], Y_VIRCAM['aperMag3AverAB'],   color='y'             )
#ax.scatter(J_VIRCAM['mjdObs'], J_VIRCAM['aperMag3AverAB'],    color='goldenrod'    )
#ax.scatter(H_VIRCAM['mjdObs'], H_VIRCAM['aperMag3AverAB'],   color='darkgoldenrod' )
#ax.scatter(Ks_VIRCAM['mjdObs'], Ks_VIRCAM['aperMag3AverAB'],   color='orangered'    )

ms = 6.
ax.errorbar(Y_VIRCAM['mjdObs'], Y_VIRCAM['aperMag3AverAB'],  yerr=Y_VIRCAM['aperMag3Err'], fmt='h', color='y',             ms=ms)
ax.errorbar(J_VIRCAM['mjdObs'], J_VIRCAM['aperMag3AverAB'],  yerr=J_VIRCAM['aperMag3Err'], fmt='h', color='goldenrod',     ms=ms)
ax.errorbar(H_VIRCAM['mjdObs'], H_VIRCAM['aperMag3AverAB'],  yerr=H_VIRCAM['aperMag3Err'], fmt='h', color='darkgoldenrod', ms=ms)
ax.errorbar(Ks_VIRCAM['mjdObs'], Ks_VIRCAM['aperMag3AverAB'],  yerr=Ks_VIRCAM['aperMag3Err'], fmt='h',  color='orangered',   ms=ms)



## WISE W1/W2
ms=16
#ax.errorbar(WISE_W1['MJD'], WISE_W1_ABave, yerr=WISE_W1['W1_unc'], fmt='o', ms=ms, linestyle=ls, linewidth=lw*2.5, color='indigo')
#ax.errorbar(WISE_W2['MJD'], WISE_W2_ABave, yerr=WISE_W2['W2_unc'], fmt='o', ms=ms, linestyle=ls, linewidth=lw*2.5, color='brown')
ms=4
#ax.errorbar(WISE_L1bs['mjd'], WISE_W1_ABs, yerr=WISE_L1bs['w1sigmpro'], fmt='o', ms=ms, color='indigo')
#ax.errorbar(WISE_L1bs['mjd'], WISE_W2_ABs, yerr=WISE_L1bs['w2sigmpro'], fmt='o', ms=ms, color='brown')


## Tidy up the figure
mjd_offset = 50.
xmin = min(min(WSA_data['mjdObs']), min(VSA_data['mjdObs'])) - mjd_offset
xmax = max(min(WSA_data['mjdObs']), max(VSA_data['mjdObs'])) + mjd_offset
mag_offset = 0.5
ymin = max(max(WSA_data['aperMag3AverAB']), max(VSA_data['aperMag3AverAB'])) + (mag_offset*1.25)
ymax = min(max(WSA_data['aperMag3AverAB']), min(VSA_data['aperMag3AverAB'])) - (mag_offset*2.0)

ax.set_xlim((xmin, xmax))
ax.set_ylim((ymin, ymax))
ax.tick_params('x', direction='in')
ax.tick_params('y', direction='in')
#ax.minorticks_on('x', direction='in')
#ay.minorticks_on()
#ax.get_xaxis().set_tick_params(which='both', direction='out')
#ax.get_yaxis().set_tick_params(which='both', direction='out')
#ax.grid(True)

## https://matplotlib.org/api/legend_api.html
plt.legend([
            'WFCAM Y', 'WFCAM J', 'WFCAM H', 'WFCAM K',
             'VIRCAM Y', 'VIRCAM J', 'VIRCAM H', 'VIRCAM Ks', ],
    #        'WISE W1', 'WISE W2'  ],
#           loc="lower left", ncol=3, shadow=True, fancybox=True,
           loc="upper left", ncol=3, shadow=True, fancybox=True,
           fontsize=16, frameon=True)

plt.title(inputQuasar, fontsize=fontsize*1.6)
plt.xlabel('MJD')
plt.ylabel('magnitude (AB)')

##plt.show()
#fig.savefig("plot.pdf",)
#fig.savefig("plot.eps",format='eps')
plt.savefig(inputQuasar+'LC_temp.png', format='png')
#plt.savefig(inputQuasar+'LC_temp.pdf', format='pdf')
#plt.savefig('bias_with_redshift_temp.png',format='png')
plt.show()

plt.close(fig)

