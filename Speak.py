#!/usr/bin/env python3
"""
__author__  =  "Blaze Sanders"
__email__   =  "blaze.d.a.sanders@gmail.com"
__company__ =  "Unlimited Custom Creations"
__status__  =  "Development"
__date__    =  "Late Updated: 2021-06-19"
__doc__     =  "Class to utlize sox and AWS Polly for voice generation "
"""

# sudo apt install sox

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
from subprocess import Popen, PIPE
from subprocess import check_call

# Allow creation of temporary directory to save harddrive space
# https://docs.python.org/3/library/tempfile.html
from tempfile import gettempdir

# Allow 'dependency-free' playback of .wav audio on Linux, MacOS, &> 17 # https://simpleaudio.readthedocs.io/en/latest/
import simpleaudio as sa

# Allow the control of the space-time fabric :)
# Allow pausing of code so that programmers can read terminal output
# https://docs.python.org/3/library/time.html
import time

# Generate .txt data logging and custom terminal debugging output
from Debug import *


class Speak:

	# Spanish Voice CONSTANTS
	SPAN_SCENE_1 = "SpanishReplyToScene1.wav"
	SPAN_SCENE_2 = "SpanishReplyToScene2.wav"
	SPAN_SCENE_3 = "SpanishReplyToScene3.wav"
	SPAN_SCENE_4 = "SpanishReplyToScene4.wav"
	SPAN_SCENE_5 = "SpanishReplyToScene5.wav"

	# English Voice CONTANTS
	ENG_SCENE_1 = "EnglishReplyToScene1.wav"
	ENG_SCENE_2 = "EnglishReplyToScene2.wav"
	ENG_SCENE_3 = "EnglishReplyToScene3.wav"
	ENG_SCENE_4 = "EnglishReplyToScene4.wav"
	ENG_SCENE_5 = "EnglishReplyToScene5.wav"

	#TODO  Use Google Translate OR human translator to convert engligh text below
	ENG_BAD_ACCENT_TEXT = "Close but its pronouced lee-me-nod-da"
	SPAN_BAD_ACCENT_TEXT = ""
	WORKING_TEXT = "We will have your drink in just a few seconds."
	COUNTDOWN_TEXT = "5, 4, 3, 2, 1"
	PRODUCT_DISPENSE_TEXT = "Here is your Limonada, enjoy!"

	NULL = -1
	SOX = 0
	AWS = 1
	SIMPLE_AUDIO
	STATE_0_TEXT = ""
	STATE_9_TEXT = ""


	def unitTest():

		TestObject1 = Speak(Speak.ENG_SCENE_2, Speak.SIMPLE_AUDIO)
		TestObject1.say()

		time.sleep(3)

	def __init__(self, text, voiceId):
		"""
		Constructor to initialize an Speak object
		Defaults to TODO if invalid voiceId variable is passed

		Key arguments:
		self -- Newly created Speak() object
		text -- TODO
		voiceID -- AWS Polly coice configuration to be spoken

		Object instance variables:
		voiceRepliesDict -- DICTIONARY: A Collection of valid sound clips

		Return:
		New Speak() object
		"""

		thisCodesFilename = os.path.basename(__file__)
		self.DebugObject = Debug(True, thisCodesFilename)

		# UPDATE this dictionary, Speak.py global CONSTANTS,
		# and the ~/Limonada/Audio folder to add new clips
		self.voiceRepliesDict = {
			Speak.ENG_BAD_ACCENT_TEXT: 0,
			Speak.ENG_SCENE_1: 1,
			Speak.ENG_SCENE_2: 2,
			Speak.ENG_SCENE_3: 3,
			Speak.ENG_SCENE_4: 4,
			Speak.ENG_SCENE_5: 5,
			Speak.NULL: 6,
			Speak.NULL: 7,
			Speak.NULL: 8,
			Speak.NULL: 9,
			Speak.SPAN_BAD_ACCENT_TEXT: 10,
			Speak.SPAN_SCENE_1: 11,
			Speak.SPAN_SCENE_2: 12,
			Speak.SPAN_SCENE_3: 13,
			Speak.SPAN_SCENE_4: 14,
			Speak.SPAN_SCENE_5: 15,
			Speak.NULL: 16
		}

		self.soundId = self.voiceRepliesDict[text]
		pathEnding = "./Audio/" + text
		#REMOVE print("Fullpath = ", fullpath)
		#REMOVE self.filePath = os.path.basename(fullpath)
		#print("filePath = ", self.filePath)
		#WORKS self.SoundObject = sa.WaveObject.from_wave_file("./EnglishReplyToScene1.wav")
		self.SoundObject = sa.WaveObject.from_wave_file(pathEnding)
		self.DebugObject.Dprint("Audio clip found in dictionary")


	def say(self):
		"""
		"""
		playObj = self.SoundObject.play()
		playObj.wait_done()

		#check_call("cd Audio", shell=True)
		#check_call("play EnglishReplayToScene1.wav", shell=True)

		#sox_message = "play ./Audio/" + filename
		#print(sox_message)

		#test = 'play ./Audio/EnglishReplayToScene2.wav'

		#check_call(test, shell=True)
		#check_call(sox_message, shell=True)


if __name__ == "__main__":
	Speak.unitTest()
