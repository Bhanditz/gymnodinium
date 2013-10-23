#!/usr/bin/env python
# coding: utf-8
from __future__ import division

"""
This code generates a list of unique taxa from a metadata file and assigns a taxon ID to 
each taxon. The output is the DwC-A core file.
 
"""
in_file_name = "all_wikip_names.txt"
in_file = open(in_file_name, 'r')
out_file_name = "wikip_taxa.txt"
out_file = open(out_file_name, 'w')

taxa = []

for line in in_file:
	row = line.strip().split('\t')
	taxa.append(row[1])
	
unique_taxa = set(taxa)

counter = 10000
for taxon in unique_taxa:
	counter = counter + 1
	out_file.write('T' + str(counter) + '\t' + taxon + '\n')
	
out_file.close()