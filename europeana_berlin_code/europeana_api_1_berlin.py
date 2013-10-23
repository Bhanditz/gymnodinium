#!/usr/bin/env python
# coding: utf-8
from __future__ import division
import urllib, json

"""
This code uses the Europeana API search function to return IDs for all items in a specified
collection. In this instance, the collection is 11605. The API will return a maximum of 100
records at a time. This means that if we want to gather all 117499 records, we need to call
the API 1175 times. We can control which of the records are retrieved using the "start"
parameter in the API query. In this instance, I made a list of integers from 1 to 150000 in
increments of 100. For example 1, 101, 201, 301, etc. This is in the file query_rows_150000.txt. The 
increment needs to equal the "rows" parameter in the API call. Replace the "X" with your 
own API key.
"""
in_file_name = "query_rows_150000.txt"
in_file = open(in_file_name, 'r')
out_file_name = "europeana_berlin_ids.txt"
out_file = open(out_file_name, 'w')

def data_object_url(q):
    return 'http://europeana.eu/api//v2/search.json?wskey=XXXXXXXXX&profile=standard&query=europeana_collectionName%3A11605*&start=' + str(q) + '&rows=100'

for q in in_file:
	print q
	results = urllib.urlopen(data_object_url(q)).read()
	data = json.loads(results)
	for i in range(100):
		identifier = data ['items'][i]['id']
		print identifier
		out_file.write(identifier + '\n')
out_file.close()
