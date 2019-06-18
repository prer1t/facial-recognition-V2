import cv2
import numpy as np

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('training/Recogniser.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_DUPLEX
