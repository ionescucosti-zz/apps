# create a new socket able to handle connection-oriented transmissions based on TCP;
# connect the socket to the HTTP server of a given address;
# send a request to the server (the server wants to know what we want from it)
# receive the server's response (it will contain the requested root document of the site)
# close the socket (end the connection)

import socket

#creating a socket
server_addr = input("What server do you want to connect to? ") #www.pythoninstitute.org
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connecting to a server
sock.connect((server_addr, 80))

#The GET method
'''
GET / HTTP/1.1\r\n
Host: www.site.com\r\n
Connection: close\r\n
\r\n
'''
#Requesting a document from a server
sock.send(b"GET / HTTP/1.1\r\nHost: " +
          bytes(server_addr, "utf8") +
          b"\r\nConnection: close\r\n\r\n")
reply = sock.recv(10000)

#Closing the connection
sock.shutdown(socket.SHUT_RDWR)
sock.close()

#server response
print(repr(reply))

# exceptions: socket.gaierror ,getaddrinfo(), 