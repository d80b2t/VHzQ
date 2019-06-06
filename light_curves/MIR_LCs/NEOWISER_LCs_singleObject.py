'''
http://blog.marmakoide.org/?p=94
'''

from astropy.io import ascii

import numpy as np

#import matplotlib.backends.backend_pdf
#import matplotlib.pyplot as plt

from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

import random

#path='/cos_pc19a_npr/data/highest_z_QSOs/'
path = '/cos_pc19a_npr/programs/quasars/highest_z/light_curves/MIR_LCs/'
file = 'NEOWISER-R_SingleExposure_L1bs.tbl'

data = ascii.read(path+file) 
type(data)
upto_this = data['cntr_01'].max()

##pdf_pages = PdfPages('my-fancy-document.pdf')
out_pdf = 'NEOWISER_LCs_VHzQs_temp.pdf'
#pdfs = matplotlib.backends.backend_pdf.PdfPages(out_pdf)
pdf_pages = PdfPages(out_pdf)

#cnt = 0
#figs = plt.figure()

#fig = plt.figure(figsize=(10, 10)) # inches
plot_num = 321
totes = 0


## define the colormap
cmap = plt.cm.inferno_r

ls = 'solid'
lw = 1.0
ms = 60.
ms_large = ms*3.
fontsize=24
alpha=1.00

for x in range(upto_this):
#for x in range(10):
    x=x+1
    data_one = data[np.where(data['cntr_01'] == x)]

    if len(data_one) > 0:  
    
        #print(x, data_one['ra'][0], data_one['dec'][0], len(data_one))
        print(len(data_one))
        totes = totes + len(data_one)
        ra = data_one['ra'][0]
        dec = data_one['dec'][0]

        ## Setting up a 3 panel, "triptych" style plot
        fig, (ax1, ax2, ax3) = plt.subplots(1,3, figsize=(21.5, 8.5)) # inches
        
        left   = 0.06   # the left side of the subplots of the figure
        right  = 0.98   # the right side of the subplots of the figure
        bottom = 0.10   # the bottom of the subplots of the figure
        top    = 0.94   # the top of the subplots of the figure
        wspace = 0.26   # the amount of width reserved for blank space between subplots
        hspace = 0.06   # the amount of height reserved for white space between subplots
        plt.subplots_adjust(left=left, bottom=bottom, right=right, top=top, wspace=wspace, hspace=hspace)
        
        ## W1/2 Light-curves, y-axis reverse   
        ax1.scatter(data_one['mjd'], data_one['w1mpro'], color='k', alpha=alpha, s=ms*1.8)
        ax1.scatter(data_one['mjd'], data_one['w1mpro'], color='r', alpha=alpha, s=ms)
        ax1.scatter(data_one['mjd'], data_one['w2mpro'], color='k', alpha=alpha, s=ms*1.8)
        ax1.scatter(data_one['mjd'], data_one['w2mpro'], color='c', alpha=alpha, s=ms)
        ax1.set_xlim((56500,58140))
        ax1.set_ylim(ax1.get_ylim()[::-1])
        ax1.set_xlabel('MJD',                   fontsize=fontsize)
        ax1.set_ylabel('WISE  W1/2  magnitude', fontsize=fontsize)
        ax1.tick_params('x', direction='in', which='both', bottom='True', top='True', left='True', right='True', labelsize=fontsize)
        ax1.tick_params('y', direction='in', which='both', bottom='True', top='True', left='True', right='True', labelsize=fontsize)

        ## W1/2 vs. color to look for color-changes...
        ax2.scatter(data_one['w1mpro'], (data_one['w1mpro']-data_one['w2mpro']),color='k', alpha=alpha, s=ms*1.8)
        ax2.scatter(data_one['w1mpro'], (data_one['w1mpro']-data_one['w2mpro']),color='r', alpha=alpha, s=ms)
        ax2.set_xlabel('W1 magnitude',                   fontsize=fontsize)
        ax2.set_ylabel('W1 - W2', fontsize=fontsize)
        ax2.tick_params('x', direction='in', which='both', bottom='True', top='True', left='True', right='True', labelsize=fontsize)
        ax2.tick_params('y', direction='in', which='both', bottom='True', top='True', left='True', right='True', labelsize=fontsize)
        ax2.set_title('(R.A., Decl.) = {} {} {}'.format(ra,',',dec), fontsize=fontsize)

        ax3.scatter(data_one['w2mpro'], (data_one['w1mpro']-data_one['w2mpro']),color='k', alpha=alpha, s=ms*1.8)
        ax3.scatter(data_one['w2mpro'], (data_one['w1mpro']-data_one['w2mpro']),color='c', alpha=alpha, s=ms)
        ax3.set_xlabel('W2 magnitude',                   fontsize=fontsize)
        ax3.set_ylabel('W1 - W2', fontsize=fontsize)
        ax3.tick_params('x', direction='in', which='both', bottom='True', top='True', left='True', right='True',  labelsize=fontsize)
        ax3.tick_params('y', direction='in', which='both', bottom='True', top='True', left='True', right='False', labelsize=fontsize)

    ## Putting in the `else' will give you enteries for 0 in NoOfEpochs_perQuasar.dat
    ## and will also have the NEOWISER_LCs_VHzQs_temp.pdf be 463 pages long. However,
    ## you get duplicate plots in NEOWISER_LCs_VHzQs_temp.pdf for the `else' objects. 
    else:
        print('0')
        
    ## Done with the page
    pdf_pages.savefig(fig)

                               
    
## Write the PDF document to the disk
pdf_pages.close()   
