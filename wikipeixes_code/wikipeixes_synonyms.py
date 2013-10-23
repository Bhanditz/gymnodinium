#!/usr/bin/env python
# coding: utf-8
import re

"""
This code adds synonyms to the DwC-A core file from a metadata file.
 
"""

in_file_name = "wikipiexes_metadata_final.txt"
in_file = open(in_file_name, 'r')
out_file_name = "wikip_taxa.txt"
out_file = open(out_file_name, 'a')

taxon_id_lookup = eval(open('wikip_taxa_dict.txt').read())

TaxonRank = 'synonym'
counter = 0
synonymid = 10000

for line in in_file:
	counter = counter + 1
	print counter
	row = line.strip().split('\t')
	taxon = row[1]
	print taxon
	print row[2]
	taxon_id = taxon_id_lookup[taxon]
	
	if row[2] == 'nd':
		print "No synonyms listed"
	else:
		block = re.sub('(?<=[a-z])_(?=[A-Z(])',' ',row[2])
		block1 = re.sub('_(?=var)',' ',block)
		block2 = re.sub('(?<=var.)_',' ',block1)
		block3 = re.sub('(?<=var)_',' ',block2)
		synonyms = block3.split('_')
		for synonym in synonyms:
			synonymid = synonymid + 1
			synonym_id = 'S' + str(synonymid)
			print synonym
			out_file.write('\t'.join([synonym_id,synonym,taxon_id,TaxonRank + '\n']))

out_file.close()
