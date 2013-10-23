#!/usr/bin/env python
# coding: utf-8
from __future__ import division
import urllib, re
from bs4 import BeautifulSoup

"""
This code scrapes the text from the site map on the wikipeixes home page to generate a 
list of all the taxon page urls at wikipeixes. This code will only grab urls for species 
and genera. At this time wikipeixes has no content for higher level taxa.
"""

out_file_name = "wikipiexes_url.txt"
out_file = open(out_file_name, 'w')

web_page = urllib.urlopen("http://wikipeixes.com.br/Start").read()
soup = BeautifulSoup(web_page)
species = soup.find_all('script')
taxon_list = species[5]
clean = taxon_list.get_text('|', strip=True)
taxon_table = clean.split(');')
for line in taxon_table:
	if re.search('especies|generos',line) == None:
		print "No value"
		continue
	elif re.search('\(\'\w+:\w+\'', line) == None:
		print "No value"
		print line
		continue
	else:
		q = re.search('\w+:\w+', line)
		segment = q.group(0)
		print segment
		out_file.write('http://wikipeixes.com.br/' + segment + '\n')
		
out_file.close()
