from debug import *

I =  lambda :int(input())
L = lambda :list(map(int, input().split()))
T = lambda :map(int, input().split())
mod = int(1e9) + 7


N, K = T()
lis = L()

dp = [0]*(K+1)
dp[0] = 1

for i in range(1, N+1):
    
    s = [0]*(K+1)
    s[0] = dp[0]
    for k in range(1, K+1):
        s[k] = (s[k-1] + dp[k])%mod

    for k in range(K+1):
        if k<=lis[i-1]:
            dp[k] = s[k]
        else:
            dp[k] = s[k] - s[k-lis[i-1]-1]

print(dp[-1]%mod)