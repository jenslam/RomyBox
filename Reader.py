import RPi.GPIO as GPIO
import libs.MFRC522 as MFRC522
#import signal

class Reader:
	def  __init__(self):
#		GPIO.cleanup()
		self.MIFAREReader = MFRC522.MFRC522()

# This loop keeps checking for chips. If one is near it will get the UID and authenticate

	def readCard(self):
		 # Scan for cards
		(self.status,self.TagType) = self.MIFAREReader.MFRC522_Request(self.MIFAREReader.PICC_REQIDL)

		# If a card is found
  		if self.status == self.MIFAREReader.MI_OK:
        		print "Card detected"
		
		#Get UID of the Card
		(self.status,self.uid) = self.MIFAREReader.MFRC522_Anticoll()
		
		if self.status == self.MIFAREReader.MI_OK:
			self.key = str(self.uid[0]) + str(self.uid[1]) + str(self.uid[2]) + str(self.uid[3])
			print "Card UID = " + self.key
			return self.key
		return ' '
