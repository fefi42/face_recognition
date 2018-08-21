import cv2
from recognition import Recognition
from ui import Ui
import tkinter
from tkinter import *
from tkinter import ttk


def main():

    #lists of faces and names
    known_face_encodings = []
    known_face_names = []

    rec = Recognition()

    root = Tk()
    ui = Ui(root)

    def task():
        #while True:
        #print("length: "+ str(len(known_face_names)))
        rec.find_faces(known_face_encodings, known_face_names)

        ui.setList(known_face_names)

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
