from collections import deque

class Queue:
	def __init__(self):
		self.queue = deque()

	def isEmpty(self):
		return self.queue.isEmpty

	def enqueue(self,item):
		self.queue.append(item)

	def deque(self):
		return self.queue.popleft()

	def size(self):
		return self.queue.size()
