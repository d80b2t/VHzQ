'''
Some pretty basic code that takes in the 'superset' list of
all known VHzQs and then matches it up against the unWISE W1 and W2 lists
and matches.
'''

import numpy as np
from astropy.io import ascii
from astropy.io import fits

## `Super-set' of VHzQs, in that not of these will be unWISE
## detections
VHzQs = ascii.read("LIST_OF_VHzQs.dat") 

## unWISE magnitudes and fluxes
unWISE_W1 = ascii.read("unWISE/unWISE_W1_20181204.dat")
unWISE_W2 = ascii.read("unWISE/unWISE_W2_20181204.dat")

## matching distance in arcsecs
dist = 2.75


f = open('myfile', 'w')

counter               = 0
counter_both_matched  = 0
counter_justW1_match  = 0
counter_justW2_match  = 0
counter_nomatch       = 0

print('abcd count        RA           Dec   redshift  unW1_RA    unW1_Dec     unW2_RA    unW2_Dec     unW1_mag unW1_magerr    unW1_snr     unW2_mag unW2_magerr    unW2_snr idx_w1 idx_w2    sep_w1         sep_w2', file=f)
## Looping over all the VHzQs and writing out R.A.s, Decls, redshifts.
## Then figuring out/matching the VHzQs and unWISE objects
for ii,jj,kk in zip(VHzQs['ra'], VHzQs['dec'], VHzQs['redshift'])  :
    counter = counter + 1

    delta_ra_W1  = ii - unWISE_W1['ra']
    delta_dec_W1 = jj - unWISE_W1['dec']
    delta_w1     = np.sqrt(delta_ra_W1**2 + delta_dec_W1**2)

    delta_ra_W2  = ii - unWISE_W2['ra']
    delta_dec_W2 = jj - unWISE_W2['dec']
    delta_w2     = np.sqrt(delta_ra_W2**2 + delta_dec_W2**2)

    idx_w1       = np.argmin(delta_w1)
    am_w1, bm_w1 = VHzQs[idx_w1], unWISE_W1[idx_w1]
    idx_w2       = np.argmin(delta_w2)
    am_w2, bm_w2 = VHzQs[idx_w2], unWISE_W2[idx_w2]


    ## Now go into the logic
    ## First both W1 AND W2 mathced..
    if (  ((delta_w1.min()*3600.) < dist) and ((delta_w2.min()*3600.) < dist) ):
        counter_both_matched = counter_both_matched + 1 
        print('A,{: 4d}{: 14.8f}{: 14.8f} {:6.2f} {: 12.5f}{: 12.5f}{: 12.5f}{: 12.5f} {: 12.5f}{: 12.5f}{: 12.5f} {: 12.5f}{: 12.5f}{: 12.5f} {: 4d}{: 4d} {: 14.6f} {: 14.6f} '.format(
            counter, ii, jj, kk, 
            bm_w1['ra'],     bm_w1['dec'],       bm_w2['ra'],    bm_w2['dec'],
            bm_w1['w1mpro'], bm_w1['w1sigmpro'], bm_w1['w1snr'],
            bm_w2['w2mpro'], bm_w2['w2sigmpro'], bm_w2['w2snr'], 
            idx_w1, idx_w2, delta_w1.min()*3600., delta_w2.min()*3600.,),  file=f)             

    ## only W1 mathced..
    elif (  ((delta_w1.min()*3600.) < dist) and ((delta_w2.min()*3600.) > dist) ):
        counter_justW1_match = counter_justW1_match + 1
        print('B,{: 4d}{: 14.8f}{: 14.8f} {:6.2f} {: 12.5f}{: 12.5f}{: 12.5f}{: 12.5f} {: 12.5f}{: 12.5f}{: 12.5f}  {:11.5f}{:12.5f}{:12.5f} {: 4d}{: 4d} {: 14.6f} {: 14.6f} '.format(
            counter, ii, jj, kk, 
            bm_w1['ra'],     bm_w1['dec'],       -99.999, -99.999,
            bm_w1['w1mpro'], bm_w1['w1sigmpro'], bm_w1['w1snr'],
            -99.999, -9.99, -99.999, 
            idx_w1, idx_w2, delta_w1.min()*3600., delta_w2.min()*3600.,),  file=f)             

    ## only W2 mathced..
    elif (  ((delta_w1.min()*3600.) > dist) and ((delta_w2.min()*3600.) < dist) ):
        counter_justW2_match = counter_justW2_match + 1
        print('C,{: 4d}{: 14.8f}{: 14.8f} {:6.2f} {: 12.5f}{: 12.5f}{: 12.5f}{: 12.5f}  {: 11.5f}{: 12.5f}{: 12.5f} {: 12.5f}{: 12.5f}{: 12.5f} {: 4d}{: 4d} {: 14.6f}{: 14.6f} '.format(
            counter, ii, jj, kk, 
            -99.999, -99.999, bm_w2['ra'], bm_w2['dec'],
            -99.999, -9.99, -99.999, 
            bm_w2['w2mpro'], bm_w2['w2sigmpro'], bm_w2['w2snr'], 
            idx_w1, idx_w2, delta_w1.min()*3600., delta_w2.min()*3600.,),  file=f)             

    ## neither W1 nor W2 matched    
    else:
        print('D,{: 4d}{: 14.8f}{: 14.8f} {:6.2f} {: 12.5f}{: 12.5f}{: 12.5f}{: 12.5f} {: 12.5f}{: 12.5f}{: 12.5f}  {: 11.5f}{:12.5f}{:12.5f} {: 4d}{: 4d} {: 14.6f} {: 14.6f} '.format(
            counter, ii, jj, kk, 
            -99.999, -99.999, -99.999, -99.999,
            -99.999, -9.99, -99.999,
            -99.999, -9.99, -99.999,
            idx_w1, idx_w2, delta_w1.min()*3600., delta_w2.min()*3600.,),  file=f)             
        counter_nomatch = counter_nomatch +1

        
print()
print('Both    matched :: ',  counter_both_matched)
print('Just W1 matched :: ',  counter_justW1_match)
print('Just W2 matched :: ',  counter_justW2_match)
print('Matched in W1   :: ',  counter_both_matched+counter_justW1_match)
print('Matched in W2   :: ',  counter_both_matched+counter_justW2_match)
print('Neither matched :: ',  counter_nomatch)
print()
print('Total matched   = ', counter_both_matched+counter_justW1_match+counter_justW2_match+counter_nomatch, 'vs. total counters', counter)
f.close() 

