# point to be NOTED
# 0 base index left child -> 2*i+1, right child -> 2*i+2 (i is parent)
# and parent -> (i-1)//2 (i is child)
from debug import *
from math import log2, ceil
max_size = 2*int(15)
tree = [0]*(max_size)

def build(lis):
	p = len(lis)
	n = 2**ceil(log2(p))
	for i in range(n-p): lis.append(0)
	for i in range(n): tree[i+n] = lis[i]
	for i in range(n-1, 0, -1): tree[i] = tree[i*2] + tree[i*2 + 1] # bit addition, after shifting for sure 0 th postion is 0 so adding 1 there only

def querry(l, r):
	ans = 0
	l+=n; r+=n 
	while l<=r:
		if (l&1): ans+=tree[l]; l+=1
		if (r&1 == 0): ans+=tree[r]; r-=1
		l >>= 1; r >>= 1
	return ans

def update(pos, val):
	tree[pos+n] = val
	i = pos+n
	while i>1:
		tree[i//2] = tree[i] + tree[i^1]  # bit inversion at 0th postion
		i>>=1

def check(lis):
	for i in range(len(lis)):
		update(i+1, i**2)
		lis[i] = i**2
		for i in range(n):
			for j in range(i+1):
				if sum(lis[i:j+1]) != querry(i+1, j+1): print("INCORRECT"); return 0
	print("CORRECT")
	

if __name__ == "__main__":
	lis = [1,2,3,4,5,6,7]
	n = len(lis)
	build(lis)
	print(tree)
	update(1, 5)
	print(tree)
	# check(lis)
