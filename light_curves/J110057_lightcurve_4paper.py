'''
Why doesn't matplotlib look as good as SM??!!!
http://space.mit.edu/home/turnerm/python.html
'''

import math
import numpy as np
import matplotlib.pyplot as plt
#import image

from matplotlib import colors as mcolors
from astropy.io import ascii

path = '/cos_pc19a_npr/data/J110057/photometry/'


##
##  P h o t o m e t r y    d a t a
##
## CRTS
CRTS = ascii.read(path+'CRTS_LC.dat')
## LINEAR
LINEAR = ascii.read(path+'LINEAR_full.dat')

## SSA - SuperCOSMOS Science Archive
## For the Declination of your object, the plates scanned by SuperCOSMOS were UK-J, POSSI-e, UK-R, UK-I

UK_J    = ascii.read(path+'SSA_UK-J.dat')
POSSI_e = ascii.read(path+'SSA_POSS_Red1.dat')
UK_R    = ascii.read(path+'SSA_UK-R_Red2.dat')
UK_I    = ascii.read(path+'SSA_UK-I.dat')

UK_J_mjd  =  UK_J['mjd']
POSS_mjd  =  POSSI_e['mjd']         ## 1955, April
UK_R_mjd  =  UK_R['mjd']
UK_I_mjd  =  UK_I['mjd']

## sCorMag's in Vega. 
## https://www.astro.umd.edu/~ssm/ASTR620/mags.html
## assume:
##   UK-J ~ g;  POSSI_e and UK_R ~ r and UK_I ~ i
SSA_B_AB  =  UK_J['sCorMagB']     - 0.103
SSA_R1_AB =  POSSI_e['sCorMagR1'] + 0.146
SSA_R2_AB =  UK_R['sCorMagR2']    + 0.146
SSA_I_AB  =  UK_I['sCorMagI']     + 0.366

## Pan-STARRS
PS_g = ascii.read(path+'PanSTARRS_LC_g.dat')
PS_r = ascii.read(path+'PanSTARRS_LC_r.dat')
PS_i = ascii.read(path+'PanSTARRS_LC_i.dat')
PS_z = ascii.read(path+'PanSTARRS_LC_z.dat')
PS_y = ascii.read(path+'PanSTARRS_LC_y.dat')

## SDSS 
SDSS_u = ascii.read(path+'SDSS_orig_u.dat')
SDSS_g = ascii.read(path+'SDSS_orig_g.dat')
SDSS_r = ascii.read(path+'SDSS_orig_r.dat')
SDSS_i = ascii.read(path+'SDSS_orig_i.dat')
SDSS_z = ascii.read(path+'SDSS_orig_z.dat')

## DECaLS
DECaLS_g = ascii.read(path+'DECaLS_DR4_g.dat')
DECaLS_r = ascii.read(path+'DECaLS_DR4_r.dat')
DECaLS_z = ascii.read(path+'DECaLS_DR4_z.dat')

## UKIDSS LAS
ULAS_Y = ascii.read(path+'ULAS_Y.dat')
ULAS_J = ascii.read(path+'ULAS_J1.dat')
ULAS_H = ascii.read(path+'ULAS_H.dat')
ULAS_K = ascii.read(path+'ULAS_K.dat')

## From good ol' Peth et al. (2011)
#Y_AB  = Y  + 0.634
#J_AB  = J  + 0.938
#H_AB  = H  + 1.379
#Ks_AB = Ks + 1.84	
#K_AB  = K  + 1.900

ULAS_Y_AB  = ULAS_Y['YAperMag3']   + 0.634
ULAS_J_AB  = ULAS_J['J1_AperMag3'] + 0.938
ULAS_H_AB  = ULAS_H['HAperMag3']   + 1.379
ULAS_Ks_AB = ULAS_K['KAperMag3']   + 1.84	
   
## WISE    
WISE_W1 = ascii.read(path+'WISE_W1_LC.dat')
WISE_W2 = ascii.read(path+'WISE_W2_LC.dat')

WISE_L1bs = ascii.read(path+'J110057_l1b.tbl')

## For WISE, we adopt 2.699 and 3.339 as the conversions to AB from W1 and W2 Vega magnitudes,
WISE_W1_ABave = WISE_W1['W1_vega'] + 2.699
WISE_W2_ABave = WISE_W2['W2_vega'] + 3.339
WISE_W1_ABs   = WISE_L1bs['w1mpro'] + 2.699
WISE_W2_ABs   = WISE_L1bs['w2mpro'] + 3.339



