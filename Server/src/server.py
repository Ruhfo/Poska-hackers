#!usr/bin/env python3

import socket
import configuration
import queue
import threading
import struct

DEFAULT_LENGTH = 2048

def receive (c):
#Function responsible for listening to one client
    while True:

        length = c.recv(4)

        if (len(length) > 0): #Aquiring message length

            length = struct.unpack("I", length) 

            
            chunks = []
            msgLength = 0
            msg = ""
 
            while (msgLength<length):
                chunk = c.recv(min(length-msgLength, DEFAULT_LENGTH))
                chunks.append(chunk)
                msgLength += len(chunk)
            
            for item in chunks:
                msg+=item.decode()
             
            message = (c , msg)
            msgQueue.put(message) #Add msg to queue 
            print("Message: ", msg.decode())
        else:
            print("Client has disconnected") 
            clients.remove(c)
            c.close
            return

def sendMessage (message, client):
#This function is responsible for sending one message to a client
    msg = message.encode() 
    length = len(msg)
    
    blength = struct.pack("I", length) 
 
    sent = 0
    client.send(blength)

    while (sent<length):
        #Sending string until everything is sent
        sent = client.send(msg[sent:]) 

#Configuring initial parametres
msgQueue = queue.Queue()

s = socket.socket() #Creating new socket
port, name = 12345, "nimi"    # configuration.configurator()
host = socket.gethostname() #
s.bind((host, port)) #Binding host to port

clients = [] #Creating a list containing client's addresses
threads = [] #Creating a list containing threads 

s.listen(5)
while True:

    c, addr =  s.accept()  #Accepting new connection 
   
    clients.append(c)  
   
    print("New connection from ", addr, "Type", type(c) )
    message = "Welcome to "+name
    
    sendMessage(message, c)
#Starting new listener thread
    t = threading.Thread(target=receive(c))
    t.daemon= True
    threads.append(t)
    t.start()

# Sending message to all the clients
    if msgQueue.qsize() > 0:

        for i in range(msgQueue.qsize()):

            client, msg = msgQueue.get() 

            for c in clients:
                if (c != client):
                   sendMessage(msg, c) 
                else:
                    continue
            msgQueue.task_done()
