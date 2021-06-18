#!/usr/bin/env python3
"""
__author__ =  "Blaze Sanders"
__email__ =   "blaze.d.a.sanders@gmail.com"
__company__ = "Unlimited Custom Creations"
__status__ =  "Development"
__date__ =    "Late Updated: 2021-06-18"
__doc__ =     "Setup a new Limonada dev enviroment using VirtualEnv"
"""


# Hardware that code can run on CONSTANTS (WINDOWS IS NOT SUPPORTED!)
PI_4     = "Pi4"     # Raspberry Pi 4
LINUX_PC = "LinuxPC" # Intel CPU Personal Computer
MAC_OS   = "M1Mac"   # M1 Mac Personal Computer


# Allow for easy command-line install of all TesMuffler dependencies
# https://docs.python.org/3/library/argparse.html
import argparse

# Allow pausing of code so that programmers can read terminal output
# https://docs.python.org/3/library/time.html
import time

# Allow BASH commands to be run inside python code like this file
# https://docs.python.org/3/library/subprocess.html
import subprocess
from subprocess import Popen, PIPE
from subprocess import check_call


if __name__ == "__main__":

	parser = argparse.ArgumentParser(prog = "Trying to install Limonada BackEnd Software", description = __doc__, add_help=True)
	parser.add_argument("-d", "--device", type=str, default= PI_4, choices=[PI_4, LINUX_PC, MAC_OS], help="Select the hardware code is running on")
	args = parser.parse_args()

	hardware = args.device

	# Clear terminal and prompt user of next steps
	check_call("clear",shell=True)
	print("Starting Limonada install inside a virtual enviroment and performing system update!")
	print("Press CTRL-Z now to cancel install and system updates")
	for countdown in range(10, 0, -1):
		print(countdown)
		time.sleep(1)
	print("LIFTOFF!")


	# Check and update your system
	check_call("sudo apt update", shell=True)
	check_call("sudo apt upgrade", shell=True)


	# Install PIP3 and update setuptools
	check_call("sudo apt install python3-pip", shell=True)
	check_call("pip install --upgrade pip setuptools", shell=True)


	# Start autoconfiguring a virtual enviroment like a good programmer should :)
	# https://www.geeksforgeeks.org/python-virtual-environment/
	check_call("sudo apt install python3-virtualenv", shell=True)
	check_call("virtualenv --version", shell=True)
	time.sleep(2)
	check_call("virtualenv LimomadaDevEnv", shell=True)
	# Specifiy Python 3 interpreter to stay away from all things Python 2!
	check_call("virtualenv -p /usr/bin/python3 LimonadaDevEnv", shell=True)

	# Start / activate the virtual enviroment setup above
	# Important to do this before any "pip3 install" commands
	try:
		#TODO https://www.reddit.com/r/Python/comments/5lift9/how_to_activatedeactivate_virtualenv_on_linux/
		check_call("sudo . LimonadaDevEnv/bin/activate", shell=True)
		#TODO https://stackoverflow.com/questions/8052926/running-subprocess-within-different-virtualenv-with-python
		#check_call("source LimonadaDevEnv/bin/activate", shell=True)
	except subprocess.CalledProcessError as e:
		print()
		print()
		print("Beginner: LimonadaDevEnv was configured correctly using the 'source' command")
		print("Expert: source returned a non-zero exit status as expected \n\n")

	print("\n\nIf you would like to TURN OFF the Limonada Virtual Enviroment (BAD IDEA) run the 'deactivate' command\n\n")
	time.sleep(7)


	# Allow ?TODO?
	check_call("pip3 install python-statemachine", shell=True)


	# Allow the playing of .WAV or .MP3 files
	# https://simpleaudio.readthedocs.io/en/latest/capabilities.html
	check_call("sudo apt-get install -y python3-dev libasound2-dev", shell=True) 	# Only simpleaudio dependency
	check_call("pip install simpleaudio", shell=True)

	if(hardware == PI_4):

		# Allow Python code to interface via SDK to AWS services like S3, Polly, Lex, and EC2
		# https://pypi.org/project/boto3/
		check_call("pip3 install boto3", shell=True)

		# Allow other computers to SSH into Pi running this code
		# Needed since SSH is not always installed on Pi distros
		check_call("sudo apt install openssh-server", shell=True)
		check_call("sudo apt install sshguard", shell=True)

		# Allow low level control on GPIO pins to drive RFID Readers, Servos, Motors, Relays, LEDs, etc
		# Python 3 install of GPIO and servo to match Flask
		# https://pypi.org/project/RPi.GPIO/
		check_call("pip3 install RPi.GPIO", shell=True)
		#TODO REMOVE IF RPi DOESNOT HAVE ENOUGH FEATURES check_call("sudo apt install python3-gpiozero", shell=True)
		#https://gpiozero.readthedocs.io/en/stable/installing.html

	elif(hardware == LINUX_PC):

		# Install simple command line TODO .MP3 or .WAV audio player
		check_call("sudo apt install sox", shell=True) # CLI command is "play file.wav"

	else:
		print("INVALID CLI ARGUMENTS: 'python3 install -d LinuxPC' is valid for example")

	print("\n\nRUN 'source LimonadaDevEnv/bin/activate' command please...")

	#check_call("", shell=True)
	#check_call("", shell=True)
	#check_call("", shell=True)
	#check_call("", shell=True)
	#check_call("", shell=True)
