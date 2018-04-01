#!/usr/bin/python3
#
#
"""
A python program that uses a generated GRIP pipeline to detect bright light and publish the result to Networktables and streams another camera feed to the Smart Dashboard
"""

import cv2
import numpy as np
from networktables import NetworkTables
from flashtrack import GripPipeline

from cscore import CameraServer, UsbCamera

def extra_processing(pipeline):
    """
    Performs extra processing on the pipeline's outputs and publishes data to   NetworkTable
    :param pipeline: the pipeline that just processed an image
    :return: None
    """
    center_x_positions = []
    center_y_positions = []
    widths = []
    heights = []

    # Find the bounding boxes of the contours to get x, y, width, and height
    for contour in pipeline.filter_contours_output:
        x, y, w, h = cv2.boundingRect(contour)
        center_x_positions.append(x + w / 2)  # X and Y are coordinates of the top-left co$
        center_y_positions.append(y + h / 2)
        widths.append(w)
        heights.append(h)

    # Publish to the '/vision/red_areas' network table
    table = NetworkTables.getTable('red_areas')
    table.putNumberArray('x', center_x_positions)
    table.putNumberArray('y', center_y_positions)
    table.putNumberArray('width', widths)
    table.putNumberArray('height', heights)


def main():
    print('Initializing NetworkTables')
    NetworkTables.setClientMode()
    NetworkTables.setIPAddress('10.31.60.2')
    NetworkTables.initialize()
    print('starting server')
    cs = CameraServer.getInstance()
    cs.enableLogging()
    
    usb1 = cs.startAutomaticCapture(dev=1)
   
    #cs.waitForever()
  print('Creating video capture')
    cap = cv2.VideoCapture(0)

    print('Creating pipeline')
    pipeline = GripPipeline()

    print('Running pipeline')
    while cap.isOpened():
        have_frame, frame = cap.read()
        if have_frame:
            pipeline.process(frame)
            extra_processing(pipeline)

    print('Capture closed')



if __name__ == '__main__':

    # To see messages from networktables, you must setup logging
    import logging
    logging.basicConfig(level=logging.DEBUG)
    
    # You should uncomment these to connect to the RoboRIO
    #import networktables
    #networktables.initialize(server='10.xx.xx.2')

    main()






