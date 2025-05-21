# Real-Time Face Recognition System

This project is a real-time face recognition system built using Python, OpenCV, and the `face_recognition` library. It allows you to recognize known faces via webcam, log each recognition with a timestamp, and manage face data through a simple GUI.

> ⚠️ **Note:** This project does not include any personal images, only few Unsplash images for comparison. You are expected to add your own face data following the instructions below.

---

## Features

- Real-time face recognition using webcam
- Add new faces via webcam or file upload
- Timestamp logging of recognized people in `log.csv`
- Simple GUI built with Tkinter
- Clean architecture and modular code

---

## Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

## Folder Structure

real_time_face_recognition/
├── images/               # Stores folders for each person (e.g., images/John/)
├── encodings.pickle      # Pickle file with facial encodings
├── log.csv               # Logs of recognized faces with timestamps
├── encode_faces.py       # Encodes faces into pickle file
├── add_face.py           # Script to add new faces
├── gui_app.py            # Main GUI application
├── recognizer.py         # CLI face recognition (optional)
├── requirements.txt
└── README.md

## How to use

Clone repo:

```bash
git clone https://github.com/M26I/real_time_face_recognition
cd real_time_face_recognition

```
Add new Face:

```bash
python add_face.py

```

You will be prompted to:

Enter the name of the person (e.g., John)

Choose between:

'webcam' — take a photo using your webcam

'file' — provide a path to an image on your computer

Captured or uploaded images will be stored under images/{name}/.

The script will then automatically update facial encodings.

Run the app:

```bash
python gui_app.py

```
The webcam will open, and known faces will be recognized in real-time. Every recognition event is saved to log.csv with the name and timestamp.

## Notes
- You can delete all face data by removing the contents of the images/ folder and deleting encodings.pickle.

- Never commit personal images to a public repository.

- Make sure each face you add has good lighting and a clear frontal view for better accuracy.


## Author
[M26I](https://github.com/M26I)

---
© 2025 M26I – For educational/portfolio use only.  
Unauthorized use or redistribution without credit is prohibited.
