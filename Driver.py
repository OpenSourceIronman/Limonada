#!/usr/bin/env python3
"""
__author__  =  "Blaze Sanders"
__email__   =  "blaze.d.a.sanders@gmail.com"
__company__ =  "Unlimited Custom Creations"
__status__  =  "Development"
__date__    =  "Late Updated: 2021-06-13"
__doc__     =  "Logic to run back-end services via state changes in GUI"
"""

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

# Allow control of mouse & keyboard to start Zoom app and meeting
# https://pyautogui.readthedocs.io/en/latest/
import pyautogui

# Allow creation of temporary directory to save harddrive space
# https://docs.python.org/3/library/tempfile.html
from tempfile import gettempdir


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
MISSION_CONTROL_ZOOM_URL = ""


def start():
	"""
	Hardware back-end driver that launches GUI front-end
	#TODO @Murali - OF DOES GUI front-end driver call into back-end?
	"""
	print("CODE STARTS RUNNING HERE")

	lauchGUI(QTPY)

	validState = True

	while(validState):
		stateMachine()

def unitTest():
	print("Starting Driver.py Unit Test")


def launchGUI(framework):
	"""
    #TODO

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
		vendPin = SHIELD_PIN_1")
	elif(productID == GIFT_CARD_IN_CAN):
		vendPin = SHIELD_PIN_2")
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

	if(itemSensed = HIGH):
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
	"""
	# https://superuser.com/questions/1563255/start-a-zoom-meeting-from-the-command-line
	#TODO REMOVE check_call("sudo zoom", shell=True)

	# Start Zoom application and minimize to give ordering GUI screen
	command =  "xdg-open " + MISSION_CONTROL_ZOOM_URL
	check_call(command, shell=True)
	pyautogui.press('f10') 		# Fullscreen so mouse can click "Join Meeting" button

	#TODO FIND BUTTON LOCATIO
	time.pause(3)
	X_POS = 500
	Y_POS = 700
	pyautogui.click(XPOS, YPOS)
	time.pause(3)


def takeWFOVpicture():
	"""
	"""
	img = ComputerVision.ScanQRcode(CAM2)


def scanID():
	"""
	"""
	#Tapmotic - v2020.0/ComputerVision directory?
	img = ComputerVision.ScanQRcode(CAM2)


def stateMachine(nextState):
	"""
	Control for branching Limonada state machine defined at:
	https://lucid.app/lucidchart/a8d9b1e9-b963-4709-b8cf-a47e7ee67a6e/edit?beaconFlowId=3D4DF78ED9E6E012&page=0_0#

	TODO pip install python-statemachine

    Key arguments:
   	currentState -- INTERGER: Current state that GUI is in
    nextState -- INTERGER:  State that GUI would like driver.py to move to

    Return:
    Next state GUI should move to
    """

    

