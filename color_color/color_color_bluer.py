'''
Aim:: To read in Table 1 from Best et al. (2018, ApJS, 234, 1)
      http://adsabs.harvard.edu/abs/2018ApJS..234....1B
      Photometry and Proper Motions of M, L, and T Dwarfs from the Pan-STARRS1 3π Survey

Good/useful links/URLs::      
    http://docs.astropy.org/en/v0.2.1/_generated/astropy.io.ascii.cds.Cds.html
    http://vizier.u-strasbg.fr/doc/catstd.htx
    https://github.com/astropy/astropy/blob/master/docs/io/unified.rst
    http://cds.u-strasbg.fr/doc/catstd.htx
    https://mail.scipy.org/pipermail/astropy/2016-May/004207.html
    http://docs.astropy.org/en/stable/table/
    http://jakevdp.github.io/astropy/api/astropy.io.ascii.Cds.html
    http://docs.astropy.org/en/v0.2.1/_generated/astropy.io.ascii.cds.Cds.html
'''

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from matplotlib.ticker import AutoMinorLocator

from astropy.table import Table
from astropy.io import ascii

path   = '/cos_pc19a_npr/data/MLandT_dwarfs/'
infile = 'Best_2018_Table1_full.txt'
readin = path+infile
table = ascii.read(readin)

## grizy from PS1
gmag = table['PS1gmag'] 
rmag = table['PS1rmag']
imag = table['PS1imag']
zmag = table['PS1zmag']
ymag = table['PS1ymag']
## 2MASS
J_tm  = table['Jmag']
H_tm  = table['Hmag']
Ks_tm = table['Ksmag']
W1mag = table['W1mag']
W2mag = table['W2mag']
W3mag = table['W3mag']
W4mag = table['W4mag']

SpT_optn = table['SpT-opt-n']
SpT_nirn = table['SpT-nir-n']
#SpT_opt = table['SpT-opt-n']

## Just figuring out how many stars of a given Type
no_types = int((table['SpT-opt-n'].max() - table['SpT-opt-n'].min()))
for ii in range(no_types):
    w =table[np.where(table['SpT-opt-n'] == ii) ]
    if (len(w)) > 0:
        print(ii, w['SpT-opt'][0], len(w))

#path = '/cos_pc19a_npr/data/highest_z_QSOs/'
path = '/cos_pc19a_npr/data/highest_z_QSOs/THE_TABLES/v0pnt97/'
filename  ='THE_TABLE_v0pnt97x_PS1_ULAS_VHS_photom_v2.dat'
table=path+filename
VHzQ = ascii.read(table)

VHzQ = VHzQ[np.where( (VHzQ['iMag']  - VHzQ['zMag'] != 0.0))]

redshift = VHzQ['redshift']
g_PS1 = VHzQ['gMag']
r_PS1 = VHzQ['rMag']
i_PS1 = VHzQ['iMag']
z_PS1 = VHzQ['zMag']
y_PS1 = VHzQ['yMag']
Ymag  = VHzQ['Yapermag']
Jmag  = VHzQ['Jmag']
Hmag  = VHzQ['Hmag']
Kmag  = VHzQ['Kmag']
W1mag = VHzQ['W1mag']
W2mag = VHzQ['W2mag']
W3mag = VHzQ['W3mag']
W4mag = VHzQ['W4mag']


##        
##  Making the plot(s)
##
plt.rcParams.update({'font.size': 14})
#matplotlib.rc('text', usetex=True)
fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(nrows=3, ncols=2, figsize=(14, 16),
                                                         dpi=80, facecolor='w', edgecolor='k')

#fig.tight_layout() # Or equivalently,  "plt.tight_layout()"

#minorLocator = AutoMinorLocator()

labelsize       = 24
tickwidth       = 2.0
majorticklength = 12
minorticklength = 6
ticklabelsize   = labelsize

ls       = 'solid'
lw       = 1.0
ms_clrsize  = ((redshift-3.9)**5.5)
ms_large = 360.
ms       = 120.
ms_small =  14.
cmap = plt.cm.rainbow

left   = 0.12   # the left side of the subplots of the figure
right  = 0.95   # the right side of the subplots of the figure
bottom = 0.06   # the bottom of the subplots of the figure
top    = 0.95   # the top of the subplots of the figure
wspace = 0.35   # the amount of width reserved for space between subplots,
                # expressed as a fraction of the average axis width
