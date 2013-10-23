#!/usr/bin/env python
# coding: utf-8
from __future__ import division
import urllib, json

"""
This code uses the Europeana API record function to return the metadata for a record. The 
IDs for each record were gathered in europeana_api_1.py. 
"""

in_file_name = "europeana_ids_job.txt"
in_file = open(in_file_name, 'r')
out_file_name = "europ_metadata.txt"
out_file = open(out_file_name, 'w')

def data_object_url(q):
    return 'http://europeana.eu/api//v2/record' + q + '.json?wskey=QcneaFyv2&profile=full'

for q in in_file:
	print q
	results = urllib.urlopen(data_object_url(q.strip())).read()
	data = json.loads(results)
	
	if data['success'] == True:
		scientificName = data ['object']['proxies'][0]['dcTitle']['def'][0]
		creator = data ['object']['aggregations'][0]['edmDataProvider']['def'][0]
		license = data ['object']['aggregations'][0]['edmRights']['def'][0]
		contributor = data ['object']['aggregations'][0]['edmProvider']['def'][0]
		accessuri = data ['object']['aggregations'][0]['webResources'][0]['about']
		furtherinfourl = data ['object']['europeanaAggregation']['edmLandingPage']
		specimentype = data ['object']['proxies'][0]['dcType']['def'][0]
		specimennumber = data ['object']['proxies'][0]['dcIdentifier']['def'][0]
		owner = data ['object']['aggregations'][0]['edmDataProvider']['def'][0]
		description = " ".join([specimentype,specimennumber])
		row = '\t'.join([scientificName,creator,license,contributor,accessuri,furtherinfourl,description,owner])
		out_file.write(row.encode('utf8') + '\n')
out_file.close()
