#!/usr/bin/env python
# coding: utf-8
from __future__ import division
import urllib, re
from bs4 import BeautifulSoup

"""
This code scrapes the references from a taxon page at wikipeixes and exports it as a tab
delimited file. Be sure wikipiexes_references_metadata.txt is empty before you begin.
"""

in_file_name = "wikipiexes_url.txt"
in_file = open(in_file_name, 'r')
out_file_name = "wikipiexes_references_metadata.txt"
out_file = open(out_file_name, 'a')

def wikipeixes_text(url):
	print url
	web_page = urllib.urlopen(url).read()
	soup = BeautifulSoup(web_page)
	tag = soup.html
	lang = tag['xml:lang']
	text = soup.get_text()
	object = soup.find('div', class_ = 'page')
	clean = object.get_text('|', strip=True)
	return clean,lang

def metadata_table(clean,lang):
	if re.search('TOC END.*Links Externos', clean) == None:
		print "No data for this species"
		return results
	else:
		q = re.search('TOC END.*Links Externos', clean)
		part = q.group(0)
		elementList = []
		elementList = part.split('|')
		name = elementList[2] + ' ' + elementList[3]
		results.append(name + '*')
		print name
		reference_index = None
		links_index = None
		for element in elementList:
			if element == 'Referências'.decode('utf8'):
				reference_index = elementList.index('Referências'.decode('utf8'))
			elif element == 'Links Externos'.decode('utf8'):
				links_index = elementList.index('Links Externos'.decode('utf8'))
			else:
				continue
		
		if reference_index == None:
			print "No references listed"
			results.append('nd')
		else:
			if elementList[reference_index+1] == 'Autor, AB; Autor CD & Autor EF. 2000.'.decode('utf8'):
				print "No references listed"
				results.append('nd')
			elif elementList[reference_index+1] == 'Links Externos'.decode('utf8'):
				print "No references listed"
				results.append('nd')
			else:
				reference_text = elementList[reference_index+1:links_index]
				reference = " ".join(reference_text)
				results.append(reference)
				
		if results[1] == 'nd':
			print "No results"
		else:
			row = "".join(results)
			print row
			return row


out_file.write("Name\tReferences\n")
for url in in_file:
	results = []
	data = metadata_table(*wikipeixes_text(url))
	print data
	if data == None:
		print "No data"
	else:
		if len(data) > 1:
			remove = re.sub('\*','\t',data)
			out_file.write(remove.encode('utf8') + '\n')
out_file.close()
