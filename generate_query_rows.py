#!/usr/bin/env python
# coding: utf-8

out_file_name = "query_rows_150000.txt"
out_file = open(out_file_name, 'w')

count = 1

while count < 150000:
	out_file.write(str(count) + '\n')
	count = count + 100