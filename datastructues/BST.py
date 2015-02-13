class TreeNode(object):
	"""docstring for TreeNode"""
	def __init__(self,key,val,leftChild=None,rightChild=None,parent=None):
		self.key = key
		self.payload = val
		self.leftChild = leftChild
		self.rightChild = rightChild
		self.parent = parent

	def hasLeftChild(self):
		return self.leftChild

	def hasRightChild(self):
		return self.rightChild

	def isLeftChild(self):
		return self.parent and self.parent.leftChild == self

	def isRightChild(self):
		return self.parent and self.parent.rightChild == self

	def isRoot(self):
		return not (self.parent)

	def isLeaf(self):
		return not (self.rightChild or self.leftChild)

	def hasAnyChild(self):
		return self.rightChild or self.leftChild

	def hasBothChild(self):
		return self.rightChild and self.leftChild

	def replaceNodeData(self,key,val,lChild,rChild):
		self.key = key
		self.payload = val
		self.leftChild = lChild
		self.rightChild = rChild
		if self.hasLeftChild():
			self.leftChild.parent = self
		if self.hasRightChild():
			self.rightChild.parent = self


class BinarySearchTree(object):
	"""docstring for BinarySearchTree"""
	def __init__(self):
		self.root = None
		self.size = 0

	def length(self):
		return self.size

	def __len__(self):
		return self.size

	def __iter__(self):
		return self.root.__iter__()

	def put(self,key,val):
		if self.root:
			self._put(key,val,self.root)
		else:
			self.root = TreeNode(key,val)
		self.size += self.size

	def _put(self,key,val,currentNode):
		if key < currentNode.key:
			if currentNode.hasLeftChild():
				self._put(key,val,currentNode.leftChild)
			else:
				currentNode.leftChild = TreeNode(key,val,parent=currentNode)
		else:
			if currentNode.hasRightChild():
				self._put(key,val,currentNode.rightChild)
			else:
				currentNode.rightChild = TreeNode(key,val,parent=currentNode)
	def __setitem__(self,k,v):
		self.put(k,v)

	def get(self,key):
		if self.root:
			res = self._get(key,self.root)
			if res:
				return res.payload
			else:
				return None
		else:
			return None

	def _get(self,key,currentNode):
		if not currentNode:
			return None
		elif currentNode.key == key:
			return currentNode
		elif key < currentNode.key:
			return self._get(key,currentNode.leftChild)
		else:
			return self._get(key,currentNode.rightChild)

	def __getitem__(self,key):
	 	return self.get(key)

	def __contains__(self,key):
		if self._get(key,self.root):
			return True
		else:
			return False

	def delete(self,key):
		if self.size > 1:
			nodeToDelete = self._get(key,self.root)
			if nodeToDelete:
				self.remove(nodeToDelete)
				self.size -= 1
			else:
				raise KeyError('Error: Key(Item to be deleted) is not in the BST')
		elif self.size == 1 and self.root.key == key:
			self.root = None
			self.size = 0
		else:
			raise KeyError('Error: Key(Item to be deleted) is not in the BST')

	def remove(self,currentNode):
		if currentNode.isLeaf(): #Leaf
			if currentNode == currentNode.parent.leftChild:
				currentNode.parent.leftChild = None
			else:
				currentNode.parent.rightChild = None
		
		elif currentNode.hasBothChild(): #Interior Node
			successor = currentNode.findSuccessor()
			successor.spliceOut()
			currentNode.key = successor.key
			currentNode.payload = successor.payload

		else: #This node has one child
			if currentNode.hasLeftChild():				
				if currentNode.isLeftChild():
					currentNode.leftChild.parent = currentNode.parent
					currentNode.parent.leftChild = currentNode.leftChild
				elif currentNode.isRightChild():
					currentNode.rightChild.parent = currentNode.parent
					currentNode.parent.rightChild = currentNode.rightChild
				else:
					currentNode.replaceNodeData(currentNode.leftChild.key,
												currentNode.leftChild.payload,
												currentNode.leftChild.leftChild,
												currentNode.leftChild.rightChild)
			else:
				if currentNode.isLeftChild():
					currentNode.rightChild.parent = currentNode.parent
					currentNode.parent.leftChild = currentNode.rightChild
				elif currentNode.isRightChild():
					currentNode.rightChild.parent = currentNode.parent
					currentNode.parent.rightChild = currentNode.rightChild
				else:
					currentNode.replaceNodeData(currentNode.rightChild.key,
												currentNode.rightChild.payload,
												currentNode.rightChild.leftChild,
												currentNode.rightChild.rightChild)
	def findSuccessor(self):
		successor = None	
		if self.hasRightChild():
			successor = self.rightChild.findMin()
		else:
			if self.parent:
				if self.isLeftChild():
					successor = self.parent
				else:
					self.parent.rightChild = None
					successor = self.parent.findSuccessor()
					self.parent.rightChild = self
		return successor
	def findMin(self):
		currentNode = self
		while currentNode.hasLeftChild():
			currentNode = currentNode.leftChild
		return currentNode

	def spliceOut(self):
		if self.isLeaf():
			if self.isLeftChild():
				self.parent.leftChild = None
			else:
				self.parent.rightChild = None
		elif self.hasAnyChild():
			if self.hasLeftChild():
				if self.isLeftChild():
					self.parent.leftChild = self.leftChild
				else:
					self.parent.rightChild = self.leftChild
				self.leftChild.parent = self.parent
			else:
				if self.isLeftChild():
					self.parent.leftChild = self.rightChild
				else:
					self.parent.rightChild = self.rightChild
				self.rightChild.parent = self.parent

	def __iter__(self):
		if self:
			if self.hasLeftChild():
				for element in self.leftChild:
					yield element
			yield self.key
			if self.hasRightChild():
				for element in self.rightChild:
					yield element





mytree = BinarySearchTree()
mytree[3]="red"
mytree[4]="blue"
mytree[6]="yellow"
mytree[2]="at"

print(mytree[6])
print(mytree[2])









