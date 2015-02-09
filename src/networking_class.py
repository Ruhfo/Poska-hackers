#!bin/usr/env python3

import socket
import struct
import threading
import queue

class Networker():
    def __init__(self, port, name):
        #Initializing msgQueue and main loop
        self.msgQueue = queue.Queue() #Threadsafe message queue
        main_loop()
    def main_loop(self):
        pass
    def send_message (self, message, target):
        #This function is responsible for sending one message to a client
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
                    msg+=item
                
                message = (c , msg)
                self.msgQueue.put(message) #Add msg to queue 
            else:
                clients.remove(c)
                c.close
                return
