#!/usr/bin/env python
# coding: utf-8
from __future__ import division
import re

"""
This code generates DwCA media file from a metadata file.
 
"""

in_file_name = "genus_metadata.txt"
in_file = open(in_file_name, 'r')
out_file_name = "wikip_media_test.txt"
out_file = open(out_file_name, 'w')

taxon_id_lookup = eval(open('wikip_taxa_dict.txt').read())
# url_lookup = eval(open('wikip_url_list.txt').read())

type = 'http://purl.org/dc/dcmitype/Text'
format = 'text/plain'
publisher = 'Wikipeixes'
license = 'http://creativecommons.org/licenses/by-nc/3.0/'
line_number = 0
counter = 10000

for line in in_file:
	line_number = line_number + 1
	print counter
	row = line.strip().split('\t')
	taxon = row[1]
	taxon_id = taxon_id_lookup[taxon]
	language = row[0]
	furtherinfourl = row[2]
"""
	m = re.search('(\w+) \w+',taxon)
	look_up = m.group(1)
	furtherinfourl = url_lookup['%s' % (look_up,)]
"""

	counter = counter + 1
	if row[4] == 'nd':
		print "No morphological information"
	else:
		mediaid = 'M' + str(counter)
		morphology = row[5]
		CVterm = 'http://rs.tdwg.org/ontology/voc/SPMInfoItems#Morphology'
		out_file.write('\t'.join([mediaid,taxon_id,language,type,format,license,publisher,CVterm,morphology,tab,furtherinfourl + '\n']))
	
	counter = counter + 1
	if row[5] == 'nd':
		print "No habitat information"
	else:
		mediaid = 'M' + str(counter)
		habitat = row[6]
		CVterm = 'http://rs.tdwg.org/ontology/voc/SPMInfoItems#Habitat'
		out_file.write('\t'.join([mediaid,taxon_id,language,type,format,license,publisher,CVterm,habitat,tab,furtherinfourl + '\n']))

	counter = counter + 1
	if row[6] == 'nd':
		print "No feeding information"
	else:
		mediaid = 'M' + str(counter)
		feeding = row[7]
		CVterm = 'http://rs.tdwg.org/ontology/voc/SPMInfoItems#TrophicStrategy'
		out_file.write('\t'.join([mediaid,taxon_id,language,type,format,license,publisher,CVterm,feeding,tab,furtherinfourl + '\n']))

	counter = counter + 1
	if row[7] == 'nd':
		print "No behavior information"
	else:
		mediaid = 'M' + str(counter)
		behavior = row[8]
		CVterm = 'http://rs.tdwg.org/ontology/voc/SPMInfoItems#Behaviour'
		out_file.write('\t'.join([mediaid,taxon_id,language,type,format,license,publisher,CVterm,behavior,tab,furtherinfourl + '\n']))
	
	counter = counter + 1
	if row[8] == 'nd':
		print "No reproduction information"
	else:
		mediaid = 'M' + str(counter)
		reproduction = row[9]
		CVterm = 'http://rs.tdwg.org/ontology/voc/SPMInfoItems#Reproduction'
		out_file.write('\t'.join([mediaid,taxon_id,language,type,format,license,publisher,CVterm,reproduction,tab,furtherinfourl + '\n']))

	counter = counter + 1
	if row[10] == 'nd':
		print "No distribution information"
	else:
		mediaid = 'M' + str(counter)
		geo_dist = row[11]
		CVterm = 'http://rs.tdwg.org/ontology/voc/SPMInfoItems#Distribution'
		out_file.write('\t'.join([mediaid,taxon_id,language,type,format,license,publisher,CVterm,geo_dist,tab,furtherinfourl + '\n']))
	
	counter = counter + 1
	if row[11] == 'nd':
		print "No diagnostic information"
	else:
		mediaid = 'M' + str(counter)
		diag_char = row[12]
		CVterm = 'http://rs.tdwg.org/ontology/voc/SPMInfoItems#DiagnosticDescription'
		out_file.write('\t'.join([mediaid,taxon_id,language,type,format,license,publisher,CVterm,diag_char,tab,furtherinfourl + '\n']))

out_file.close()

