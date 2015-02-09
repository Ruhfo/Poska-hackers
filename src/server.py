#!bin/usr/env python3

import socket
import struct
import threading
import queue
from networking_class import Networker

#Constants
MAX_CLIENTS = 5

class Server(Networker):
    def __init__():
        #Creating new socket  
        s = socket.socket() #Creating new socket
        port, name = 12345, "nimi"    # configuration.configurator()
        host = socket.gethostname() #
        s.bind((host, port)) #Binding host to port

        self.clients = [] #Creating a list containing client addresses
        self.threads = [] #Creating a list containing threads
        
        super()
    def main_loop():
        s.listen(MAX_CLIENTS)
        while True:
            #Accepting new connection
            c, addr =  s.accept()  
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

