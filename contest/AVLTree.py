# AVL Tree
# Rotations are important; if in Doubt GFG is the best.
from debug import *
from treeVisuals import *

class AVLTree:
	def __init__(self, lis=None):
		self.root = None
		if lis:
			for i in lis: self.insert(i)

	def insert(self, data):
		self.root = self._insert(data, self.root)

	def delete(self, data):
		self.root = self._delete(data, self.root)

	def _insert(self, data, root):
		if root == None: 
			root = Node(data)
			return root
		if root.val < data: root.right = self._insert(data, root.right)
		else: root.left = self._insert(data, root.left)
		root.height = 1+max(self.getHeight(root.right), self.getHeight(root.left))
		balance = self.getBalance(root)
		if balance > 1 and data < root.left.val: return self.rotateRight(root)
		if balance < -1 and data > root.right.val: return self.rotateLeft(root)
		if balance > 1 and data > root.left.val:
			root.left = self.rotateLeft(root.left)
			return self.rotateRight(root)
		if balance <-1 and data < root.right.val:
			root.right = self.rotateRight(root.right)
			return self.rotateLeft(root)
		return root

	def _delete(self, data, root):
		if root is None: return root
		if root.val > data: root.left = self._delete(data, root.left)
		elif root.val < data: root.right = self._delete(data, root.right)
		else:
			if root.left is None:
				temp = root.right
				root = None
				return temp
			if root.right is None:
				temp = root.left
				root = None
				return temp
			succ = root.right
			while succ.left: succ = succ.left
			root.val = succ.val
			root.right = self._delete(succ.val,root.right)
		if root is None: return root
		root.height = 1+max(self.getHeight(root.right), self.getHeight(self.root.left))
		balance = self.getBalance(root)
		if balance > 1 and self.getBalance(root.left) >= 0: return self.rotateRight(root)
		if balance < -1 and self.getBalance(root.left) <= 0: return self.rotateLeft(root)
		if balance > 1 and self.getBalance(root.right) < 0:
			root.left = self.rotateLeft(root.left)
			return self.rotateRight(root)
		if balance < -1 and self.getBalance(root.right) > 0:
			root.right = self.rotateRight(root.right)
			return self.rotateLeft(root)
		return root

	def rotateRight(self, z):
		y = z.left
		T2 = y.right
		y.right = z
		z.left = T2
		z.height = 1+max(self.getHeight(z.left), self.getHeight(z.right))
		y.height = 1+max(self.getHeight(y.left), self.getHeight(y.right))
		return y

	def rotateLeft(self, z):
		y = z.right
		T2 = y.left
		y.left = z
		z.right = T2
		z.height = 1+max(self.getHeight(z.left), self.getHeight(z.right))
		y.height = 1+max(self.getHeight(y.left), self.getHeight(y.right))
		return y

	def getHeight(self, root):
		if root is None: return 0
		return root.height

	def getBalance(self, root):
		if root is None: return 0
		return self.getHeight(root.left) - self.getHeight(root.right)

	def find(self, data, low=False):
		node = self.root
		less = great = None
		return self._find(node, data, less, great, low)

	def _find(self, root, data, less, great, low):
		if root:
			if root.val == data: less = great = root; return less
			if root.val > data:
				great = root
				if root.left: return self._find(root.left, data, less, great, low)
			if root.val < data:
				less = root
				if root.right: return self._find(root.right, data, less, great, low)
		return less if low else great

	def inOrder(self):
		self._inOrder()
		print()

	def _inOrder(self, root=-1):
		if root == -1: root = self.root
		if root:
			self._inOrder(root=root.left)
			print(root.val, end=" ")
			self._inOrder(root=root.right)

	def printTree(self):
		visual(self.root)
		
	def draw(self, color=None):
		d = DrawTree(self.root)
		d.drawTree(color)
	
if __name__ == "__main__":
	from time import sleep
	lis = [10, 20, 30, 40, 50, 60, 70, 70, 70]
	tree = AVLTree(lis)
	tree.draw('red')
	time.sleep(2)
	tree.insert(80)
	tree.printTree()
	print(tree.root.val)
	tree.draw('blue')
	time.sleep(2)
	tree.delete(40)
	tree.printTree()
	print(tree.find(30).val)
	tree.draw('green')
	time.sleep(2)
	tree.delete(70)
	tree.printTree()
	print(tree.find(30).val)
	tree.draw('cyan')
