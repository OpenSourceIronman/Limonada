#!/usr/bin/env python3
"""
"""

BOARD = 1
OUT = 1
IN = 0

HIGH = 1
LOW = 0

def setmode(a):
   print(a)

def setup(a, b):
   print(a)

def output(pin, state):
   print("Simulated: ", state, "output on pin /#", pin)

def input(pin):
	state = LOW
	print("Simulated: ", state, "sensed on input pin /#", pin)

def cleanup():
   print("Cleaning up all simulated input & output pins")

def setwarnings(flag):
   print(False)
