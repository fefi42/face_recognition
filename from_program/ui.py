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

        self.rename = Button(self.root, text="Rename", command=self.openRenamePopup)
        self.rename.pack()

        #Status bar
        self.statusText = StringVar()
        self.statusText.set("started and running")
        self.status = Label(self.root, textvariable=self.statusText, bd=1, relief=SUNKEN, anchor=W)
        self.status.pack(side=BOTTOM, fill=X)


    def setList(self, fd): #TODO besser machen (nur updates)
        fd.updateListBox(self.listbox)
        #self.listbox.get(0, END)
        #self.listbox.delete(0, END) #clear
        #for item in list:
            #if item in self.listbox

        #    self.listbox.insert(END, item)

    def startLoop(self):
        self.root.mainloop()

    def openRenamePopup(self):
        selectedItems = self.listbox.curselection()
        if len(selectedItems) == 0:
            #inform user that there is nothing selected
            self.statusText.set("No item selected")
            return

        self.popup = Toplevel()
        self.popup.title("Rename")

        popupLabel = Label(self.popup, text="New name:")
        popupLabel.grid(row=0, column=0)

        self.popupEntry = Entry(self.popup)
        self.popupEntry.grid(row=0, column=1)

        popupButton = Button(self.popup, text="OK", command=self.renameItem)
        popupButton.grid(row=0, column=2)

        self.idSelectedForRenaming = selectedItems[0]

    def renameItem(self):
        self.listbox.delete(self.idSelectedForRenaming)
        self.listbox.insert(self.idSelectedForRenaming, self.popupEntry.get())
        self.popup.destroy()

#listbox.insert(END, "a list entry")

#for item in ["one", "two", "three", "four"]:
#    listbox.insert(END, item)
