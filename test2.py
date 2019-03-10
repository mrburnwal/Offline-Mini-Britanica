# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 23:06:39 2018
@author: Abhik Banerjee
This .py code gives out the GUI for Stegnography.
"""
import tkinter as tk
from tkinter import ttk
from tkinter import IntVar ,DISABLED ,NORMAL ,filedialog

"""
The Main Controller.
"""
class SimpleEncrypt(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self)
        container=tk.Frame(self)
        self.title("Steg101 v1.10")
        
        container.pack(side="top",fill="both",expand="True")
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        self.frames={}
        for x in (IntroPage,StartPage):
            frame=x(container,self)
            self.frames[x]=frame
            frame.grid(row=0,column=0,sticky="nsew")
            
        self.showFrame(IntroPage)
    def showFrame(self,cont):
        frame=self.frames[cont]
        frame.tkraise()   
    def showError(self,mess):
        tk.Label(self,text=mess).pack()
        
class IntroPage(tk.Frame):
    def __init__(self,parent,controller):
        ttk.Frame.__init__(self,parent)
        message1="""This is a test Application. Please Read the Introduction if
                        you are a first-timer. 
        """
        message2="""
        This application is made for basic Stenography. Assuming you know what that is,
        we shall skip it. Steg101 hides your message or text from a file into another file
        without affecting the target file's quality. Right now it can only use Pictures for hiding.
        
        Please note that it is recommended to not use a file multiple times to hide messages many 
        messages simultanousely in multiple goes. That being said, you should know that the hide 
        option will be disabled once a file is successfully used.
        To hide a message again, you need to restart the application."""
        message3="""
        Final Note: Please Enter the correct file locations and names in correct format.
        Use "\\\\" or "/" and not "\\" for file path."""
        message4="""Warning: The Makers would not be held responsible for the actions of the User."""
        ttk.Label(self,text=message1,font=("Comic Sans MS",12,'bold')).pack(padx=20,anchor="center")
        ttk.Label(self,text=message2,font=("Helvetica",12)).pack(fill="both",anchor="center")
        ttk.Label(self,text=message3,font=("Verdana",10,"bold")).pack(fill="both",anchor="center")
        ttk.Label(self,text=message4,font=("Times",12,"bold italic underline")).pack(pady=10,anchor="center")
        ttk.Button(self,text="Start",command=lambda:controller.showFrame(StartPage)).pack(padx=10,pady=(0,20),anchor="center")        
"""        
This is the Start Page.
"""       
class StartPage(tk.Frame):
    def __init__(self,parent,controller):
        ttk.Frame.__init__(self,parent)
        label=tk.Label(self,text="Welcome to Steg101\nPlease Select your Action:",font=("Times",14))
        label.pack(pady=(0,10))
        button1=ttk.Button(self,text="Hide     ->",command=lambda:controller.showFrame(IntroPage))
        button1.pack(pady=10,anchor="center")
        button2=ttk.Button(self,text="Retrieve ->",command=lambda:print("Button 2 Pressed"))
        button2.pack(pady=10,anchor="center")
        button4=ttk.Button(self,text="<-Go Back to Intro",command=lambda:controller.showFrame(IntroPage))
        button4.pack(pady=10,anchor="center")
        button3=ttk.Button(self,text="Quit",command=controller.destroy)
        button3.pack(pady=10,anchor="center")
        
inst=SimpleEncrypt()
inst.mainloop()