'''
Taking the WSA data for the VHzQ sample and looking at how many
enteries there are per object.
'''

from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

## Reading in the data
path = '/cos_pc19a_npr/programs/quasars/highest_z/data/WSA/'
filename = 'results16_20_2_38_44430.fits'
fits_table=path+filename

## open a FITS file
hdul = fits.open(fits_table)  

## assume the first extension is a table
data = hdul[1].data  
## Saying what the columns are::
data.columns

## Converting from radians to degrees
data.RA  = data.RA  * (180./np.pi)
data.DEC = data.DEC * (180./np.pi)

## Looking for unique entries per column
print('No. of unique enteries by QSONAME::         ', len(np.unique(data.QSONAME)))
print('No. of unique enteries by RA::              ', len(np.unique(data.RA)))
print('No. of unique enteries by DEC::             ', len(np.unique(data.DEC)))
print('No. of unique enteries by APERTUREID::      ', len(np.unique(data.APERTUREID)))
print('No. of unique enteries by APERJKY3AVER::    ', len(np.unique(data.APERJKY3AVER)))
print('No. of unique enteries by APERJKY3AVERERR:: ', len(np.unique(data.APERJKY3AVERERR)))
print('No. of unique enteries by SUMWEIGHT::       ', len(np.unique(data.SUMWEIGHT)))
print('No. of unique enteries by MJDOBS::          ', len(np.unique(data.MJDOBS)))
print('No. of unique enteries by FILTERID::        ', len(np.unique(data.FILTERID)))
print('No. of unique enteries by APERJKY3::        ', len(np.unique(data.APERJKY3)))
print('No. of unique enteries by APERJKY3ERR::     ', len(np.unique(data.APERJKY3ERR)))
print('No. of unique enteries by WEIGHT::          ', len(np.unique(data.WEIGHT)))
print('No. of unique enteries by PPERRBITS::       ', len(np.unique(data.PPERRBITS)))
print('No. of unique enteries by PROJECT::         ', len(np.unique(data.PROJECT)))


## Check if two to get unique values from list
##
# function to get unique values 
def unique(list1): 
  
    # intilize a null list 
    unique_list = [] 
      
    # traverse for all elements 
    for x in list1: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x) 
    # print list 
    for x in unique_list: 
        print(x)

## Look at the unique RAs
#unique(data.RA)

unique_elements, counts_elements = np.unique(data.QSONAME, return_counts=True)
print("Frequency of unique values of the said array:")
print(np.asarray((unique_elements, counts_elements)))
print('type(counts_elements)', type(counts_elements))

##
## https://stackoverflow.com/questions/6618515/sorting-list-based-on-values-from-another-list
##
X = unique_elements
Y = counts_elements
[x for _,x in sorted(zip(Y,X))]

## Looking at the histogram of the entry values
np.histogram(counts_elements, 20)


a = np.hstack(counts_elements)
## https://stackoverflow.com/questions/6855710/how-to-have-logarithmic-bins-in-a-python-histogram
xmin=0.1; xmax=2500.; 
ymin=0.1; ymax=110.; 

#plt.hist(a)  # arguments are passed to np.histogram
plt.hist(a, bins = 10 ** np.linspace(np.log10(xmin), np.log10(xmax), 50))

axes = plt.gca()

axes.set_xlim([xmin,xmax])
axes.set_ylim([ymin,ymax])
axes.set_xscale("log")
axes.set_yscale("log")

plt.xlabel("No. of entries")
plt.ylabel("No. of quasars")

#plt.show()
plt.savefig('No_entries_per_quasar_temp.png', format='png')

