import threading
import time
from ir import setUpAndListen
from chromecast import ChromecastController

class commandHandler:
	def __init__(self,ccc):
		self.ccc = ccc
	def handleCommand(self,command):
		if command == "play/pause":
			self.ccc.togglePlayPause()
		elif command == "fwd":
			self.ccc.jump(1)
		elif command == "rew":
			self.ccc.jump(-1)
		else:
			print("Does not compute")


ccc = ChromecastController()

ch = commandHandler(ccc)

try:
	setUpAndListen(ch.handleCommand)
except KeyboardInterrupt:
	exit(0)
