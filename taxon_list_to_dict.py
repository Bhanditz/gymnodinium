#!/usr/bin/env python
# coding: utf-8
from __future__ import division

"""
This code generates a dictionary from a DwC-A core file. This dictionary can be used to 
match the taxon ID to the other metadata in the extension files.
 
"""

in_file_name = "europ_taxa_berlin.txt"
in_file = open(in_file_name, 'r')
out_file_name = "europ_taxa_dict_berlin.txt"
out_file = open(out_file_name, 'w')

out_file.write('{\n')

for line in in_file:
	row = line.strip().split('\t')
	#row = line.split('\t')
	out_file.write('\'' + row[1] + '\':\'' + row[0] + '\',\n')
	
out_file.write('}')
out_file.close()
