from mpd import MPDClient
#import re
#import libs.utils
#import sys
import time
from logger import Logger
import subprocess

class Player:
	def __init__(self):
		self.client = self.connectMPD()

	def connectMPD(self):
		connected = False
		wait_time = 5
		nclient = MPDClient()               # create client object
		nclient.timeout = 200               # network timeout in seconds (floats allowed), default: None
		nclient.idletimeout = None
		while connected == False:
			try:
				Logger.logr.info("Connecting...")
				nclient.connect("localhost", 6600)
				Logger.logr.info("Connected!")
				connected = True
				return nclient
			except:
				connected = False
       				Logger.logr.error("Couldn't connect. Retrying in %s secons",wait_time)
				time.sleep(wait_time)

	def load(self, plist):
		Logger.logr.debug("Spiele Playlist %s",plist)
		self.stop()
		self.clear()
		subprocess.check_call(["mpc","load",plist])
		self.play()

	def add(self, uri):
		Logger.logr.debug("Lade Track: %s", uri)
		self.clear()
		subprocess.check_call(["mpc","add",uri])
		self.play()

	def play(self):
		subprocess.check_call(["mpc","play"])

	def pause(self):
		subprocess.check_call(["mpc","toggle"])

	def next(self):
		subprocess.check_call(["mpc","next"])

	def prev(self):
		subprocess.check_call(["mpc","prev"])

	def stop(self):
		subprocess.check_call(["mpc","stop"])

	def clear(self):
		subprocess.check_call(["mpc","clear"])
