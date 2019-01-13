# Webcam Motion Detector
### Author: Peter Swanson
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) 
[![imutils](https://img.shields.io/badge/imutils-0.5.2-green.svg)](https://pypi.org/project/imutils/) 
[![opencv-python](https://img.shields.io/badge/opencv—python-4.0.0.21-green.svg)](https://pypi.org/project/opencv-python/)
[![PyInstaller](https://img.shields.io/badge/PyInstaller-3.4-green.svg)](https://pypi.org/project/PyInstaller/)

## Background:
An application that makes it easy to set up a motion detecting
security camera for your Raspberry Pi or laptop.

<b>Known Compatibility: </b>
- Ubuntu

## Installing:
### Download the Binary
1. [Click here to download](https://github.com/Topazoo/Webcam_Motion_Detector/raw/master/binaries/Webcam%20Motion%20Capture.zip)
2. Install opencv
```
sudo apt-get install python-opencv
```
3. Extract and run

### From the Command Line
1. Clone the repository
2. Install Dependencies
3. Run <i>run.py</i>

```
git clone https://github.com/Topazoo/Webcam_Motion_Detector.git
cd Webcam_Motion_Detector
pip install -r "requirements.txt"
./run.py
```

## Command Line Arguments:
#### <i>run.py</i> can be executed with the following arguments
```
./run.py
```
Displays the feed of the first available camera
```
./run.py -V [N] (-W -M -S -C)
```
<b>-V [N]</b> : Displays the feed of the Nth available camera

- e.g. "-V 2" to use camera 2

```
./run.py -W (-V [N] -M -S -C)
```
<b>-W</b> : Displays the feed of the first available camera and writes to a file

- Can be combined with <b>-V [N]</b> to use an alternative camera
- The recorded footage is not displayed when used without the command <b>-S</b>

```
./run.py -M (-V [N] -W -S -C)
```
<b>-M</b> : Displays the feed of the first available camera and detects motion

- Can be combined with <b>-V [N]</b> to use an alternative camera
- The footage is not recorded when used without the command <b>-W</b>
- The detected motion can be viewed with a contour box using the command <b>-C</b>

```
./run.py -S (-V [N] -W -M -C)
```
<b>-S</b> : Displays the feed of the first available camera

- Can be combined with <b>-V [N]</b> to use an alternative camera
- The footage is not recorded when used without the command <b>-W</b>
- The detected motion can be viewed with a contour box using the command <b>-C</b> and <b>-M</b>

```
./run.py -C -M (-V [N] -W -S)
```
<b>-C -M</b> : Records from the first available camera and outlines detected motion with a contour box

- Can be combined with <b>-V [N]</b> to use an alternative camera
- The footage is not recorded when used without the command <b>-W</b>

### Common Recipes
```
./run.py -V 2 -M -W
```
Record motion from camera 2 without showing a feed on screen
```
./run.py -M -C
```
Display a feed from camera 1 with a contour box around motion
```
./run.py -V 1 -W
```
Record from camera 1 without showing a feed on screen
```
./run.py -V 2 -M -W -C -S
```
Display and record a feed from camera 2 with a contour box around motion


### <b>Open feeds can be closed by pressing 'q'</b>
