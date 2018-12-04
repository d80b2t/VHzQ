
# coding: utf-8

# In[1]:


''' A simple little bit of code to figure out which survey the VHzQs came from.'''


# In[2]:


import numpy as np
import pandas as pd

from astropy.io    import fits
from astropy.io    import ascii
from astropy.table import Table


# In[3]:


##  V H z Q    data
path     = '../data/'
filename = 'LIST_OF_VHzQs.dat'
table    = path+filename

VHzQ_list = ascii.read(table)


# In[4]:


print('type(VHzQ_list)', type(VHzQ_list))
print('len(VHzQ_list)',   len(VHzQ_list))


# In[5]:


VHzQ_list.colnames


# In[6]:


## Column 'na' has the original survey designations
len(np.unique(VHzQ_list['na']))


# In[7]:


np.unique(VHzQ_list['na'])


# In[8]:


type(np.unique(VHzQ_list['na']))


# In[9]:


#VHzQ_list.group_by('na').size().sort_values(ascending=False)
survey, counts = np.unique(VHzQ_list["na"], return_counts=True)


# In[11]:


## Loop through the number of entries the variable 'survey' has
for x in range(len(survey)):
    print('{:7} & {:4d}'.format(survey[x], counts[x]))

