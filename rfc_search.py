"""RFC Search
Author: Samuel DeLaughter
License: MIT
Last Updated: 12/12/16

Search the full text of (previously downloaded) IETF RFCs for a given string
Print the line numbers of all matches

Maintained at https://github.com/sdelaughter/rfc_search

"""

__version__ = "1.2"


import os
import sys
import argparse
from pprint import pprint


parser = argparse.ArgumentParser(description = 'RFC Search')
parser.add_argument('-d', '--display', action='store_true', default=False, dest='display', help='Print the actual lines as well as their line numbers')
parser.add_argument('-m', '--min', action='store', default=False, dest='min', help='Lowest-numbered RFC to check')
parser.add_argument('-M', '--max', action='store', default=False, dest='max', help='Highest-numbered RFC to check')
parser.add_argument('-s', '--string', action='store', default=False, dest='string', help='The string to search for')
parser.add_argument('-v', '--verbose', action='store_true', default=False, dest='verbose', help='Run in verbose mode')
parser.add_argument('-V', '--version', action='version', version=__version__, help='Print version number and exit')
args = parser.parse_args()


def main():
	if not args.string:
		print ('Please supply a string to search for using the -s / --string option')
		sys.exit()
	else:
		search_string = args.string.strip('"')
	
	hits = {}
	for filename in os.listdir('.'):
		try:
			rfc_num = filename.split('.txt')[0]
			rfc_num = rfc_num.split('rfc')[1]
			rfc_num = int(rfc_num)
			if(args.min and (rfc_num < int(args.min))):
				if args.verbose:
					print 'Skipping RFC below minimum threshold of ' + str(args.min) + ': ' + str(rfc_num)
				continue
			if(args.max and (rfc_num > int(args.max))):
				if args.verbose:
					print 'Skipping RFC above maximum threshold of ' + str(args.max) + ': ' + str(rfc_num)
				continue
			if args.verbose:
				print 'Checking RFC ' + str(rfc_num)
		except:
			if args.verbose:
				print 'Skipping non-numeric RFC: ' + str(filename)
			continue
		line_number = 0
		for line in open(filename, 'r'):
			line_number += 1
			if search_string in line:
				if rfc_num not in hits:
					if args.display:
						hits[rfc_num] = ['Line ' + str(line_number) + ': ' + str(line)]
					else:
						hits[rfc_num] = [line_number]
				else:
					if args.display:
						hits[rfc_num].append('Line ' + str(line_number) + ': ' + str(line))
					else:
						hits[rfc_num].append(line_number)
					
	if len(hits) > 0:				
		pprint(hits)
	else:
		print('No results found')


if __name__ == "__main__":
	main()
