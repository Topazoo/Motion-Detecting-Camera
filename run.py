#!/usr/bin/env python
import sys
from lib.webcam import Webcam

def main(cla=" ".join(sys.argv)):

    webcam = Webcam(1)

    try:
        webcam.motion_capture()
    except KeyboardInterrupt:
        webcam.close()
    

main()