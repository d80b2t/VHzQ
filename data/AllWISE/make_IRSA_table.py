'''
A simple little bit of code to make the IPAC table for uploading to
the IRSA WISE website.

IPAC Table Validator:: 
https://irsa.ipac.caltech.edu/applications/TblValidator/

v1.00    Fri Dec 14 16:59:29 GMT 2018
'''

import numpy as np
import pandas as pd

from astropy.io    import fits
from astropy.io    import ascii
from astropy.table import Table

##
##  V H z Q    data
##
path     = '../'
filename = 'LIST_OF_VHzQs.dat'
table    = path+filename

VHzQ_list = ascii.read(table)

## Just a little bit of info 
print('type(VHzQ_list)', type(VHzQ_list))

VHzQ_list.colnames

data = [VHzQ_list['ra'], VHzQ_list['dec']]
ascii.write(data, 'VHzQs463_4IPAC_temp.tbl', format='ipac')
