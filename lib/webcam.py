#!/usr/bin/env python

import cv2
from framewriter import FrameWriter
from motiondetector import Motion_Detector

class Webcam(object):
    ''' Class for interfacing with a webcam '''

    def __init__(self, camera_num=0, codec="XVID", fileindicator=""):
        # Attach to a webcam
        self.camera = cv2.VideoCapture(camera_num)
        # Instantiate helper class for writing videos
        self.framewriter = FrameWriter(fileindicator, codec)

    def motion_capture(self, show, write, contour):
        # Instantiate a Motion Detector
        motion_detector = Motion_Detector(self.camera)
        # Read with specified options
        motion_detector.read(show, write, contour)

        self.close()

    def read(self):
        ''' Read camera footage '''

        # While the camera is open
        while(self.camera.isOpened()):
            # Get a frame
            ret, frame = self.camera.read()
            # If a frame was received
            if ret==True:
                cv2.imshow('frame',frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break

        # Clean up
        self.close()

    def write(self, show):
        ''' Write to file while motion is being read '''

        # Open a file to write to
        self.framewriter.open_output()

        # While the camera is open
        while(self.camera.isOpened()):
            # Get a frame
            ret, frame = self.camera.read()
            # If a frame was received
            if ret==True:
                # Write it to output
                self.framewriter.write_output(frame)

                # Display on screen if True
                if show:
                    cv2.imshow('frame',frame)

                # End on q
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break

        #Close output
        self.framewriter.close_output()

    def close(self):
        # Release camera
        self.camera.release()
        # Close output
        self.framewriter.close_output()
        # Remove show window
        cv2.destroyAllWindows()