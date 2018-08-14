#!/usr/bin/python
from CardList import CardList
from Player import Player
from logger import Logger
from pirc522 import RFID
import sys
import RPi.GPIO as GPIO
import signal
import time


#reader = Reader()
cardlist = CardList()
player = Player()
rdr = RFID()


continue_reading = True

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
	global continue_reading
	print "Ctrl+C captured, ending read."
	continue_reading = False
	rdr.cleanup()
	GPIO.cleanup()
	sys.exit()

def startup():
	global player	
	player.load("Startup")
	Logger.logr.info("Play Start up sound")

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

startup()
Logger.logr.info('Ready: place a card on top of the reader')

last_card = ' '

while continue_reading:
	rdr.wait_for_tag()

	(error, data) = rdr.request()
	if not error:
		Logger.logr.debug("Detected: %s" , format(data, "02x"))
    		(error, uid) = rdr.anticoll()
		if not error:
			card = str(uid[0]) + str(uid[1]) + str(uid[2]) + str(uid[3])
			if card != ' ':
				if card != last_card:
					print last_card, card
					plist = cardlist.getPlaylist(card)
					if plist != '':
						Logger.logr.info("Starte Playlist: %s ", plist)
						player.add(plist)
					last_card = card
				else:
					Logger.logr.info("Laeuft schon.. Locker bleiben")
			time.sleep(1)
