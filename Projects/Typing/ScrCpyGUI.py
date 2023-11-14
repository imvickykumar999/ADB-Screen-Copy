
from tkinter import *
import os

root = Tk()
root.geometry("500x500")
root.title("My App")
root.config(bg="#ff0000")

def printhi(*args):
	os.system('scrcpy --tcpip=192.168.0.103')
    
btn = Button(root, text="Click to print hi", command=printhi)
btn.place(x=200, y=200)

root.mainloop()
