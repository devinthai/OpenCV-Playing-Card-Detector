"""
Author: Devin Thai
Description: Defines the CasinoStream program that grabs frames from Danmemo's
casino.
Based on Evan Jura's VideoStream.py.
"""

# Import the necessary packages
from threading import Thread
from PIL import ImageGrab
import cv2


class VideoStream:
    """Camera object"""
    def __init__(self, resolution=(0, 0, 1920, 1080),framerate=30,src=0):
        global res
        res = resolution
        # Read frame from screen
        self.frame = ImageGrab.grab(bbox = resolution)

	# Create a variable to control when the camera is stopped
        self.stopped = False

    def start(self):
	# Start the thread to read frames from the video stream
        Thread(target=self.update,args=()).start()
        return self

    def update(self):

        # Keep looping indefinitely until the thread is stopped
        while True:
            # If the camera is stopped, stop the thread
            if self.stopped:
                # Close camera resources
                self.stream.release()
                return

            # Otherwise, grab the next frame from the stream
            (self.grabbed, self.frame) = ImageGrab.grab(bbox = res)
    def read(self):
		# Return the most recent frame
        return ImageGrab.grab(bbox = res)

    def stop(self):
		# Indicate that the camera and thread should be stopped
        self.stopped = True
