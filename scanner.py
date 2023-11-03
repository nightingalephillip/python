#!/bin/python

import sys
import socket
from datetime import datetime

#Define our target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4
else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py <ip>")
	
#Add banner
print("*" * 50)
print("Scanning target " + target)
print("Time started: " + str(datetime.now()))
print("*" * 50)

try:
	for port in range(1, 1000):		# port in range 1 - 1000
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # connect to ipv4 and port
		socket.setdefaulttimeout(1)	# when make connection, timeout 1 sec
		result = s.connect_ex((target, port)) # connect to target and port, returns an error indicator if open
		# print("checking port {}".format(port))
		if result == 0:
			print("Port {} is open".format(port))
		s.close()								# loop until 85
		
		
except KeyboardInterrupt:			#ctrl+C exit
	print("\nExiting program.")
	sys.exit()
	
except socket.gaierror:					#no host name resolution, exit
	print("Hostname could not be resolved.")
	sys.exit()
	
except socket.error:					#no host, exit
	print("Couldn't connect to server.")		
	sys.exit()
