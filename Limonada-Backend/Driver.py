#!/usr/bin/env python3
"""
__author__  =  "Blaze Sanders"
__email__   =  "blaze.d.a.sanders@gmail.com"
__company__ =  "Unlimited Custom Creations"
__status__  =  "Development"
__date__    =  "Late Updated: 2021-07-04"
__doc__     =  "Logic to run back-end services via state changes in GUI"
"""

# Allow control of mouse & keyboard to start Zoom app and meeting
# https://pyautogui.readthedocs.io/en/latest/
import pyautogui

# Allow GPIO control of HDMI switcher 
# https://learn.adafruit.com/circuitpython-on-any-computer-with-ft232h
# https://learn.adafruit.com/circuitpython-on-any-computer-with-ft232h/mac-osx
import board  

# Simple GPIO HIGH and LOW
import digitalio

# Allow program to extract filename of the current file and exit gracefully
# https://docs.python.org/3/library/os.html
import os
import sys

# Allow BASH commands to be run inside python code like this file
# https://docs.python.org/3/library/subprocess.html
import subprocess
from subprocess import Popen, PIPE
from subprocess import check_call

# Allow pausing of code to sync with User Interface
# https://docs.python.org/3/library/time.html
import time

# Allow programmantic control of the mouse and keyboard
# https://pyautogui.readthedocs.io/en/latest/
import pyautogui

# Allow creation of temporary directory to save harddrive space
# https://docs.python.org/3/library/tempfile.html
from tempfile import gettempdir

# Generate .txt data logging and custom terminal debugging output
from Debug import *

# If code is running on Raspberry Pi 3+ or higher hardware, the TRY block will run
# Otherwise input & output pins will be simulated since code is running a Mac or Linux PC (Do NOT use Windows)
# https://raspberrypi.stackexchange.com/questions/34119/gpio-library-on-windows-while-developing
try:
	# Allow the control on high power relay shield
	# https://www.amazon.com/KEYESTUDIO-4-Channel-Shield-Expansion-Raspberry/dp/B072XGF4Z3
	# https://raspi.tv/2013/rpi-gpio-basics-5-setting-up-and-using-outputs-with-rpi-gpio
	import RPi.GPIO as GPIO
except RuntimeError:
	#TODO Currently using local folder named RPi with files __init__.py and GPIO.py to trick import
	import GPIOSimulator as GPIO


