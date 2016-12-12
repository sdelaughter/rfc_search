# RFC Search
Search the full text of IETF RFCs to find occurances of a given string

This script requires you to download the RFCs you want to search in advance.
You can download the entire collection (currently ~175MB) or 500-RFC chunks from this site:
https://www.rfc-editor.org/retrieve/bulk/

It shouldn't take more than a minute or two to search all 8000+ files, so you might as well get them all.

Be sure to get the .txt versions, not .pdf

Once you've acquired the documents you'd like to search, place rfc_search.py in the folder containing them.
cd to that folder, and run:

    python rfc_search.py "search string"
 
Where "search string" is the word or phrase you're looking for.

It will print the matching lines and/or line numbers for all relevant RFCs along with their RFC numbers


###Parameters
####Use the -s/--string paramater to specify which string to search for
	#####This is mandatory, if left out the program will print an error message and exit.
	#####If your string contains multiple words, wrap it in double quotes.
	#####Currently no support is provided for more complicated regex searches.
	#####No guarantees can be made for input with non alpha-numeric characters.
####Use the -m/--min option to specify a lower bound on the RFC numbers to be searched.
####Use the -M/--max option to specify an upper bound on the RFC numbers to be searched.
####Set the -d/--display flag to print the matching lines in their entirety in addition to line numbers.
	#####Without this flag, only the numbers of matching lines will be printed
####Set the -v/--verbose flag to give progress indication by printing a statement as each file in the foler is checked or skipped
####Set the -V/--version flag to print the version number and exit
