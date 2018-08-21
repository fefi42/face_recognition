import tkinter
from tkinter import *
from tkinter import ttk

#Datastructure for faces and names
class FaceData:

    TIME_TO_LIVE = 50
    SEEN_ACCEPTENCE_THRESHOLD = 15

    def __init__(self):
        #TODO in matrix umändern damit ids garantiert immer gleich sind
        self.known_face_encodings = [] #from registring
        self.known_face_names = [] #from registring

        #to exclude oneframe vectors that look like other persons but are actually the same
        #we introduce a time to live and a seen counter
        #if the seen counter is not high enough after the ttl is 0 the vector will be deleted
        self.ttl = [] #time to life (registering)
        self.seen = [] #how often it has been seen (registering)

        self.ui_names = [] # visible

    def getKnownFaceEncodings(self):
        return self.known_face_encodings

    def getKnownFaceNames(self):
        return self.known_face_names

    def getMatchedFaceName(self, index):
        if self.seen[index] < FaceData.SEEN_ACCEPTENCE_THRESHOLD:
            self.seen[index] = self.seen[index] + 1
        return self.known_face_names[index]

    def addNewFace(self, face_encoding, face_name):
        self.known_face_encodings.append(face_encoding)
        self.known_face_names.append(face_name)
        self.ttl.append(FaceData.TIME_TO_LIVE)
        self.seen.append(0)


    def updateListBox(self, listbox):
        #print("Names \t:" + str(self.known_face_names))
        #print("TTL \t" + str(self.ttl))
        #print("seen \t:" + str(self.seen))

        indices_for_deletion = []

        for n, i in enumerate(self.ttl): #reduce ttl
            if i > -1:
                self.ttl[n] = i -1
            if self.ttl[n] == 0 and self.seen[n] < FaceData.SEEN_ACCEPTENCE_THRESHOLD:
                #print("it is 0 and gets deleted")
                #the face has not been seen for more than 25 frames and is not important
                indices_for_deletion.append(n) #save indice for delete
            if self.ttl[n] == 0 and self.seen[n] >= FaceData.SEEN_ACCEPTENCE_THRESHOLD:
                #print("it is 0 and stays")
                #the face has been seen for more frames and should be shown as name
                self.ui_names.append(self.known_face_names[n])

        while len(indices_for_deletion) > 0:
            #remove all the faces that are not important
            delete_index = indices_for_deletion.pop()
            self.known_face_names.pop(delete_index)
            self.known_face_encodings.pop(delete_index)
            self.ttl.pop(delete_index)
            self.seen.pop(delete_index)

        while listbox.size() < len(self.ui_names):
            listbox.insert(END, self.ui_names[listbox.size()])
