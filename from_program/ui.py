import tkinter
from tkinter import *
from tkinter import ttk
from face_data import FaceData

class Ui:

    def __init__(self, root):
        self.root = root
        self.root.title("Known names")

        self.listbox = Listbox(self.root)
        self.listbox.pack()

        self.rename = Button(self.root, text="Rename", command=self.renamePopup)
        self.rename.pack()


    def setList(self, fd): #TODO besser machen (nur updates)
        fd.updateListBox(self.listbox)
        #self.listbox.get(0, END)
        #self.listbox.delete(0, END) #clear
        #for item in list:
            #if item in self.listbox

        #    self.listbox.insert(END, item)

    def startLoop(self):
        self.root.mainloop()

    def renamePopup(self):
        popup = Toplevel()
        popup.title("Rename")

        label = Label(popup, text="New name:")
        label.grid(row=0, column=0)

        entry = Entry(popup)
        entry.grid(row=0, column=1)

        button = Button(popup, text="OK", command=popup.destroy)
        button.grid(row=0, column=2)


#listbox.insert(END, "a list entry")

#for item in ["one", "two", "three", "four"]:
#    listbox.insert(END, item)
