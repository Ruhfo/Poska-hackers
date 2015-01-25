#!bin/usr/env python3

import tkinter as tk
import threading

class Applet ():
#Class for GUI components
    def __init__(self):

        self.parrent = tk.Tk()
        self.parrent.wm_title("a Very shity Messenger")

        #Frame that includes only widgets that show data
        self.infoFrame = tk.Frame(self.parrent)
        self.infoFrame.pack(side = tk.TOP, fill = tk.BOTH, expand = True)
        
        #Frame that includes only widgets that interact with user
        self.inputFrame = tk.Frame(self.parrent)
        self.inputFrame.pack(side = tk.BOTTOM, fill=tk.BOTH, expand = True)
        
        #Widget scrollbar
        self.scrollbar = tk.Scrollbar(self.infoFrame)
        self.scrollbar.pack(side = tk.RIGHT, expand=True,fill=tk.Y)

        #Widget showing text
        self.feed = tk.Text(self.infoFrame, yscrollcommand=self.scrollbar,
                            wrap=tk.WORD, state=tk.DISABLED)
        self.feed.pack(side = tk.LEFT, expand = True, fill = tk.BOTH) 
        
        #Widget for getting user's messages 
        self.usrInput = tk.Entry(self.inputFrame)
        self.usrInput.pack(side =tk.LEFT, fill = tk.X, expand = True)
        
        #Send button 
        self.sendButton = tk.Button(self.inputFrame, height = 1, text = "Send",
                                    command = lambda: self.send_input)
        self.sendButton.pack(side = tk.RIGHT)

        #Key commands:
        self.usrInput.bind("<Return>", self.event_handler)
        
        #Starting event listener mainloop
        self.parrent.mainloop()

    def event_handler (self,event):
        #Function for handling different events
        if (event.type == "2"): #if key press event
            if (event.keysym == "Return"):
                self.send_input()

    def send_input(self):
        #Function for sending user input
        msg = self.usrInput.get()
        self.receive_message(msg+"\n")
        self.usrInput.delete(first=0,last=tk.END)

    def receive_message(self, message):
        #function for displaying incoming messages
        self.feed.configure(state=tk.NORMAL)
        self.feed.insert(tk.INSERT,message)
        self.feed.configure(state=tk.DISABLED)

