# tensorrt-yolo
TensorRT for YOLOv3 with screenshot and beep function as well as GPS Overlay

## Contents
1. Description
2. Architecture of Solution
2. Setup and Explanation
3. Results
4. Built with:
5. Credits and Contact

## 1. Description
TensorRT is a Software Development Kit that specializes in high performance deep learning. It provides low latency and high throughput for deep learning applications and can import different trained models from various deep learning frameworks for application in TensorRT.

It converts Tiny-yolo weights to ONNX weights to TensorRT weights.

## 2. Architecture of Solution
Not applicable

## 3. Setup and Explanation
#### Main
Refer to my documentation link  

#### Add ons

###### Auto screenshot upon detection
Navigate to this directory: tensorrt-yolo/utils and open ‘visualization.py. Scroll down to line 102. This line of code is responsible for performing a screenshot upon detection and drawing of boundary boxes. 

- os.system is a python programming command to activate terminal on Ubuntu
- scrot translate to screenshot, self explanatory
- ~/tensorrt-yolo/screenshots/%b%d::%H%M%S.jpeg -q100 sets the directory to store the image as date and time with minimal compression

###### Beeping sound upon detection
Navigate to this directory: darknet/src and open ‘image.c’. Scroll down to line 309. This line of code is responsible for beeping upon detection and drawing of boundary boxes.

- fprintf(stdout, "\aBeep!\n" ) outputs a beeping sound and print ‘Beep’ on the terminal

###### GPS data overlay on detection frame
Navigate to this directory: tensorrt-yolo/utils and open ‘display.py’ Scroll down to line 34 and 35.

- file1 = open("/home/eee/tensorrt-yolo/utils/GPS.txt","r") is to open up the text file continuing GPS data as read only.
- cv2.putText(img, file1.read(), (10, 470), font, 1.0, (240, 240, 240), 1, line) is to set the parameters for insert GPS data into the frame.

## 4. Results
Upon detection, a boundary box will appear for visual impact. When the boundary box appears, a screenshot will be made and stored to a specified directory for further analysis.

For areas with GPS, live GPS coordinates will be shown on the feed.

## 5. Built with:
- CUDA
- cuDNN
- OpenCV

## 6. Credits and Contact
Full credits goes to: https://github.com/jkjung-avt/tensorrt_demos

Feel free to contact me regarding any questions

>>Ian: ianlim0309@gmail.com
