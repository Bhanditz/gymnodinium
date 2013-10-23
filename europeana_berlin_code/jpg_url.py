#!/usr/bin/env python
# coding: utf-8
import re

"""
This code generates the direct jpg URL from the URL that .
 
"""

in_file_name = "europ_metadata_final.txt"
in_file = open(in_file_name, 'r')
out_file_name = "test_results.txt"
out_file = open(out_file_name, 'w')
line_number = 0

for line in in_file:
	line_number = line_number + 1
	print line_number
	row = line.strip().split('\t')
	viewer_url = row[4]
	taxon = row[0]
	creator = row[1]
	license = row[2]
	contributor = row[3]
	furtherinfourl = row[5]
	description = row[6]
	owner = row[7]
	m = re.search('- (B [-W1023468]+ \d+)',description)
	specimen_number = m.group(1)
	bits = specimen_number.split(' ')
	first = bits[0]
	second = bits[1]
	third = bits[2]
	a = third[:2]
	b = third[2:4]
	c = third[4:6]
	if second == '10':	
		access_uri = 'http://ww2.bgbm.org/herbarium/images/' + first + '/' + second + '/' + a + '/' + b + '/' + c + '/' + first + '_' + second + '_' + third + '.jpg'
		out_file.write('\t'.join([taxon,creator,license,contributor,access_uri,furtherinfourl,description,owner + '\n']))
	elif second == '-W':
		access_uri = 'http://ww2.bgbm.org/herbarium/images/' + first + '/' + second + '/' + a + '/' + b + '/' + first + '_' + second + '_' + third + '%20-01%200.jpg'
		out_file.write('\t'.join([taxon,creator,license,contributor,access_uri,furtherinfourl,description,owner + '\n']))
	elif second == '20':
		access_uri = 'http://ww2.bgbm.org/herbarium/images/' + first + '/' + second + '/' + a + '/' + b + '/' + c + '/' + first + '_' + second + '_' + third + '.jpg'
		out_file.write('\t'.join([taxon,creator,license,contributor,access_uri,furtherinfourl,description,owner + '\n']))
	elif second == '31':
		access_uri = 'http://ww2.bgbm.org/herbarium/images/' + first + '/' + second + '/' + a + '/' + b + '/' + c + '/' + first + '_' + second + '_' + third + '%2001__2.jpg'
		out_file.write('\t'.join([taxon,creator,license,contributor,access_uri,furtherinfourl,description,owner + '\n']))
	elif second == '40':
		access_uri = 'http://ww2.bgbm.org/herbarium/images/' + first + '/' + second + '/' + a + '/' + b + '/' + c + '/' + first + '_' + second + '_' + third + '.jpg'
		out_file.write('\t'.join([taxon,creator,license,contributor,access_uri,furtherinfourl,description,owner + '\n']))
	elif second == '60':
		access_uri = 'http://ww2.bgbm.org/herbarium/images/' + first + '/' + second + '/' + a + '/' + b + '/' + c + '/' + first + '_' + second + '_' + third + '.jpg'
		out_file.write('\t'.join([taxon,creator,license,contributor,access_uri,furtherinfourl,description,owner + '\n']))
	elif second == '81':
		access_uri = 'http://ww2.bgbm.org/herbarium/images/' + first + '/' + second + '/' + a + '/' + b + '/' + c + '/' + first + '_' + second + '_' + third + '.jpg'
		out_file.write('\t'.join([taxon,creator,license,contributor,access_uri,furtherinfourl,description,owner + '\n']))

out_file.close()
