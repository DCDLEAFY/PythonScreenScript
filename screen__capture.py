#!/usr/bin/python3

import numpy as np
from PIL import ImageGrab
import cv2
import time


def frame_capture():
    previous_time = time.time()
    while(True):
        #(bbox= x,y,width,height) - Grabbing section of screen
        print_screen = ImageGrab.grab(bbox=(0, 40, 800, 640))

        #Making sure the colour is the same
        frame = cv2.cvtColor(np.array(print_screen), cv2.COLOR_BGR2RGB)

        # Seconds between frames
        print('Seconds between frames = {}'.format(time.time()-previous_time))
        previous_time = time.time()
        
        # Show frame in cv2 window
        cv2.imshow('window', frame) 

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

if __name__ == "__main__":
    frame_capture()
    pass