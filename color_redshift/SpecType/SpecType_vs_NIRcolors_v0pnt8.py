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
sum_ii=0
## Just figuring out how many stars of a given Type
no_types = int((table['SpT-opt-n'].max() - table['SpT-opt-n'].min()))
for ii in range(no_types):
    w  = table[np.where(table['SpT-opt-n'] == ii) ]
    ww = table[np.where(table['SpT-nir-n'] == ii) ]
    sum_ii = sum_ii + len(w)
    print(ii, len(w), len(ww))
    if (len(w)) > 0:
        print('opt', ii, sum_ii, w['SpT-opt'][0], len(w))
    if (len(ww)) > 0:
        print('nir', ii, sum_ii, ww['SpT-nir'][0], len(ww))
        

path = '/cos_pc19a_npr/data/highest_z_QSOs/'
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
W1    = VHzQ['W1mag']
W2    = VHzQ['W2mag']
W3    = VHzQ['W3mag']
W4    = VHzQ['W4mag']


##        
##  Making the plot(s)
##
plt.rcParams.update({'font.size': 14})
#matplotlib.rc('text', usetex=True)
fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(nrows=3, ncols=2, figsize=(12, 16), dpi=80, facecolor='w', edgecolor='k')

minorLocator = AutoMinorLocator()

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

xmin_SpecT=-2; xmax_SpecT=32
xmin_redshift = 4.4
xmax_redshift = 7.6
## Figure 5 of Best et al. (2018, ApJS, 234, 1)

##   i  -  J
ymin=-0.6; ymax=7.8
## Redshift
cmap = plt.cm.autumn_r
ax1.axis([xmin_redshift, xmax_redshift, ymin, ymax])
ax1.scatter(redshift, (i_PS1 - Jmag), c=redshift, cmap=cmap, s=ms, alpha=1.0)
minorLocator = MultipleLocator(.1)
ax1.xaxis.set_minor_locator(minorLocator)
minorLocator = AutoMinorLocator()
ax1.yaxis.set_minor_locator(minorLocator)
ax1.tick_params(axis='both', which='major', labelsize=ticklabelsize, top=True,
                right=True, direction='in', length=majorticklength, width=tickwidth)
ax1.tick_params(axis='both', which='minor',  right=True, direction='in', width=tickwidth)
ax1.set_ylabel(r" i - J ", fontsize=labelsize)
## Spectral Type
x1 = [0, 5, 10, 15, 20, 25, 30]
squad = ['M0', 'M5', 'L0', 'L5', 'T0', 'T5', 'Y0']
cmap = plt.cm.rainbow
ax7 = ax1.twiny()
ax7.scatter(SpT_optn, (imag - J_tm), c=(SpT_optn**5.), cmap=cmap, alpha=0.60, s=ms_small)
ax7.scatter(SpT_nirn, (imag - J_tm), c=(SpT_optn**5.), cmap=cmap, alpha=0.60, s=ms_small)
ax7.set_xlim(xmin_SpecT, xmax_SpecT)
ax7.set_xticks(x1)
ax7.set_xticklabels(squad, fontsize=(labelsize*.9))
ax7.set_xlabel(r"Spectral Type", fontsize=labelsize)
ax7.xaxis.set_label_coords(0.50, 1.15)
minorLocator = MultipleLocator(1)
ax7.xaxis.set_minor_locator(minorLocator)