hspace = 0.35   # the amount of height reserved for space between subplots,
                # expressed as a fraction of the average axis height
plt.subplots_adjust(left=left, bottom=bottom, right=right, top=top,
               wspace=wspace, hspace=hspace)
 
##
## Figure 7 of Best et al. (2018, ApJS, 234, 1)
##
##  1.
##   (r - i)   vs.  (z - y)
##
xmin=-0.4; xmax=3.8
ymin=-0.3; ymax=1.3
ax1.axis([xmin, xmax, ymin, ymax])
## Quasars
cmap = plt.cm.autumn_r
ax1.scatter((r_PS1 - i_PS1), (z_PS1 - y_PS1), c=redshift, cmap=cmap, s=ms, alpha=1.0)
## Spectral Type
cmap = plt.cm.rainbow
ax1.scatter((rmag - imag),   (zmag - ymag), c=(SpT_optn**5.), cmap=cmap, alpha=0.60, s=ms_small)

major_ticks = np.arange(0, 4, 1)
ax1.set_xticks(major_ticks)
minorLocator = MultipleLocator(.1)
ax1.xaxis.set_minor_locator(minorLocator)
minorLocator = MultipleLocator(.1)
ax1.yaxis.set_minor_locator(minorLocator)

ax1.tick_params(axis='both', which='major', labelsize=ticklabelsize, top=True, right=True, direction='in', length=majorticklength, width=tickwidth)
ax1.tick_params(axis='both', which='minor', top=True, right=True, direction='in', width=tickwidth)
ax1.set_xlabel(r" r - i ", fontsize=labelsize)
ax1.set_ylabel(r" z - y ", fontsize=labelsize)


##  2.
##   (i - z)   vs.  (z - y)
##
xmin=-0.8; xmax=3.8
ymin=-0.6; ymax=1.6
ax2.axis([xmin, xmax, ymin, ymax])
## Quasars
cmap = plt.cm.autumn_r
ax2.scatter((i_PS1 - z_PS1), (z_PS1 - y_PS1), c=redshift, cmap=cmap, s=ms, alpha=1.0)
## Spectral Type
cmap = plt.cm.rainbow
ax2.scatter((imag - zmag),   (zmag - ymag), c=(SpT_optn**5.), cmap=cmap, alpha=0.60, s=ms_small)

major_ticks = np.arange(0, 4, 1)
ax2.set_xticks(major_ticks)
minorLocator = MultipleLocator(.1)
ax2.xaxis.set_minor_locator(minorLocator)
minorLocator = MultipleLocator(.1)
ax2.yaxis.set_minor_locator(minorLocator)
ax2.tick_params(axis='both', which='major', labelsize=ticklabelsize, top=True, right=True, direction='in', length=majorticklength, width=tickwidth)
ax2.tick_params(axis='both', which='minor', top=True, right=True, direction='in', width=tickwidth)
ax2.set_xlabel(r" i - z ", fontsize=labelsize)
ax2.set_ylabel(r" z - y ", fontsize=labelsize)


##  3.
##   (i - z)   vs.  (z - J)
##
xmin=-0.8; xmax=3.8
ymin=-0.2; ymax=3.8
ax3.axis([xmin, xmax, ymin, ymax])
## Quasars
cmap = plt.cm.autumn_r
ax3.scatter((i_PS1 - z_PS1), (z_PS1 - Jmag), c=redshift, cmap=cmap, s=ms, alpha=1.0)
## Spectral Type
cmap = plt.cm.rainbow
ax3.scatter((imag - zmag),   (zmag - J_tm), c=(SpT_optn**5.), cmap=cmap, alpha=0.60, s=ms_small)

major_ticks = np.arange(0, 4, 1)
ax3.set_xticks(major_ticks)
minorLocator = MultipleLocator(.1)
ax3.xaxis.set_minor_locator(minorLocator)
minorLocator = MultipleLocator(.1)
ax3.yaxis.set_minor_locator(minorLocator)
ax3.tick_params(axis='both', which='major', labelsize=ticklabelsize, top=True, right=True, direction='in', length=majorticklength, width=tickwidth)
ax3.tick_params(axis='both', which='minor', top=True, right=True, direction='in', width=tickwidth)
ax3.set_xlabel(r" i - z ", fontsize=labelsize)
ax3.set_ylabel(r" z - J ", fontsize=labelsize)


