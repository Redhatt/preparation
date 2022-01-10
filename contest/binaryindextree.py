from debug import debug
from math import ceil, log2

# root of a node x is x - ((x)&(-x))
# So first set bit of a number is for eg. b110 is b10, and for b1000 is b1000, for b110100 is b100.
# this first set bit can be easily calulated with (x)&(-x) operation.
# so root of node is first set bit subtracted from the node.
# 4 - 4 = 0 so root of 4 is 0(FSB of 4 = 4)
# 6 - 2 = 4 so root of 6 is 2(FSB of 6 = 2)
# https://www.hackerearth.com/practice/notes/binary-indexed-tree-or-fenwick-tree/
# go to above site for more recollection.


lis = [3, 2, 4, 5, 1, 1, 5, 3]
n = len(lis)
b = [0]*(n+1)

# update function takes only delta(differnce from previous data to curr changed data)
# so do not pass the changed value rather pass changed_value-previous_value.
def update(b, delta, index):
	index+=1
	while (index < len(b)):
		b[index] += delta
		index += ((index)&(-index))

def presum(b, index):
	ans = 0
	index+=1
	while index>0:
		ans += b[index]
		index -= ((index)&(-index))
	return ans

for i in range(n):
	update(b, lis[i], i)

# IMPORTANT: DO NOT FORGET TO UPDATE INITIAL LIST, AND UPDATE THE LIST AFTER YOU CALL THE 
# UPDATE FUNCTION AND NOT INSIDE UPDATE FUNCTION.

if __name__ == "__main__":
	print(b)
	print(presum(b, 3)-presum(b, 0))