##   z  -  y
ymin=-0.7; ymax=2.3
cmap = plt.cm.autumn_r
## Redshift
ax2.axis([xmin_redshift, xmax_redshift, ymin, ymax])
ax2.set_xlim(xmin_redshift, xmax_redshift)
ax2.scatter(redshift, (z_PS1 - y_PS1), c=redshift, cmap=cmap, s=ms, alpha=1.0)
minorLocator = MultipleLocator(.1)
ax2.xaxis.set_minor_locator(minorLocator)
minorLocator = AutoMinorLocator()
ax2.yaxis.set_minor_locator(minorLocator)
ax2.tick_params(axis='both', which='major', labelsize=ticklabelsize, top=True, right=True, direction='in', length=majorticklength, width=tickwidth)
ax2.tick_params(axis='both', which='minor', right=True, direction='in', width=tickwidth)
ax2.set_ylabel(r" z - y ", fontsize=labelsize)
## Spectral Type
cmap = plt.cm.rainbow
ax8 = ax2.twiny()
ax8.set_xlim(xmin_SpecT, xmax_SpecT)
ax8.scatter(SpT_optn, (zmag - ymag), c=(SpT_optn**5.), cmap=cmap, alpha=0.60, s=ms_small)
ax8.scatter(SpT_nirn, (zmag - ymag), c=(SpT_optn**5.), cmap=cmap, alpha=0.60, s=ms_small)
ax8.set_xticks(x1)
ax8.set_xticklabels(squad, fontsize=(labelsize*.9))
ax8.set_xlabel(r"Spectral Type", fontsize=labelsize)
ax8.xaxis.set_label_coords(0.50, 1.15)
minorLocator = MultipleLocator(1)
ax8.xaxis.set_minor_locator(minorLocator)


##   z - J
ymin=-0.6; ymax=4.8
## Redshift
cmap = plt.cm.autumn_r
ax3.axis([xmin_redshift, xmax_redshift, ymin, ymax])
ax3.scatter(redshift, (z_PS1 - Jmag), c=redshift, cmap=cmap, s=ms, alpha=1.0)
minorLocator = MultipleLocator(.1)
ax3.xaxis.set_minor_locator(minorLocator)
minorLocator = AutoMinorLocator()
ax3.yaxis.set_minor_locator(minorLocator)
ax3.tick_params(axis='both', which='major', labelsize=ticklabelsize, right=True, direction='in', length=majorticklength, width=tickwidth)
ax3.tick_params(axis='both', which='minor', right=True, direction='in', width=tickwidth)
ax3.set_ylabel(r" z - J ", fontsize=labelsize)
## Spectral Type
cmap = plt.cm.rainbow
ax9 = ax3.twiny()
ax9.set_xlim(xmin_SpecT, xmax_SpecT)
ax9.scatter(SpT_optn, (zmag - J_tm), c=(SpT_optn**5.), cmap=cmap, alpha=0.60, s=ms_small)
ax9.scatter(SpT_nirn, (zmag - J_tm), c=(SpT_optn**5.), cmap=cmap, alpha=0.60, s=ms_small)
ax9.tick_params(axis='both', which='major', labeltop=False,
                labelsize=ticklabelsize, top=True, right=True, direction='in', length=majorticklength, width=tickwidth)
minorLocator = MultipleLocator(1)
ax9.xaxis.set_minor_locator(minorLocator)


##   y - J
ymin=-0.4; ymax=3.2
## Redshift
cmap = plt.cm.autumn_r
ax4.axis([xmin_redshift, xmax_redshift, ymin, ymax])
ax4.scatter(redshift, (y_PS1 - Jmag), c=redshift, cmap=cmap, s=ms, alpha=1.0)
minorLocator = MultipleLocator(.1)
ax4.xaxis.set_minor_locator(minorLocator)
minorLocator = AutoMinorLocator()
ax4.yaxis.set_minor_locator(minorLocator)
ax4.tick_params(axis='both', which='major', labelsize=ticklabelsize, top=True, right=True, direction='in', length=majorticklength, width=tickwidth)
ax4.tick_params(axis='both', which='minor', top=True, right=True, direction='in', width=tickwidth)
ax4.set_ylabel(r" y - J ", fontsize=labelsize)
## Spectral Type
cmap = plt.cm.rainbow
ax10 = ax4.twiny()
ax10.set_xlim(xmin_SpecT, xmax_SpecT)
ax10.scatter(SpT_optn, (ymag - J_tm), c=(SpT_optn**5.), cmap=cmap, alpha=0.60, s=ms_small)
ax10.scatter(SpT_nirn, (ymag - J_tm), c=(SpT_optn**5.), cmap=cmap, alpha=0.60, s=ms_small)
ax10.tick_params(axis='both', which='major',  labeltop=False, 
                 labelsize=ticklabelsize, top=True, right=True, direction='in', length=majorticklength, width=tickwidth)
