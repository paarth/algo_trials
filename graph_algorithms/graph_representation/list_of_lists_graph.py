def BinaryTree(r):
	return [r, [], []]

def insertLeft(root,new_branch):
	t = root.pop(1)
	root.insert(1,[new_branch,t,[]])

	return root

def insertRight(root,new_branch):
	t = root.pop(2)
	root.insert(2, [new_branch, [], t])		

	return root

def getRootVal(root):
	return root[0]

def setRootVal(root,new_value):
	root[0] = new_value

def getLeftChild(root):
	return root[1]

def getRightChild(root):
	return root[2]

## Test to simluate and check the implementation 
# r = BinaryTree(3)
# insertLeft(r,4)
# insertLeft(r,5)
# insertRight(r,6)
# insertRight(r,7)
# l = getLeftChild(r)
# print(l)

# setRootVal(l,9)
# print(r)
# insertLeft(l,11)
# print(r)
# print(getRightChild(getRightChild(r)))

## Sample Result to tally
# [5, [4, [], []], []]
# [3, [9, [4, [], []], []], [7, [], [6, [], []]]]
# [3, [9, [11, [4, [], []], []], []], [7, [], [6, [], []]]]
# [6, [], []]