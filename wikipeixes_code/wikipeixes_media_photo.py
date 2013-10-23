#!/usr/bin/env python
# coding: utf-8
from __future__ import division
import re

"""
This code generates DwC-A media file from a photo metadata file.
 
"""

in_file_name = "wikipiexes_photo_metadata_final.txt"
in_file = open(in_file_name, 'r')
out_file_name = "wikip_media.txt"
out_file = open(out_file_name, 'a')

taxon_id_lookup = eval(open('wikip_taxa_dict.txt').read())

type = 'http://purl.org/dc/dcmitype/StillImage'
publisher = 'Wikipeixes'
license = 'http://creativecommons.org/licenses/by-nc/3.0/'
line_number = 0
counter = 20000

for line in in_file:
	line_number = line_number + 1
	results = []
	counter = counter + 1
	mediaid = 'M' + str(counter)
	print line_number
	row = line.strip().split('\t')
	taxon = row[1].strip()
	taxon_id = taxon_id_lookup[taxon]
	language = row[0]
	access_uri = row[8]
	further_info_url = row[7]
	results.append(mediaid + '*' + taxon_id + '*' + language + '*' + type + '*')
	
	if row[4] == 'nd':
		print "No format listed"
		results.append('*')
	else:
		format = 'image/' + row[4].lower()
		results.append(format + '*')
	
	results.append(license + '*' + publisher + '**')
	
	if row[5] == 'nd':
		print "No camera listed"
		results.append('*')
	else:
		description = row[5]	
		results.append(description + '*')
	
	if row[2] == 'nd':
		print "No creation date"
		results.append('*')
	else:
		CreateDate = row[2]
		results.append(CreateDate + '*')

	if row[3] == 'nd':
		print "No photographer listed"
		results.append('*')
	else:
		creator = row[3]
		results.append(creator + '*')
		
	results.append(further_info_url + '*' + access_uri)
	
	row = "".join(results)
	remove = re.sub('\*','\t',row)
	out_file.write(remove + '\n')

out_file.close()
