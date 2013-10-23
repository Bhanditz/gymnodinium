#!/usr/bin/env python
# coding: utf-8

"""
This code generates DwCA vernacular name extension file from a metadata file. Be sure 
wikip_vernacular.txt is empty before you begin.
 
"""

in_file_name = "wikipiexes_metadata_final.txt"
in_file = open(in_file_name, 'r')
out_file_name = "wikip_vernacular.txt"
out_file = open(out_file_name, 'a')

taxon_id_lookup = eval(open('wikip_taxa_dict.txt').read())

source = 'Wikipeixes'
country = 'BR'
counter = 0

for line in in_file:
	counter = counter + 1
	print counter
	row = line.strip().split('\t')
	taxon = row[1]
	print taxon
	taxon_id = taxon_id_lookup[taxon]
	language = row[0]

	if row[3] == 'nd':
		print "No vernacular names listed"
	else:
		commonnames = row[3].split(', ')
		for commonname in commonnames:
			print commonname
			out_file.write('\t'.join([taxon_id,commonname,source,language,country + '\n']))

out_file.close()
