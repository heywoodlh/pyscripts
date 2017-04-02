#!/usr/bin/python
#Python script to search a records

import sys
import socket

host1 = sys.argv[1]
addr1 = socket.gethostbyname(host1)

print(addr1)
