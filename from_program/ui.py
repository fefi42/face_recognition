import tkinter
from tkinter import *
from tkinter import ttk

class Ui:

    def __init__(self, root):
        self.root = root
        self.root.title("Known names")

        self.listbox = Listbox(self.root)
        self.listbox.pack()


    def setList(self, list): #TODO besser machen (nur updates)
        self.listbox.delete(0, END) #clear
        for item in list:
            self.listbox.insert(END, item)

    def startLoop(self):
        self.root.mainloop()

#listbox.insert(END, "a list entry")

#for item in ["one", "two", "three", "four"]:
#    listbox.insert(END, item)
