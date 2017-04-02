#Python script to search a records
import sys
import socket
import dns.resolver

if sys.argv[1].upper() == "NS":
	myResolver = dns.resolver.Resolver()
	for hosts in sys.argv[2:]:
		resolved_hosts = myResolver.query(hosts, "NS")
	for rdata in resolved_hosts:
		print(rdata)
	quit()		

if sys.argv[1].upper() == "A":
	for hosts in sys.argv[2:]:
		print(socket.gethostbyname(hosts))
	quit()
