# coding: utf-8
"""
Our system consists of two major layers.
In the first layer, a deep convolutional neural network mainly used for object detection and image segmentation.
The network takes in a raw pixel image, then classify it into one of the labels defined in the dataset.
The output of the CNN will then be fed into the second layer,
which is going to perform online motion analysis and trajectory-based tracking
to detect any situations that may pose a potential threat to the driving agent.
Lastly, the result of our structure for motion (SfM) system will then be transformed
to voice warning system that would notify the driver of any upcoming threats.

- Window Management:
    We use a cross-platform API for captureing screenshots called (MSS)
    For more information about MSS-API refer to http://python-mss.readthedocs.io/examples.html

    Note: By default our calss will capture the entire main monitor and pass it into the CNN.
    - monitor_id: ID of the monitor to be captured
    - window_top_offset: Top Offset in pixels (0 by default)
    - window_left_offset: Left Offset in pixels (0 by default)
    - window_width: The desired width of the captured window (full width of the given monitor by default)
    - window_height: The desired height of the captured window (full height of the given monitor by default)
    - window_scale: A scaling factor for the captured window (1.0 by default)

"""

# libraries and dependencies
# ---------------------------------------------------------------------------- #
import numpy as np
import cv2
import os, sys
import mss
import mss.tools
import time

from object_classifier.ObjectClassifier import *
from lane_detector.LaneDetector import *

# ---------------------------------------------------------------------------- #

class DrivingAssistant:
    # Constructor
    def __init__(self,
        classifier_codename,
        dataset_codename,
        classifier_threshold,
        object_detection = True,
        object_visualization = True,
        lane_detection = True,
        lane_visualization = True,
        diagnostic_mode = True,
        monitor_id = 1,
        window_top_offset = 0,
        window_left_offset = 0,
        window_width = None,
        window_height = None,
        window_scale = 1.0):

        # Boolean flag for feature-customization
        self.object_detection = object_detection
        self.object_visualization = object_visualization

        self.lane_detection = lane_detection
        self.lane_visualization = lane_visualization

        # Instance of the MSS-API for captureing screenshots
        self.window_manager = mss.mss()

        # Note:
        #   - monitor_id = 0 | grab all monitors together
        #   - monitor_id = n | grab a given monitor (n) : where n > 0
        self.target_window = self.window_manager.monitors[monitor_id]

        # Update position of the window that will be captured
        if window_left_offset:
            self.target_window['left'] += window_left_offset
            self.target_window['width'] -= window_left_offset
        if window_top_offset:
            self.target_window['top'] += window_top_offset
            self.target_window['height'] -= window_top_offset
        if window_width:
            self.target_window['width'] = window_width
        if window_height:
            self.target_window['height'] = window_height
        if window_scale:
            self.target_window['scale'] = window_scale

        print("Activating DeepEye Advanced Co-pilot Mode")
        
        self.object_detector = ObjectClassifier(
            classifier_codename = classifier_codename,
            dataset_codename = dataset_codename,
            classifier_threshold = classifier_threshold,
            visualization = object_visualization,
            diagnostic_mode = diagnostic_mode
        )

        self.lane_detector = LaneDetector(
            visualization = lane_visualization
        )

        self.threats = {
            "COLLISION": False,
            "PEDESTRIAN": False,
            "STOP_SIGN": False,
            "TRAFFIC_LIGHT": False,
            "VEHICLES": False,
            "BIKES": False,
            "FAR_LEFT": False,
            "FAR_RIGHT": False,
            "RIGHT": False,
            "LEFT": False,
            "CENTER": False,
            "UNKNOWN": True
        }

        self.frame_id = 0


    def run(self):   
        """
        Capture frames, initiate both objects and lane detectors, and then visualize output. 
        """
        timestamp = time.strftime("%Y%m%d-%H%M%S")

        # Get raw pixels from the screen, save it to a Numpy array
        pixels_arr = np.asarray(self.window_manager.grab(self.target_window))
        
        # convert pixels from BGRA to RGB values
        self.frame = cv2.cvtColor(pixels_arr, cv2.COLOR_BGRA2RGB)

        if self.frame_id % 5:
            cv2.imwrite("test/" + timestamp + "pre.jpg", pixels_arr)

        # detect objects in the given frame
        if self.object_detection:
            (self.frame, self.threats) = self.object_detector.scan_road(self.frame, self.threats)

        # detect lane in the given frame
        if self.lane_detection:
            (self.frame, self.threats) = self.lane_detector.detect_lane(self.frame, self.threats)

        #visualization customization 
        if (self.object_visualization and self.lane_visualization) or self.lane_visualization:
            # Display frame with detected objects.
            cv2.imshow('DeepEye Dashboard', cv2.resize(self.frame, (640, 480)))

        elif self.object_visualization and not self.lane_visualization:
            # convert to grayscale to reduce computational power needed for the process
            self.frame = cv2.cvtColor(self.frame, cv2.COLOR_RGB2GRAY)
            # Display frame with detected objects.
            cv2.imshow('DeepEye Dashboard', cv2.resize(self.frame, (640, 480)))

        else:
            pass # skip visualization
        
        if self.frame_id % 5:
            cv2.imwrite("test/" + timestamp + "post.jpg", self.frame)

        self.frame_id += 1

                   




           

        