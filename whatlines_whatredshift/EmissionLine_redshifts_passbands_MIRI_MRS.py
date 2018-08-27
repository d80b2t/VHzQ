#!/usr/bin/env python
'''
Python code to figure out/state when various (quasar) emission lines 
move in and out of various SDSS/UKIDSS/WISE and JWST passbands
'''

import numpy as np

np.set_printoptions(precision=3)


## Table 9, Peth et al. (2011, AJ, 141, 105)
Channel_1 = np.array([ 4.89,  5.65,  7.66])
Channel_2 = np.array([ 7.49,  8.65,  11.71])
Channel_3 = np.array([11.53, 13.37,  18.05])
Channel_4 = np.array([17.66, 20.54,  28.45])

## VdB01, Table 2, lambda_lab IN MICRONS!
Lya_lambda    = 0.121567
CIV_lambda    = 0.154906        
MgII_lambda   = 0.279875
Halpha_lambda = 0.656461
## Figre from Glikman et al. 2006, ApJ, 640, 579
## e.g. Table 6 and Fig. 1 etc. 
## Balmer, Paschen, and Brackett     # Flux / Flux_Halpha
O_one_lambda         = 0.8446         #  3.78
S_three_lambda       = 0.9069         #  0.25
Fe_two_lambda        = 0.9202         #  1.10
Pa_epsilon_lambda    = 0.9545         #  2.02
Pa_delta_lambda      = 1.0049        #  5.72
## See also, Selsing et al, 2016, A&A, 585A, 87
He_one_lambda        = 1.0830        # 10.05
Pa_gamma_lambda      = 1.0941        #  1.85
O_one_prime_lambda   = 1.1287        #  0.89
Pa_beta_lambda       = 1.2820        #  4.82
Pa_alpha_lambda      = 1.8756        #  3.10
He_20k_lambda        = 2.0580        #  1.89
Br_gamma_lambda      = 2.1654
Br_beta_lambda       = 2.6260

Channel_1_Lya = (Channel_1/Lya_lambda)-1
Channel_2_Lya = (Channel_2/Lya_lambda)-1
Channel_3_Lya = (Channel_3/Lya_lambda)-1
Channel_4_Lya = (Channel_4/Lya_lambda)-1
    
Channel_1_CIV = (Channel_1/CIV_lambda)-1
Channel_2_CIV = (Channel_2/CIV_lambda)-1
Channel_3_CIV = (Channel_3/CIV_lambda)-1
Channel_4_CIV = (Channel_4/CIV_lambda)-1
        
Channel_1_MgII = (Channel_1/MgII_lambda)-1
Channel_2_MgII = (Channel_2/MgII_lambda)-1
Channel_3_MgII = (Channel_3/MgII_lambda)-1
Channel_4_MgII = (Channel_4/MgII_lambda)-1

Channel_1_Halpha = (Channel_1/Halpha_lambda)-1
Channel_2_Halpha = (Channel_2/Halpha_lambda)-1
Channel_3_Halpha = (Channel_3/Halpha_lambda)-1
Channel_4_Halpha = (Channel_4/Halpha_lambda)-1
          
Channel_1_Pa_delta = (Channel_1/Pa_delta_lambda)-1
Channel_2_Pa_delta = (Channel_2/Pa_delta_lambda)-1
Channel_3_Pa_delta = (Channel_3/Pa_delta_lambda)-1
Channel_4_Pa_delta = (Channel_4/Pa_delta_lambda)-1
      
Channel_1_He_one = (Channel_1/He_one_lambda)-1
Channel_2_He_one = (Channel_2/He_one_lambda)-1
Channel_3_He_one = (Channel_3/He_one_lambda)-1
Channel_4_He_one = (Channel_4/He_one_lambda)-1
    

print('\n')
print('Lyman-alpha enters MRS Channel 1 at redshift' , "%6.3f" % Channel_1_Lya[0], 'and exits at ', "%6.3f" % Channel_1_Lya[-1])
print('Lyman-alpha enters MRS Channel 2 at redshift' , "%6.3f" % Channel_2_Lya[0], 'and exits at ', "%6.3f" % Channel_2_Lya[-1])
print('Lyman-alpha enters MRS Channel 3 at redshift' , "%6.3f" % Channel_3_Lya[0], 'and exits at ', "%6.3f" % Channel_3_Lya[-1])
print('Lyman-alpha enters MRS Channel 4 at redshift' , "%6.3f" % Channel_4_Lya[0], 'and exits at ', "%6.3f" % Channel_4_Lya[-1])

