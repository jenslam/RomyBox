from CardList import CardList
#from Reader import Reader
from logger import Logger
import signal
import sys
import RPi.GPIO as GPIO
from pirc522 import RFID
import time
#reader = Reader()
cardList = CardList()
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

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)


while continue_reading:
	print 'Place the card in the reader'
	rdr.wait_for_tag()
	(error, data) = rdr.request()
	if not error:
                Logger.logr.debug("Detected: %s" , format(data, "02x"))
		(error, uid) = rdr.anticoll()
		if not error:
			card = str(uid[0]) + str(uid[1]) + str(uid[2]) + str(uid[3])
			Logger.logr.info("Card: %s detected", card)
                        if card != ' ':
	        		plist=raw_input('Playlist Link, q to quit: ')
        			if plist=="q":
                			break
        			pname=raw_input('Playlist Name, q to quit: ')
        			if plist=="q":
                			break
				cardList.addPlaylist(card, plist, pname)
				Logger.logr.info("Card added!")
				card = ' '
				time.sleep(1)
