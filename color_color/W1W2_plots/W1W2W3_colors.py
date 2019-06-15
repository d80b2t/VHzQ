'''
Just some simple W1/2/3 VHzQ numbers
'''

import numpy as np
from astropy.io    import ascii

## Read-in the data
path      = '/cos_pc19a_npr/programs/quasars/highest_z/data/'
filename  = 'VHzQs_ZYJHK_WISE.dat'
table     = path+filename
VHzQ_full = ascii.read(table)


## Vega to AB conversion
#VHzQ_full['unW1mag'] = VHzQ_full['unW1mag'] - 0.004 + 2.673
#VHzQ_full['unW2mag'] = VHzQ_full['unW2mag'] - 0.032 + 3.313
#VHzQ_full['w3mpro']  = VHzQ_full['w3mpro'] + 5.148
#VHzQ_full['w4mpro']  = VHzQ_full['w4mpro'] + 6.66



## Selections...
W3_goodSNR   = VHzQ_full[np.where( VHzQ_full['w3snr']   > 3.0)]
W1andW2      = VHzQ_full[np.where((VHzQ_full['unW1mag'] > 0.0)  &  (VHzQ_full['unW2mag'] >0.0)) ]


bluest_W1andW2  = W1andW2[np.where((W1andW2['unW1mag']-W1andW2['unW2mag'])  ==
                                   (W1andW2['unW1mag']-W1andW2['unW2mag']).min())]

reddest_W1andW2 = W1andW2[np.where((W1andW2['unW1mag']-W1andW2['unW2mag'])  ==
                                   (W1andW2['unW1mag']-W1andW2['unW2mag']).max())]

print()
print('Number of objects with good (>0.0) unW1mag and unW2mag: ', len(W1andW2))
print('    of which ',  bluest_W1andW2['na'][0],  bluest_W1andW2['desig'][0], '    is the bluest with (W1-W2) =  ', bluest_W1andW2['unW1mag'][0]-bluest_W1andW2['unW2mag'][0] )
print('    of which ', reddest_W1andW2['na'][0], reddest_W1andW2['desig'][0], ' is the reddest with (W1-W2) =  ',   reddest_W1andW2['unW1mag'][0]-reddest_W1andW2['unW2mag'][0] )
print()


### GOOD 
bluest_W1andW3  = W3_goodSNR[np.where((W3_goodSNR['unW1mag']-W3_goodSNR['w3mpro'])  ==
                                      (W3_goodSNR['unW1mag']-W3_goodSNR['w3mpro']).min())]

bluest_W2andW3 = W3_goodSNR[np.where((W3_goodSNR['unW2mag']-W3_goodSNR['w3mpro'])  ==
                                     (W3_goodSNR['unW2mag']-W3_goodSNR['w3mpro']).min())]

###  Argh!!!!!
###  TAKE GREAT CARE!!
###    PSO J075.9356-07.5061
### 
reddest_W1andW3 = W3_goodSNR[np.where((W3_goodSNR['unW1mag']-W3_goodSNR['w3mpro'])  ==
                                      (W3_goodSNR['unW1mag']-W3_goodSNR['w3mpro']).max())]
reddest_W2andW3 = W3_goodSNR[np.where((W3_goodSNR['unW2mag']-W3_goodSNR['w3mpro'])  ==
                                      (W3_goodSNR['unW2mag']-W3_goodSNR['w3mpro']).max())]

print()
print('Number of objects with good (>3.0) W3 SNR : ', len(W3_goodSNR))
print('    of which ',  bluest_W1andW3['na'][0],  bluest_W1andW3['desig'][0], '    is the bluest with (W1-W3) =  ', bluest_W1andW3['unW1mag'][0]  - bluest_W1andW3['w3mpro'][0] )
print('    of which ', reddest_W1andW3['na'][0], reddest_W1andW3['desig'][0], ' is the reddest with (W1-W3) =  ',   reddest_W1andW3['unW1mag'][0] - reddest_W1andW3['w3mpro'][0] )
print('    of which ',  bluest_W2andW3['na'][0],  bluest_W2andW3['desig'][0], '    is the bluest with (W2-W3) =  ', bluest_W2andW3['unW2mag'][0]  - bluest_W1andW3['w3mpro'][0] )
print('    of which ', reddest_W2andW3['na'][0], reddest_W2andW3['desig'][0], ' is the reddest with (W2-W3) =  ',   reddest_W2andW3['unW2mag'][0] - reddest_W1andW3['w3mpro'][0] )

print()

## bluest (W1-W3) and (W2-W3)::    SDSS J0100+2802 15.0542635 28.040532     6.33
## reddest (W1-W3) and (W2-W3):: PSO J075.9356-07.5061 
