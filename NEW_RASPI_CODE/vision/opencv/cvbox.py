#!/usr/bin/env python3
#
# This is a demo program showing CameraServer usage with OpenCV to do image
# processing. The image is acquired from the USB camera, then a rectangle
# is put on the image and sent to the dashboard. OpenCV has many methods
# for different types of processing.
#
# Warning: If you're using this with a python-based robot, do not run this
# in the same program as your robot code!
#
# Created by Aidan Jarrett for team FROG 3160

import cv2
import numpy as np

from cscore import CameraServer, UsbCamera

def main():
    cs = CameraServer.getInstance()
    cs.enableLogging()
    
    usb1 = cs.startAutomaticCapture(dev=1)
    usb2 = cs.startAutomaticCapture(dev=0)

    
    #camera.setResolution(320, 240)
    
    # Get a CvSink. This will capture images from the camera
    cvSink = cs.getVideo()
    
    # (optional) Setup a CvSource. This will send images back to the Dashboard
    outputStream = cs.putVideo("Rectangle", 320, 240)
    
    # Allocating new images is very expensive, always try to preallocate
    img = np.zeros(shape=(240, 320, 3), dtype=np.uint8)    

    while True:
        # Tell the CvSink to grab a frame from the camera and put it
        # in the source image.  If there is an error notify the output.
        time, img = cvSink.grabFrame(img)
        if time == 0:
            # Send the output the error.
            outputStream.notifyError(cvSink.getError());
            # skip the rest of the current iteration
            continue
        
         

        # Draws two  vertical green line with thickness of 5 px
        cv2.line(img,(143,40),(147,100),(0,255,0),1)

        cv2.line(img,(20,40),(20,100),(0,255,0),1)

        
 
        # Draws two  vertical orange line with thickness of 5 px
        cv2.line(img,(133,40),(137,100),(0,0,100),1)

        cv2.line(img,(30,40),(30,100),(0,0,100),1)

        # Draws two  vertical red line with thickness of 5 px
        cv2.line(img,(153,40),(157,100),(200,0,0),1)

        cv2.line(img,(10,40),(10,100),(100,0,0),1)
        
        # Put a rectangle on the image
        #cv2.rectangle(img, (100, 100), (400, 400), (255, 255, 255), 5)
        
        # Give the output stream a new image to display
        outputStream.putFrame(img)    

if __name__ == '__main__':
    
    # To see messages from networktables, you must setup logging
    import logging
    logging.basicConfig(level=logging.DEBUG)
    
    # You should uncomment these to connect to the RoboRIO
    #import networktables
    #networktables.initialize(server='10.xx.xx.2')
    
    main()
    


