#!/usr/bin/env python

import Tkinter as tk
from lib.interface.clahandler import CLA_Handler, Dispatcher
import cv2

class GUI(object):
    def __init__(self):
        ''' Build the GUI '''

        # Main window
        self.window = tk.Tk()
        self.build_window(self.window)
        # Device Field
        self.build_dev_field(self.window)
        # Show checkbox
        self.build_checkbox(self.window, "Show Video Stream (Press 'q' to quit)", self.set_show, 8)
        self.build_checkbox(self.window, "Show Contour", self.set_contour, 0)
        # Buttons
        self.build_buttons(self.window)

        # Set toggle-able variables
        self.device = 0
        self.show = False
        self.contour = False

    def start(self):
        ''' Show the GUI '''

        self.window.mainloop()

    def get_devices(self):
        ''' Collect attached cameras '''

        dev_list = []
        x = 0

        # Open cameras until none left, count each
        while True:
            template_string = "Device {}"
            capture = cv2.VideoCapture(x)

            if not capture.read()[0]:
                break

            dev_list.append(template_string.format(str(x + 1)))
            x += 1

        return dev_list

    def set_device(self, name):
        ''' Change the selected device '''

        name = name[name.rfind(" ") + 1::]
        name = int(name) - 1

        self.device = name

    def set_show(self):
        ''' Toggle video stream '''
        self.show = not self.show

    def set_contour(self):
        ''' Toggle contour '''
        self.contour = not self.contour

    def build_dev_field(self, window):
        ''' Build device select field '''

        optionList = self.get_devices()
        def_opt = tk.StringVar(value="Device")
        self.dev_menu = tk.OptionMenu(window, def_opt, *optionList, command=self.set_device)
        tk.Label(window, text="Select a device:").pack(anchor=tk.W, padx=10, pady=6)
        self.dev_menu.pack(side=tk.TOP, anchor=tk.W, padx=8)

    def build_checkbox(self, window, text, command, pady=0):
        ''' Build a checkbox '''

        val = tk.IntVar(value=0)
        tk.Checkbutton(window, text=text, variable=val, command=command).pack(side=tk.TOP, anchor=tk.W, pady=pady)

    def run(self, cla=""):
        # Read CLAs
        cla_handler = CLA_Handler()
        commands = cla_handler.parse(cla)

        # Execute CLAs
        dispatcher = Dispatcher()
        dispatcher.run(commands)

    def build_window(self, window):
        ''' Build the main window '''

        window.geometry('300x160')
        window.title("Webcam Motion Capture")

    def build_buttons(self, window):
        ''' Build bottom buttons '''
        tk.Button(window, text='Capture Motion', command=self.run_motion).pack(side=tk.RIGHT,
                                                                                        anchor=tk.S, padx=5, pady=5)
        tk.Button(window, text='Record', command=self.run_rec).pack(side=tk.RIGHT, anchor=tk.S, pady=5)
        tk.Button(window, text='Watch', command=self.run_read).pack(side=tk.RIGHT, anchor=tk.S, padx=5, pady=5)

    def run_read(self):
        ''' Wrapper for stream functionality '''

        cla = "-V {}".format(str(self.device))
        if self.contour:
            cla += " -C"

        self.run(cla)

    def run_rec(self):
        ''' Wrapper for record functionality '''

        cla = "-V {} -W".format(str(self.device))

        if self.contour:
            cla += " -C"
        if self.set_show:
            cla += " -S"

        self.run(cla)

    def run_motion(self):
        ''' Wrapper for motion detection functionality '''

        cla = "-V {} -M -W".format(str(self.device))

        if self.contour:
            cla += " -C"
        if self.set_show:
            cla += " -S"

        self.run(cla)
