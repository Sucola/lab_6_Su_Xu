class Node():
	def __init__(self, data, nextPointer = None):
		self.data		 = data
		self.nextPointer = nextPointer

	def getData(self):
		return(self.data)

	def setData(self, nData):
		self.data = nData

	def getnextPointer(self):
		return(self.nextPointer)

	def setnextPointer(self, n):
		self.nextPointer = n

