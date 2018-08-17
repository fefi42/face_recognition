import tkinter
from tkinter import *
from tkinter import ttk

class Ui:

    def __init__(self):
        self.root = Tk()
        self.root.title("Known names")

        self.listbox = Listbox(self.root)
        self.listbox.pack()

        #dTODO detach 
        self.root.mainloop()

    def setList(self, list): #TODO besser machen (nur updates)
        self.listbox.delete(0, END) #clear
        for item in list:
            self.listbox.insert(END, item)

#listbox.insert(END, "a list entry")

#for item in ["one", "two", "three", "four"]:
#    listbox.insert(END, item)
