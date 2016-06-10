#!/usr/bin/python

import socket


# Create client socket and connect to the port 8000
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.connect(("0.0.0.0", 8000))

# Receive data from the server
data = s1.recv(2048)
print data

# Send data to the server
s1.send("hello from client")

# Close the socket
s1.close()
