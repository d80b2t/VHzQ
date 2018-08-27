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

'''
import numpy as np

import matplotlib
import matplotlib.pyplot as plt

from astropy.table import Table
from astropy.io import ascii


##http://docs.astropy.org/en/stable/table/
#t = Table(rows=data_rows, names=('a', 'b', 'c'),
#          meta={'name': 'first table'}, dtype=('i4', 'f8', 'S1'))
#
#df = pd.read_table('Best_2018_Table1.txt', sep=r"\s*")


## http://jakevdp.github.io/astropy/api/astropy.io.ascii.Cds.html
## http://docs.astropy.org/en/v0.2.1/_generated/astropy.io.ascii.cds.Cds.html
path   = '/cos_pc19a_npr/data/MLandT_dwarfs/'
infile = 'Best_2018_Table1_full.txt'
readin = path+infile
table = ascii.read(readin)

## grizy from PS1
gmag  = table['PS1gmag'] 
rmag  = table['PS1rmag']
imag  = table['PS1imag']
zmag  = table['PS1zmag']
ymag  = table['PS1ymag']
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

no_types = int((table['SpT-opt-n'].max() - table['SpT-opt-n'].min()))
for ii in range(no_types):
    w =table[np.where(table['SpT-opt-n'] == ii) ]
    if (len(w)) > 0:
        print(ii, w['SpT-opt'][0], len(w))


path = '/cos_pc19a_npr/data/highest_z_QSOs/'
#filename ='THE_TABLE_v0pnt96.dat'
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

        

##  Making the plot(s)
plt.rcParams.update({'font.size': 14})
#matplotlib.rc('text', usetex=True)

## https://matplotlib.org/examples/pylab_examples/subplots_demo.html
## Will scale this up at some point to a full-page 3x2
fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(nrows=3, ncols=2, figsize=(12, 16), num=None, dpi=80, facecolor='w', edgecolor='k')

#table['SpT-opt-n'][0:100]                

labelsize       = 16
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
##
## Figure 5 of Best et al. (2018, ApJS, 234, 1)
##

##   i  -  J
ymin=1.2; ymax=7.8
## Redshift
cmap = plt.cm.autumn_r
ax1.axis([xmin_redshift, xmax_redshift, ymin, ymax])
ax1.scatter(redshift, (i_PS1 - Jmag), c=redshift, cmap=cmap, s=ms, alpha=1.0)
ax1.tick_params(axis='both', which='major', labelsize=ticklabelsize, top='on', right='on', direction='in', length=majorticklength, width=tickwidth)
ax1.tick_params(axis='x', which='minor', labelsize=ticklabelsize, top='on', right='on', direction='in', length=minorticklength, width=tickwidth)
ax1.set_ylabel(r" i - J ", fontsize=labelsize)
## Spectral Type 
cmap = plt.cm.rainbow
ax7 = ax1.twiny()
ax7.scatter(SpT_optn, (imag - J_tm,), c=(SpT_optn**5.), cmap=cmap, alpha=0.60, s=ms_small)
ax7.axis([xmin_SpecT, xmax_SpecT, ymin, ymax])
ax7.set_xlabel(r"Spectral Type", fontsize=labelsize)
ax7.tick_params(axis='both', which='major', labelsize=ticklabelsize, top='on', right='on', direction='in', length=majorticklength, width=tickwidth)


##   z  -  y
ymin=-0.2; ymax=2.2
cmap = plt.cm.autumn_r
ax2.axis([xmin_redshift, xmax_redshift, ymin, ymax])
ax2.set_xlim(xmin_redshift, xmax_redshift)
ax2.scatter(redshift, (z_PS1 - y_PS1), c=redshift, cmap=cmap, s=ms, alpha=1.0)
ax2.tick_params(axis='both', which='major', labelsize=ticklabelsize, top='on', right='on', direction='in', length=majorticklength, width=tickwidth)
ax2.tick_params(axis='both', which='minor', labelsize=ticklabelsize, top='on', right='on', direction='in', length=minorticklength, width=tickwidth)
#ax2.set_xlabel(r"Spectral Type", fontsize=labelsize)
ax2.set_ylabel(r" z - y ", fontsize=labelsize)
## Spectral Type
cmap = plt.cm.rainbow
ax8 = ax2.twiny()
ax8.set_xlim(xmin_SpecT, xmax_SpecT)
ax8.scatter(SpT_optn, (zmag - ymag), c=(SpT_optn**5.), cmap=cmap, alpha=0.60, s=ms_small)
ax8.tick_params(axis='both', which='major', labelsize=ticklabelsize, top='on', right='on', direction='in', length=majorticklength, width=tickwidth)


##   z - J
ymin=0.6; ymax=4.8
## Redshift
cmap = plt.cm.autumn_r
ax3.axis([xmin_redshift, xmax_redshift, ymin, ymax])
ax3.scatter(redshift, (z_PS1 - Jmag), c=redshift, cmap=cmap, s=ms, alpha=1.0)
ax3.tick_params(axis='both', which='major', labelsize=ticklabelsize, top='on', right='on', direction='in', length=majorticklength, width=tickwidth)
ax3.tick_params(axis='both', which='minor', labelsize=ticklabelsize, top='on', right='on', direction='in', length=minorticklength, width=tickwidth)
ax3.set_ylabel(r" z - J ", fontsize=labelsize)
## Spectral Type
cmap = plt.cm.rainbow
ax9 = ax3.twiny()
ax9.set_xlim(xmin_SpecT, xmax_SpecT)
ax9.scatter(SpT_optn, (zmag - J_tm), c=(SpT_optn**5.), cmap=cmap, alpha=0.60, s=ms_small)
ax9.tick_params(axis='both', which='major', labelsize=ticklabelsize, top='on', right='on', direction='in', length=majorticklength, width=tickwidth)


##   y - J
ymin=0.4; ymax=3.2
## Redshift
cmap = plt.cm.autumn_r
ax4.axis([xmin_redshift, xmax_redshift, ymin, ymax])
ax4.scatter(redshift, (y_PS1 - Jmag), c=redshift, cmap=cmap, s=ms, alpha=1.0)
ax4.tick_params(axis='both', which='major', labelsize=ticklabelsize, top='on', right='on', direction='in', length=majorticklength, width=tickwidth)
ax4.tick_params(axis='both', which='minor', labelsize=ticklabelsize, top='on', right='on', direction='in', length=minorticklength, width=tickwidth)
ax4.set_ylabel(r" y - J ", fontsize=labelsize)
##
cmap = plt.cm.rainbow
ax10 = ax4.twiny()
ax10.set_xlim(xmin_SpecT, xmax_SpecT)
ax10.scatter(SpT_optn, (ymag - J_tm), c=(SpT_optn**5.), cmap=cmap, alpha=0.60, s=ms_small)
ax10.tick_params(axis='both', which='major', labelsize=ticklabelsize, top='on', right='on', direction='in', length=majorticklength, width=tickwidth)


##   J - K 
cmap = plt.cm.autumn_r
ymin=-1.2; ymax=2.6
ax5.axis([xmin_redshift, xmax_redshift, ymin, ymax])
ax5.scatter(redshift, (Jmag - Kmag), c=redshift, cmap=cmap, s=ms, alpha=1.0)
ax5.tick_params(axis='both', which='major', labelsize=ticklabelsize, top='on', right='on', direction='in', length=majorticklength, width=tickwidth)
ax5.tick_params(axis='both', which='minor', labelsize=ticklabelsize, top='on', right='on', direction='in', length=minorticklength, width=tickwidth)
ax5.set_xlabel(r"redshift", fontsize=labelsize)
ax5.set_ylabel(r" J - Ks ", fontsize=labelsize)
## 
cmap = plt.cm.rainbow
ax11 = ax5.twiny()
ax11.set_xlim(xmin_SpecT, xmax_SpecT)
ax11.scatter(SpT_optn, (J_tm - Ks_tm), c=(SpT_optn**5.), cmap=cmap, alpha=0.60, s=ms_small)
ax11.tick_params(axis='both', which='major', labelsize=ticklabelsize, top='on', right='on', direction='in', length=majorticklength, width=tickwidth)


##   y - W1
ymin=1.8; ymax=6.2
## Redshift
cmap = plt.cm.autumn_r
ax6.axis([xmin_redshift, xmax_redshift, ymin, ymax])
ax6.scatter(redshift, (y_PS1 - W1), c=redshift, cmap=cmap, s=ms, alpha=1.0)
ax6.tick_params(axis='both', which='major', labelsize=ticklabelsize, top='on', right='on', direction='in', length=majorticklength, width=tickwidth)
ax6.tick_params(axis='both', which='minor', labelsize=ticklabelsize, top='on', right='on', direction='in', length=minorticklength, width=tickwidth)
ax6.set_xlabel(r"redshift", fontsize=labelsize)
ax6.set_ylabel(r" y - W1 ", fontsize=labelsize)
## 
cmap = plt.cm.rainbow
ax12 = ax6.twiny()
ax12.set_xlim(xmin_SpecT, xmax_SpecT)
ax12.scatter(SpT_optn, (ymag - W1mag), c=(SpT_optn**5.), cmap=cmap, alpha=0.60, s=ms_small)
ax12.tick_params(axis='both', which='major', labelsize=ticklabelsize, top='on', right='on', direction='in', length=majorticklength, width=tickwidth)



plt.show()

