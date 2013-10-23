#!/usr/bin/env python
# coding: utf-8
from __future__ import division
import urllib
from bs4 import BeautifulSoup

"""
This code scrapes the text from the photo gallery to generate a list of all the image
urls at wikipeixes. You will probably have to delete some strange urls from the end of 
the output file.
"""

out_file_name = "wikipiexes_photo_url.txt"
out_file = open(out_file_name, 'w')

web_page = urllib.urlopen("http://wikipeixes.com.br/galeria").read()
soup = BeautifulSoup(web_page)
counter = 0
for link in soup.find_all('a'):
	counter = counter + 1
	if counter > 20:
		out_file.write("http://wikipeixes.com.br" + link.get('href') + "\n")

out_file.close()
