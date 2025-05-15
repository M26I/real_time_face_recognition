import cv2
import face_recognition
import pickle

# Load encodings
with open('encodings.pickle', 'rb') as f:
    data = pickle.load(f)

video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    boxes = face_recognition.face_locations(rgb_frame)
    encodings = face_recognition.face_encodings(rgb_frame, boxes)
    
    for (top, right, bottom, left), encoding in zip(boxes, encodings):
        matches = face_recognition.compare_faces(data['encodings'], encoding)
        name = "Unknown"

        if True in matches:
            match_index = matches.index(True)
            name = data['names'][match_index]

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)

    cv2.imshow("Face Recognition", frame)

    if cv2.waitKey(1) == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
