# point to be NOTED
# 0 base index left child -> 2*i+1, right child -> 2*i+2 (i is parent)
# and parent -> (i-1)//2 (i is child)
from debug import *
from math import log2, ceil
max_size = 2*int(15)
tree = [0]*(max_size)
lazy = [0]*(max_size)
def build(lis):
	p = len(lis)
	n = 2**ceil(log2(p))
	for i in range(n-p): lis.append(0)
	for i in range(n): tree[i+n] = lis[i]
	for i in range(n-1, 0, -1): tree[i] = tree[i<<1] + tree[(i<<1)|1] # bit addition, after shifting for sure 0 th postion is 0 so adding 1 there only

def querry(node, start, end, l, r):
	if lazy[node]:
		dif = lazy[node]
		lazy[node] = 0
		tree[node] += dif*(end-start+1)
		if start != end: lazy[2*node] += dif; lazy[2*node + 1] += dif

	if start>r or end<l: return 0

	if start >= l and end <= r: return tree[node]

	mid = (start+end)//2
	return querry(2*node, start, mid, l, r) + querry(2*node+1, mid+1, end, l, r)

def updateRange(node, start, end, l ,r, val):
	if lazy[node]:
		dif = lazy[node]
		lazy[node] = 0
		tree[node] += dif*(end-start+1)
		if start != end: lazy[2*node] += dif; lazy[2*node + 1] += dif

	if start>r or end<l: return

	if start >= l and end <= r:
		tree[node] += val*(end-start+1)
		if start != end: lazy[2*node] += val; lazy[2*node + 1] += val
		return

	mid = (start+end)//2
	updateRange(2*node, start, mid, l, r, val)
	updateRange(2*node+1, mid+1, end, l, r, val)
	tree[node] = tree[2*node] + tree[2*node + 1]


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
	updateRange(1, 1, n, 1, 1, 2) 
	print(querry(1, 1, n, 1, n))


"""
DYNAMIC SEGMENT TREE
USE delfaultdict and its amazing...

def update(node,  l, r, start=0, end=int(1e9), val=1):
    # passing and updating
    if self.lazy[node]:
        self.seg[node] += self.lazy[node]
        if start != end: 
            self.lazy[2*node] += self.lazy[node]
            self.lazy[2*node+1] += self.lazy[node]
        self.lazy[node] = 0
    if start>r or end<l: return 
    if start>=l and end<=r:
        self.seg[node] += val
        if start != end:
            self.lazy[2*node] += val
            self.lazy[2*node+1] += val
        return 
    mid = (start+end)//2
    update(2*node, l, r, start, mid)
    update(2*node+1, l, r, mid+1, end)  
    self.seg[node] = max(self.seg[2*node], self.seg[2*node+1])
update(1, l, r-1)
return self.seg[1]
"""
	
