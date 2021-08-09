#!/bin/python
from tkinter import * 
from tkinter import filedialog, messagebox
import os

def saveAs():
        my_text_info = mytext.get("1.0",END)  
        file = filedialog.askopenfilename(initialdir="/home", title="Save as", filetypes=(("text files", "*.*"), ))
        file = open(file, "w")
        file.write(my_text_info)
        file.close()

#Create new file
def createFile():
        add_file = filedialog.asksaveasfilename(initialdir="/home", title="Create new file", filetypes=(("text file", "*.*"), ))
        add_file = open(add_file, "a")
        add_file.close()


#Open new file
def openFile():
    mytext.delete("1.0", END)
    text = filedialog.askopenfilename(initialdir="/home/", title="open file", filetypes=(("text files", "*.*"), ))
    text = open(text, "r")
    stuff = text.read()
    mytext.insert(END, stuff)
    text.close()    

#Delete files
def deleteFile():
    file = filedialog.askopenfilename(initialdir="/home/", title="delete file", filetypes=(("all files", "*.*"), ))
    os.remove(file)

def alert():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

#Adding root var
root= Tk()
#Define program parameters
root.geometry("520x400")
root.title("EasyWrite(1.1)")
root.resizable(False, False)

#menubar 
menubar = Menu(root, bg="orange", fg="white")
filemenu = Menu(menubar, tearoff=0)

#menubar items
filemenu.add_command(label="New", command=createFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save As", command=saveAs)
filemenu.add_command(label="Delete", command=deleteFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=alert)
menubar.add_cascade(label="File", menu=filemenu )

root.config(menu=menubar)

heading = Label(text="Easy Write", fg="orange",font="Fixedsys 14 bold")
heading.pack()

#Textbox
mytext = Text(root, width=60, height=20)
mytext.place(x=15, y=30)

#About app 
print("Easy Write(1.1)")
print("Developing mode ...")

root.protocol("WM_DELETE_WINDOW", alert)
mainloop()
