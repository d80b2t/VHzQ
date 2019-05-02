'''
http://blog.marmakoide.org/?p=94
'''

from astropy.io import ascii
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

import numpy as np
import random

#path='/cos_pc19a_npr/data/highest_z_QSOs/'
#file = 'NEOWISER-R_SingleExposure_L1bs.tbl'

path='/cos_pc19a_npr/programs/quasars/highest_z/data/light_curves/NEOWISE-R/'
file = 'NEOWISER-R_SingleExposure_L1bs_20190429.tbl'


data = ascii.read(path+file) 
type(data)
upto_this = data['cntr_01'].max()

out_pdf = 'NEOWISER_LCs_VHzQs_temp.pdf'
pdf_pages = PdfPages(out_pdf)

## data['mjd'].max()
## 58465.28598113        2018-Dec-13

ALLWISE_MJD_min = 55210.     # 2010-Jan-14 
ALLWISE_MJD_max = 55593.     # 2011-Feb-01
ALLWISE_MJD_mid = ((ALLWISE_MJD_max + ALLWISE_MJD_min))/2.
mjd_range_ALLWISE=[ALLWISE_MJD_min,ALLWISE_MJD_max]

NEOWISER_MJD_max  = 58465.

## define the colormap
#plt.style.use('dark_background')
cmap = plt.cm.inferno_r

ls       = 'solid'
lw       = 2.0
s        = 60.
s_large  = s*5.
ms       = 6.0
fontsize = 24
alpha    = 1.00
plot_num = 321
totes    = 0

for x in range(upto_this):
#for x in range(10):
    x=x+1
    data_one = data[np.where(data['cntr_01'] == x)]

    if len(data_one) < 1:
          print('0')
          
    if len(data_one) > 0:  
