from lab6 import Node

class LinkedList():

	def __init__(self, head = None, size = 0, tail = None):
		self.head = head
		self.size = size
		self.tail = tail

	def getHead(self):
		return(self.head)
	def setHead(self, newHead):
		self.head = newHead

	def getSize(self):
		return(self.size)
	def setSize(self, newSize):
		self.size = newSize

	def getTail(self):
		return(self.tail)
	def setTail(self, newTail):
		self.tail = newTail

	def isEmpty(self):
		if(self.getSize() > 0):
			return(False)
		return(True)

	def addNode(self, d):
		newNode = Node(data = d)

		# Simple Case
		if(self.isEmpty()):
			self.setHead(newNode)
		else:
			self.getTail().setnextPointer(newNode)

		self.setTail(newNode)
		self.setSize(self.size + 1)

def main():
	ll = LinkedList()
	ll.addNode(1000)
	print(ll.getSize())
if __name__ == '__main__':
	main()