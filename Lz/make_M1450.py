
# coding: utf-8

# In[1]:


from astropy.io import fits
from astropy.io import ascii
from astropy.table import Table
from matplotlib.ticker import AutoMinorLocator

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math

from matplotlib import colors as mcolors
from matplotlib import gridspec


# In[2]:


from astropy.cosmology import FlatLambdaCDM
# In this case we just need to define the matter density 
# and hubble parameter at z=0.
# Note the default units for the hubble parameter H0 are km/s/Mpc. 
# You can also pass an astropy `Quantity` with the units specified. 
cosmo = FlatLambdaCDM(H0=67.7, Om0=0.307)  #Banados thesis


# In[3]:


import astropy.units as u
ages = np.array([13, 10, 8, 6, 5, 4, 3, 2, 1.5, 1.2, 1, 0.8, 0.70])*u.Gyr
from astropy.cosmology import z_at_value
ageticks = [z_at_value(cosmo.age, age) for age in ages]


# In[4]:


## READ-IN THE DATA FILE(S)
path = '/cos_pc19a_npr/programs/quasars/highest_z/data/'
infile = 'THE_TABLE_v0pnt971.ascii'
readin = path+infile
all_VHzQs  = ascii.read(readin, delimiter=r'\s')


# In[5]:


all_VHzQs


# In[6]:


## Gotta give credit where it's due... 
## Kulkarni, of arXiv:1807.09774v1 fame, 
## gives full datafiles and scripts on their GitHub::
## https://github.com/gkulkarni/QLF 
##
## Load e.g. the k-correction based on Lusso et al. (2015)
kcorr_path= '/cos_pc19a_npr/programs/quasars/highest_z/Lz/kcorr/'

## There's the g-band correction (essentially z<2.2)
z_kcorr_gband, kcorr_Lusso15_gband = np.loadtxt(kcorr_path+'kcorrg_l15.dat', usecols=(1,2), unpack=True)
## There's the g-band correction (essentially z<4.7)
z_kcorr_iband, kcorr_Lusso15_iband = np.loadtxt(kcorr_path+'kcorri_l15.dat', usecols=(1,2), unpack=True)
## There's the g-band correction (essentially 4.7<z<5.5)
z_kcorr_zband, kcorr_Lusso15_zband = np.loadtxt(kcorr_path+'kcorrz_l15.dat', usecols=(1,2), unpack=True)


# In[7]:


##
## DISTANCE MODULUS CALCULATIONS!!!!
##
##   m - M = 5 * log(d) - 5
## m is the apparent magnitude of the object
## M is the absolute magnitude of the object
## d is the distance to the object in parsecs


# In[8]:


cosmo


# In[9]:


cosmo.luminosity_distance(4)


# In[10]:


cosmo.luminosity_distance(all_VHzQs['redshift'])


# In[11]:


d_Mpc = cosmo.luminosity_distance(all_VHzQs['redshift'])


# In[12]:


#d_Mpc.value


# In[13]:


kcorr = 0.0


# In[14]:


Abs_Mag = (all_VHzQs['mag'])  - (5.*(np.log10(d_Mpc.value))) - 25. + kcorr
#Abs_Mag


# In[15]:


delta_mags = Abs_Mag - all_VHzQs['M1450'] 


# In[16]:


Abs_Mag[0]


# In[17]:


all_VHzQs[1]


# In[18]:


Abs_Mag[1]


# In[19]:


z_slope_in = (np.arange(800)/100)
z_slope = -2.5*(np.log10(1+z_slope_in))


# In[20]:


fig, ax = plt.subplots()
ax.scatter(all_VHzQs['redshift'], Abs_Mag, marker='.')
ymin = -20.5
ymax = -34.0
ax.set_ylim((ymin, ymax))


# In[21]:


fig, ax = plt.subplots(figsize=(14,6))
s = 500
lw=6

plt.plot(z_kcorr_gband, kcorr_Lusso15_gband, c='b', lw=lw) 
plt.plot(z_kcorr_iband, kcorr_Lusso15_iband, c='r', lw=lw) 
plt.plot(z_kcorr_zband, kcorr_Lusso15_zband, c='k', lw=lw) 

plt.plot(z_slope_in, z_slope, lw=2)

ax.scatter(all_VHzQs['redshift'], delta_mags, marker='.', s=s, alpha=0.8)

xmin =  0.0
xmax =  8.0
ax.set_xlim((xmin, xmax))

ymin = -2.5
ymax = -0.0
ax.set_ylim((ymin, ymax))


# In[26]:


fig, ax = plt.subplots(figsize=(12,8))
s = 500
lw=6

plt.plot(z_kcorr_gband, kcorr_Lusso15_gband, c='b', lw=lw) 
plt.plot(z_kcorr_iband, kcorr_Lusso15_iband, c='r', lw=lw) 
plt.plot(z_kcorr_zband, kcorr_Lusso15_zband, c='k', lw=lw) 

plt.plot(z_slope_in, z_slope, lw=2)

ax.scatter(all_VHzQs['redshift'], delta_mags, marker='.', s=s, alpha=0.8)

xmin =  4.9
xmax =  7.6
ax.set_xlim((xmin, xmax))

ymin = -2.5
ymax = -1.8
ax.set_ylim((ymin, ymax))

