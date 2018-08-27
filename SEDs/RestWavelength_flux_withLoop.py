'''
RestWavelength_flux April 6, 2018
'''
import math
import numpy as np
import matplotlib.pyplot as plt

from matplotlib import colors as mcolors
from matplotlib import gridspec
from astropy.io import fits
from astropy.io import ascii
from astropy.table import Table

##
## READ-IN THE DATA FILE(S)
##

## 
## Composite quasar spectra
##
## The Vanden Berk et al. (2001) composite
path = '/cos_pc19a_npr/data/SDSS/VdB01/'
infile = 'Vanden_Berk_2001_Table1.dat'
table = path+infile
VdB01_comp = ascii.read(table)
VdB01_wave = VdB01_comp['Wavelength']
VdB01_flux = VdB01_comp['Flux']

## The Glikman et al. (2006) composites
path = '/cos_pc19a_npr/data/Glikman2006/'
infile = 'Glikman_2006_ApJ_Table3.dat'
#file = 'Glikman_2006_ApJ_Table7.dat'
table = path+infile
Glikman_comp = ascii.read(table)
Glik_wave = Glikman_comp['Wavelength']
Glik_flux = Glikman_comp['Flux']

## Hernan-Caballero et al. (2016)
path = '/cos_pc19a_npr/data/SEDs/Hernan-Caballero_2016/'
infile = 'table3.dat'
table = path+infile
HernanCab_comp= ascii.read(table)
HernCab_wave = HernanCab_comp['Wavelength']
HernCab_tot  = HernanCab_comp['Fnu_tot']
HernCab_disk = HernanCab_comp['Fnu_disk']
HernCab_dust = HernanCab_comp['Fnu_dust']

## Assef et al. 2010, range of templates
##  1 uJy = 10^-17 erg s^-1 cm2 Hz1
path = '/cos_pc19a_npr/data/SEDs/Assef2010/'
infile = 'Assef_2010_Table1.dat'
table = path+infile
Assef2010_all = ascii.read(table)
Assef_wave = Assef2010_all['Wavelength']
Assef_AGN  = (Assef2010_all['AGN']   * 1e-11) / 1e-17 ## given in table as 1e-11, putting in uJy
Assef_AGN2 = (Assef2010_all['AGN2']  * 1e-14) / 1e-17 ## given in table as 1e-11, putting in uJy
Assef_E    = (Assef2010_all['Ellip'] * 1e-16) / 1e-17 ## given in table as 1e-11, putting in uJy
Assef_Sbc  = (Assef2010_all['Sbc']   * 1e-17) / 1e-17 ## given in table as 1e-11, putting in uJy
Assef_Im   = (Assef2010_all['Im']    * 1e-15) / 1e-17 ## given in table as 1e-11, putting in uJy

##   THE  VHzQs
path = '/cos_pc19a_npr/data/highest_z_QSOs/'
infile = 'THE_TABLE_v0pnt97.dat'
readin = path+infile
## na desig        ra_hms  dec_dms ra      dec     redshift        mag     M1450   errM
all_VHzQs  = ascii.read(readin, delimiter=r'\s')

w1mag = all_VHzQs['w1mag']
w2mag = all_VHzQs['w2mag']
w3mag = all_VHzQs['w3mag']
w4mag = all_VHzQs['w4mag']
w1snr   = all_VHzQs['w1snr']
w2snr   = all_VHzQs['w2snr']
w3snr   = all_VHzQs['w3snr']
w4snr   = all_VHzQs['w4snr']
w1_min_w2_all = (w1mag-w2mag)
w2_min_w3_all = (w1mag-w2mag)
w3_min_w4_all = (w1mag-w2mag)

redshift = all_VHzQs['redshift']
M1450    = all_VHzQs['M1450']

## Figures 6 and 7 from Wright et al. 2018 W1_band_min = 2.8
W1_band_med = 3.4
W1_band_max = 3.9
W2_band_min = 4.0
W2_band_med = 4.6
W2_band_max = 5.3
W3_band_min = 7.5
W3_band_med = 12.0
W3_band_max = 18.0
W4_band_min = 19.0
W4_band_med = 23.0 ## M.Brown et al. (2013) W4_band_max = 27.5

## Wright et al. (2010) Figure 9
w1mag_limit = 17.2
w2mag_limit = 15.8
w3mag_limit = 11.4
w4mag_limit =  8.0

##  1  Jy = 10-26 W m^-2 Hz^-1  = 10^-23 erg s^-1 cm^-2 Hz^-1
##  1 uJy = 10^-17 erg s^-1 cm2 Hz1
##
##  http://wise2.ipac.caltech.edu/docs/release/allwise/faq.html
##  http://wise2.ipac.caltech.edu/docs/release/allsky/expsup/sec4_4h.html

