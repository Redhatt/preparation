from debug import *
import sys;input = sys.stdin.readline
# import sys, os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
S = lambda :input().strip()
L = lambda :list(map(int, input().split()))
I = lambda :int(input().strip())
T = lambda :map(int, input().split())


def solve(temp, s):
    low = high = 0
    curs = 0
    while low<=high and high<n:
        a,b,c = temp[low]
        x,y,z = temp[high]
        if (b-a+1)*c + (y-x+1)*z 



t = I()

for _ in range(t):
    n, q = T()
    lis = L()

    temp = []

    cur = 0
    while cur<n:
        last = cur
        while cur+1<n and lis[cur+1] == lis[cur]: cur+=1
        temp.append([last, cur, lis[cur]])
        cur+=1

    for _ in range(q):
        p = L()
        if p[0] == 1:
            s = p[1]
            

















