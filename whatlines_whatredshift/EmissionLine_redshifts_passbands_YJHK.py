#!/usr/bin/env python
'''
Python code to figure out/state when various (quasar) emission lines 
move in and out of various SDSS/UKIDSS/WISE and JWST passbands
'''

import numpy as np

np.set_printoptions(precision=3)


## Table 9, Peth et al. (2011, AJ, 141, 105)
Y_UKIDSS = np.array([ 0.9790,  1.0305,  1.0810])
J_UKIDSS = np.array([ 1.16909, 1.2483,  1.3280])
H_UKIDSS = np.array([ 1.4920,  1.6313,  1.7840])
K_UKIDSS = np.array([ 2.0290,  2.2010,  2.3800])

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

Y_UKIDSS_Lya = (Y_UKIDSS/Lya_lambda)-1
J_UKIDSS_Lya = (J_UKIDSS/Lya_lambda)-1
H_UKIDSS_Lya = (H_UKIDSS/Lya_lambda)-1
K_UKIDSS_Lya = (K_UKIDSS/Lya_lambda)-1
    
Y_UKIDSS_CIV = (Y_UKIDSS/CIV_lambda)-1
J_UKIDSS_CIV = (J_UKIDSS/CIV_lambda)-1
H_UKIDSS_CIV = (H_UKIDSS/CIV_lambda)-1
K_UKIDSS_CIV = (K_UKIDSS/CIV_lambda)-1
        
Y_UKIDSS_MgII = (Y_UKIDSS/MgII_lambda)-1
J_UKIDSS_MgII = (J_UKIDSS/MgII_lambda)-1
H_UKIDSS_MgII = (H_UKIDSS/MgII_lambda)-1
K_UKIDSS_MgII = (K_UKIDSS/MgII_lambda)-1

Y_UKIDSS_Halpha = (Y_UKIDSS/Halpha_lambda)-1
J_UKIDSS_Halpha = (J_UKIDSS/Halpha_lambda)-1
H_UKIDSS_Halpha = (H_UKIDSS/Halpha_lambda)-1
K_UKIDSS_Halpha = (K_UKIDSS/Halpha_lambda)-1
          
Y_UKIDSS_Pa_delta = (Y_UKIDSS/Pa_delta_lambda)-1
J_UKIDSS_Pa_delta = (J_UKIDSS/Pa_delta_lambda)-1
H_UKIDSS_Pa_delta = (H_UKIDSS/Pa_delta_lambda)-1
K_UKIDSS_Pa_delta = (K_UKIDSS/Pa_delta_lambda)-1
      
Y_UKIDSS_He_one = (Y_UKIDSS/He_one_lambda)-1
J_UKIDSS_He_one = (J_UKIDSS/He_one_lambda)-1
H_UKIDSS_He_one = (H_UKIDSS/He_one_lambda)-1
K_UKIDSS_He_one = (K_UKIDSS/He_one_lambda)-1
    

print('\n')
print('Ly-alpha enters UKIDSS Y at redshift' , "%6.3f" % Y_UKIDSS_Lya[0], 'and exits at ', "%6.3f" % Y_UKIDSS_Lya[-1])
print('Ly-alpha enters UKIDSS J at redshift' , "%6.3f" % J_UKIDSS_Lya[0], 'and exits at ', "%6.3f" % J_UKIDSS_Lya[-1])
print('Ly-alpha enters UKIDSS H at redshift' , "%6.3f" % H_UKIDSS_Lya[0], 'and exits at ', "%6.3f" % H_UKIDSS_Lya[-1])
print('Ly-alpha enters UKIDSS K at redshift' , "%6.3f" % K_UKIDSS_Lya[0], 'and exits at ', "%6.3f" % K_UKIDSS_Lya[-1], '\n')