## nu^-2
fc_W1 = 1.000; fc_W2 = 1.000; fc_W3 = 1.000; fc_W4 = 1.000;

## Flux_nu0 is the flux density for sources with constant power-law spectra:
## F_nu \propto nu^0
Flux_nu0_W1 = 309.540
Flux_nu0_W2 = 171.787
Flux_nu0_W3 =  31.674
Flux_nu0_W4 =   8.363

## Flux_nu0_star is the flux density for sources with power-law spectra:
## F_nu \propto nu^-2 and hence the fcs for v^-2 are
## all equal to 1.000.
Flux_nu0_star_W1 = 306.682
Flux_nu0_star_W2 = 170.663
Flux_nu0_star_W3 =  29.045
Flux_nu0_star_W4 =   8.284

Flux_nu_W1_Jy = (Flux_nu0_star_W1 / fc_W1) * (10** (-w1mag_limit/2.5))
Flux_nu_W2_Jy = (Flux_nu0_star_W2 / fc_W2) * (10** (-w2mag_limit/2.5))
Flux_nu_W3_Jy = (Flux_nu0_star_W3 / fc_W3) * (10** (-w3mag_limit/2.5))
Flux_nu_W4_Jy = (Flux_nu0_star_W4 / fc_W4) * (10** (-w4mag_limit/2.5))

Flux_nu_W1_mJy = Flux_nu_W1_Jy *1000
Flux_nu_W2_mJy = Flux_nu_W2_Jy *1000
Flux_nu_W3_mJy = Flux_nu_W3_Jy *1000
Flux_nu_W4_mJy = Flux_nu_W4_Jy *1000

## Wright 2010 Abstract
## WISE is achieving 5 point source sensitivities better than 0.08, 0.11, 1, and 6 mJy
print(Flux_nu_W1_mJy, Flux_nu_W2_mJy, Flux_nu_W3_mJy, Flux_nu_W4_mJy)

##
##  Making the plot...
##
plt.rcParams.update({'font.size': 14})
#fig = plt.figure(figsize=(14, 7))
fig, ax = plt.subplots(figsize=(14, 7))

fontsize        = 18
labelsize       = 18
tickwidth       = 2.0
majorticklength = 12
minorticklength = 6
ticklabelsize   = labelsize

ls       = 'solid'
lw       = 3.0
ms       = 80.
ms_large = ms*3.
ms_small = ms/10.
cmap = plt.cm.plasma  ## Good for W1-W2

xmin     =    .08   ## um
xmax     =  12.00    ## 4.0um in Ang
ymin     =   0.005    ## mJy
ymax     =  50.00 #1e8 # 50.00   ## mJy
ymin_log =  -2.4    ## -2.4, for full W1-4.;  -2.0 for just W1&2
ymax_log =   1.6    ## 1.4 works well... ;2.0, for full W1-4.    0.2 for just W1&2

ax.set_xlim([xmin,xmax])
#plt.xlim([xmin_w12,xmax_w12])
ax.set_xscale('log')

#plt.ylim([ymin,ymax])
#plt.yscale('log')
ax.set_ylim([ymin_log, ymax_log])


## Plotting the Vanden Berk et al. (2001) and Glikman et al. (2006) QSO composites
ax.plot((Glik_wave[0::20]/10000.), np.log10((Glik_flux[0::20]/2.)), alpha=1.0, lw=lw, color='gold')
ax.plot((VdB01_wave/10000.), np.log10(VdB01_flux),                  alpha=0.5, lw=lw, color='darkcyan')

## Plotting Hernan-Caballero_2016_MNRAS_463_2064
ax.plot(HernCab_wave, np.log10(HernCab_tot),  alpha=0.8, color='k',                   lw=lw)
ax.plot(HernCab_wave, np.log10(HernCab_dust), alpha=0.8, color='salmon', ls='dashed', lw=lw)
ax.plot(HernCab_wave, np.log10(HernCab_disk),  alpha=0.8, color='forestgreen',         lw=lw)

#ax.plot(Assef_wave, np.log10(Assef_AGN),  alpha=0.75)
#ax.plot(Assef_wave, np.log10(Assef_AGN2), alpha=0.75)
#ax.plot(Assef_wave, np.log10(Assef_E),    alpha=0.75)
#ax.plot(Assef_wave, np.log10(Assef_Sbc),  alpha=0.75)
#ax.plot(Assef_wave, np.log10(Assef_Im),   alpha=0.75)

xxx = np.array(range(len(w1mag)))
yyy = np.array(range(len(w1mag)))

