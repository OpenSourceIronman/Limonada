# Allow BASH commands to be run inside python code like this file
# https://docs.python.org/3/library/subprocess.html
import subprocess
from subprocess import Popen, PIPE
from subprocess import check_call

import time

# Allow Adafruit FT232H to communicate over USB
import board
import digitalio
import os

import pyautogui

class switch:
	def toggle():
		hdmiNPN = digitalio.DigitalInOut(board.C3)
		hdmiNPN = led.direction = digitalio.Direction.OUTPUT

		hdmiNPN.value = False
		time.sleep(1.5)
		hdmiNPN.value = True


if __name__ == "__main__":
	# Run the following commands in the command line before running
	print("export BLINKA_FT232H=1")
	check_call("export BLINKA_FT232H=1", shell=True)

	#print("python3 -c 'from switch import *; toggle()'")
	#check_call("python3 -c 'from switch import *; toggle()'", shell=True)

	print("Check Call Python3")
	check_call("python3", shell=True)

	# import board
	print("Writing import board")
	check_call("import board", shell=True)
	#pyautogui.write("import board")

	# from pyftdi.ftdi import Ftdi
	pyautogui.write("from pyftdi.ftdi import Ftdi", shell=True)

	# Ftdi().open_from_url('ftdi:///?')
	pyautogui.write("Ftdi().open_from_url('ftdi:///?')")

	# python3
	check_call("python3", shell=True)

	# import os
	pyautogui.write("import os")

	command = 'os.environ["BLINKA_FT232H"]'
	pyautogui.write(command)

	pyautogui.write("import digitialio")
