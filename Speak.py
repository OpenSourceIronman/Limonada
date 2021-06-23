#!/usr/bin/env python3
"""
__author__  =  "Blaze Sanders"
__email__   =  "blaze.d.a.sanders@gmail.com"
__company__ =  "Unlimited Custom Creations"
__status__  =  "Development"
__date__    =  "Late Updated: 2021-06-23"
__doc__     =  "Class to utlize simple audio and AWS Polly for voice generation "
"""

# Allow the use of the AWS SDK in Python
# https://pypi.org/project/boto3/
# https://docs.aws.amazon.com/polly/latest/dg/get-started-what-next.html
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError

# Allow the closing of an audio stream to reduce AWS costs
#https://docs.python.org/3/library/contextlib.html
from contextlib import closing

# Allow program to extract filename of the current file and exit gracefully
# https://docs.python.org/3/library/os.html
import os
import sys

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
	ENG_ONE_MORE_TIME_TEXT = "You think thats Spanish, no way TODO Joseph one more time. "
	SPAN_ONE_MORE_TIME_TEXT = "TODO"

	ENG_SPAN_TRY_AGAIN_TEXT = "Nope, try again por favor."
	ENG_TRY_AGAIN_TEXT = "Nope, try again"
	SPAN_TRY_AGAIN_TEXT = "TODO"

	SPAN_ENG_ANOTHER_TRY = "TODO, come on give it another try."
	ENG_ANOTHER_TRY = "come on give it another try."
	SPAN_ANOTHER_TRY = "TODO"

	SPAN_ENG_TRUE_MEXICAN_DRINK = "TODO!TODO. For a Spanish speaker a true Mexican drink."
	ENG_TRUE_MEXICAN_DRINK = "For a Spanish speaker a true Mexican drink."
	SPAN_TRUE_MEXICAN_DRINK = "TODO"

	SPAN_ENG_YOU_DESERVE = "TODO. You deserve a Corona lee ma nod da. Salut!"
	ENG_YOU_DESERVE = "You deserve a Corona Limonada"
	SPAN_YOU_DESERVE_PART_1 = "TODO"
	SPAN_YOU_DESERVE_PART_2 = "TODO"

	ENG_COME_ON =  "ENG_COME_ON.wav" # Come on! Show me you know more than nachos in Spanish, try again.
	SPAN_COME_ON = "TODO"

	ENG_SPAN_NOPE = "ENG_SPAN_NOPE.wav" # Nope, but TODO"
	ENG_NOPE = "Nope, but"
	SPAN_NOPE = "TODO"

	ENG_NO_ACCENT_HERE_IS_LIMONADA = "No TODO here is a Corona Limonada for you."

	ENG_SORRY_HERE_IS_DUOLINGO = "Sorry, but that is TODO for you. TODO here take a DuoLingo subscription for you to improve."

	SPAN_ENG_HEY_DUOLINGO = "TODO. Hey you just got a DuoLingo subscription to learn Spanish."
	SPAN_HEY_DUOLINGO = "TODO"
	ENG_HEY_DUOLINGO = "Hey you just got a DuoLingo subscription to learn Spanish."


	WORKING_TEXT = "We will have your drink in just a few seconds."
	COUNTDOWN_TEXT = "5, 4, 3, 2, 1"
	PRODUCT_DISPENSE_TEXT = "Here is your Limonada, enjoy!"

	NULL = -1
	SOX = 0
	AWS = 1
	SIMPLE_AUDIO = 2

	STATE_0_TEXT = ""
	STATE_9_TEXT = ""


	def unitTest():

		TestObject1 = Speak(Speak.ENG_COME_ON, Speak.SIMPLE_AUDIO)
		TestObject1.say()
		time.sleep(3)


		TestObject2 = Speak(Speak.ENG_SPAN_NOPE, Speak.SIMPLE_AUDIO)
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
			Speak.ENG_ONE_MORE_TIME_TEXT: 0,
			Speak.SPAN_ONE_MORE_TIME_TEXT: 1,
			Speak.ENG_SPAN_TRY_AGAIN_TEXT: 2,
			Speak.ENG_TRY_AGAIN_TEXT: 3,
			Speak.SPAN_TRY_AGAIN_TEXT: 4,
			Speak.SPAN_ENG_ANOTHER_TRY: 5,
			Speak.ENG_ANOTHER_TRY: 6,
			Speak.SPAN_ANOTHER_TRY: 7,
			Speak.SPAN_ENG_TRUE_MEXICAN_DRINK: 8,
			Speak.ENG_TRUE_MEXICAN_DRINK: 9,
			Speak.SPAN_TRUE_MEXICAN_DRINK: 10,
			Speak.SPAN_ENG_YOU_DESERVE: 11,
			Speak.ENG_YOU_DESERVE: 12,
			Speak.SPAN_YOU_DESERVE_PART_1: 13,
			Speak.SPAN_YOU_DESERVE_PART_2: 15,
			Speak.ENG_COME_ON: 16,
			Speak.SPAN_COME_ON: 17,
			Speak.ENG_SPAN_NOPE: 18,
			Speak.ENG_NOPE: 19,
			Speak.SPAN_NOPE: 20,
			Speak.ENG_NO_ACCENT_HERE_IS_LIMONADA: 21,
			Speak.ENG_SORRY_HERE_IS_DUOLINGO: 22,
			Speak.SPAN_ENG_HEY_DUOLINGO: 23,
			Speak.SPAN_HEY_DUOLINGO: 24,
			Speak.ENG_HEY_DUOLINGO: 25
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
