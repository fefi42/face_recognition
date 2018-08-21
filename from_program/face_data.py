import tkinter
from tkinter import *
from tkinter import ttk

#Datastructure for faces and names
class FaceData:

    TIME_TO_LIVE = 50
    SEEN_ACCEPTENCE_THRESHOLD = 15

    KNOWN_FACE_ENCODINGS = 0    #from face recognition
    KNOWN_FACE_NAMES = 1        #from face recognition (including unnamed)
    TTL = 2                     #time to live
    SEEN = 3                    #seen counter
    SHOW_IN_UI = 4               #Names shown in UI


    def __init__(self):
        row, col = 0, 5
        self.data = [[0 for x in range(row)] for y in range(col)] #create the data matrix


    def getKnownFaceEncodings(self):
        return self.data[FaceData.KNOWN_FACE_ENCODINGS]

    def getKnownFaceNames(self):
        return self.data[FaceData.KNOWN_FACE_NAMES]

    def getMatchedFaceName(self, index):
        if self.data[FaceData.SEEN][index] < FaceData.SEEN_ACCEPTENCE_THRESHOLD:
            self.data[FaceData.SEEN][index] = self.data[FaceData.SEEN][index] + 1
        return self.data[FaceData.KNOWN_FACE_NAMES][index]

    def addNewFace(self, face_encoding, face_name):
        self.data[FaceData.KNOWN_FACE_ENCODINGS].append(face_encoding)
        self.data[FaceData.KNOWN_FACE_NAMES].append(face_name)
        self.data[FaceData.TTL].append(FaceData.TIME_TO_LIVE)
        self.data[FaceData.SEEN].append(0)
        self.data[FaceData.SHOW_IN_UI].append(False)

    def updateListBox(self, listbox):
        #print("Names \t:" + str(self.data[FaceData.KNOWN_FACE_NAMES]))
        #print("TTL \t" + str(self.data[FaceData.TTL]))
        #print("seen \t:" + str(self.data[FaceData.SEEN]))

        indices_for_deletion = []
        indices_for_ui = []

        for n, i in enumerate(self.data[FaceData.TTL]): #reduce ttl
            if i > -1:
                self.data[FaceData.TTL][n] = i -1
            if self.data[FaceData.TTL][n] == 0 and self.data[FaceData.SEEN][n] < FaceData.SEEN_ACCEPTENCE_THRESHOLD:
                #print("it is 0 and gets deleted")
                #the face has not been seen for more than 25 frames and is not important
                indices_for_deletion.append(n) #save indice for delete
            if self.data[FaceData.TTL][n] == 0 and self.data[FaceData.SEEN][n] >= FaceData.SEEN_ACCEPTENCE_THRESHOLD:
                #print("it is 0 and stays")
                #the face has been seen for more frames and should be shown as name
                self.data[FaceData.SHOW_IN_UI][n] = True
                indices_for_ui.append(n)

        while len(indices_for_deletion) > 0:
            #remove all the faces that are not important
            delete_index = indices_for_deletion.pop()
            self.data[FaceData.KNOWN_FACE_NAMES].pop(delete_index)
            self.data[FaceData.KNOWN_FACE_ENCODINGS].pop(delete_index)
            self.data[FaceData.TTL].pop(delete_index)
            self.data[FaceData.SEEN].pop(delete_index)
            self.data[FaceData.SHOW_IN_UI].pop(delete_index)

        for i in indices_for_ui:
            listbox.insert(END, self.data[FaceData.KNOWN_FACE_NAMES][i])
