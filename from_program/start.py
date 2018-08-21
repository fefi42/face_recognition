import cv2
from recognition import Recognition
from ui import Ui
from face_data import FaceData

import tkinter
from tkinter import *
from tkinter import ttk

def main():

    #Datastructure for faces and names
    fd = FaceData()

    rec = Recognition()

    root = Tk()
    ui = Ui(root)

    def task():
        #while True:
        #print("length: "+ str(len(known_face_names)))
        rec.find_faces(fd)
        ui.setList(fd)

        ## TODO:  Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("q pressed")
        #    break
        root.after(20, task)  # reschedule event in 2 seconds


    root.after(20, task)
    ui.startLoop()

    rec.close()

if __name__ == '__main__':
    main()
