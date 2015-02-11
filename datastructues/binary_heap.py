class BinHeap(object):
	"""docstring for BinHeap"""
	def __init__(self):
		self.heapList = []
		self.currentSize = 0

	def swap(self,i,j):
		tmp = self.heapList[i]
		self.heapList[i] = self.heapList[j]
		self.heapList[j] = tmp

	def bubble_up(self, index):
		while index > 0:
			if self.heapList[index] < self.heapList[(index-1) // 2]:
				self.swap(index,(index-1)//2)
			index = index // 2

	def insert(self,item):
		self.heapList.append(item)
		self.currentSize += 1
		self.bubble_up(self.currentSize)

	def min_child(self,index):
		if (2*index + 2) > self.currentSize-1:
			return (2*index + 1)
		else:
			if self.heapList[2*index + 1] < self.heapList[2*index+2]:
				return (2*index+1)
			else:
				return (2*index+2)

	def bubble_down(self, index):
		while (2*index + 1) <= self.currentSize-1 :
			mc = self.min_child(index)
			if self.heapList[index] > self.heapList[mc]:
				self.swap(index,mc)
			index = mc

	def delMin(self):
		return_val = self.heapList[0]
		self.heapList[0] = self.heapList[self.currentSize-1]
		self.currentSize -= 1
		self.heapList.pop()
		self.bubble_down(0)
		return return_val

	def buildHeap(self,aList):
		self.currentSize = len(aList)
		self.heapList = aList
		index = self.currentSize-1
		while index >= 0:
			self.bubble_down(index)
			index -= 1


bh = BinHeap()
bh.buildHeap([9,5,6,2,3,2,44,2,11,1,56,223])

print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
