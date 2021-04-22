import cv2

cap=cv2.VideoCapture("New folder/rabbit_vid.mp4")

fps = cap.get(cv2.CAP_PROP_FPS)
print(fps)