'''
A simple little bit of code to figure out which survey the VHzQs came
from.  I haven't gone "fully, fully" here's the plug in .tex, but
could easily see that happening and would be happy for it!!

v1.00    Wed Dec  5 19:14:34 GMT 2018
'''

import numpy as np

from astropy.io    import fits
from astropy.io    import ascii
from astropy.table import Table

##
##  V H z Q    data
##
path     = '../data/'
filename = 'LIST_OF_VHzQs.dat'
table    = path+filename

VHzQ_list = ascii.read(table)

## just a little bit of info 
print('type(VHzQ_list)', type(VHzQ_list))

## the column names
VHzQ_list.colnames

## Column 'na' has the original survey designations
len(np.unique(VHzQ_list['na']))
#type(np.unique(VHzQ_list['na']))
np.unique(VHzQ_list['na'])

## Nice, cute way to pick out the survey and the number of
## objects from that survey -- thanks @nudomarinero !!
survey, counts = np.unique(VHzQ_list["na"], return_counts=True)

percent_count = 0.00
## Loop through the number of entries the variable 'survey' has
print()
for x in range(len(survey)):
    print('{:7}  &  {:4d}  &  ({:5.2f})'.format(survey[x], counts[x], (counts[x]/463.*100) )) 
    percent_count = percent_count + (counts[x]/463.*100)
    
print()
print('...for a total of ', len(VHzQ_list), ' VHzQs (at ', percent_count,'%)')
print()