## "Somehow", these three lines convert the
## 10^-1, 10^0 and 10^1 x-axis lables to 0.1, 1, 10...
from matplotlib.ticker import ScalarFormatter
for axis in [ax.xaxis, ax.yaxis]:
    axis.set_major_formatter(ScalarFormatter())

#col_4mypoints = [ (w1snr), (w2snr), (w3snr]), (w4snr)]
   
for ii in range(len(w1mag)):
    W1_sampling_rest = W1_band_med/(1+redshift[ii]) #* 10000. ## um to Ang
    W2_sampling_rest = W2_band_med/(1+redshift[ii]) #* 10000.
    W3_sampling_rest = W3_band_med/(1+redshift[ii]) #* 10000.
    W4_sampling_rest = W4_band_med/(1+redshift[ii]) #* 10000.

    W1minW2_color = w1mag[ii] - w2mag[ii]
    Flux_nu_W1_mJy = ((Flux_nu0_star_W1 / fc_W1) * (10** (-w1mag[ii]/2.5))) *1000.
    Flux_nu_W2_mJy = ((Flux_nu0_star_W2 / fc_W2) * (10** (-w2mag[ii]/2.5))) *1000.
    Flux_nu_W3_mJy = ((Flux_nu0_star_W3 / fc_W3) * (10** (-w3mag[ii]/2.5))) *1000.
    Flux_nu_W4_mJy = ((Flux_nu0_star_W4 / fc_W4) * (10** (-w4mag[ii]/2.5))) *1000.
        
    #print(ii, w1mag[ii], w2mag[ii], w3mag[ii], w4mag[ii], redshift[ii], W1_sampling_re
    W_samp_rest   = [W1_sampling_rest, W2_sampling_rest, W3_sampling_rest, W4_sampling_rest]
    Flux_nu_W_mJy = [Flux_nu_W1_mJy,   Flux_nu_W2_mJy,   Flux_nu_W3_mJy,  Flux_nu_W4_mJy]
    log_Flux = np.log10(Flux_nu_W_mJy)

    #plt.plot(W_samp_rest, log_Flux)
    #plt.scatter(W_samp_rest, log_Flux)
    #plt.pause(0.005)
#    col_4mypoints = [ (w1snr[ii]), (w2snr[ii]), (w3snr[ii]), (w4snr[ii])]
    hdl = ax.scatter(W_samp_rest, log_Flux, c='k', cmap=cmap, s=ms*1.3, alpha=1.0)
#    hdl = ax.scatter(W_samp_rest, log_Flux, c=col_4mypoints, cmap=cmap, s=ms, alpha=1.0)
    hdl = ax.scatter(W_samp_rest, log_Flux, c=col_4mypoints, cmap=cmap, s=ms, alpha=0.85)
#    print(ii, redshift[ii], w1mag[ii], w2mag[ii], w3mag[ii], w4mag[ii], W_samp_rest, col_4mypoints)
    print(ii, W_samp_rest, col_4mypoints)
    
#    xxx[ii] = np.array(W_samp_rest)
#    yyy[ii] =log_Flux

     
ax.set_xlabel(r"Rest-frame wavelength / $\mu$m")
ax.set_ylabel("log Flux density  / $\mu$Jy");

datco=[0.68, 0.80, 0.20, 0.025]     ## W1-W2 SNR

##and finally the new colorabar axes at the right position!
cbar_ax = fig.add_axes(datco)
clevs = [0, 10, 20]  ## W1-W2

cb1 = plt.colorbar(hdl, cax=cbar_ax, orientation='horizontal', ticks=clevs)
#cb1.set_label(r'W1 SNR', labelpad=-80, fontsize=fontsize)
cb1.set_label(r'W1/2/3/4 SNR',  labelpad=-80, fontsize=fontsize/1.4)
cb1.ax.tick_params(labelsize=fontsize/1.4)



fontsize = 20
weight = 600
ax.text(1.5,  -1.60, r'Vanden Berk (2001)',        fontsize=fontsize, weight=weight, color='c')
ax.text(1.5,  -1.90, r'Glikman (2006)',            fontsize=fontsize, weight=weight, color='gold')
ax.text(1.5,  -2.20, r'Hernan-Caballero+ (2016)',  fontsize=fontsize, weight=weight, color='k')
ax.text(0.12, -1.60, r'Disk',                      fontsize=fontsize, weight=weight, color='forestgreen')
ax.text(0.30, -2.10, r'Dust',                      fontsize=fontsize, weight=weight, color='salmon')


plt.savefig('RestWavelength_flux_temp.png', format='png')
plt.savefig('RestWavelength_flux_temp.pdf', format='pdf')
plt.close(fig)
#plt.show()
