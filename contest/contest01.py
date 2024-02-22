from debug import *
import sys;input = sys.stdin.readline
# import sys, os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
from collections import defaultdict
from math import ceil


S = lambda :input().strip()
L = lambda :list(map(int, input().split()))
I = lambda :int(input().strip())
T = lambda :map(int, input().split())

inf = 10**10
t = I()
for _ in range(t):
    n,m = T()
    line = [0]*(n+2)
    left = list(range(n+1))

    for i in range(m): 
        a,b = T()
        line[a] += 1
        line[b+1] -= 1
        left[b] = min(left[b], a)

    for i in range(1, n+1):
        line[i] += line[i-1]

    for i in range(n-1,-1,-1):
        left[i] = min(left[i], left[i+1])

    dp = [0]*(n+1)
    for i in range(1, n+1):
        dp[i] = max(dp[left[i]-1] + line[i], dp[i-1])

    print(dp[-1])
