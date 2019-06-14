''' 
 A simple little bit of code to convert the 
 [W/V]SA_wWISE.dat files into nicely formatted .tex tables. 
 v0.01    Thu May  9 12:57:29 BST 2019
'''

import numpy as np

from astropy.io    import fits
from astropy.io    import ascii
from astropy.table import Table

##
##  V H z Q    data
##
path      = '/cos_pc19a_npr/programs/quasars/highest_z/tables_for_paper/'
#filename  = 'WSA_wWISE.dat'
filename   = 'VHzQs_ZYJHK_WISE.dat' 
table     = path+filename
VHzQ_list = ascii.read(table)

print()
print(type(VHzQ_list['ra']))
print()

## Just the top 10 or 5\% for demo purposes in the .tex manuscript
VHzQ_Top10 = VHzQ_list[0:23]


## Set-up the table header
header = """\\begin{table}
\\begin{tabular}{llrrc cccc cccc}
 \hline
 \hline
  \multirow{2}{*}{Survey} &  \multirow{2}{*}{QsoName} &   R.A. / deg  &   Decl. / deg  &  \multirow{2}{*}{redshift}   &  \multirow{2}{*}{Y}  &  \multirow{2}{*}{J}   &  \multirow{2}{*}{H}  &  \multirow{2}{*}{K}     &  \multicolumn{2}{c}{unWISE}  &  \multicolumn{2}{c}{AllWISE} \\\ 
                          &                           &   (J2000)     &  (J2000)       &                              &                      &                       &                      &                         &          W1       & W2       & W3   & W4 \\\ 
  \hline
  \hline
  \\\\\n"""

print(header)


## Set-up the table footer...
footer = """    \hline
    \hline
    \\end{tabular}
    \caption{The first 23 (i.e. 5\%) of 463 very high-$z$ quasars in Right Ascension order with near and mid-infrared photometry. 
                  The full table can be found \href{https://github.com/d80b2t/VHzQ/tree/master/data}{here}. 
                  Since none of the first 23 objects have $Z$-band detections, we don't report that column here (but
                  is reported in the main table).} 
     \label{tab:output_table}
     \\end{table}
     \n"""
print(footer)

##  {0}, {1}, {2}, {3}, {4}, are Survey, QsoName, ra, dec, redshift
##  
with open("output_table.tex", "w") as out:
   out.write(header)
   #for row in VHzQ_list:
   for row in VHzQ_Top10:
       out.write("{0} & {1} & {2:10.5f} & {3:10.5f} & {4:5.2f}   &   ${7:5.2f}\\pm{8:5.3f}$  &  ${9:5.2f}\\pm{10:5.3f}$  &  ${11:5.2f}\\pm{12:5.3f}$   & ${13:5.2f}\\pm{14:5.3f}$    &   ${15:5.3f}\\pm{16:5.3f}$   &  ${18:5.2f}\\pm{19:5.3f}$   &   ${21:5.2f}\\pm{22:5.3f}$   &   ${24:5.2f}\\pm{25:5.3f}$   \\\\\n".format(*row))
   out.write(footer)

   

