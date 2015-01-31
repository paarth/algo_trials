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

	def pre_order_traversal(self):
		print(self.key)
		if self.left_child:
			self.left_child.pre_order_traversal()
		if self.right_child:
			self.right_child.pre_order_traversal()

	def post_order_traversal(self):
		if self.left_child:
			self.left_child.post_order_traversal()
		if self.right_child:
			self.right_child.post_order_traversal()
		print(self.key)

	def in_order_traversal(self):
		if self.left_child:
			self.left_child.in_order_traversal()
		print(self.key)
		if self.right_child:
			self.right_child.in_order_traversal()


# Methods of external traversals of tree. 
# Required as in most cases we would not like to just traverse the tree.
def pre_order_traversal(tree):
	if tree != None:
		print(tree.getRootVal())
		pre_order_traversal(tree.getLeftChild())
		pre_order_traversal(tree.getRightChild())

def post_order_traversal(tree):
	if tree != None:
		post_order_traversal(tree.getLeftChild())
		post_order_traversal(tree.getRightChild())
		print(tree.getRootVal())

def in_order_traversal(tree):
	if tree != None:
		in_order_traversal(tree.getLeftChild())
		print(tree.getRootVal)
		in_order_traversal(tree.getRightChild())

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