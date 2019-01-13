#!/usr/bin/env python

from lib.webcam import Webcam

def main():

    webcam = Webcam(1)

    try:
        webcam.read(show=False, write=True)
    except KeyboardInterrupt:
        webcam.close()

main()