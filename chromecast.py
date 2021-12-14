import pychromecast


class ChromecastController:
	def __init__(self):
		chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=["Vardagsrum TV"])
		cc = chromecasts[0]
		cc.wait()
		mc = cc.media_controller
		mc.block_until_active()
		self.mc = mc


	def togglePlayPause(self):
		if self.mc.is_playing:
			self.mc.pause()
		else:
			self.mc.play()

	def jump(self, direction):
		jump_to = self.mc.status.adjusted_current_time + (direction * 15)
		self.mc.seek(jump_to)
