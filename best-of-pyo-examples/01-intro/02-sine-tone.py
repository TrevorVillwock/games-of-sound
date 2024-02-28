"""
02-sine-tone.py - The "hello world" of audio programming!

This script simply plays a 1000 Hz sine tone.

"""
from pyo import Server

# Creates and boots the server.
# The user should send the "start" command from the GUI.
s = Server().boot()

# This tells pyo to place the recording in the same directory as the file and name it test.wav
s.recordOptions(filename = "./test.wav")


# Drops the gain by 20 dB.
s.amp = 0.1

# Creates a sine wave player.
# The out() method starts the processing
# and sends the signal to the output.
a = Sine().out()

# Opens the server graphical interface.
s.gui(locals())
