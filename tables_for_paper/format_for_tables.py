''' 
# coding: utf-8

# A simple little bit of code to convert the 
# [W/V]SA_wWISE.dat files into nicely formatted .tex tables. 
# v0.01    Thu May  9 12:57:29 BST 2019
# 
'''

import numpy as np

from astropy.io    import fits
from astropy.io    import ascii
from astropy.table import Table


##
##  V H z Q    data
##
path     = '/cos_pc19a_npr/programs/quasars/highest_z/tables_for_paper/'
filename = 'WSA_wWISE.dat'
table    = path+filename

VHzQ_list = ascii.read(table)


print(type(VHzQ_list['ra']))

## Just the top 10 for demo purposes in the .tex manuscript
VHzQ_Top10 = VHzQ_list[0:10]


## Set-up the table header
header = """\\begin{table*}
\\begin{tabular}{ccccc ccccc cccc}
  \hline \hline
  survey   & qsoName &  ra  & dec & redshift  &  
  Z        & Y       &  J   &  H  &  K & 
  W1       & W2      & W3   & W4 
  \hline \hline
  \\\\\n"""

print(header)

## Set-up the table footer...
footer = """  \hline \hline \\end{tabular}
\\end{table*}\n"""
print(footer)


with open("output_table.tex", "w") as out:
   out.write(header)
   #for row in VHzQ_list:
   for row in VHzQ_Top10:
       out.write("{0} & {1} & {2:10.5f} & {3:10.5f} & {4:5.2f}   &   ${5:5.2f}\\pm{6:5.3f}$  &  ${7:5.2f}\\pm{8:5.3f}$  &  ${9:5.2f}\\pm{10:5.3f}$  &  ${11:5.2f}\\pm{12:5.3f}$   & ${13:5.2f}\\pm{14:5.3f}$    &   ${15:5.3f}\\pm{16:5.3f}$   &  ${18:5.2f}\\pm{19:5.3f}$   &   ${21:5.2f}\\pm{22:5.3f}$   &   ${24:5.2f}\\pm{25:5.3f}$   \\\\\n".format(*row))
   out.write(footer)

   