print('C-IV     enters UKIDSS Y at redshift' , "%6.3f" % Y_UKIDSS_CIV[0], 'and exits at ', "%6.3f" % Y_UKIDSS_CIV[-1])
print('C-IV     enters UKIDSS J at redshift' , "%6.3f" % J_UKIDSS_CIV[0], 'and exits at ', "%6.3f" % J_UKIDSS_CIV[-1])
print('C-IV     enters UKIDSS H at redshift' , "%6.3f" % H_UKIDSS_CIV[0], 'and exits at ', "%6.3f" % H_UKIDSS_CIV[-1])
print('C-IV     enters UKIDSS K at redshift' , "%6.3f" % K_UKIDSS_CIV[0], 'and exits at ', "%6.3f" % K_UKIDSS_CIV[-1], '\n')

print('Mg-II    enters UKIDSS Y at redshift' , "%6.3f" % Y_UKIDSS_MgII[0], 'and exits at ', "%6.3f" % Y_UKIDSS_MgII[-1])
print('Mg-II    enters UKIDSS J at redshift' , "%6.3f" % J_UKIDSS_MgII[0], 'and exits at ', "%6.3f" % J_UKIDSS_MgII[-1])
print('Mg-II    enters UKIDSS H at redshift' , "%6.3f" % H_UKIDSS_MgII[0], 'and exits at ', "%6.3f" % H_UKIDSS_MgII[-1])
print('Mg-II    enters UKIDSS K at redshift' , "%6.3f" % K_UKIDSS_MgII[0], 'and exits at ', "%6.3f" % K_UKIDSS_MgII[-1], '\n')

print('H-alpha  enters UKIDSS Y at redshift' , "%6.3f" % Y_UKIDSS_Halpha[0], 'and exits at ', "%6.3f" % Y_UKIDSS_Halpha[-1])
print('H-alpha  enters UKIDSS J at redshift' , "%6.3f" % J_UKIDSS_Halpha[0], 'and exits at ', "%6.3f" % J_UKIDSS_Halpha[-1])
print('H-alpha  enters UKIDSS H at redshift' , "%6.3f" % H_UKIDSS_Halpha[0], 'and exits at ', "%6.3f" % H_UKIDSS_Halpha[-1])
print('H-alpha  enters UKIDSS K at redshift' , "%6.3f" % K_UKIDSS_Halpha[0], 'and exits at ', "%6.3f" % K_UKIDSS_Halpha[-1], '\n')

print('Pa-delta enters UKIDSS Y at redshift' , "%6.3f" % Y_UKIDSS_Pa_delta[0], 'and exits at ', "%6.3f" % Y_UKIDSS_Pa_delta[-1])
print('Pa-delta enters UKIDSS J at redshift' , "%6.3f" % J_UKIDSS_Pa_delta[0], 'and exits at ', "%6.3f" % J_UKIDSS_Pa_delta[-1])
print('Pa-delta enters UKIDSS H at redshift' , "%6.3f" % H_UKIDSS_Pa_delta[0], 'and exits at ', "%6.3f" % H_UKIDSS_Pa_delta[-1])
print('Pa-delta enters UKIDSS K at redshift' , "%6.3f" % K_UKIDSS_Pa_delta[0], 'and exits at ', "%6.3f" % K_UKIDSS_Pa_delta[-1], '\n')

print('He I     enters UKIDSS Y at redshift' , "%6.3f" % Y_UKIDSS_He_one[0], 'and exits at ', "%6.3f" % Y_UKIDSS_He_one[-1])
print('He I     enters UKIDSS J at redshift' , "%6.3f" % J_UKIDSS_He_one[0], 'and exits at ', "%6.3f" % J_UKIDSS_He_one[-1])
print('He I     enters UKIDSS H at redshift' , "%6.3f" % H_UKIDSS_He_one[0], 'and exits at ', "%6.3f" % H_UKIDSS_He_one[-1])
print('He I     enters UKIDSS K at redshift' , "%6.3f" % K_UKIDSS_He_one[0], 'and exits at ', "%6.3f" % K_UKIDSS_He_one[-1], '\n')