minorLocator = MultipleLocator(1)
ax10.xaxis.set_minor_locator(minorLocator)


##   J  -  K
cmap = plt.cm.autumn_r
ymin=-1.3; ymax=2.6
## Redshift
ax5.axis([xmin_redshift, xmax_redshift, ymin, ymax])
ax5.scatter(redshift, (Jmag - Kmag), c=redshift, cmap=cmap, s=ms, alpha=1.0)
minorLocator = MultipleLocator(.1)
ax5.xaxis.set_minor_locator(minorLocator)
minorLocator = AutoMinorLocator()
ax5.yaxis.set_minor_locator(minorLocator)
ax5.tick_params(axis='both', which='major', labelsize=ticklabelsize, top=True, right=True, direction='in', length=majorticklength, width=tickwidth)
ax5.tick_params(axis='both', which='minor', right=True, direction='in', width=tickwidth)
ax5.set_xlabel(r"redshift", fontsize=labelsize)
ax5.set_ylabel(r" J - K ", fontsize=labelsize)
## Spectral Type
cmap = plt.cm.rainbow
ax11 = ax5.twiny()
ax11.set_xlim(xmin_SpecT, xmax_SpecT)
ax11.scatter(SpT_optn, (J_tm - Ks_tm), c=(SpT_optn**5.), cmap=cmap, alpha=0.60, s=ms_small)
ax11.scatter(SpT_nirn, (J_tm - Ks_tm), c=(SpT_optn**5.), cmap=cmap, alpha=0.60, s=ms_small)
ax11.tick_params(axis='both', which='major',  labeltop=False,
                 labelsize=ticklabelsize, top=True, right=True, direction='in', length=majorticklength, width=tickwidth)
minorLocator = MultipleLocator(1)
ax11.xaxis.set_minor_locator(minorLocator)


##   y - W1
ymin=1.2; ymax=6.8
## Redshift
cmap = plt.cm.autumn_r
ax6.axis([xmin_redshift, xmax_redshift, ymin, ymax])
ax6.scatter(redshift, (y_PS1 - W1), c=redshift, cmap=cmap, s=ms, alpha=1.0)
minorLocator = MultipleLocator(.1)
ax6.xaxis.set_minor_locator(minorLocator)
minorLocator = AutoMinorLocator()
ax6.yaxis.set_minor_locator(minorLocator)
ax6.tick_params(axis='both', which='major', labelsize=ticklabelsize, top=True, right=True, direction='in', length=majorticklength, width=tickwidth)
ax6.tick_params(axis='both', which='minor', right=True, direction='in',  width=tickwidth)
ax6.set_xlabel(r"redshift", fontsize=labelsize)
ax6.set_ylabel(r" y - W1 ", fontsize=labelsize)
## Spectral Type
cmap = plt.cm.rainbow
ax12 = ax6.twiny()
ax12.set_xlim(xmin_SpecT, xmax_SpecT)
ax12.scatter(SpT_optn, (ymag - W1mag), c=(SpT_optn**5.), cmap=cmap, alpha=0.60, s=ms_small)
ax12.scatter(SpT_nirn, (ymag - W1mag), c=(SpT_optn**5.), cmap=cmap, alpha=0.60, s=ms_small)
ax12.tick_params(axis='both', which='major',  labeltop=False,
                 labelsize=ticklabelsize, top=True, right=True, direction='in', length=majorticklength, width=tickwidth)
minorLocator = MultipleLocator(1)
ax12.xaxis.set_minor_locator(minorLocator)


plt.savefig('SpecType_vs_NIRcolors_temp.png', format='png')
plt.savefig('SpecType_vs_NIRcolors_temp.pdf', format='pdf')
plt.close(fig)

#plt.show()

