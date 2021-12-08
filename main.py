import usb.core
import time

def isControl(ctrl1,ctrl2):
	if ctrl2 == 0 and (ctrl1 == 1 or ctrl1 == 2):
		return True
	return False

def parseCommand(ctrl1,ctrl2,command):
	if ctrl1 == 1 and ctrl2 == 1:
		if command == 5:
			return "prev"
		elif command == 9:
			return "next"
		elif command == 19:
			return "play"
		elif command == 22:
			return "stop"
	if ctrl1 == 1 and ctrl2 == 3:
		if command == 5:
			return "rew"
		elif command == 9:
			return "fwd"
	return "don't know yet"

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

try:
	while True:
		try:
			r=dev.read(eaddr,8)
			if isControl(r[0],r[1]):
				continue
			print(parseCommand(r[0],r[1],r[3]))
		except KeyboardInterrupt:
			raise
		except:
			time.sleep(0.1)
except KeyboardInterrupt:
	print("CTRL+C detected, exiting")
	exit(0)

