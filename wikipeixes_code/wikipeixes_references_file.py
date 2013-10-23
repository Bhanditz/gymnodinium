#!/usr/bin/env python
# coding: utf-8
from __future__ import division

"""
This code generates DwC-A references file from a metadata file.
 
"""

in_file_name = "wikipiexes_references_metadata_final.txt"
in_file = open(in_file_name, 'r')
out_file_name = "wikip_references.txt"
out_file = open(out_file_name, 'w')

taxon_id_lookup = eval(open('wikip_taxa_dict.txt').read())

counter = 10000

for line in in_file:
	counter = counter + 1
	print counter
	row = line.strip().split('\t')
	print len(row)
	if len(row) > 1:
		taxon = row[0]
		taxon_id = taxon_id_lookup[taxon]
		reference = row [1]
		refid = 'R' + str(counter)
		out_file.write('\t'.join([refid,taxon_id,reference + '\n']))
	
out_file.close()