#        print(x, data_one['ra'][0], data_one['dec'][0], len(data_one))
        print(len(data_one))
        totes = totes + len(data_one)
        ra = data_one['ra'][0]
        dec = data_one['dec'][0]

        ## Setting up a 3 panel, "triptych" style plot
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14.0, 8.5),sharex=True, gridspec_kw = {'height_ratios':[5, 3]}) # inches
        #ax1 = plt.subplot(131, figsize=(12.0, 8.5) )
        #ax2 = plt.subplot(132, figsize=(5.0, 8.5))

        left   = 0.10   # the left side of the subplots of the figure
        right  = 0.98   # the right side of the subplots of the figure
        bottom = 0.10   # the bottom of the subplots of the figure
        top    = 0.94   # the top of the subplots of the figure
        wspace = 0.26   # the amount of width reserved for blank space between subplots
        hspace = 0.06   # the amount of height reserved for white space between subplots
        plt.subplots_adjust(left=left, bottom=bottom, right=right, top=top, wspace=wspace, hspace=hspace)

        ## W1/2 Light-curves, y-axis reverse
        ##
        ## NEOWISE-R data
        #ax1.errorbar(DECaLS_g['mjd'], DECaLS_g['aper_diam2pnt0'], yerr=DECaLS_g['err_diam2pnt0'], ms=ms, fmt='P', linestyle=ls, linewidth=lw, color='olivedrab')
        ms       = 7.0
        ## ms = 1.8 for 'k'; ms=  
        ax1.errorbar(data_one['mjd'], data_one['w1mpro'], yerr=data_one['w1sigmpro'], color='w', alpha=alpha, ms=ms*1.6,  fmt='o')
        ax1.errorbar(data_one['mjd'], data_one['w1mpro'], yerr=data_one['w1sigmpro'], color='r', alpha=alpha, ms=ms,  fmt='o')
        ax1.errorbar(data_one['mjd'], data_one['w2mpro'], yerr=data_one['w2sigmpro'], color='w', alpha=alpha, ms=ms*1.6,  fmt='o')
        ax1.errorbar(data_one['mjd'], data_one['w2mpro'], yerr=data_one['w2sigmpro'], color='c', alpha=alpha, ms=ms,  fmt='o')

        ## ALLWISE SINGLE MJD POINT
        #ax1.scatter(ALLWISE_MJD_mid,  data_one['w1mpro_allwise'][0], color='k', alpha=alpha, s=s_large*1.8)
        #ax1.scatter(ALLWISE_MJD_mid,  data_one['w1mpro_allwise'][0], color='r', alpha=alpha, s=s_large)
        #ax1.scatter(ALLWISE_MJD_mid,  data_one['w2mpro_allwise'][0], color='k', alpha=alpha, s=s_large*1.8)
        #ax1.scatter(ALLWISE_MJD_mid,  data_one['w2mpro_allwise'][0], color='c', alpha=alpha, s=s_large)
        s = 14.0
        ax1.errorbar(ALLWISE_MJD_mid, data_one['w1mpro_allwise'][0], yerr=data_one['w1sigmpro_allwise'][0], color='k', alpha=alpha, ms=s*1.4,  fmt='o')
        ax1.errorbar(ALLWISE_MJD_mid, data_one['w1mpro_allwise'][0], yerr=data_one['w1sigmpro_allwise'][0], color='r', alpha=alpha, ms=s,  fmt='o')
        ax1.errorbar(ALLWISE_MJD_mid, data_one['w2mpro_allwise'][0], yerr=data_one['w2sigmpro_allwise'][0], color='k', alpha=alpha, ms=s*1.4,  fmt='o')
        ax1.errorbar(ALLWISE_MJD_mid, data_one['w2mpro_allwise'][0], yerr=data_one['w2sigmpro_allwise'][0], color='c', alpha=alpha, ms=s,  fmt='o')


        ## Going back to ALLWISE...
        ax1.set_xlim((ALLWISE_MJD_min-210, NEOWISER_MJD_max+200))         # 2009-Jun-18  to  2019-Apr-27
        ## Just NEOWISE-R
        #ax1.set_xlim((56500,58140))
        ax1.set_ylim(ax1.get_ylim()[::-1])
        #ax1.set_xlabel('MJD',                   fontsize=fontsize)
        ax1.set_ylabel('WISE  W1/2  magnitude', fontsize=fontsize)
        ax1.tick_params('x', direction='in', which='both', bottom='True', top='True', left='True', right='True', labelsize=fontsize)
        ax1.tick_params('y', direction='in', which='both', bottom='True', top='True', left='True', right='True', labelsize=fontsize)
        ax1.set_title('(R.A., Decl.) = {} {} {}'.format(ra,',',dec), fontsize=fontsize)

        
        ##
        ## W1 vs. color to look for color-changes...
        ##
        #ax2.scatter(data_one['w1mpro'], (data_one['w1mpro']-data_one['w2mpro']),color='k', alpha=alpha, s=ms*1.8)
        #ax2.scatter(data_one['w1mpro'], (data_one['w1mpro']-data_one['w2mpro']),color='r', alpha=alpha, s=ms)
        #ax2.scatter(data_one['w2mpro'], (data_one['w1mpro']-data_one['w2mpro']),color='k', alpha=alpha, s=ms*1.8)
        #ax2.scatter(data_one['w2mpro'], (data_one['w1mpro']-data_one['w2mpro']),color='c', alpha=alpha, s=ms)
        mss= 60.
        ax2.scatter(data_one['mjd'], (data_one['w1mpro']-data_one['w2mpro']),                       color='k', alpha=alpha, s=mss*1.8)
        ax2.scatter(ALLWISE_MJD_mid, (data_one['w1mpro_allwise'][0]-data_one['w2mpro_allwise'][0]), color='k', alpha=alpha, s=s_large*1.8)
    
        #ax2.set_xlabel('W1/W2 magnitude',                   fontsize=fontsize)
        ax2.set_xlabel('MJD',                   fontsize=fontsize)
        ax2.set_ylabel('W1 - W2', fontsize=fontsize)
        ax2.tick_params('x', direction='in', which='both', bottom='True', top='True', left='True', right='True', labelsize=fontsize)
        ax2.tick_params('y', direction='in', which='both', bottom='True', top='True', left='True', right='True', labelsize=fontsize)

        ax2.set_xlim((ALLWISE_MJD_min-210, NEOWISER_MJD_max+200))    
        ax2.set_ylim(-0.2, 3.2)

        plt.subplots_adjust(hspace=0)

        ## Done with the page
        pdf_pages.savefig(fig)
    
## Write the PDF document to the disk
pdf_pages.close()

plt.close()







