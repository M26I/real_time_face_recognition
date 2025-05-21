# © 2025 M26I - For educational/portfolio use only
import tkinter as tk
from tkinter import messagebox
import cv2
import face_recognition
import pickle
from datetime import datetime
import csv
import os
from threading import Thread

class FaceRecognitionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Real-Time Face Recognition")
        self.root.geometry("300x200")
        self.running = False

        self.start_btn = tk.Button(root, text="Start Recognition", command=self.start_recognition)
        self.start_btn.pack(pady=20)

        self.stop_btn = tk.Button(root, text="Stop", command=self.stop_recognition)
        self.stop_btn.pack(pady=10)

        self.quit_btn = tk.Button(root, text="Exit", command=root.quit)
        self.quit_btn.pack(pady=10)

    def start_recognition(self):
        if not self.running:
            self.running = True
            self.thread = Thread(target=self.run_recognition)
            self.thread.start()

    def stop_recognition(self):
        self.running = False

    def run_recognition(self):
        # Load encodings
        with open('encodings.pickle', 'rb') as f:
            data = pickle.load(f)

        video = cv2.VideoCapture(0)

        log_file = 'log.csv'
        if not os.path.exists(log_file):
            with open(log_file, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Name', 'Timestamp'])

        seen_names = {}

        while self.running:
            ret, frame = video.read()
            if not ret:
                break

            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            boxes = face_recognition.face_locations(rgb_frame)
            encodings = face_recognition.face_encodings(rgb_frame, boxes)

            for (top, right, bottom, left), encoding in zip(boxes, encodings):
                matches = face_recognition.compare_faces(data['encodings'], encoding)
                name = "Unknown"

                if True in matches:
                    match_index = matches.index(True)
                    name = data['names'][match_index]

                    now = datetime.now()
                    if name not in seen_names or (now - seen_names[name]).total_seconds() > 5:
                        with open(log_file, 'a', newline='') as f:
                            writer = csv.writer(f)
                            writer.writerow([name, now.strftime("%Y-%m-%d %H:%M:%S")])
                        seen_names[name] = now

                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                cv2.putText(frame, name, (left, top - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)

            cv2.imshow("Face Recognition", frame)
            if cv2.waitKey(1) == ord('q'):
                break

        video.release()
        cv2.destroyAllWindows()

        self.running = False

# Run GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = FaceRecognitionApp(root)
    root.mainloop()
