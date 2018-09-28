'''

'''

from astropy.io import ascii
import numpy as np

from matplotlib import pyplot as plt
from matplotlib import colors
from matplotlib.ticker import ScalarFormatter

# Fixing random state for reproducibility
np.random.seed(19680801)

path='/cos_pc19a_npr/programs/quasars/highest_z/MIR_LCs/'
file = 'NoOfEpochs_perQuasar.dat'

data_in = ascii.read(path+file) 
print(type(data_in))
data = np.array(data_in).astype(np.float)


N_points = 100000
# Generate a normal distribution, center at x=0 and y=5
x = np.random.randn(N_points)
y = .4 * x + np.random.randn(100000) + 5

fig, ax = plt.subplots(figsize=(8.5, 8.5)) # inches

## placement of figure...
left   = 0.16   # the left side of the subplots of the figure
right  = 0.98   # the right side of the subplots of the figure
bottom = 0.12   # the bottom of the subplots of the figure
top    = 0.96   # the top of the subplots of the figure
wspace = 0.00   # the amount of width reserved for blank space between subplots
hspace = 0.00   # the amount of height reserved for white space between subplots
plt.subplots_adjust(left=left, bottom=bottom, right=right, top=top, wspace=wspace, hspace=hspace)


## define the colormap
cmap = plt.cm.inferno_r

ls = 'solid'
lw = 1.0
ms = 60.
ms_large = ms*3.
fontsize=24
alpha=1.00
nbins = 20

#ax.hist(x, bins=nbins)
ax.hist(data, bins=nbins)

ax.set_xlim((0.9, 360))
ax.set_ylim((0.8, 300))

#ax.set_xscale("log", nonposx='clip')
ax.set_yscale("log", nonposy='clip')
for axis in [ax.xaxis, ax.yaxis]:
    axis.set_major_formatter(ScalarFormatter())

ax.set_xlabel('No. of NEOWISE-R epochs', fontsize=fontsize)
ax.set_ylabel('No. of VHzQs',            fontsize=fontsize)
ax.tick_params('x', direction='in', which='both', bottom='True', top='True', left='True', right='True', labelsize=fontsize)
ax.tick_params('y', direction='in', which='both', bottom='True', top='True', left='True', right='True', labelsize=fontsize)
ax

#plt.show()
plt.savefig('NEOWISER_LC_histogram_temp.png', format='png')
plt.savefig('NEOWISER_LC_histogram_temp.pdf', format='pdf')
plt.close(fig)


