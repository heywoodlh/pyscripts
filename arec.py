#!/usr/bin/python
#Python script to search a records

import sys
import socket

for hosts in sys.argv[1:]:
	print(socket.gethostbyname(hosts))
