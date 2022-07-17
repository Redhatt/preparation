from debug import *
import sys
sys.setrecursionlimit(10**5)

I =  lambda :int(input())
L = lambda :list(map(int, input().split()))
T = lambda :map(int, input().split())
mod = int(1e9) + 7



n, k = T()
lis = L()


def rec(i, s):
    if s<0: return 0
    if i == n:
        return s == 0

    ans = 0
    for p in range(lis[i]+1):
        ans += rec(i+1, s-p)
    return ans

print(rec(0, k))