##  4.
##   (i - y)   vs.  (y - J)
##
xmin=-0.4; xmax=3.8
ymin=-0.4; ymax=2.8
ax4.axis([xmin, xmax, ymin, ymax])
## Quasars
cmap = plt.cm.autumn_r
ax4.scatter((i_PS1 - y_PS1), (y_PS1 - Jmag), c=redshift, cmap=cmap, s=ms, alpha=1.0)
## Spectral Type
cmap = plt.cm.rainbow
ax4.scatter((imag - ymag),   (ymag - J_tm), c=(SpT_optn**5.), cmap=cmap, alpha=0.60, s=ms_small)

major_ticks = np.arange(0, 4, 1)
ax4.set_xticks(major_ticks)
minorLocator = MultipleLocator(.1)
ax4.xaxis.set_minor_locator(minorLocator)
minorLocator = MultipleLocator(.1)
ax4.yaxis.set_minor_locator(minorLocator)
ax4.tick_params(axis='both', which='major', labelsize=ticklabelsize, top=True, right=True, direction='in', length=majorticklength, width=tickwidth)
ax4.tick_params(axis='both', which='minor', top=True, right=True, direction='in', width=tickwidth)
ax4.set_xlabel(r" i - y ", fontsize=labelsize)
ax4.set_ylabel(r" y - J ", fontsize=labelsize)


##  5.
##   (i - J)   vs.  (J - K)
##
xmin=-0.2; xmax=7.8
ymin=-0.2; ymax=2.8
ax5.axis([xmin, xmax, ymin, ymax])
## Quasars
cmap = plt.cm.autumn_r
ax5.scatter((i_PS1 - Jmag), (Jmag - Kmag), c=redshift, cmap=cmap, s=ms, alpha=1.0)
## Spectral Type
cmap = plt.cm.rainbow
ax5.scatter((imag - J_tm),   (J_tm - Ks_tm), c=(SpT_optn**5.), cmap=cmap, alpha=0.60, s=ms_small)

minorLocator = MultipleLocator(.2)
ax5.xaxis.set_minor_locator(minorLocator)
minorLocator = MultipleLocator(.1)
ax5.yaxis.set_minor_locator(minorLocator)
ax5.tick_params(axis='both', which='major', labelsize=ticklabelsize, top=True, right=True, direction='in', length=majorticklength, width=tickwidth)
ax5.tick_params(axis='both', which='minor', top=True, right=True, direction='in', width=tickwidth)
ax5.set_xlabel(r" i - J ", fontsize=labelsize)
ax5.set_ylabel(r" J - K ", fontsize=labelsize)


##  6.
##   (z - y)   vs.  (y - J)
##
xmin=-0.8; xmax=2.2
ymin=-0.2; ymax=3.2
ax6.axis([xmin, xmax, ymin, ymax])
## Quasars
cmap = plt.cm.autumn_r
ax6.scatter((z_PS1 - y_PS1), (y_PS1 - Jmag), c=redshift, cmap=cmap, s=ms, alpha=1.0)
## Spectral Type
cmap = plt.cm.rainbow
ax6.scatter((zmag - ymag),   (ymag - J_tm), c=(SpT_optn**5.), cmap=cmap, alpha=0.60, s=ms_small)

minorLocator = MultipleLocator(.1)
ax6.xaxis.set_minor_locator(minorLocator)
minorLocator = MultipleLocator(.1)
ax6.yaxis.set_minor_locator(minorLocator)
ax6.tick_params(axis='both', which='major', labelsize=ticklabelsize, top=True, right=True, direction='in', length=majorticklength, width=tickwidth)
ax6.tick_params(axis='both', which='minor', top=True, right=True, direction='in', width=tickwidth)
ax6.set_xlabel(r" z - y ", fontsize=labelsize)
ax6.set_ylabel(r" y - J ", fontsize=labelsize)



plt.savefig('color_color_bluer_temp.png', format='png')
plt.savefig('color_color_bluer_temp.pdf', format='pdf')
plt.close(fig)

#plt.show()

