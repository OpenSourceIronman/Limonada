#!/usr/bin/env python3
"""
__author__  =  "Blaze Sanders"
__email__   =  "blaze.d.a.sanders@gmail.com"
__company__ =  "Unlimited Custom Creations"
__status__  =  "Development"
__date__    =  "Late Updated: 2021-06-14"
__doc__     =  "Process flow state machine for hardware & GUI syncing"
"""

# This state machine allow syncing the process flow between hardware and GUI
# https://pypi.org/project/python-statemachine/
from statemachine import StateMachine, State

class LimonadaStateMachine(StateMachine):

	# Lucid diagram for Limonada State Machine
	# https://lucid.app/lucidchart/a8d9b1e9-b963-4709-b8cf-a47e7ee67a6e/edit?beaconFlowId=3D4DF78ED9E6E012&page=0_0#

	# Custom portrait mode boot (aka splash) screen
	# https://www.raspberrypi.org/forums/viewtopic.php?t=212008
	# https://keytosmart.com/single-board-computers/raspberry-pi/custom-splash-screen-for-raspberry-pi-raspbian/
	piBootScreen = State('-2', initial=True)

	# Standard Pi Desktop in portrait mode
	# https://www.raspberrypi.org/forums/viewtopic.php?t=224229
	piDesktopScreen = State('-1')

	# Full Screen Zoom application
	# TODO Should this be in portrait mode also?
	zoomScreen = State('0')

	# First QTPY GUI screen
	qtpyHomeScreen = State('1')
	voiceBubbleScreen = State('2')
	buttonScreen = State('3')
	vendScreen = State('4')
	endScreen = State('5')


	Desktop_To_Zoom = piDesktopScreen.to(zoomScreen)
	Zoom_To_AppHomeScreen = zoomScreen.to(qtpyHomeScreen)

