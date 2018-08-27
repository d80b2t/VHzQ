from astropy.io import fits
from astropy.io import ascii
from astropy.table import Table

#import matplotlib
import matplotlib as mpl

import matplotlib.pyplot as plt
import numpy as np
import math

from matplotlib import colors as mcolors
from matplotlib import gridspec

from mpl_toolkits.axes_grid1.axes_divider  import make_axes_locatable
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, zoomed_inset_axes
from mpl_toolkits.axes_grid1.colorbar      import colorbar

## READ-IN THE DATA FILE(S)
path = '/cos_pc19a_npr/data/highest_z_QSOs/'
m1  = ascii.read(path+'THE_TABLE_v0pnt971.dat', delimiter=r'\s', guess=False)
m2  = ascii.read(path+'THE_TABLE_v0pnt97_WISE_coverage.dat', delimiter=r'\s', guess=False)

for ii in range(len(m1)):
    diff_w1 = (m1['w1mag'][ii] - m2['w1mpro'][ii])
    diff_w2 = (m1['w2mag'][ii] - m2['w2mpro'][ii])
    diff_w3 = (m1['w3mag'][ii] - m2['w3mpro'][ii])
    diff_w4 = (m1['w4mag'][ii] - m2['w4mpro'][ii])

    print(diff_w1, diff_w2, diff_w3, diff_w4)    
    if  ((diff_w4 < 800.0) and (diff_w4 <0.0)):
        print(ii, m1['na'][ii], m1['desig'][ii], diff_w1)
        print(ii, m1['ra'][ii], m1['dec'][ii], m1['w1mag'][ii], m1['w1snr'][ii],  m1['w2mag'][ii],  m1['w2snr'][ii] )
        print(ii, m2['ra'][ii], m2['dec'][ii], m2['w1mpro'][ii], m2['w1snr'][ii], m2['w2mpro'][ii], m2['w2snr'][ii])
        print()
#    if  ((diff > 0.0) or (diff >0.0)): print(ii,diff)
