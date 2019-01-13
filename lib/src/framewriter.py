#!/usr/bin/env python

import cv2
import datetime

class FrameWriter(object):
    ''' Class to write frames to file '''

    # Map of codecs to extensions
    codec_map = {
                    "XVID" : ".avi"
                }

    def __init__(self, fileindicator="", codec="XVID"):
        # Build filename
        self.filename = fileindicator +" {}" + self.codec_map[codec]
        # Set codec
        self.fcc_codec = cv2.VideoWriter_fourcc(*codec)
        # Wait to open output file
        self.out = None

    def open_output(self):
        ''' Open an output file '''

        # Get the date
        date = datetime.datetime.now().strftime("%c")
        # Use it for the file name
        self.filename = self.filename.format(date)

        # Close previous output
        if self.out:
            self.close_output()

        # Create output
        self.out = cv2.VideoWriter(self.filename,self.fcc_codec, 20.0, (640,480))

    def write_output(self, frame):
        ''' Write frames to output '''

        self.out.write(frame)

    def close_output(self):
        ''' Close the output file '''

        if self.out:
            self.out.release()



