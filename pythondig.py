#Python script to search a records
import sys
import socket
import dns.resolver
import os
import urllib2

#Check network connection
def internet_on():
    try:
        urllib2.urlopen('http://google.com', timeout=1)
        return True
    except urllib2.URLError as err: 
        return False

if not internet_on():
	print("Unable to connect to network")
	quit()

#ARGUMENTS SECTION

#help 
if sys.argv[1].lower() == "help":
	print(" ")
	print("Arguments: [A, NS, TXT, MX, CNAME")
	print(" ")
	print("Usage: 'python pythondig.py [A, NS, TXT, MX, CNAME] google.com facebook.com'")
	print(" ") 
	print("Example: 'python pythondig.py A google.com facebook.com'")
	quit()

#NS 
if sys.argv[1].upper() == "NS":
	myResolver = dns.resolver.Resolver()
	for hosts in sys.argv[2:]:
		resolved_hosts = myResolver.query(hosts, "NS")
	for rdata in resolved_hosts:
		print(rdata)
	quit()
		
#MX
if sys.argv[1].upper() == "MX":
        myResolver = dns.resolver.Resolver()
        for hosts in sys.argv[2:]:
                resolved_hosts = myResolver.query(hosts, "MX")
        for rdata in resolved_hosts:
                print(rdata)
        quit()

#A
if sys.argv[1].upper() == "A":
	for hosts in sys.argv[2:]:
		print(socket.gethostbyname(hosts))
	quit()

#TXT
if sys.argv[1].upper() == "TXT":
        myResolver = dns.resolver.Resolver()
        for hosts in sys.argv[2:]:
                resolved_hosts = myResolver.query(hosts, "TXT")
        for rdata in resolved_hosts:
                print(rdata)
        quit()

#CNAME
if sys.argv[1].upper() == "CNAME":
        myResolver = dns.resolver.Resolver()
        for hosts in sys.argv[2:]:
                resolved_hosts = myResolver.query(hosts, "CNAME")
        for rdata in resolved_hosts:
                print(rdata)
        quit()
