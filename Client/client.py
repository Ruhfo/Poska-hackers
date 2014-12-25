#!/usr/bin/env python3

import socket
import struct

DEFAULT_LENGTH = 2048
def receive_message(sock):
    blength  = sock.recv(4)
    
    if (len(blength) > 0): 
       blength = struct.unpack("I", blength)
       length = blength[0]       

       print("Length: ", length)         
       print("BLength: ", blength)         
 
       chunks = []
       msgLength = 0
       msg = ""
       
       while (msgLength<length):
           chunk = sock.recv(min(length-msgLength, DEFAULT_LENGTH))
           chunks.append(chunk)
           msgLength+=len(chunk)

       for item in chunks:
           msg+=item.decode()

       print(msg) 

    else:
        print("We have lost connection with the server")
        sock.close   
        return
 
s = socket.socket()
host = socket.gethostname()
port = 12345

s.connect((host, port))
receive_message(s)
s.close
