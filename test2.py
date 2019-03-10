# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 23:06:39 2018
@author: Abhik Banerjee
This .py code gives out the GUI for Stegnography.
"""
import tkinter as tk
from tkinter import ttk
from tkinter import IntVar ,DISABLED ,NORMAL ,filedialog
import datetime
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
        This application is a Mini Britannica Quiz. You will be given 10 Question and 40 minutes to solve them.
        """
        message3="""
        """
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
        
        self.controller=controller
       
        self.controller.after(datetime.timedelta(seconds=40*60).seconds*1000,lambda: self.root.destroy())
        
        button1=ttk.Button(self,text="Hide     ->",command=lambda:self.clock_start())
        button1.pack(pady=10,anchor="center")
        button2=ttk.Button(self,text="Retrieve ->",command=lambda:print("Button 2 Pressed"))
        button2.pack(pady=10,anchor="center")
        button4=ttk.Button(self,text="<-Go Back to Intro",command=lambda:controller.showFrame(IntroPage))
        button4.pack(pady=10,anchor="center")
        button3=ttk.Button(self,text="Quit",command=controller.destroy)
        button3.pack(pady=10,anchor="center")
    def clock_start(self):
        self.done_time=datetime.datetime.now() + datetime.timedelta(seconds=40*60) # half hour
        self.label = tk.Label(text="")
        self.label.pack(fill="y")
        self.update_clock()
        
    def update_clock(self):
        elapsed = self.done_time - datetime.datetime.now()
        print(elapsed.seconds)
        #h,m,s= elapsed.seconds/3600,elapsed.seconds/60,elapsed.seconds%60   
        h,m=0,0
        e=elapsed.seconds
        while(e>3600):
            h+=1
            e-=3600
        while(e>60):
            m+=1
            e-=60
        self.label.configure(text="Time Left:%02d:%02d:%02d"%(h,m,e))
        self.controller.after(1000, self.update_clock)

inst=SimpleEncrypt()
inst.mainloop()