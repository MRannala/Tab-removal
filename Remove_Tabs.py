# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 11:32:57 2016

This script will allow input of a file. It then creates a secondfile where tabs have been replaced with single
spaces. The new filename will be the same as the initial but with a '+' appended.

@author: Magnus Rannala
"""

import os
import sys
import tkinter as tk
import tkFileDialog

# Open interactive window
filepath =  tkFileDialog.askopenfilename()
filename = filepath.split('/')
filename = filename[-1]
# filename = "test1.txt"

# Test if file name exists and exit if not
if os.path.isfile(filename) == False:
    print " "
    print "No Such File in Directory! "    
    print " "
    sys.exit()
else:
    pass

data_array = []

# open file for read
ifile = open(filename, 'r')

for line in ifile:
    data_array.append(line)
    
# close input file
ifile.close()

# Create new file name using + appended to input filename
ofilename = filename.rsplit(".")[0] + "+." + filename.rsplit(".")[1]

# open output file
ofile = open(ofilename, 'w')

for i in range(len(data_array)):
    ofile.write(data_array[i].replace("\t", " "))
    
ofile.close()

