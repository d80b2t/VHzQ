'''
http://blog.marmakoide.org/?p=94
'''

import os
import numpy as np

from astropy.io import ascii
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

## Reading-in the NEOWISE-R L1b single exposure numbers
path = '../../data/light_curves/NEOWISE-R/'
#path = os.path.join(os.path.dirname(os.getcwd()),'/MIR_LCs/')
file = 'NEOWISER-R_SingleExposure_L1bs.tbl'

data = ascii.read(path+file) 
type(data)
upto_this = data['cntr_01'].max()


## Reading-in the *averaged*
##   Generated using::    average_NEOWISE_lightcurves.py 
path  = '../../data/light_curves/NEOWISE-R/'
file  = 'NEOWISER-R_SingleExposure_L1bs_20190429_averaged.tbl'
avers = ascii.read(path+file) 


out_pdf = 'NEOWISER_LCs_VHzQs_temp.pdf'
pdf_pages = PdfPages(out_pdf)
## http://wise2.ipac.caltech.edu/docs/release/allwise/expsup/sec1_2.html#phases
ALLWISE_MJD_min = 55203.     #  2010-January-07 
ALLWISE_MJD_max = 55593.
ALLWISE_MJD_mid = ((ALLWISE_MJD_max + ALLWISE_MJD_min))/2.
mjd_range_ALLWISE=[ALLWISE_MJD_min,ALLWISE_MJD_max]

## MJDs in NEOWISE-R data:
##    NEOWISE 2015    December 13, 2013 and December 13, 2014 UTC
##    NEOWISE 2016    December 13, 2014 and December 13, 2015 UTC
##    NEOWISE 2017    December 13, 2015 and December 13, 2016 UTC
##    NEOWISE 2018    December 13, 2016 and December 13, 2017 UTC
##    NEOWISE 2019    December 13, 2017 and December 13, 2018 UTC
## from NEOWISER-R_SingleExposure_L1bs.tbl:
##    data['mjd'].min()   56639.790   which is 2013-Dec-13
##    data['mjd'].max()   58465.286   which is 2018-Dec-13

## https://neowise.ipac.caltech.edu/
##  NEOWISE survey observations are continuing in 2019.
##  As of mid-May 2019, NEOWISE is 94% of the way through its
##  11th coverage of the sky since the start of the Reactivation mission. 


## define the colormap
cmap = plt.cm.inferno_r

ls       = 'solid'
lw       = 2.0
ms       = 30.
ms_large = ms*5.
ms_full  = ms*5.
fontsize = 24
alpha    = 1.00
plot_num = 321
totes    = 0

