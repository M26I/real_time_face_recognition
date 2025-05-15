import face_recognition
import cv2
import os
import pickle

known_encodings = []
known_names = []

image_dir = 'images'

for name in os.listdir(image_dir):
    person_dir = os.path.join(image_dir, name)
    if not os.path.isdir(person_dir):
        continue
    for filename in os.listdir(person_dir):
        image_path = os.path.join(person_dir, filename)
        image = face_recognition.load_image_file(image_path)
        encodings = face_recognition.face_encodings(image)
        if encodings:
            known_encodings.append(encodings[0])
            known_names.append(name)

# Save to file
data = {'encodings': known_encodings, 'names': known_names}
with open('encodings.pickle', 'wb') as f:
    pickle.dump(data, f)

print("Encoding complete.")
