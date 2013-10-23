#!/usr/bin/env python
# coding: utf-8
from __future__ import division
import random

"""
This code generates DwC-A core file from a taxon list.
 
"""
in_file_name = "europeana_taxon_list.txt"
in_file = open(in_file_name, 'r')
out_file_name = "europ_taxa.txt"
out_file = open(out_file_name, 'w')
counter = 10000

for line in in_file:
	print line
	counter = counter + 1
	out_file.write('T' + str(counter) + '\t' + line)
out_file.close()
