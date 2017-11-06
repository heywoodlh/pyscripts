#!/usr/bin/env python3
import httplib2
import sys
from bs4 import BeautifulSoup, SoupStrainer

try:
	website = sys.argv[1]
	http = httplib2.Http()
	status, response = http.request(website)

	for link in BeautifulSoup(response, "html.parser", parse_only=SoupStrainer('a')):
    		if link.has_attr('href'):
        		print(link['href'])
except IndexError:
	print('syntax: ' + sys.argv[0] + ' http://google.com')
