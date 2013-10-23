#!/usr/bin/env python
# coding: utf-8
from __future__ import division
import urllib, re
from bs4 import BeautifulSoup

"""
This code scrapes the text from a web page at wikipeixes and exports it as a tab
delimited file. It consists of two functions: wikipeixes_text and metadata_table. 
wikipeixes_text takes the url and uses Beautiful Soup to scrape the page. It returns the 
cleaned text scraped from the page and the language code. metadata_table takes the clean 
text and the language code from wikipeixes_text. The clean text is partitioned into the 
appropriate content parts and placed in one row per web page. metadata_table returns the 
row of data which is then added to the final tab-delimited table. Be sure 
wikipiexes_metadata.txt is empty before you begin.
"""

in_file_name = "wikipiexes_url.txt"
in_file = open(in_file_name, 'r')
out_file_name = "wikipiexes_metadata.txt"
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
	return clean,lang,url

def metadata_table(clean,lang,url):
	if re.search('TOC END.*Links Externos', clean) == None:
		print "No data for this species"
		return results
	else:
		results.append(lang + '*')
		q = re.search('TOC END.*Links Externos', clean)
		print q.group(0)
		part = q.group(0)
		elementList = []
		elementList = part.split('|')
		print elementList
		name = elementList[2] + ' ' + elementList[3]
		results.append(name + '*')
		print name
		results.append(url + '*')
		synonym_index = None
		commonname_index = None
		morphology_index = None
		habitat_index = None
		food_index = None
		behavior_index = None
		reproduction_index = None
		observation_index = None
		geography_index = None
		reference_index = None
		diagnostic_index = None
		for element in elementList:
			if element == 'Sinônimos'.decode('utf8'):
				synonym_index = elementList.index('Sinônimos'.decode('utf8'))
				print synonym_index
			elif element == 'Características diagnósticas'.decode('utf8'):
				diagnostic_index = elementList.index('Características diagnósticas'.decode('utf8'))
				print diagnostic_index
			elif element == 'Nomes populares'.decode('utf8'):
				commonname_index = elementList.index('Nomes populares'.decode('utf8'))
			elif element == 'Características'.decode('utf8'):
				morphology_index = elementList.index('Características'.decode('utf8'))
			elif element == 'Habitat e ecologia'.decode('utf8'):
				habitat_index = elementList.index('Habitat e ecologia'.decode('utf8'))
			elif element == 'Alimentação'.decode('utf8'):
				food_index = elementList.index('Alimentação'.decode('utf8'))
			elif element == 'Comportamento'.decode('utf8'):
				behavior_index = elementList.index('Comportamento'.decode('utf8'))
			elif element == 'Reprodução'.decode('utf8'):
				reproduction_index = elementList.index('Reprodução'.decode('utf8'))
			elif element == 'Observações'.decode('utf8'):
				observation_index = elementList.index('Observações'.decode('utf8'))
			elif element == 'Distribuição geográfica'.decode('utf8'):
				geography_index = elementList.index('Distribuição geográfica'.decode('utf8'))
			else: 
				element == 'Referências'.decode('utf8')
				reference_index = elementList.index('Referências'.decode('utf8'))

		if synonym_index == None:
			print "No synonyms listed"
			results.append('nd*')
		else:
			if elementList[synonym_index+1] == 'Nomes populares'.decode('utf8'):
				print "No synonyms listed"
				results.append('nd*')
			elif elementList[synonym_index+1] == 'Características diagnósticas'.decode('utf8'):
				print "No synonyms listed"
				results.append('nd*')
			elif elementList[synonym_index+1] == 'Nenhum.'.decode('utf8'):
				print "No synonyms listed"
				results.append('nd*')
			else:
				if commonname_index == None:
					part = elementList[synonym_index+1:diagnostic_index]
					print part
					synonym = "_".join(part)
				else:
					part = elementList[synonym_index+1:commonname_index]
					print part
					synonym = "_".join(part)
				results.append(synonym + '*')
		
		if commonname_index == None:
			print "No vernacular names listed"
			results.append('nd*')
		else:
			if elementList[commonname_index+1] == 'Características'.decode('utf8'):
				print "No verncular names listed"
				results.append('nd*')
			else:
				vernacularName = elementList[commonname_index+1]
				results.append(vernacularName + '*')
		
		if morphology_index == None:
			print "No morphological characters listed"
			results.append('nd*')
		else:
			if elementList[morphology_index+1] == 'Principais características morfológicas e de coloração…'.decode('utf8'): 
				print "No morphological characters listed"
				results.append('nd*')
			elif elementList[morphology_index+1] == 'Galeria de fotos da espécie'.decode('utf8'):
				print "No morphological characters listed"
				results.append('nd*')
			else:
				morphology = elementList[morphology_index+1]
				results.append(morphology + '*')
		
		if habitat_index == None:
			print "No habitats listed"
			results.append('nd*')
		else:
			if elementList[habitat_index+1] == 'Observações'.decode('utf8'):
				print "No habitats listed"
				results.append('nd*')
			else:
				habitat = elementList[habitat_index+1]
				results.append(habitat + '*')
		
		if food_index == None:
			print "No food listed"
			results.append('nd*')
		else:
			if elementList[food_index+1] == 'Comportamento'.decode('utf8'):
				print "No food listed"
				results.append('nd*')
			else:
				food = elementList[food_index+1]
				results.append(food + '*')
		
		if behavior_index == None:
			print "No behavior listed"
			results.append('nd*')
		else:
			if elementList[behavior_index+1] == 'Reprodução'.decode('utf8'):
				print "No synonyms listed"
				results.append('nd*')
			else:
				behavior = elementList[behavior_index+1]
				results.append(behavior + '*')
		
		if reproduction_index == None:
			print "No reproduction details listed"
			results.append('nd*')
		else:
			if elementList[reproduction_index+1] == 'Observações'.decode('utf8'):
				print "No synonyms listed"
				results.append('nd*')
			else:
				reproduction = elementList[reproduction_index+1]
				results.append(reproduction + '*')
		
		if observation_index == None:
			print "No observations listed"
			results.append('nd*')
		else:
			if elementList[observation_index+1] == 'Distribuição geográfica'.decode('utf8'):
				print "No observations listed"
				results.append('nd*')
			else:
				observations = elementList[observation_index+1]
				results.append(observations + '*')
		
		if geography_index == None:
			print "No geography listed"
			results.append('nd*')
		else:
			if elementList[geography_index+1] == 'Referências'.decode('utf8'):
				print "No geography listed"
				results.append('nd*')
			else:
				geography = elementList[geography_index+1]
				results.append(geography + '*')
		
		if diagnostic_index == None:
			print "No diagnostic characters listed"
			results.append('nd*')
		else:
			if elementList[diagnostic_index+1] == 'Composição'.decode('utf8'):
				print "No diagnostic characters listed"
				results.append('nd*')
			else:
				diag_text = elementList[diagnostic_index+1:elementList.index('Composição'.decode('utf8'))]
				print diag_text
				diagnostic = " ".join(diag_text)
				results.append(diagnostic + '*')
		
		if reference_index == None:
			print "No references listed 1"
			results.append('nd')
		else:
			if elementList[reference_index+1] == 'Autor, AB; Autor CD & Autor EF. 2000.'.decode('utf8'):
				print "No references listed 2"
				results.append('nd')
			elif elementList[reference_index+1] == 'Links Externos'.decode('utf8'):
				print "No references listed 2"
				results.append('nd')
			else:
				reference_text = elementList[reference_index+1:elementList.index('Links Externos'.decode('utf8'))]
				reference = " ".join(reference_text)
				results.append(reference)
	
	row = "".join(results)					
	print row
	return row

out_file.write("Language\tName\tURL\tSynonyms\tVernacular Names\tMorphology\tHabitat\tFeeding\tBehavior\tReproduction\tObservations\tGeographical Distribution\tDiagnostic Characters\tReferences\n")
for url in in_file:
	results = []
	data = metadata_table(*wikipeixes_text(url))
	print data
	if len(data) > 1:
		remove = re.sub('\*','\t',data)
		out_file.write(remove.encode('utf8') + '\n')
out_file.close()
