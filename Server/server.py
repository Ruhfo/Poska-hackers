#!usr/bin/env python3
import configparser
import socket

def write_config():
    config = configparser.ConfigParser()
    config["DEFAULT"] ={"PORT"  : 12345,
                        "NAME"  : "Default chat server"
                       }
    with open("config.ini", "w") as configfile:
        config.write(configfile)

def read_config(configfile):
    config = configparser.ConfigParser()
    config.read("config.ini")
    
    global port
    global name

    default = config["DEFAULT"]

    port = default.get("PORT","12345")
    name = default.get("NAME", "Default chat server")
    
    port = int(port) #Converting str to int

#Opening configuration file

try:
    config = open("config.ini", "r")
except IOError:
    print("File doesn't exist")
    write_config()
else:
    read_config(config)

#Setting up initial server
s = socket.socket() #Creating new socket
#We already have port
#We already have server name
host = socket.gethostname() #
s.bind((host, port)) #Binding host to port

clients = [] #Creating a list containing client's addresses


s.listen(5)
while True:
    clients.append(s.accept()) #Accepting new connection 
    print("New connection from ", clients[clients.len()])
    clients[clients.len()].send = bytes("Welcome to "+ name) #Encode our welcome message
     
