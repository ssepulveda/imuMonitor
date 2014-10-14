import smbus

bus=smbus.SMBus(1)

class PCA9547:
	address=None
	
	def __init__(self,address=0x70):
		self.address=address

	def setChannel(self,channel=0):
		channel+=8
		bus.write_byte(self.address,channel)

	def getChannel(self):
		return bus.read_byte(self.address)

	def resetChannel(self):
		bus.write_byte(self.address,0x08)
