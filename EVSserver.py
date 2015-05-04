#!/usr/bin/python          
# This is server.py file

import socket              


s = socket.socket()         # Create a socket object
host = '192.168.50.179'        # IP address
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.

print host, port
c, addr = s.accept()        # Establish connection with client.
print "Connected"

appliance={	"lights on":"corresponding command 1",
			"lights off":"corresponding command 2",
			"fan on":"corresponding command 3",
			"fan off":"corresponding command 4"}

while True:
	try:
		user_wish = c.recv(10240)
		if user_wish in appliance:
			print user_wish
			print appliance[user_wish]
			c.send("done")
		else:
			print "appliance not found"
			c.send("appliance not found")

	except:
		c.close
		print "Disconnected"
		c, addr = s.accept()
		print "Connected"

	
