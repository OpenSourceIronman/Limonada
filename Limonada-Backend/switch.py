# Allow Adafruit FT232H to communicate over USB 
import board
import digitalio
import os

# Allow BASH commands to be run inside python code like this file
# https://docs.python.org/3/library/subprocess.html
import subprocess
from subprocess import Popen, PIPE
from subprocess import check_call

import time

def toggle():
	hdmiNPN = digitalio.DigitalInOut(board.C3)
	hdmiNPN = led.direction = digitalio.Direction.OUTPUT

	hdmiNPN.value = False
	time.sleep(1.5)
        hdmiNPN.value = True


if __name__ == "__main__":
	# Run the following commands in the command line before running$	
	# export BLINKA_FT232H=1
	check_call("export BLINKA_FT232H=1", shell=True")

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

                successfullSwitch = False
                led = digitalio.DigitalInOut(board.D7)
                led = led.direction = digitalio.Direction.OUTPUT

                led.value = False
                time.sleep(1.5)
                led.value = True

                successfullSwitch = True

                return successfullSwitch
