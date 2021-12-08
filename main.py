import usb.core
import time

def isControl(first,second):
	if second == 0 and (first == 1 or first == 2):
		return True
	return False

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

print(eaddr)

try:
	while True:
		try:
			r=dev.read(eaddr,8)
			if isControl(r[0],r[1]):
				continue
			print(r)
		except KeyboardInterrupt:
			raise
		except:
			time.sleep(0.1)
except KeyboardInterrupt:
	print("CTRL+C detected, exiting")
	exit(0)

