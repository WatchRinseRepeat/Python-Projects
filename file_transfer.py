import tkinter as tk
from tkinter import *
import tkinter.filedialog

import os
import shutil
import datetime 
from datetime import timedelta  #This will allow comparing time stamps
#from datetime import datetime


#Setup the GUI window
class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self)
        #set title of window
        self.master.title('File Transfer')
        #Create button to select files from source directory
        self.sourceDir_btn = Button(text='Select Source', width=20, command=self.sourceDir)
        #Position the button
        self.sourceDir_btn.grid(row=0, column=0, padx=(20,10), pady=(30,0))
        #Creates entry for source directory selection
        self.source_dir = Entry(width=75)
        #position the entry in GUI, padx and pady are used to line
        #up the button and the entry
        self.source_dir.grid(row=0,column=1, columnspan=2, padx=(20,10), pady=(30,0))

        #Create button to select files from source directory
        self.destDir_btn = Button(text='Select Destination', width=20, command=self.destDir)
        #Position the button
        self.destDir_btn.grid(row=1, column=0, padx=(20,10), pady=(15,10))
        #Creates entry for desitnation directory selection
        self.destination_dir = Entry(width=75)
        #position the entry in GUI, padx and pady are used to line
        #up the button and the entry
        self.destination_dir.grid(row=1,column=1, columnspan=2, padx=(20,10), pady=(15,10))

        #Creates the button to transfer files
        self.transfer_btn = Button(text="Transfer Files", width = 20, command = self.transferFiles)
        #Positions transfer files button
        self.transfer_btn.grid(row=2, column=1, padx=(200, 0), pady=(0,15))

        #Create an exit button
        self.exit_btn = Button(text='Exit', width = 20, command = self.exit_program)
        #positions the exit button
        self.exit_btn.grid(row=2,column=2,padx = (10,40), pady=(0,15))

    #Create function to select the source destination
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        #THe .delete(0,END) will clear the content that is inserted in the Entry Widget
        #this allows the path to be inserted into the Entry widget properly
        self.source_dir.delete(0,END)
        #The .insert method will insert the user selection to the source_dir Entry
        self.source_dir.insert(0, selectSourceDir)

    def destDir(self):
        selectDestDir = tkinter.filedialog.askdirectory()
        #THe .delete(0,END) will clear the content that is inserted in the Entry Widget
        #this allows the path to be inserted into the Entry widget properly
        self.destination_dir.delete(0,END)
        #The .insert method will insert the user selection to the source_dir Entry
        self.destination_dir.insert(0, selectDestDir)

    def transferFiles(self):
        #Gets source directory
        source = self.source_dir.get()
        #Gets destination directory
        destination = self.destination_dir.get()
        #Gets a list of files in the source directory
        source_files = os.listdir(source)
        #Runs through each file in the source directory
        for i in source_files:
            #moves each file from the source to the destination
            if self.isRecent(source + '/' + i): #check if the modified date was recent enough
                shutil.move(source + '/' + i, destination)
                print( i + ' was successfully transferred.')
            else:
                print(i + ' was too old to move')

    def exit_program(self):
        #root is the main GUI window, the Tkinter destroy method
        #tells python to terminate root.mainloop and all widgets inside the GUI window
        root.destroy()
    
    def isRecent(self,filepath):
        #get the current time
        ctime = datetime.datetime.now()
        #get file modified time
        mtime = os.path.getmtime(filepath)
        #make mtime a datetime object
        mtime = datetime.datetime.fromtimestamp(mtime)
        #get difference between them
        dtime = ctime - mtime
        #set limit of 1 day
        limit = timedelta(days=1)
        if dtime < limit: #is the difference in time less than 1 day?
            return True
        else:
            return False




if __name__ == '__main__':
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
