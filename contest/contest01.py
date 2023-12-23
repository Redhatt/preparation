from debug import *
from collections import deque, defaultdict, Counter
from itertools import accumulate
from bisect import *
import operator
import sys;input = sys.stdin.readline
# sys.setrecursionlimit(100001)
# import sys, os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
S = lambda : input().strip()
L = lambda :list(map(int, input().split()))
I =  lambda :int(input().strip())
T = lambda :map(int, input().split())
mod = int(1e9) + 7


t = I()
for _ in range(t):
    n = I()
    lis = L()
    lis.sort()
    x = 0
    c = 0
    for i in lis:
        # print(i, x, c)
        if x and i>1:
            temp = i
            i -= min(0, i-x)
            x -= temp-i
            c += 1

        if i<4:
            c += i
            x += i
        else:
            c += i//2 + 1 + (i&1)
            x = 0

    print(c)