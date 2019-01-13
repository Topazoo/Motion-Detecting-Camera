#!/usr/bin/env python

import cv2, imutils, datetime
from framewriter import FrameWriter

class Motion_Detector(object):
    def __init__(self, camera):
        self.first_frame = None
        self.camera = camera
        self.framewriter = None
        self.is_moving = False

    def compute_frame(self, gray, frame, area=500, with_contour=False):
        ''' Detect motion in a frame '''

        # Find the absolute difference between the current frame and first frame
        frameDelta = cv2.absdiff(self.first_frame, gray)
        thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]

        # Dilate the threshold image to fill in holes, then find contours
        thresh = cv2.dilate(thresh, None, iterations=2)
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)

        found_contour = False
        # Loop over the contours
        for c in cnts:
            # If the contour is too small, ignore it
            if cv2.contourArea(c) < area:
                continue

            # Compute the bounding box for the contour, draw it on the gray,
            # and the original
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 255, 0), 2)
            if with_contour:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            found_contour = True

        return found_contour

    def read(self, show=False, write=True):
        ''' Read the camera feed '''

        while(self.camera.isOpened()):
            # Get a frame if possible
            ret, frame = self.camera.read()
            if ret == False:
                break

            # Resize read area to a smaller width
            frame = imutils.resize(frame, width=640, height=480)
            # Create a grayscale version of the image
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # Blur pixels to account for noise
            gray = cv2.GaussianBlur(gray, (21, 21), 0)

            # If the first frame is None, initialize it
            if self.first_frame is None:
                self.first_frame = gray
                continue

            res = self.compute_frame(gray, frame)

            # Draw the timestamp on the frame
            cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
                (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

            if self.is_moving and res:
                self.framewriter.write_output(frame)

            # Look for motion in the frame, optional write if found
            elif res and write and not self.is_moving:
                self.framewriter = FrameWriter()
                self.framewriter.open_output()
                self.framewriter.write_output(frame)
                self.is_moving = True

            elif not res and write and self.is_moving:
                self.framewriter.close_output()
                self.is_moving = False

            if show:
                # Show the frame
                cv2.imshow("Camera Feed", frame)

            # If the q key is pressed, break from the loop
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break