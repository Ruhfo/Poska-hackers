#!usr/bin/env python3

import socket
import configuration

#Configuring initial parametres

s = socket.socket() #Creating new socket
port, name = 12345, "nimi"    # configuration.configurator()
host = socket.gethostname() #
s.bind((host, port)) #Binding host to port

clients = [] #Creating a list containing client's addresses


s.listen(5)
while True:
   # clients.append(s.accept()) #Accepting new connection 
    c, addr =  s.accept()      # clients[len(clients)-1]

    print("New connection from ", addr )
    c.send(b'UTF-8') #Encode our welcome message
    c.close
