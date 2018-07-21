# OpenCV-Playing-Card-Detector
This is a Python program that uses OpenCV to detect and identify playing cards from a PiCamera video feed on a Raspberry Pi. Check out the YouTube video that describes what it does and how it works:

https://www.youtube.com/watch?v=m-QPjO-2IkA

## Usage
Download this repository to a directory and run CardDetector.py from that directory. Cards need to be placed on a dark background for the detector to work. Press 'q' to end the program.

The program was originally designed to run on a Raspberry Pi with a Linux OS, but it can also be run on Windows 7/8/10. To run on Windows, download and install Anaconda (https://www.anaconda.com/download/, Python 3.6 version), launch Anaconda Prompt, and execute the program by launching IDLE (type "idle" and press ENTER in the prompt) and opening/running the CardDetector.py file in IDLE. The Anaconda environment comes with the opencv and numpy packages installed, so you don't need to install those yourself. If you are running this on Windows, you will also need to change the program to use a USB camera, as described below.

The program allows you to use either a PiCamera or a USB camera. If using a USB camera, change line 38 in CardDetector.py to:
```
videostream = VideoStream.VideoStream((IM_WIDTH,IM_HEIGHT),FRAME_RATE,2,0).start()
```

The card detector will work best if you use isolated rank and suit images generated from your own cards. To do this, run Rank_Suit_Isolator.py to take pictures of your cards. It will ask you to take a picture of an Ace, then a Two, and so on. Then, it will ask you to take a picture of one card from each of the suits (Spades, Diamonds, Clubs, Hearts). As you take pictures of the cards, the script will automatically isolate the rank or suit and save them in the Card_Imgs directory (overwriting the existing images).


## Files
CardDetector.py contains the main script

Cards.py has classes and functions that are used by CardDetector.py

PiVideoStream.py creates a video stream from the PiCamera, and is used by CardDetector.py

Rank_Suit_Isolator.py is a standalone script that can be used to isolate the rank and suit from a set of cards to create train images

Card_Imgs contains all the train images of the card ranks and suits

## Dependencies
Python 3.6

OpenCV-Python 3.2.0 and numpy 1.8.2:
See https://www.pyimagesearch.com/2016/04/18/install-guide-raspberry-pi-3-raspbian-jessie-opencv-3/
for how to build and install OpenCV-Python on the Raspberry Pi

picamera library:
```
sudo apt-get update
sudo apt-get install python-picamera python3-picamera
```
## Notes

How Evan Juras' CardDetector works:

Before Execution:
Use the Rank_Suit_Isolator file to take pictures of the cards to learn from.

During Execution:
1. he creates a way to capture an image using videostream
2. he loops over a number of frames
	a. he captures a frame to analyze
	b. pre-processes the frame (gray, blurs, adaptive thresholding image)
	c. find and sort contours of all cards (query cards)
		1. if there are no contours, do nothing
	d. creates a list to store recognized cards
	e. loops over detected contours
		1. finds a best match card rank and suit match for contour using preprocess
		2. matches center points and then draws the recognized card

What I have to figure out how to do:

(1). find a way to capture an image from a window -> PIL method works fine. See test.py
	- maybe use PIL to capture the whole screen and then make it fit to a screen?
		- maybe just the whole screen is fine
		- apparently this method has really low fps
	- maybe use mss as the fps is potentially higher
(2). use Rank_Suit_Isolator to process screenshots from danmemo -> modified Rank_Suit_Isolator into Casino_Rank_Isolator, still needs work.
(3). use test.py as an example to replace his VideoStream
4. change the size of the rank and suit isolators in Casino_Rank_Isolator so that it looks at the proper region.
5. implement the test.py VideoStream to fix CasinoCardDetector
(6). need to adjust how CasinoCardDetector looks for cards. As it stands, CasinoCardDetector does not detect Jacks and Queens because it is the designs makes it hard
	the program to decide that they look like cards. 
	- perhaps try to create a new method that looks targets the rank and suit only.
		- maybe modify how the Cards.find_cards method looks for cards.
7. maybe modify the card recognition software to also record backs.
8. we've figured out how to constantly update an array filled with ranks/suit, now we need to find a way to get the positions of corresponding cards
9. code the algorithm to make poker decisions.

Link I'm currently working with:
https://stackoverflow.com/questions/35097837/capture-video-data-from-screen-in-python
https://stackoverflow.com/questions/46629878/image-capture-the-center-of-the-screen-using-python
https://stackoverflow.com/questions/11122291/python-find-char-in-string-can-i-get-all-indexes
http://briancaffey.github.io/2018/01/02/checking-poker-hands-with-python.html


Notes:
If i run the preprocessing algorithm on the image, the only contours are the cards.

The first five contours sorted by area are generally the cards. perhaps I should set it so that it simply takes the first 5 cards then?
	-> Cards2 uses this approach and CasinoCardDetector(v2) utilizes this version of Cards.

Casino_Rank_Isolater(v2) attempts to create the files for a "back" card along with all the other traditional cards.
