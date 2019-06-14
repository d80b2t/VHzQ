#! /usr/bin/env python
#------------------------------------------------------------------------------
# $Id: average_NEOWISE_lightcurves.py 11588 2017-02-12 21:38:25Z NicholasCross $
"""
   


   @author: N.J.G.. Cross
   @org:    WFAU, IfA, University of Edinburgh
"""
#------------------------------------------------------------------------------
from __future__      import division, print_function
from   operator             import attrgetter, itemgetter
from   itertools            import groupby

import math
import os
import sys
import numpy
from astropy.io import fits, ascii
from astropy.table    import Table

def getMjdRanges(mjdData):
    """ Looks for groups of data separated by about 6 months, over a few days
    """
    startMjd=mjdData[0]
    mjdGroupList=[]
    mjdGroup=[]
    for mjd in mjdData:
        if mjd<startMjd+20.:
            mjdGroup.append(mjd)
        elif mjd>startMjd+130.:
            startMjd=mjd
            # calc stats
            minMjd=min(mjdGroup)
            maxMjd=max(mjdGroup)
            meanMjd=numpy.mean(mjdGroup)
            mjdGroupList.append((minMjd,meanMjd,maxMjd,len(mjdGroup)))
            mjdGroup=[mjd]
        else:
            print("mjd does not fall in group, nor start new group: ",mjd,startMjd)
    return mjdGroupList
    
def getAveragePhot(data,mjdRangeMask,band):
    """ Uses weighted mean to average photometry
    """
    default_value = -999.999

    mpro=data['w%smpro' % band][mjdRangeMask]
    sigma_mpro=data['w%ssigmpro' % band][mjdRangeMask]
    weights = numpy.where(sigma_mpro>0.,1./(sigma_mpro*sigma_mpro),0.)
    sumweight = numpy.sum(weights)
    if sumweight>0.:
        mpro_err = math.sqrt(1./sumweight)
        mpro_weight = numpy.sum(mpro*weights)/sumweight   
    else:
        mpro_err=default_value
        mpro_weight = default_value
    return mpro_weight,mpro_err

inputTable = sys.argv[1]

data= Table.read(inputTable, format='ipac')
# Useful columns: cntr_01,ra,dec,w1mpro,w1sigmpro,w1snr,w2mpro,w2sigmpro,w2snr,cc_flags,mjd


sourceIDs=sorted(list(set(data['cntr_01'])))
outputDataList=[]
for srcID in sourceIDs:
    srcDataMask=numpy.nonzero(data['cntr_01']==srcID)
    ra,dec=data['ra_01'][srcDataMask][0],data['dec_01'][srcDataMask][0]
    mjdData= sorted(data['mjd'][srcDataMask])
    # Group mjd values.
    mjdRanges = getMjdRanges(mjdData) # min,mean,max
    # Now select data for each range and average:
    for mjdMin,mjdMean,mjdMax,nMeas in mjdRanges:
        if nMeas>=2:
            mjdRangeMask=numpy.nonzero(numpy.logical_and(
                data['mjd'][srcDataMask]>=mjdMin,data['mjd'][srcDataMask]<=mjdMax))
            w1mpro_weight,w1mpro_err=getAveragePhot(data,mjdRangeMask,1)
            w2mpro_weight,w2mpro_err=getAveragePhot(data,mjdRangeMask,2)
            outputDataList+=[(srcID,ra,dec,mjdMean,w1mpro_weight,w1mpro_err,w2mpro_weight,w2mpro_err,nMeas)]

# Output data to table.

out_table = Table(rows=outputDataList, names=('cntr_01', 'ra_01', 'dec_01','mean_mjd','w1mpro_wgt','w1mpro_err',
    'w2mpro_wgt','w2mpro_err','nMeas'), dtype=('i4', 'f8', 'f8','f8','f8','f8','f8','f8','i4'))

out_table.write(inputTable.replace('.tbl','_averaged.tbl'),format='ipac',overwrite=True)