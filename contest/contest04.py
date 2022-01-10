#=================================
# Author: Danish Amin
# Date: Mon Nov 30 17:47:32 2020
#=================================
from debug import * 
import sys;input = sys.stdin.readline
from bisect import *
from collections import defaultdict

s1 = input().strip()
s2 = input().strip()
d = defaultdict(list)
n = len(s1)
for i in range(n): d[s1[i]].append(i)

cnt = 1
j = -1
print(d)
for s in s2:
	x = bisect_right(d[s], j)
	print(x, cnt)
	if x == len(d[s]):
		cnt += 1
		j = -1
	else:
		j = d[s][x]

if cnt > len(s2): print(-1)
else: print(cnt)