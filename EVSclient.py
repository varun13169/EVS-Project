#!/usr/bin/python           
# This is client.py file

import time
import socket              

time.sleep(1) 

s = socket.socket()         # Create a socket object
host = '172.16.0.33'        # IP address
port = 12345                # Reserve a port for your service.

s.connect((host, port))


while True:
	wish = raw_input("Please enter <Appliance_Name><space><Mode>\n")
	s.send(wish.lower())
	print s.recv(32)
	print "\n"
