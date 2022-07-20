from debug import *

I =  lambda :int(input())
L = lambda :list(map(int, input().split()))
T = lambda :map(int, input().split())
mod = int(1e9) + 7

import random

# n, h, a = I(), L(), L()
n = 10**5
h = random.sample(list(range(1, n+1)), n)
a = random.choices(list(range(10**6)), k=n)

bit = [0]*(n + 10)
N = n+1

def update(x, d):
    x+=1
    while x<N:
        bit[x] = max(bit[x], d)
        x += (-x&x)

def premax(x):
    x+=1
    ans = 0
    while x>0:
        ans = max(ans, bit[x])
        x -= (-x&x)
    return ans

seq = sorted([(h[i], i) for i in range(n)])
dp = [0]*(n+10)
ans = 0 

for i in range(n):
    index = seq[i][1]
    dp[index] = premax(index-1) + a[index]
    update(index, dp[index])
    ans = max(ans, dp[index])

print(ans)