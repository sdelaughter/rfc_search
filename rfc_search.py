import os
import sys

from pprint import pprint

search_string = sys.argv[1].strip('"')

hits = {}
for filename in os.listdir('.'):
	try:
		rfc_num = filename.split('.txt')[0]
		rfc_num = rfc_num.split('rfc')[1]
		rfc_num = int(rfc_num)
		print 'Checking RFC ' + str(rfc_num)
	except:
		print 'Skipping non-numeric rfc: ' + str(filename)
		continue
	lines = []
	for line in open(filename, 'r'):
		lines.append(line)
	for l in range(len(lines)):
		if search_string in lines[l]:
			if rfc_num not in hits:
				hits[rfc_num] = [l]
			else:
				hits[rfc_num].append(l)
				
pprint(hits)
