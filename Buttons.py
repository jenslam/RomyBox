#!/usr/bin/python

#import RPi.GPIO as GPIO
from gpiozero import Button
from signal import pause
import subprocess

def but_shutdown():
	print  "Shtudown"
	subprocess.Popen(["mpc", "stop"])
	subprocess.Popen("poweroff")

def but_reboot():
	print "Reboot"
	subprocess.Popen(["mpc", "stop"])
	subprocess.Popen("reboot")

def but_reset():
	print "reset"
	subprocess.Popen(["service","RomyBox","restart"])

def but_next():
	print "Next"
	subprocess.Popen(["mpc","next"])


def but_prev():
	print "Prev"
	subprocess.Popen(["mpc", "prev"])

def but_pause():
	print "pause"
	subprocess.Popen(["mpc", "toggle"])


#GPIO.setmode(GPIO.BCM)

shut = Button(19, hold_time=2)
#res = Button(19)
next = Button(26)
prev = Button(20)
paus = Button(21, hold_time=5)

shut.when_held = but_shutdown
shut.when_pressed = but_reset
next.when_pressed = but_next
prev.when_pressed = but_prev
paus.when_pressed = but_pause
paus.when_held = but_reboot
print "Warte auf Buttons"

pause()