print('Carbon-IV enters MRS Channel 1 at redshift' , "%6.3f" % Channel_1_CIV[0], 'and exits at ', "%6.3f" % Channel_1_CIV[-1])
print('Carbon-IV enters MRS Channel 2 at redshift' , "%6.3f" % Channel_2_CIV[0], 'and exits at ', "%6.3f" % Channel_2_CIV[-1])
print('Carbon-IV enters MRS Channel 3 at redshift' , "%6.3f" % Channel_3_CIV[0], 'and exits at ', "%6.3f" % Channel_3_CIV[-1])
print('Carbon-IV enters MRS Channel 4 at redshift' , "%6.3f" % Channel_4_CIV[0], 'and exits at ', "%6.3f" % Channel_4_CIV[-1])

print('Mg-II enters MRS Channel 1 at redshift' , "%6.3f" % Channel_1_MgII[0], 'and exits at ', "%6.3f" % Channel_1_MgII[-1])
print('Mg-II enters MRS Channel 2 at redshift' , "%6.3f" % Channel_2_MgII[0], 'and exits at ', "%6.3f" % Channel_2_MgII[-1])
print('Mg-II enters MRS Channel 3 at redshift' , "%6.3f" % Channel_3_MgII[0], 'and exits at ', "%6.3f" % Channel_3_MgII[-1])
print('Mg-II enters MRS Channel 4 at redshift' , "%6.3f" % Channel_4_MgII[0], 'and exits at ', "%6.3f" % Channel_4_MgII[-1])

print('H-alpha enters MRS Channel 1 at redshift' , "%6.3f" % Channel_1_Halpha[0], 'and exits at ', "%6.3f" % Channel_1_Halpha[-1])
print('H-alpha enters MRS Channel 2 at redshift' , "%6.3f" % Channel_2_Halpha[0], 'and exits at ', "%6.3f" % Channel_2_Halpha[-1])
print('H-alpha enters MRS Channel 3 at redshift' , "%6.3f" % Channel_3_Halpha[0], 'and exits at ', "%6.3f" % Channel_3_Halpha[-1])
print('H-alpha enters MRS Channel 4 at redshift' , "%6.3f" % Channel_4_Halpha[0], 'and exits at ', "%6.3f" % Channel_4_Halpha[-1])

print('Pa-delta enters MRS Channel 1 at redshift' , "%6.3f" % Channel_1_Pa_delta[0], 'and exits at ', "%6.3f" % Channel_1_Pa_delta[-1])
print('Pa-delta enters MRS Channel 2 at redshift' , "%6.3f" % Channel_2_Pa_delta[0], 'and exits at ', "%6.3f" % Channel_2_Pa_delta[-1])
print('Pa-delta enters MRS Channel 3 at redshift' , "%6.3f" % Channel_3_Pa_delta[0], 'and exits at ', "%6.3f" % Channel_3_Pa_delta[-1])
print('Pa-delta enters MRS Channel 4 at redshift' , "%6.3f" % Channel_4_Pa_delta[0], 'and exits at ', "%6.3f" % Channel_4_Pa_delta[-1])

print('He I enters MRS Channel 1 at redshift' , "%6.3f" % Channel_1_He_one[0], 'and exits at ', "%6.3f" % Channel_1_He_one[-1])
print('He I enters MRS Channel 2 at redshift' , "%6.3f" % Channel_2_He_one[0], 'and exits at ', "%6.3f" % Channel_2_He_one[-1])
print('He I enters MRS Channel 3 at redshift' , "%6.3f" % Channel_3_He_one[0], 'and exits at ', "%6.3f" % Channel_3_He_one[-1])
print('He I enters MRS Channel 4 at redshift' , "%6.3f" % Channel_4_He_one[0], 'and exits at ', "%6.3f" % Channel_4_He_one[-1])

