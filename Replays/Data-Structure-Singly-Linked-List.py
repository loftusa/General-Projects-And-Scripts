class Node(object):
		def __init__(self, value, nextNode = None):
			self.value = value
			self.nextNode = nextNode

		def __repr__(self): 
			return ("Node object - attributes: value = {0}, nextNode at {1}."
				.format(self.value, id(self.nextNode)))

		def getValue(self):
			return self.value

		def setValue(self, value):
			self.value = value

		def getNext(self):
			return self.nextNode

		def setNext(self, nextNode):
			self.nextNode = nextNode

class LinkedList(object):

	def __init__(self, *initialValues):

		if initialValues:
			self.head = Node(initialValues[0])
			currentNode = self.head
			for value in initialValues[1:]:
				currentNode.setNext(Node(value))
				currentNode = currentNode.getNext()
		else:
			self.head = None

	def __repr__(self):
		
		representation = "["
		tracerNode = self.head
		if tracerNode:
			representation += str(tracerNode.getValue())
			tracerNode = tracerNode.getNext()
		while tracerNode:
			representation += ", " + str(tracerNode.getValue())
			tracerNode = tracerNode.getNext()
		representation += "]"

		return representation

	def size(self):

		numNodes = 0
		tracerNode = self.head

		while tracerNode:
			numNodes += 1
			tracerNode = tracerNode.getNext()

		return numNodes

	def getAt(self, index = 0):
		"""Returns the Node at the requested index."""

		try:
			index = int(index)
		except ValueError:
			print("Index could not be converted to an integer.")
		
		if index == 0:
			return self.head

		elif index > 0:
			desiredNode = self.head
			# Set desiredNode to the Node at the given index.
			for i in range(index):
				if desiredNode and desiredNode.getNext():
					desiredNode = desiredNode.getNext()
				else:
					raise IndexError("Index out of bounds.")

			return desiredNode

		else: # index < 0
		# Set pastLastNode ahead of desiredNode by |index|, 
		# then step both forward until pastLastNode is past the last Node.
			pastLastNode = self.head
			for i in range(-index):
				if pastLastNode:
					pastLastNode = pastLastNode.getNext()
				else:
					raise IndexError("Index out of bounds.")
			desiredNode = self.head
			while pastLastNode:
				pastLastNode = pastLastNode.getNext()
				desiredNode = desiredNode.getNext()
			# pastLastNode is now past the last Node in the LinkedList. 
			# desiredNode is |index| Nodes behind pastLastNode.

			return desiredNode

	def getIndex(self, value):
		"""Returns the index of the first Node found with the requested value."""

		index = 0

		tracerNode = self.head
		while tracerNode:
			if tracerNode.getValue() == value:
				return index
			tracerNode = tracerNode.getNext()
			index += 1

		return None # value not found

	def put(self, value, index = 0):
		"""Negative indices are inserted after the given index such that 
		the result for both positive and negative indices is a new element 
		at the given index after insertion."""

		index = int(index)

		size = self.size()
		if size == 0 and index in [0, -1]: # Case 1: create head
			self.head = Node(value)
		elif index == 0 or -index == self.size() + 1: # Case 2: insert at head
			newNode = Node(value, self.head)
			self.head = newNode
		else: # Case 3: insert after head
			if index > 0:
				previousNode = self.getAt(index - 1)
			else: # index < 0
				previousNode = self.getAt(index)
			newNode = Node(value, previousNode.getNext())
			previousNode.setNext(newNode)

	def delete(self, value):
		"""Excises and returns the first Node in the LinkedList with this value."""
		
		if self.head.getValue() == value:
			oldHead = self.head
			self.head = self.head.getNext()
			return oldHead

		leadNode = self.head.getNext()
		followNode = self.head
		while leadNode:
			if leadNode.getValue() == value:
				followNode.setNext(leadNode.getNext())
				return leadNode
			leadNode = leadNode.getNext()
			followNode = followNode.getNext()

		raise ValueError("Value not found.")

	def deleteAt(self, index):
		"""Excises and returns the Node at the requested index."""

		if index == 0 or -index == self.size(): # If deleting at head
			deletedNode = self.head
			self.head = self.head.getNext()
		else:
			previousNode = self.getAt(index - 1)
			deletedNode = previousNode.getNext()
			previousNode.setNext(previousNode.getNext())

		return deletedNode

