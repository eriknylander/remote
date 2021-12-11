import usb.core
import time

def isControl(pos3):
	if pos3 == 0:
		return True
	return False

def setUpAndListen():
	dev=usb.core.find(idVendor=0x3353,idProduct=0x3713)

	if dev is None:
		raise ValueError("Device not found")
	else:
		print("Found device")

	ep=dev[0].interfaces()[0].endpoints()[0]
	i=dev[0].interfaces()[0].bInterfaceNumber
	dev.reset()

	if dev.is_kernel_driver_active(i):
		print("kernel driver was active")
		dev.detach_kernel_driver(i)


#dev.set_configuration()

	eaddr=ep.bEndpointAddress

	while True:
		try:
			r=dev.read(eaddr,8,5000)
			if isControl(r[3]):
				continue
			print("New button press")
			print(r)
		except KeyboardInterrupt:
			raise
		except:
			time.sleep(0.1)

try:
	setUpAndListen()
except:
	exit(0)
