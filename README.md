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
