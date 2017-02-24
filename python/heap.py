
# Following Princeton example: 
# https://www.cs.princeton.edu/~wayne/kleinberg-tardos/pdf/DemoHeapify.pdf
# array = [8, 12, 9, 7, 22, 3, 26, 14, 11, 15, 22]

import math
import random
array = [random.randint(0,200) for _ in range(100)]

class Heap(object):

	def __init__(self, A):
		'''Initialize object members.'''

		# Instantiate input array.
		self.A = A

		# Determine nodes that have children
		max_range = 0
		while 2*(max_range+1)+1 < len(self.A):
			max_range = max_range + 1

		# Call heapify for nodes with children
		self.heapify(range(max_range,-1,-1))


	def siftDown(self,i):
		'''Method to sink down elements in tree.'''
		
		# Find index of min of subchildren
		if len(self.A) <= 2*i+2: 
			switch = 2*i+1
		elif len(self.A) > 2*i+2 and self.A[2*i+1] < self.A[2*i+2]:
			switch = 2*i+1
		else:
			switch = 2*i+2

		# Swap parent and min subchild if parent > child and switch index in range
		try:
			if self.A[i] > self.A[switch]:
				self.A[i], self.A[switch] = self.A[switch], self.A[i]
				return self.siftDown(switch)
		except IndexError:
			return


	# @staticmethod might go here
	def heapify(self, node_generator):
		'''Creates heap using sift down method for specified nodes.'''

		for j in node_generator:
			print(j)
			self.siftDown(j)


	def addNode(self, element):
		'''Add node to heap, re-heapify for relevant nodes.'''

		# Define max node to pass to generator. Add node to heap.
		max_node = len(self.A)
		self.A.append(element)
	
		# Define generator to construct parent node indices for new node.
		def node_construct(node):
			while node >= 0:
				yield node
				node = int(math.floor((node-1)/2))
		
		# Call heapify for relevant nodes yielded from generator.
		self.heapify(node_construct(max_node))


	def __str__(self):
		'''Prints array as tree structure.'''
		# Do something interesting here please.

		return str(self.A)


if __name__ == '__main__':
	
	test_heap = Heap(array)
	print(test_heap)

	test_heap.addNode(-1)
	print(test_heap)

	# test_heap.deleteNode(22)

