from debug import debug
import math
inf = int(1e6)

def recMinTree(arr, tree, i):
	l = 2*i+1
	r = 2*(i+1)

	if r<len(tree):
		recMinTree(arr, tree, l)
		recMinTree(arr, tree, r)
		tree[i] = min(tree[l], tree[r])
	else:
		tree[i] = arr[i-len(arr)+1]


def minTree(arr):
	n = len(arr)
	l = math.log2(n)

	lis = arr[:]
	if int(l) != math.ceil(l):
		k = 2**(math.ceil(l))-n
		lis += [inf for i in range(k)]  # for max tree -inf
		n = 2**(math.ceil(l))

	tree = [inf for i in range(2*n-1)]
	recMinTree(lis, tree, 0)

	return tree


# below one is wrong, always convert curr node to its parent
# then check for left and right child of it and then keep updating root.
def minChange(tree, a, data):
	a += (len(tree)+1)//2 - 1

	val = tree[a]
	tree[a] = data

	while a:
		root = (a-1)//2
		if tree[a]<tree[root]:
			tree[root] = tree[a]
		else:
			break
		a = root

def minQuerry(tree, a, b):
	n = (len(tree)+1)//2 - 1
	ans = inf
	a += n
	b += n

	while a<=b:
		if a%2 == 0:
			ans = min(ans, tree[a])
			a += 1

		if b%2 == 1:
			ans = min(ans, tree[b])
			b -= 1

		a = (a-1)//2
		b = (b-1)//2

	return ans


def recMaxTree(arr, tree, i):
	l = 2*i+1
	r = 2*(i+1)

	if r<len(tree):
		recMaxTree(arr, tree, l)
		recMaxTree(arr, tree, r)
		tree[i] = max(tree[l], tree[r])
	else:
		tree[i] = arr[i-len(arr)+1]


def maxTree(arr):
	n = len(arr)
	l = math.log2(n)

	lis = arr[:]
	if int(l) != math.ceil(l):
		k = 2**(math.ceil(l))-n
		lis += [-inf for i in range(k)]  # for max tree -inf
		n = 2**(math.ceil(l))

	tree = [-inf for i in range(2*n-1)]
	recMaxTree(lis, tree, 0)

	return tree


def maxChange(tree, a, data):
	a += (len(tree)+1)//2 - 1

	val = tree[a]
	tree[a] = data

	while a:
		root = (a-1)//2
		if tree[a]>tree[root]:
			tree[root] = tree[a]
		else:
			break
		a = root

def maxQuerry(tree, a, b):
	n = (len(tree)+1)//2 - 1
	ans = -inf
	a += n
	b += n

	while a<=b:
		if a%2 == 0:
			ans = max(ans, tree[a])
			a += 1

		if b%2 == 1:
			ans = max(ans, tree[b])
			b -= 1

		a = (a-1)//2
		b = (b-1)//2

	return ans

if __name__ == "__main__":
	arr = [1,2,3,4,5,6,7,8]
	tree = minTree(arr)
	# print(tree)
	val = minQuerry(tree, 2, 3)
	print(val)
	minChange(tree, 2, 5)
	# print(tree)
	val = minQuerry(tree, 2, 3)
	print(val)


