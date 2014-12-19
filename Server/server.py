#!usr/bin/env python3

import socket
import configuration

#Configuring initial parametres

s = socket.socket() #Creating new socket
port, name = configuration.configurator()
host = socket.gethostname() #
s.bind((host, port)) #Binding host to port

clients = [] #Creating a list containing client's addresses


s.listen(5)
while True:
    clients.append(s.accept()) #Accepting new connection 
    print("New connection from ", clients[clients.len()])
    clients[clients.len()].send = bytes("Welcome to "+ name) #Encode our welcome message
     