## SPECTRO-PHOTOMETRY
sdss_spec_u = ascii.read(path+'SDSS_spectrophot_u.dat')
sdss_specu = 22.5-2.5*(math.log10(sdss_spec_u['flux_nanomaggies']))
sdss_spec_g = ascii.read(path+'SDSS_spectrophot_g.dat')
sdss_specg = 22.5-2.5*(math.log10(sdss_spec_g['flux_nanomaggies']))
sdss_spec_r = ascii.read(path+'SDSS_spectrophot_r.dat')
sdss_specr = 22.5-2.5*(math.log10(sdss_spec_r['flux_nanomaggies']))
sdss_spec_i = ascii.read(path+'SDSS_spectrophot_i.dat')
sdss_speci = 22.5-2.5*(math.log10(sdss_spec_i['flux_nanomaggies']))
sdss_spec_z = ascii.read(path+'SDSS_spectrophot_z.dat')
sdss_specz = 22.5-2.5*(math.log10(sdss_spec_z['flux_nanomaggies']))

boss_spec_u = ascii.read(path+'BOSS_spectrophot_u.dat')
boss_specu = 22.5-2.5*(math.log10(boss_spec_u['flux_nanomaggies']))
boss_spec_g = ascii.read(path+'BOSS_spectrophot_g.dat')
boss_specg = 22.5-2.5*(math.log10(boss_spec_g['flux_nanomaggies']))
boss_spec_r = ascii.read(path+'BOSS_spectrophot_r.dat')
boss_specr = 22.5-2.5*(math.log10(boss_spec_r['flux_nanomaggies']))
boss_spec_i = ascii.read(path+'BOSS_spectrophot_i.dat')
boss_speci = 22.5-2.5*(math.log10(boss_spec_i['flux_nanomaggies']))
boss_spec_z = ascii.read(path+'BOSS_spectrophot_z.dat')
boss_specz = 22.5-2.5*(math.log10(boss_spec_z['flux_nanomaggies']))


##
## Making the plot
##
## http://matplotlib.org/examples/statistics/errorbar_limits.html
## http://matplotlib.org/examples/color/named_colors.html
plt.rcParams.update({'font.size': 14})

# 17.0 and 8.0 for paper
#fig, ax = plt.subplots(figsize=(17.0, 8.0))
# 12.0 and 8.0 for job app figure
fig, ax = plt.subplots(figsize=(12.0, 8.0))


## Plotting the SPECTRA as vertical lines
lw = 5.0
plt.axvline(x=51908, linewidth=lw, color='b')
#plt.axvline(x=55302, linewidth=lw, linestyle='dotted', color='darkgoldenrod')
plt.axvline(x=55302, linewidth=lw, linestyle='dotted', color='r')
#plt.axvline(x=57809, linewidth=lw, linestyle='dashed', color='slategrey')
plt.axvline(x=57809, linewidth=lw, linestyle='dashed', color='k')
plt.axvline(x=58132, linewidth=lw, linestyle='dashed', color='g')

## CRTS and LINEAR
ls = 'solid'
lw = 1.0
ms = 5
ax.errorbar(CRTS['MJD'],   CRTS['mag'],   yerr=CRTS['mag_err'],   fmt='o', linewidth=lw, ms=ms, color='black')
ax.errorbar(LINEAR['MJD'], LINEAR['mag'], yerr=LINEAR['mag_err'], fmt='o', linewidth=lw, ms=ms, color='dimgray')

## POSS from SuperCOSMOS
ms = 12
#ax.plot(UK_J_mjd, SSA_B_AB,  's', linewidth=lw, ms=ms, color='mediumblue')
#ax.plot(POSS_mjd, SSA_R1_AB, 's', linewidth=lw, ms=ms, color='red')
#ax.plot(UK_R_mjd, SSA_R2_AB, 's', linewidth=lw, ms=ms, color='red')
#ax.plot(UK_I_mjd, SSA_I_AB,  's', linewidth=lw, ms=ms, color='teal')


