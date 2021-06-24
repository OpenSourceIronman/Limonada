#!/usr/bin/env python3
"""
__author__  =  "Blaze Sanders"
__email__   =  "blaze.d.a.sanders@gmail.com"
__company__ =  "Unlimited Custom Creations"
__status__  =  "Development"
__date__    =  "Late Updated: 2021-06-21"
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
# STILL NEEDED IF ZOOM IS ON MAC MINI? import pyautogui

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

# Allow creation of temporary directory to save harddrive space
# https://docs.python.org/3/library/tempfile.html
from tempfile import gettempdir

# Allow Driver.py to follow the hardware state machine based off GUI process flow
# TODO FUTURE WORD from LimonadaStateMachine import *

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

	# GUI framework CONSTANTS
	FLASK = 0
	QTPY = 1
	VEND4YOU = 2

	# Function return and debugging helper CONSTANTS
	OK = 1
	NOT_OK = 0
	HIGH = 1
	LOW = 0
	DEBUG_STATEMENTS_ON = True
	THIS_CODES_FILENAME = os.path.basename(__file__)

	# Zoom Vidoe & Audio CONSTANTS
	MISSION_CONTROL_ZOOM_URL = "https://us04web.zoom.us/j/2770448765?pwd=MUVJWGZUelJHMmNuYW4xL0hndjdHQT09"
	ZOOM_MEETING_ID = 2770448765
	ZOOM_PASSCODE = "8ND3ae"


	def __init__(self, state):
		"""
		#TODO Only need this if using python-statemachine library
		"""
		self.state = state

	def unitTest():
		print("Starting Limonada Driver.py Unit Test")

		# Rotate screen into portrait mode
		# https://www.raspberrypi.org/forums/viewtopic.php?t=212008
		check_call("xrandr --output HDMI-1 --primary --mode 1920x1080 --pos 0x0 --rotate right --output DP-1 --off", shell=True)


		modelObj = Driver(state='-2')
		kiosk =  LimonadaStateMachine() #(modelObj)
		print("Boot Screen is STATE =", modelObj.state)

		kiosk.Desktop_To_Zoom()
		print("Zoom Screen is STATE =", modelObj.state)


		kiosk.Zoom_To_AppHomeScreen()
		lauchGUI(QTPY)


	def launchGUI(framework):
		"""
    	TODO

    	Key arguments:
   		framework -- INTERGER: Global CONSTANT for GUI framework this code should launch in parallel

    	Return:
    	OK if GUI was launched succesfully, and NOT_OK otherwise
		"""

		if(framework == VEND4YOU):
			print("CMS")
		elif(framework == FLASK):
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

	def switchHDMIto(portNumber):
		"""
		TODO
		# https://raspberrypi.stackexchange.com/questions/99823/rpi-uart-control-ir-remote-hdmi-switch-problem

		BOM TO PURCHASE
		IR LED 5mm (940nm) - TSAL6200
		IR Receiver Module (3.3V type) - TSOP38238
		2N2222 NPN transistor
		36 Ohm 1/4W Resistor
		680 Ohm 1/4W Resistor
		10K Ohm 1/4W Resistor

		Key argument(s):
		portNumber -- INTERGER: HDMI input to use to driver ouput on HDMI switcher ASIN: B0739GSKV2
		https://www.amazon.com/dp/B0739GSKV2/?coliid=I1G5FSDF5QEW1I&colid=1YXO1OO36TF2L&psc=1&ref_=lv_ov_lig_dp_it

		Return:
		True if ALL the steps to switch HMDI input where successfull; False otherwise
		"""

		successfullSwitch = False

		if(portNumber == 1):
			portPin = BCM1
			successfullSwitch = True
		elif(portNumber == 2):
			portPin = BCM1
			successfullSwitch = True
		else:
			DebugObject = Debug(DEBUG_STATEMENTS_ON, THIS_CODES_FILENAME)
			DebugObject.Dprint("INVALID HDMI port number passed as parameter to Driver.switchHDMIto()")

		GPIO.cleanup()
		GPIO.setup(portPin, GPIO.OUT, initial=GPIO.LOW)
		GPIO.output(portPin, HIGH)

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


if __name__ == "__main__":

	currentProgramFilename = os.path.basename(__file__)
	DebugObject = Debug(Driver.DEBUG_STATEMENTS_ON, currentProgramFilename)
	DebugObject.Dprint("Starting  Driver.py main()")

	GPIO.setmode(GPIO.BOARD)

	if(Driver.DEBUG_STATEMENTS_ON):
		#Driver.unitTest()
		print("Uncomment unitTest()?")
	# Hardware back-end driver that launches GUI front-end
	# TODO @Murali - OF DOES GUI front-end driver call into back-end?

	validState = True
	nextState = -1

	while(validState):
		try:
			#nextState = nextStateIs(GUIdrivenState)
			if(nextState == '1'):
				print("TODO")
				#kiosk.currentState = LimonadaStateMachine.qtpyHomeScreen
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
			time.sleep(0.010)

		except KeyboardInterrupt:
		    GPIO.cleanup()
