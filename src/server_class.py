#!bin/usr/env python3

import socket
import queue
import threading
import struct

#Class for TCP/IP server 

class Server():
    def __init__(self):

        self.msgQueue = queue.Queue() #Threadsafe message queue

        s = socket.socket() #Creating new socket
        port, name = 12345, "nimi"    # configuration.configurator()
        host = socket.gethostname() #
        s.bind((host, port)) #Binding host to port

        self.clients = [] #Creating a list containing client addresses
        self.threads = [] #Creating a list containing threads
        
        self.main_loop(s)
    def main_loop(self, s):
        s.listen(5)
        while True:

            c, addr =  s.accept()  #Accepting new connection 
            self.clients.append(c)  

            #Starting new listener thread
            t = threading.Thread(target=self.receive(c))
            t.daemon= True
            self.threads.append(t)
            t.start()

            # Sending message to all the clients
            if self.msgQueue.qsize() > 0:

                for i in range(self.msgQueue.qsize()):

                    client, msg = self.msgQueue.get() 

                    for c in self.clients:
                        if (c != client):
                            send_message(msg, c) 
                        else:
                            continue
                    self.msgQueue.task_done()

    def send_message (self, message, target):
        #This function is responsible for sending one message to a client
        msg = message.encode() 
        length = len(msg)
    
        blength = struct.pack("I", length) 
 
        sent = 0
        target.send(blength)

        while (sent<length):
            #Sending string until everything is sent
            sent = target.send(msg[sent:]) 



    def receive (self, c):
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
                self.msgQueue.put(message) #Add msg to queue 
            else:
                clients.remove(c)
                c.close
                return
            
