#!/usr/bin/env python
# coding: utf-8
from __future__ import division

"""
This code generates DwC-A media file from a metadata file created using europeana_api_2.py.
 
"""

in_file_name = "europ_metadata_newurl.txt"
in_file = open(in_file_name, 'r')
out_file_name = "europ_media_berlin.txt"
out_file = open(out_file_name, 'w')

taxon_id_lookup = eval(open('europ_taxa_dict_berlin.txt').read())

type = 'http://purl.org/dc/dcmitype/StillImage'
format = 'image/jpeg'
publisher = 'Europeana'
contributor = 'OpenUp!'
rating = '2'
linenumber = 0
counter = 10000

for line in in_file:
	linenumber = linenumber + 1
	counter = counter + 1
	print linenumber
	row = line.strip().split('\t')
	mediaid = 'M' + str(counter)
	taxon = row[0]
	taxon_id = taxon_id_lookup[taxon]
	access_uri = row[4]
	license = row[2]
	creator = row[1]
	furtherinfourl = row[5]
	if taxon.find('?') != -1:
		description = 'Taxon ID is tentative. ' + row[6]
	else:
		description = row[6]
	owner = row[1]
	out_file.write('\t'.join([mediaid,taxon_id,type,format,access_uri,license,publisher,contributor,creator,furtherinfourl,description,owner,rating + '\n']))
	
out_file.close()
