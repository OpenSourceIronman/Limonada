#!/usr/bin/env python3
"""
__author__  =  "Blaze Sanders"
__email__   =  "blaze.d.a.sanders@gmail.com"
__company__ =  "Unlimited Custom Creations"
__status__  =  "Development"
__date__    =  "Late Updated: 2021-06-14"
__doc__     =  "Process flow state machine for hardware & GUI syncing"
"""

# Use a state machine to sync the process flow betwwen hardware and GUI
# https://pypi.org/project/python-statemachine/
from statemachine import StateMachine, State

class LimonadaStateMachine(StateMachine):

	bootScreen = State('-1', initial=True)
	zoomScreen = State('0')
	homeScreen = State('1')
	voiceBubbleScreen = State('2')
	buttonScreen = State('3')
	vendScreen = State('4')
	endScreen = State('5')
