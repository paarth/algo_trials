class BinaryTree(object):
	"""docstring for BinaryTree"""
	def __init__(self, root_object):
		self.key = root_object
		self.left_child = None
		self.right_child = None

	def insertLeft(self, new_node):
		if self.left_child == None:
			self.left_child = BinaryTree(new_node)
		else:
			temp = BinaryTree(new_node)
			temp.left_child = self.left_child
			self.left_child = temp

	def insertRight(self, new_node):
		if self.right_child == None:
			self.right_child = BinaryTree(new_node)
		else:
			temp = BinaryTree(new_node)
			temp.right_child = self.right_child
			self.right_child = temp

	def getRightChild(self):
		return self.right_child

	def getLeftChild(self):
		return self.left_child

	def getRootVal(self):
		return self.key

	def setRootVal(self, new_object):
		self.key = new_object


## Test to simluate and check the implementation 
# r = BinaryTree('a')
# print(r.getRootVal())
# print(r.getLeftChild())
# r.insertLeft('b')
# print(r.getLeftChild())
# print(r.getLeftChild().getRootVal())
# r.insertRight('c')
# print(r.getRightChild())
# print(r.getRightChild().getRootVal())
# r.getRightChild().setRootVal('hello')
# print(r.getRightChild().getRootVal())

## Sample Result to tally
# a
# None
# <__main__.BinaryTree object>
# b
# <__main__.BinaryTree object>
# c
# hello