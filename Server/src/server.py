#!usr/bin/env python3

import socket
import configuration
import queue
import threading

DEFAULT_LENGTH = 255

def receive (c):
#Function responsible for listening to one client
    while True:
        length = c.recv(1)
        if (len(length) > 0):
            length = length.decode()
            if (type(length) == int):
                length = int(length)
            else:
                length = DEFAULT_LENGTH
            msg = c.recv(length) #aquiring message itself
            
            while (len(msg)<length):
                msg += c.recv(length-len(msg))
        
            message = (c , msg)
            msgQueue.put(message) #Add msg to queue 
            print("Message: ", msg.decode())
        else:
            print("Client has disconnected") 
            clients.remove(c)
            c.close
            return

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
    msg = message.encode() 
    
    c.send(msg)

    t = threading.Thread(target=receive(c))
    t.daemon= True
    threads.append(t)
    t.start()

    if msgQueue.qsize() > 0:

        for i in range(msgQueue.qsize()):

            client, msg = msgQueue.get() 

            for c in clients:
                if (c != client):
                    c.send(msg)
                else:
                    continue
            msgQueue.task_done()
