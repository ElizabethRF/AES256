''' open file 
from tkinter import filedialog
from tkinter import *
 
root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
print (root.filename)
'''
# save file 
'''
from tkinter import filedialog
from tkinter import *
 
root = Tk()
root.filename =  filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
print (root.filename)
'''

#test open from directory 
'''
import os 
import time 

file_name = '/Users/elizabeth/Documents/7mo/Seguridad/test.py'
with open(file_name, 'r') as fo:
	text = fo.read()
print(text)'''
'''
from  tkinter import *
from tkinter import filedialog
root = Tk()
root.directory = filedialog.askdirectory()
print (root.directory)
'''
'''
import re

print(bool(re.match('^(?=.*[0-9])(?=.*[A-Z])(?=.*[a-z])(?=.*[!#$?])', 'hasalAhanum2a?')))
print(bool(re.match('^(?=.*[0-9])(?=.*[a-zA-Z]$)', 'some string')))
'''

from tkinter import Text, Tk

r = Tk()
r.geometry("400x400")

t = Text(r, height=20, width=40)
t.pack()

r.mainloop()