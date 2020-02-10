#!/usr/bin/python3

import numpy as np
from PIL import ImageGrab
import cv2
import time

previous_time = time.time()

while(True):
    print_screen = ImageGrab.grab(bbox=(0, 40, 800, 640)) #(bbox= x,y,width,height)

    frame = cv2.cvtColor(np.array(print_screen), cv2.COLOR_BGR2RGB)

    print('Seconds between frames = {}'.format(time.time()-previous_time)) #Seconds between frames
    previous_time = time.time()
    
    cv2.imshow('window', frame) #Show frame in cv2 window
    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

