"""RFC Search
Author: Samuel DeLaughter
License: MIT
Last Updated: 12/12/16
Maintained at: https://github.com/sdelaughter/rfc_search

Search the full text of (previously downloaded) IETF RFCs for a given string.
Print the matching lines and/or line numbers from each document.

RFCs can be downloaded in bulk from https://www.rfc-editor.org/retrieve/bulk/

Use the -s/--string paramater to specify which string to search for
	This is mandatory, if left out the program will print an error message and exit.
	If your string contains multiple words, wrap it in double quotes.
	Currently no support is provided for more complicated regex searches.
	No guarantees can be made for input with non alpha-numeric characters.
Use the -m/--min option to specify a lower bound on the RFC numbers to be searched.
Use the -M/--max option to specify an upper bound on the RFC numbers to be searched.
Set the -d/--display flag to print the matching lines in their entirety in addition to line numbers.
	Without this flag, only the numbers of matching lines will be printed
Set the -v/--verbose flag to give progress indication by printing a statement as each file in the foler is checked or skipped
Set the -V/--version flag to print the version number and exit

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
