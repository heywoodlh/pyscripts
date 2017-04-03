#Python script to search a records
import sys
import socket
import dns.resolver
import os
import urllib2

#and then check the response...
def internet_on():
    try:
        urllib2.urlopen('http://google.com', timeout=1)
        return True
    except urllib2.URLError as err: 
        return False

if not internet_on():
	print("Unable to connect to network")
	quit()

def error_code():
	print("Error. Unable to complete")
	quit()

if sys.argv[1].lower() == "help":
	print(" ")
	print("Arguments: [A, NS]")
	print(" ")
	print("Usage: 'python pythondig.py [A, NS] google.com facebook.com'")
	print(" ") 
	print("Example: 'python pythondig.py A google.com facebook.com'")
	quit()

if sys.argv[1].upper() == "NS":
	myResolver = dns.resolver.Resolver()
	for hosts in sys.argv[2:]:
		resolved_hosts = myResolver.query(hosts, "NS")
	for rdata in resolved_hosts:
		print(rdata)
	quit()
else:
	error_code()
		

if sys.argv[1].upper() == "MX":
        myResolver = dns.resolver.Resolver()
        for hosts in sys.argv[2:]:
                resolved_hosts = myResolver.query(hosts, "MX")
        for rdata in resolved_hosts:
                print(rdata)
        quit()
else:
	error_code()


if sys.argv[1].upper() == "A":
	for hosts in sys.argv[2:]:
		print(socket.gethostbyname(hosts))
	quit()
else:
	error_code()
