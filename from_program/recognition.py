import face_recognition
import cv2

class Recognition:

    def __init__(self):
        #reference to webcam 0
        self.video_capture = cv2.VideoCapture(0)
        # Initialize some variables
        self.face_locations = []
        self.face_encodings = []
        self.face_names = []
        self.process_this_frame = True

    def generateUnknown(self, known_face_names):
        uknown = "Unknown"
        n = ""
        i = 0
        while (uknown + n) in known_face_names:
            i = i + 1
            n = str(i)
        return (uknown + n)

    def find_faces(self, known_face_encodings, known_face_names):
        # Grab a single frame of video
        ret, frame = self.video_capture.read()

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Only process every other frame of video to save time
        if self.process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            self.face_locations = face_recognition.face_locations(rgb_small_frame)
            self.face_encodings = face_recognition.face_encodings(rgb_small_frame, self.face_locations)

            self.face_names = []
            for face_encoding in self.face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = ""

                # If a match was found in known_face_encodings, just use the first one.
                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]
                else:
                    name = self.generateUnknown(known_face_names)
                    known_face_encodings.append(face_encoding)
                    known_face_names.append(name)

                self.face_names.append(name)

                #print("face_names: " + self.face_names)

        self.process_this_frame = not self.process_this_frame


        # Display the results
        for (top, right, bottom, left), name in zip(self.face_locations, self.face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # Display the resulting image
        cv2.imshow('Video', frame)

    def close(self):
        # Release handle to the webcam
        self.video_capture.release()
        cv2.destroyAllWindows()
