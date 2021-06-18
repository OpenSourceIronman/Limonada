#!/usr/bin/env python3
"""
__author__  =  "Blaze Sanders"
__email__   =  "blaze.d.a.sanders@gmail.com"
__company__ =  "Unlimited Custom Creations"
__status__  =  "Development"
__date__    =  "Late Updated: 2021-06-14"
__doc__     =  "Logic to run back-end services via state changes in GUI"
"""

# TODO ONLY IF MEDIA COMPUTER IS NOT USED
# Connect microphone to Raspberry Pi
# https://pimylifeup.com/raspberrypi-microphone/
# Connect camera to Raspberry Pi
# https://www.hackster.io/shahizat005/getting-started-with-raspberry-pi-camera-8eec28
# https://www.e-consystems.com/4k-usb-camera.asp
# Allow control of mouse & keyboard to start Zoom app and meeting
# https://pyautogui.readthedocs.io/en/latest/
import pyautogui


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

# Allow the control on high power relay shield
# https://www.amazon.com/KEYESTUDIO-4-Channel-Shield-Expansion-Raspberry/dp/B072XGF4Z3
import RPi.GPIO as GPIO

# Allow creation of temporary directory to save harddrive space
# https://docs.python.org/3/library/tempfile.html
from tempfile import gettempdir

# Allow Driver.py to follow the hardware state machine based off GUI process flow
from LimonadaStateMachine import *

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

# GUI framework CONSTANTS
FLASK = 0
QTPY = 1

# Function return and debugging helper CONSTANTS
OK = 1
NOT_OK = 0
HIGH = 1
LOW = 0
DEBUG_STATEMENTS_ON = True
THIS_CODES_FILENAME = os.path.basename(__file__)

# Zoom Vidoe & Audio CONSTANTS
MISSION_CONTROL_ZOOM_URL = "https://us04web.zoom.us/j/2770448765?pwd=MUVJWGZUelJHMmNuYW4xL0hndjdHQT09"
MISSION_CONTROL_MEETING_ID = 2770448765
MISSION_CONTROL_ZOOM_PASSCODE = 8ND3ae


class Driver(object):

	def __init__(self, state):
		self.state = state

	def unitTest():
		print("Starting Limonada Driver.py Unit Test")


	def launchGUI(framework):
		"""
    	TODO

    	Key arguments:
   		framework -- INTERGER: Global CONSTANT for GUI framework this code should launch in parallel

    	Return:
    	OK if GUI was launched succesfully, and NOT_OK otherwise
		"""

		if(framework == FLASK):
			Debug.Dprint("GUI generated using Flask microframework")
			#TODO Launch GUI.py on 2nd Pi or 2nd thread
			return OK
		elif(framework == QTPY):
			Debug.Dprint("GUI generated using QTPY framework")
			#TODO Launch GUI.py on 2nd Pi or 2nd thread
			return OK
		else:
			Debug.Dprint("LIKE A DIFFERENT GUI BUILDER? SUBMIT PULL REQUEST")

		return NOT_OK


	def vend(productID):
		"""
    	#TODO

    	Key argument(s):
   		productID -- INTERGER: Unique ID for each type on Limonada can flavor

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


	def startZoom():
		"""
		Use this start Zoom app, full screen it, and then pyautogui click to start meeting
		https://support.zoom.us/hc/en-us/articles/205683899-hot-keys-and-keyboard-for-zoom
		https://superuser.com/questions/1563255/start-a-zoom-meeting-from-the-command-line
		"""

		# Start Zoom application and minimize to give ordering GUI screen
		command =  "xdg-open " + MISSION_CONTROL_ZOOM_URL
		check_call(command, shell=True)


		#TODO FIND BUTTON X Y TO JOIN MEEETING
		time.pause(3)
		X_POS = 500
		Y_POS = 700
		pyautogui.click(XPOS, YPOS)
		time.pause(3)

		# Enter fullscreen after meeting has started
		pyautogui.press('esc')

		#TODO FIND BUTTON X Y TO TURN ON CAMERA IF NOT TODO DEFAULT ON
		time.pause(3)
		X_POS = 200
		Y_POS = 1820
		pyautogui.click(XPOS, YPOS)
		time.pause(3)

		#TODO FIND BUTTON X Y TO TURN ON MIC IF NOT TODO DEFAULT ON
		time.pause(3)
		X_POS = 100
		Y_POS = 1820
		pyautogui.click(XPOS, YPOS)
		time.pause(3)

		# Exit fullscreen
		pyautogui.press('esc')

		# TODO Minimize Zoom app so that Limonada GUI as focus
		# https://support.zoom.us/hc/en-us/articles/201362103-Minimizing-and-exiting-Zoom?mobile_site=true
		# To minimize the Zoom desktop client window so that it continues to run in the background, click on the green circle with the x inside located at the top-right corner of the Zoom window. 
		time.pause(3)
		X_POS = 1000
		Y_POS = 80
		pyautogui.click(XPOS, YPOS)
		time.pause(3)


if __name__ == "_main_":

	# Hardware back-end driver that launches GUI front-end
	# TODO @Murali - OF DOES GUI front-end driver call into back-end?

	# Rotate screen into portrait mode
	# https://www.raspberrypi.org/forums/viewtopic.php?t=212008
	check_call("xrandr --output HDMI-1 --primary --mode 1920x1080 --pos 0x0 --rotate right --output DP-1 --off", shell=True)


	driverObj = Driver(state='-2')
	kiosk =  LimonadaStateMachine(driverObj)
	print("Boot Screen is STATE /#")
	print(driverObj.state)

	kiosk.Desktop_To_Zoom()
	print("Zoom Screen is STATE /#")
	print(driverObj.state)

	kiosk.Zoom_To_AppHomeScreen()
	lauchGUI(QTPY)

	validState = True

	while(validState):

		nextState = nextStateIs(GUIdrivenState)
		if(nextState == '1'):
			kiosk.currentState = LimonadaStateMachine.qtpyHomeScreen
			#kiosk.run(qtpyHomeScreen)
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
		time.pause(0.010)