## Pan-STARRS
ms=10
ax.errorbar(PS_g['MJD'], PS_g['mag'], yerr=PS_g['mag_err'], fmt='d', linestyle=ls, ms=ms, linewidth=lw, color='olivedrab')
ax.errorbar(PS_r['MJD'], PS_r['mag'], yerr=PS_r['mag_err'], fmt='d', linestyle=ls, ms=ms, linewidth=lw, color='red')
ax.errorbar(PS_i['MJD'], PS_i['mag'], yerr=PS_i['mag_err'], fmt='d', linestyle=ls, ms=ms, linewidth=lw, color='teal')
ax.errorbar(PS_z['MJD'], PS_z['mag'], yerr=PS_z['mag_err'], fmt='d', linestyle=ls, ms=ms, linewidth=lw, color='lightgrey')
ax.errorbar(PS_y['MJD'], PS_y['mag'], yerr=PS_y['mag_err'], fmt='d', linestyle=ls, ms=ms, linewidth=lw, color='darkmagenta')


## SDSS "original photometry"
ms = 14
ax.errorbar(SDSS_u['MJD'], SDSS_u['mag'], yerr=SDSS_u['mag_err'], fmt='o', ms=ms, linestyle=ls, linewidth=lw, color='b')
ms = 12
ax.errorbar(SDSS_g['MJD'], SDSS_g['mag'], yerr=SDSS_g['mag_err'], fmt='o', ms=ms, linestyle=ls, linewidth=lw, color='olivedrab')
ms = 14
ax.errorbar(SDSS_r['MJD'], SDSS_r['mag'], yerr=SDSS_r['mag_err'], fmt='o', ms=ms, linestyle=ls, linewidth=lw, color='red')
ax.errorbar(SDSS_i['MJD'], SDSS_i['mag'], yerr=SDSS_i['mag_err'], fmt='o', ms=ms, linestyle=ls, linewidth=lw, color='teal')
ax.errorbar(SDSS_z['MJD'], SDSS_z['mag'], yerr=SDSS_z['mag_err'], fmt='o', ms=ms, linestyle=ls, linewidth=lw, color='lightgrey')


## Photometry from SDSS spectrum...
ms=12
#plt.plot(sdss_spec_u['mjd'], sdss_specu, marker='s', markersize=ms, color="b")
#plt.plot(sdss_spec_g['mjd'], sdss_specg, marker='s', markersize=ms, color="olivedrab")
#plt.plot(sdss_spec_r['mjd'], sdss_specr, marker='s', markersize=ms, color="red")
#plt.plot(sdss_spec_i['mjd'], sdss_speci, marker='s', markersize=ms, color="teal")
#plt.plot(sdss_spec_z['mjd'], sdss_specz, marker='s', markersize=ms, color="lightgrey")
## Photometry from BOSS spectrum...
#plt.plot(boss_spec_u['mjd'], boss_specu, marker='s', markersize=ms, color="b")
#plt.plot(boss_spec_g['mjd'], boss_specg, marker='s', markersize=ms, color="olivedrab")
#plt.plot(boss_spec_r['mjd'], boss_specr, marker='s', markersize=ms, color="red")
#plt.plot(boss_spec_i['mjd'], boss_speci, marker='s', markersize=ms, color="teal")
#plt.plot(boss_spec_z['mjd'], boss_specz, marker='s', markersize=ms, color="lightgrey")

##DECaLS
ms = 10
ax.errorbar(DECaLS_g['mjd'], DECaLS_g['aper_diam2pnt0'], yerr=DECaLS_g['err_diam2pnt0'], ms=ms, fmt='P', linestyle=ls, linewidth=lw, color='olivedrab')
ax.errorbar(DECaLS_r['mjd'], DECaLS_r['aper_diam2pnt0'], yerr=DECaLS_r['err_diam2pnt0'], ms=ms, fmt='P', linestyle=ls, linewidth=lw, color='red')
ax.errorbar(DECaLS_z['mjd'], DECaLS_z['aper_diam2pnt0'], yerr=DECaLS_z['err_diam2pnt0'], ms=ms, fmt='P', linestyle=ls, linewidth=lw, color='lightgrey')

## UKIDSS LAS
ms = 10
#ax.errorbar(ULAS_Y['MJD'], ULAS_Y_AB,  yerr=ULAS_Y['YAperMag3Err'],   fmt='h', linestyle=ls, linewidth=lw, color='y', ms=ms)
#ax.errorbar(ULAS_J['MJD'], ULAS_J_AB,  yerr=ULAS_J['J1_AperMag3Err'], fmt='h', linestyle=ls, linewidth=lw, color='goldenrod', ms=ms)
#ax.errorbar(ULAS_H['MJD'], ULAS_H_AB,  yerr=ULAS_H['HAperMag3Err'],   fmt='h', linestyle=ls, linewidth=lw, color='darkgoldenrod', ms=ms)
#ax.errorbar(ULAS_K['MJD'], ULAS_Ks_AB, yerr=ULAS_K['KAperMag3Err'],   fmt='h', linestyle=ls, linewidth=lw, color='orangered', ms=ms)