class Driver(object):

	# Relay Shied Pin CONSTANTS
	SHIELD_PIN_1 = 7
	SHIELD_PIN_2 = 15
	SHIELD_PIN_3 = 31
	SHIELD_PIN_4 = 37

	# Timing pauses in units of seconds
	VEND_DELAY_IN_SEC = 3
	SENSE_DELAY_IN_SEC = 1

	# ProductID vending CONSTANTS
	CANNED_DRINK = 0
	GIFT_CARD_IN_CAN = 1

	# Function return and debugging helper CONSTANTS
	OK = 1
	NOT_OK = 0
	HIGH = 1
	LOW = 0
	DEBUG_STATEMENTS_ON = True
	THIS_CODES_FILENAME = os.path.basename(__file__)

	# Zoom Vidoe & Audio CONSTANTS
	MISSION_CONTROL_ZOOM_URL = "https://zoom.us/j/7168730259?pwd=c2M4WGYzSTBrYTNFMmlDZDdjZnRBQT09"
	ZOOM_MEETING_ID = "7168730259"
	ZOOM_PASSCODE = "5vb9sL"


	def __init__(self, state):
		"""
		#TODO Only need this if using python-statemachine library
		"""
		self.state = state

		# Run the following commands in the command line before running Driver.py
		# export BLINKA_FT232H=1
		check_call("export BLINKA_FT232H=1", shell=True)
		
		# python3
		check_call("python3", shell=True)
		
		# import board
		pyautogui.write("import board")
		
		# from pyftdi.ftdi import Ftdi
		pyautogui.write("from pyftdi.ftdi import Ftdi", shell=True)
		
		# Ftdi().open_from_url('ftdi:///?')
		pyautogui.write("Ftdi().open_from_url('ftdi:///?')")
	
		# python3 
		check_call("python3", shell=True)

		# import os
		pyautogui.write("import os")

		# os.environ["BLINKA_FT232H"]
		# import digitialio

	def toggleHDMIport():
		"""
		Cycle through HDMI inputs connected, skipping any port not input video into switcher
		Using FT232H from Adafruit to simulate human button press of 1.5 seconds 
		on ASIN B0739GSKV2 HDMI switcher from Amazon
		
		Key argument(s):
		NONE

		Return:
		True if ALL the steps to switch HMDI input where successfull; False otherwise
		"""

		successfullSwitch = False
		led = digitalio.DigitalInOut(board.D7)
		led = led.direction = digitalio.Direction.OUTPUT
		
		led.value = False
		time.sleep(1.5)
		led.value = True
		
		successfullSwitch = True
		
		return successfullSwitch


	def vend(productID):
		"""
		#TODO

		Key argument(s):
		productID -- INTERGER: Unique ID for each type of item inside kiosk

		Return:
		True if ALL the steps to vend a can where successfull; False otherwise
		"""

		successfulVend = False

		if(productID == CANNED_DRINK):
			vendPin = SHIELD_PIN_1
		elif(productID == GIFT_CARD_IN_CAN):
			vendPin = SHIELD_PIN_2
		else:
			DebugObject = Debug(DEBUG_STATEMENTS_ON, THIS_CODES_FILENAME)
			DebugObject.Dprint("INVALID productID passed as parameter to Driver.vend()")

		GPIO.cleanup()
		GPIO.setup(vendPin, GPIO.OUT, initial=GPIO.LOW)
		GPIO.output(vendPin, HIGH)
		time.pause(VEND_DELAY_IN_SEC)
		GPIO.output(vendPin, LOW)

		GPIO.setup(sensePin, GPIO.out, initial=GPIO.LOW)
		itemSensed = GPIO.input(sensePin)
		time.pause(SENSE_DELAY_IN_SEC)

		if(itemSensed == HIGH):
			successfulVend = True
		else:
			successfulVend = False

		return successfulVend


	def restart():
		"""
		Restarts JUST the Raspberry Pi, no other vending machine hardware
		Use this only if Zoom or GUI has bug that can't fixed
		"""

		check_call("sudo reboot", shell=True)


	def startZoom(DebugObject):
		"""
		Use this start Zoom app, full screen it, and then pyautogui click to start meeting
		https://support.zoom.us/hc/en-us/articles/205683899-hot-keys-and-keyboard-for-zoom
		https://superuser.com/questions/1563255/start-a-zoom-meeting-from-the-command-line
		"""

		# Start Zoom application and minimize to give ordering GUI screen
		command =  "xdg-open " + Driver.MISSION_CONTROL_ZOOM_URL
		try:
			check_call(command, shell=True)
		except:
		#except CalledProcessError:
			print("Caught Called Process Error exception")


		pyautogui.PAUSE = 3	
		#TODO FIND BUTTON X Y TO JOIN MEEETING
		xPos = 500
		yPos = 700
		DebugObject.Lprint("Pausing for 3 seconds to JOIN meeting and then clicking")
		pyautogui.click(xPos, yPos)
		time.sleep(3)

		# Enter fullscreen after meeting has started
		DebugObject.Lprint("Pausing for 3 seconds to JOIN meeting and then clicking")
		pyautogui.press('esc')

		#TODO FIND BUTTON X Y TO TURN ON CAMERA IF NOT TODO DEFAULT ON
		xPos = 200
		yPos = 1820
		DebugObject.Lprint("Pausing for 3 seconds to JOIN meeting and then clicking")
		pyautogui.click(xPos, yPos)

		#TODO FIND BUTTON X Y TO TURN ON MIC IF NOT TODO DEFAULT ON
		xPos = 100
		yPos = 1820
		DebugObject.Lprint("Pausing for 3 seconds to JOIN meeting and then clicking")
		pyautogui.click(xPos, yPos)

		# Exit fullscreen
		DebugObject.Lprint("Pausing for 3 seconds to press ESC and EXIT full screen Zoom app")
		pyautogui.press('esc')

		# TODO Minimize Zoom app so that Limonada GUI as focus
		# https://support.zoom.us/hc/en-us/articles/201362103-Minimizing-and-exiting-Zoom?mobile_site=true
		# To minimize the Zoom desktop client window so that it continues to run in the background, click on the green circle with the x inside located at the top-right corner of the Zoom window. 
		xPos = 1000
		yPos = 80
		DebugObject.Lprint("Pausing for 3 seconds to press ESC and EXIT full screen Zoom app")
		pyautogui.click(xPos, yPos)


if __name__ == "__main__":

	currentProgramFilename = os.path.basename(__file__)
	DebugObject = Debug(Driver.DEBUG_STATEMENTS_ON, currentProgramFilename)
	DebugObject.Dprint("Starting  Driver.py main()")

	GPIO.setmode(GPIO.BOARD)

	validState = True
	nextState = -1

	if(Driver.DEBUG_STATEMENTS_ON):
		while(validState):
			Driver.toggleHDMIport()
			time.sleep(3)
			Driver.toggleHDMIport()
			time.sleep(3)
			Driver.toggleHDMIport()
			time.sleep(3)

			DebugObject.Dprint("Starting Zoom call and PyAutoGUI")
			Driver.startZoom(DebugObject)
			DebugObject.Dprint("Looping startZoom() test")
			
	while(validState):
		try:
			#nextState = nextStateIs(GUIdrivenState)
			if(nextState == '1'):
				print("TODO")
			elif(nextState == '2'):
				print("TODO")
			elif(nextState == '3'):
				print("TODO")
			elif(nextState == '4'):
				print("TODO")
			elif(nextState == '5'):
				print("TODO")
			else:
				print("INVALID STATE")

			# Pause 10 ms to give CPU extra time in while loop
			time.sleep(0.010)

		except KeyboardInterrupt:
		    GPIO.cleanup()
