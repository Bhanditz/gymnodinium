#!/usr/bin/env python
# coding: utf-8
from __future__ import division
import urllib, re
from bs4 import BeautifulSoup

"""
This code scrapes the text from an image detail page at wikipeixes and exports it as a tab
delimited file. There are two functions: wikipeixes_image_text and metadata_table. 
wikipeixes_text takes the url and uses Beautiful Soup to scrape the page. It returns the 
cleaned text scraped from the page and the language code. metadata_table takes the clean 
text and the language code from wikipeixes_image_text. The clean text is partitioned into 
the  appropriate content parts and placed in one row per image. metadata_table returns the 
row of data which is then added to the final tab-delimited table. Be sure 
wikipiexes_photo_metadata.txt is empty before you begin.
"""

in_file_name = "wikipiexes_photo_url.txt"
in_file = open(in_file_name, 'r')
out_file_name = "wikipiexes_photo_metadata.txt"
out_file = open(out_file_name, 'a')

def wikipeixes_image_text(url):
	print url.strip()
	web_page = urllib.urlopen(url.strip()).read()
	soup = BeautifulSoup(web_page)
	tag = soup.html
	lang = tag['xml:lang']
	print lang
	text = soup.find('body')
	clean = text.get_text('|', strip=True)
	return clean,lang

def metadata_table(clean,lang):
	results.append(lang + '*')
	elementList = []
	elementList = clean.split('|')
	element = elementList[0].replace('"', '')
	print element
	m = re.search(r':*([A-Za-z_ ]+(\(\w+, \d{4}\))*)-*\d*x*(sp.)*(.jpg)*$', element)
	name = re.sub('_', ' ', m.group(1)).capitalize()
	print name
	results.append(name + '*')
	CreateDate_index = None
	format_index = None
	creator_index = None
	camera_index = None
	keyword_index = None
	for element in elementList:
		if element == 'Data:'.decode('utf8'):
			CreateDate_index = elementList.index('Data:'.decode('utf8'))
		elif element == 'Fotógrafo:'.decode('utf8'):
			creator_index = elementList.index('Fotógrafo:'.decode('utf8'))
		elif element == 'Formato:'.decode('utf8'):
			format_index = elementList.index('Formato:'.decode('utf8'))
		elif element == 'Câmera:'.decode('utf8'):
			camera_index = elementList.index('Câmera:'.decode('utf8'))
		elif element == 'Palavras-chave:'.decode('utf8'):
			keyword_index = elementList.index('Palavras-chave:'.decode('utf8'))
		else:
			continue
	
	if CreateDate_index == None:
		print "No date listed"
		results.append('nd*')
	else:
		if elementList[CreateDate_index+1] == 'Nome do arquivo:'.decode('utf8'):
			print "No date listed"
			results.append('nd*')
		else:
			CreateDate = elementList[CreateDate_index+1]
			results.append(CreateDate + '*')
	
	if creator_index == None:
		print "No photagrapher listed"
		results.append('nd*')
	else:
		if elementList[creator_index+1] == 'Formato:'.decode('utf8'):
			print "No photagrapher listed"
			results.append('nd*')
		else:
			creator = elementList[creator_index+1]
			results.append(creator + '*')
	
	if format_index == None:
		print "No format listed"
		results.append('nd*')
	else:
		if elementList[format_index+1] == 'Tamanho:'.decode('utf8'):
			print "No format listed"
			results.append('nd*')
		else:
			format = elementList[format_index+1]
			results.append(format + '*')
			
	if camera_index == None:
		print "No camera listed"
		results.append('nd*')
	else:
		if elementList[camera_index+1] == 'Palavras-chave:'.decode('utf8'):
			print "No camera listed"
			results.append('nd*')
		else:
			camera = elementList[camera_index+1]
			results.append(camera + '*')
			
	if keyword_index == None:
		print "No keywords listed"
		results.append('nd*')
	else:
		keyword = elementList[keyword_index+1]
		results.append(keyword + '*')

	row = "".join(results)					
	print row + '\n'
	return row

out_file.write("Language\tName\tCreateDate\tCreator\tFormat\tCamera\tFurther Information URL\taccess URL\tKeywords\n")
for url in in_file:
	results = []
	data = metadata_table(*wikipeixes_image_text(url))
	if len(data) > 1:
		FIurl = url.strip('\?id=galeria\n')
		accessuri = re.sub('_detail', '_media', FIurl)
		remove = re.sub('\*','\t',data)
		out_file.write(remove.encode('utf8') + FIurl + '\t' + accessuri + '\n')
out_file.close()