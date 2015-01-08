#!/usr/bin/env python3

import socket
import struct

DEFAULT_LENGTH = 2048

def receive_message(sock):
    #This function is responsible for receiving and decoding messages sent by server
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

def send_message(sock, message):
    #This function is responsible for sending messages to server
    msg = message.encode()
    length = len(msg)
    
    blength = struct.pack("I", length)

    sent = 0
    client.send(blength)

    while(sent<length):
        #Send parts of string until everything is sent
        sent= client.send(msg[sent:])
    
s = socket.socket()
host = socket.gethostname()
port = 12345

s.connect((host, port))
receive_message(s)
s.close
