import cv2
cam = cv2.VideoCapture(0)
detector=cv2.CascadeClassifier('C:/Users/preri/AppData/Local/Programs/Python/Python37/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
Id=input('enter picture label:')
sampleNum=0
