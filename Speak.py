#!/usr/bin/env python3
"""
__author__  =  "Blaze Sanders"
__email__   =  "blaze.d.a.sanders@gmail.com"
__company__ =  "Unlimited Custom Creations"
__status__  =  "Development"
__date__    =  "Late Updated: 2021-06-09"
__doc__     =  "Class to utlize AWS Polly for voice generation "
"""

# Sample code Speak.py is based off
# https://docs.aws.amazon.com/polly/latest/dg/get-started-what-next.html

# Allow the use of the AWS SDK in Python
# https://pypi.org/project/boto3/
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError

# Allow the closing of an audio stream to reduce AWS costs
#https://docs.python.org/3/library/contextlib.html
from contextlib import closing

# Allow program to extract filename of the current file and exit gracefully
# https://docs.python.org/3/library/os.html
import os
import sys

# Allow BASH commands to be run inside python code like this file
# https://docs.python.org/3/library/subprocess.html
import subprocess

# Allow creation of temporary directory to save harddrive space
# https://docs.python.org/3/library/tempfile.html
from tempfile import gettempdir

# Allow 'dependency-free' playback of .wav audio on Linux, MacOS, &> 17 # https://simpleaudio.readthedocs.io/en/latest/
import simpleaudio as sa


class Speak:

	# Spanish Voice CONSTANTS
	#TODO  Use Google Translate OR human translator to convert engligh text below
	BAD_ACCENT_TEXT = ""

	# English Voice CONTANTS
	STATE_0_TEXT = ""
	BAD_ACCENT_TEXT = "Close but its pronouced lee-me-nod-da"


	WORKING_TEXT = "We will have your drink in just a few seconds."
	COUNTDOWN_TEXT = "5, 4, 3, 2, 1"
	PRODUCT_DISPENSE_TEXT = "Here is your Limonada, enjoy!"
	STATE_10_TEXT = ""


	def __init__(self, text, voiceId):
		"""
		Constructor to initialize an Speak object
		Defaults to TODO if invalid voiceId variable is passed

		Key arguments:
		self -- Newly created Speak() object
		text -- TODO
		voiceID -- AWS Polly coice configuration to be spoken

		Object instance variables:
		voiceRepliesDict -- DICTIONARY: A Collection of valid sound> 94         engineSoundID -- INT: Unique ID for TODO

		Return:
		New Speak() object
		"""

		thisCodesFilename = os.path.basename(__file__)
		self.DebugObject = Debug(True, thisCodesFilenam)

		# UPDATE this dictionary, Speak.py global  CONSTANTS,
		# and the ~/Limonada/Sounds folder to add new sounds
		self.voiceRepliesDict = {
			Speak.???: 0,
			Speak.???: 1,
			Speak.???: 2,
			Speak.???: 3,
			Speak.???: 4,
			Speak.???: 5,
			Speak.???: 6
		}