for x in range(upto_this):
    #for x in range(10):
    x=x+1
    data_one =  data[np.where(data['cntr_01'] == x)]
    data_two = avers[np.where(avers['cntr_01'] == x)]
    
    if len(data_one) < 1:
        print(x, 'No of epochs: 0')

    if len(data_one) > 0:
        # print(x, data_one['ra'][0], data_one['dec'][0], len(data_one))
        print(x, 'No of epochs:', len(data_one))
        
        if len(data_two) > 0:
            totes = totes + len(data_one)
            ra  = data_one['ra'][0]
            dec = data_one['dec'][0]
    
            ## Setting up a 3 panel, "triptych" style plot
            fig, (ax1, ax2, ax3) = plt.subplots(1,3, figsize=(21.5, 8.5), gridspec_kw = {'width_ratios':[3, 1, 1]}) # inches
            #ax1 = plt.subplot(131, figsize=(12.0, 8.5) )
            #ax2 = plt.subplot(132, figsize=(5.0, 8.5))
            #ax3 = plt.subplot(133, figsize=(5.0, 8.5), sharey=ax2)
    
            left   = 0.06   # the left side of the subplots of the figure
            right  = 0.98   # the right side of the subplots of the figure
            bottom = 0.10   # the bottom of the subplots of the figure
            top    = 0.94   # the top of the subplots of the figure
            wspace = 0.26   # the amount of width reserved for blank space between subplots
            hspace = 0.06   # the amount of height reserved for white space between subplots
            plt.subplots_adjust(left=left, bottom=bottom, right=right, top=top, wspace=wspace, hspace=hspace)
        
            ## W1/2 Light-curves, y-axis reverse
            ## ALLWISE SINGLE MJD POINT
            ax1.scatter(ALLWISE_MJD_mid,  data_one['w1mpro_allwise'][0], color='k', alpha=alpha, s=ms_large*1.8)
            ax1.scatter(ALLWISE_MJD_mid,  data_one['w1mpro_allwise'][0], color='r', alpha=alpha, s=ms_large)
            ax1.scatter(ALLWISE_MJD_mid,  data_one['w2mpro_allwise'][0], color='k', alpha=alpha, s=ms_large*1.8)
            ax1.scatter(ALLWISE_MJD_mid,  data_one['w2mpro_allwise'][0], color='c', alpha=alpha, s=ms_large)
    
            ## NEOWISE-R data; single-epich L1bs
            ax1.scatter(data_one['mjd'], data_one['w1mpro'], color='k', alpha=alpha, s=ms*1.8)
            ax1.scatter(data_one['mjd'], data_one['w1mpro'], color='r', alpha=alpha, s=ms)
            ax1.scatter(data_one['mjd'], data_one['w2mpro'], color='k', alpha=alpha, s=ms*1.8)
            ax1.scatter(data_one['mjd'], data_one['w2mpro'], color='c', alpha=alpha, s=ms)

            ## plotting the NEOWISE-R L1b averages...
            ax1.scatter(data_two['mean_mjd'], data_two['w1mpro_wgt'], color='k', alpha=alpha, s=ms_full*1.8)
            ax1.scatter(data_two['mean_mjd'], data_two['w1mpro_wgt'], color='r', alpha=alpha, s=ms_full)
            ax1.scatter(data_two['mean_mjd'], data_two['w2mpro_wgt'], color='k',alpha=alpha,  s=ms_full*1.8)
            ax1.scatter(data_two['mean_mjd'], data_two['w2mpro_wgt'], color='c', alpha=alpha, s=ms_full)
        
            ## AllWISE 4-Band Cryo Survey Phase started MJD 55203
            ax1.set_xlim((55000,58140))
            ## Just NEOWISE-R
            #ax1.set_xlim((56500,58140))
            ax1.set_ylim(ax1.get_ylim()[::-1])
            ax1.set_xlabel('MJD',                   fontsize=fontsize)
            ax1.set_ylabel('WISE  W1/2  magnitude', fontsize=fontsize)
            ax1.tick_params('x', direction='in', which='both', bottom='True', top='True', left='True', right='True', labelsize=fontsize)
            ax1.tick_params('y', direction='in', which='both', bottom='True', top='True', left='True', right='True', labelsize=fontsize)
    
            ## W1 vs. color to look for color-changes...
            ax2.scatter(data_one['w1mpro'], (data_one['w1mpro']-data_one['w2mpro']),color='k', alpha=alpha, s=ms*1.8)
            ax2.scatter(data_one['w1mpro'], (data_one['w1mpro']-data_one['w2mpro']),color='r', alpha=alpha, s=ms)
            ax2.set_xlabel('W1 magnitude',                   fontsize=fontsize)
            ax2.set_ylabel('W1 - W2', fontsize=fontsize)
            ax2.tick_params('x', direction='in', which='both', bottom='True', top='True', left='True', right='True', labelsize=fontsize)
            ax2.tick_params('y', direction='in', which='both', bottom='True', top='True', left='True', right='True', labelsize=fontsize)
            ax2.set_title('(R.A., Decl.) = {} {} {}'.format(ra,',',dec), fontsize=fontsize)
    
            ## W2 vs. color to look for color-changes...
            ax3.scatter(data_one['w2mpro'], (data_one['w1mpro']-data_one['w2mpro']),color='k', alpha=alpha, s=ms*1.8)
            ax3.scatter(data_one['w2mpro'], (data_one['w1mpro']-data_one['w2mpro']),color='c', alpha=alpha, s=ms)
            ax3.set_xlabel('W2 magnitude',                   fontsize=fontsize)
            #ax3.set_ylabel('W1 - W2', fontsize=fontsize)
            ax3.tick_params('x', direction='in', which='both', bottom='True', top='True', left='True', right='True',  labelsize=fontsize)
            ax3.tick_params('y', direction='in', which='both', bottom='True', top='True', left='True', right='False', labelsize=fontsize)
    
            ax2.get_shared_x_axes().join(ax2, ax3)
            ax3.set_yticklabels([])
            #plt.subplots_adjust(wspace=.0)
            
            ## Done with the page
            pdf_pages.savefig(fig)
##
## Come out both if loops..
##            
## Write the PDF document to the disk
pdf_pages.close()

plt.close()







