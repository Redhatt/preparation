from debug import *
import random
from treeVisuals import *


mx, my, mz = 100, 100, 100
inf = 1e10

n = 10
min_size = 1
shape = [(random.randint(-mx, mx), random.randint(-my, my), random.randint(-0*mz, 0*mz)) for i in range(n)]
shape =  [
   (52, -32, 0),
   (62, -77, 0),
   (0, -64, 0),
   (13, 22, 0),
   (-76, 2, 0),
   (-70, -36, 0),
   (93, 0, 0),
   (84, -50, 0),
   (30, -59, 0),
   (-66, -77, 0),
 ]
debug(s=shape)

BVH_tree = [[] for i in range(3*n+1)]
BVH_shape = [i for i in shape]
BVH_start = [() for i in range(n)]
BVH_end = [() for i in range(n)]


def BVH_insertionSort(low, high, axis):
	for i in range(low, high+1):
	    j = i-1
	    key = BVH_shape[i]
	    while j>=0 and BVH_shape[j][axis]>key[axis]:
	        BVH_shape[j+1] = BVH_shape[j]
	        j -= 1
	    BVH_shape[j+1] = key

def BVH_setBounds(node, low, high):
	minx = inf
	miny = inf
	minz = inf
	maxx = -inf
	maxy = -inf
	maxz = -inf

	for i in range(low, high+1):
		minx = min(minx, BVH_shape[i][0])
		miny = min(miny, BVH_shape[i][1])
		minz = min(minz, BVH_shape[i][2])
		maxx = max(maxx, BVH_shape[i][0])
		maxy = max(maxy, BVH_shape[i][1])
		maxz = max(maxz, BVH_shape[i][2])

	axis = sorted([(maxx - minx, 0), (maxy - miny, 1), (maxz - miny, 2)])[-1][1]
	BVH_tree[node] = [low, high, high-low+1, (minx, miny, minz), (maxx, maxy, maxz)]
	return axis

def BVH_build(node, low, high):
	if node > 3*n: return
	
	axis = BVH_setBounds(node, low, high)
	if high - low + 1 < min_size: return

	BVH_insertionSort(low, high, axis)

	index = (low + high)//2
	BVH_build(2*node + 1, low, index)
	BVH_build(2*node + 2, index+1, high)

@timit
def BVH_intersect(ray, node):
	if node > 3*n or not BVH_tree[node]: return False

	if not (BVH_tree[node][3][0]<=ray[0]<=BVH_tree[node][4][0]): return False
	if not (BVH_tree[node][3][1]<=ray[1]<=BVH_tree[node][4][1]): return False
	if not (BVH_tree[node][3][2]<=ray[2]<=BVH_tree[node][4][2]): return False

	if BVH_tree[node][1] - BVH_tree[node][0] <= min_size:
		for i in range(BVH_tree[node][0], BVH_tree[node][1]+1):
			if ray[0] == BVH_shape[i][0] and ray[1] == BVH_shape[i][1] \
				and ray[2] == BVH_shape[i][2]: return True

	if BVH_intersect(ray, 2*node+1): return True
	if BVH_intersect(ray, 2*node+2): return True

	return False

BVH_build(0, 0, n -1)
debug(to_find = shape[0], got=BVH_intersect(shape[0], 0))
debug(calls=BVH_intersect.call)
debug(tree = dict((i, BVH_tree[i]) for i in range(2*n)))
debug(shape=dict((i, BVH_shape[i]) for i in range(n)))
