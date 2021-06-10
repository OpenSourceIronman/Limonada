#!/usr/bin/env python3
"""
__author__  =  "Blaze Sanders"
__email__   =  "blaze.d.a.sanders@gmail.com"
__company__ =  "Unlimited Custom Creations"
__status__  =  "Development"
__date__    =  "Late Updated: 2021-06-09"
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

# Allow creation of temporary directory to save harddrive space
# https://docs.python.org/3/library/tempfile.html
from tempfile import gettempdir

def launchGUI(framwwork):
	"""

	"""

	if(framework == FLASK):
	elif(framework == QTPY):
	else:


def vendCan():
	"""
	"""

def vendLiquid():

def powerOff():
	"""
	"""

	check_call("sudo shutdown now")

def restart():

def startZoom():

def turnOnMics():

def turnOnCamera()

def takeWFOVpicture():

def scanID():



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

    

