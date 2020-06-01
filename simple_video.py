import cv2
import time
import psutil

cap = cv2.VideoCapture('people.mp4')
counter = 0
cpu_percent = 0


while(cap.isOpened()):
    ret, frame = cap.read()

    cv2.imshow('frame',frame)

    cpu_percent = cpu_percent + psutil.cpu_percent()
    counter = counter + 1
    print("AVG CPU-USAGE in %: " + str(cpu_percent/counter))
    if cv2.waitKey(93) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

'''
python3 just_video.py
'''