## WISE W1/W2
ms=16
ax.errorbar(WISE_W1['MJD'], WISE_W1_ABave, yerr=WISE_W1['W1_unc'], fmt='o', ms=ms, linestyle=ls, linewidth=lw*2.5, color='indigo')
ax.errorbar(WISE_W2['MJD'], WISE_W2_ABave, yerr=WISE_W2['W2_unc'], fmt='o', ms=ms, linestyle=ls, linewidth=lw*2.5, color='brown')
ms=4
#ax.errorbar(WISE_L1bs['mjd'], WISE_W1_ABs, yerr=WISE_L1bs['w1sigmpro'], fmt='o', ms=ms, color='indigo')
#ax.errorbar(WISE_L1bs['mjd'], WISE_W2_ABs, yerr=WISE_L1bs['w2sigmpro'], fmt='o', ms=ms, color='brown')



## Tidy up the figure
xmin = 34500   #  51100            ## 51259  ## 49200
xmin = 49200            ## 51259  ## 49200
xmin = 51100            ## 51259  ## 49200
xmax = 58250
ymin = 19.85   # 21.05
ymax = 15.10    #16.65

## Just WISE LCs
#xmin = 55000            ## 51259  ## 49200
#xmax = 58250
#ymin = 17.05   
#ymax = 14.70    #16.65


ax.set_xlim((xmin, xmax))
#ax.set_xlim((54000, xmax))
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
            'SDSS','BOSS', 'Palomar', 'Palomar', 
#        'SDSS spectrum','BOSS spectrum', 'Palomar spectrum', 'Palomar spectrum', 
#    'SDSS spec u', 'SDSS spec g', 'SDSS spec r', 'SDSS spec i', 'SDSS spec z',
#   'BOSS spec u', 'BOSS spec g', 'BOSS spec r', 'BOSS spec i', 'BOSS spec z',
#   '', '', '', '', '',
 #   '', '', '', '', '',
#    'SDSS spectrum','BOSS spectrum', 'Palomar spectrum',
#            'UK-J', 'POSS-I E', 'UK-R', 'UK-I', 
            'CRTS', 'LINEAR',
#            'PanSTARRS g', 'PanSTARRS r', 'PanSTARRS i', 'PanSTARRS z', 'PanSTARRS y',
            'PS g', 'PS r', 'PS i', 'PS z', 'PS y',
            'SDSS u', 'SDSS g',  'SDSS r', 'SDSS i', 'SDSS z',
            'DECaLS g', 'DECaLS r', 'DECaLS z',
#            'ULAS Y', 'ULAS J', 'ULAS H', 'ULAS K',
            'WISE W1', 'WISE W2'],
#           loc="lower left", ncol=3, shadow=True, fancybox=True,
           loc="upper left", ncol=3, shadow=True, fancybox=True,
           fontsize=16, frameon=True)

plt.xlabel('MJD')
plt.ylabel('magnitude (AB)')

## A 4-length sequence of [left, bottom, width, height] quantities.
#im = plt.imread('Legacy_SDSS_zoom_4plot.jpeg')
#newax = fig.add_axes([0.21, 0.69, 0.15, 0.18], anchor='NE')  ## top right
#newax = fig.add_axes([0.12, 0.12, 0.24, 0.19], anchor='NE') 
#newax.imshow(im)
#newax.axis('off')

#im = plt.imread('Legacy_DECaLS_DR3_zoom_4plot.jpeg')
#newax = fig.add_axes([0.33, 0.12, 0.24, 0.19], anchor='NE')
#newax.imshow(im)
#newax.axis('off')




##plt.show()
#fig.savefig("plot.pdf",)
#fig.savefig("plot.eps",format='eps')
#plt.savefig('J110057_lc_201801temp.png', format='png')
plt.savefig('J110057_lc_201801temp.pdf', format='pdf')
#plt.savefig('bias_with_redshift_temp.png',format='png')
plt.show()

plt.close(fig)

