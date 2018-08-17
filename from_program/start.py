import cv2
from recognition import Recognition
from ui import Ui


def main():
    #lists of faces and names
    known_face_encodings = []
    known_face_names = []

    rec = Recognition()
    ui = Ui()

    while True:
        #print("length: "+ str(len(known_face_names)))
        rec.find_faces(known_face_encodings, known_face_names)

        ui.setList(known_face_names)

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    rec.close()

if __name__ == '__main__':
    main()
