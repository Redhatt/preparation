from debug import *

#from debug import *

I =  lambda :int(input())
L = lambda :list(map(int, input().split()))
T = lambda :map(int, input().split())
mod = int(1e9) + 7

n, k = T()
graph = []
for i in range(n):
    graph.append(L())

print(n, k)
print(graph)


def matmul(A, B):
    n = len(A)
    ans = [[0]*n for i in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                ans[i][j] = (ans[i][j] + A[i][k] * B[k][j])%mod
    return ans

def matpow(A, k):
    n = len(A)
    if k == 0:
        ans = [[0]*n for _ in range(n)]
        for i in range(n):
            ans[i][i] = 1
        return ans
    elif k&1:
        return matmul(A, matpow(A, k-1))
    else:
        A_half = matpow(A, k//2)
        return matmul(A_half, A_half)

A = matpow(graph, k)
ans = 0
for row in A:
    ans = (ans + sum(row))%mod

print(ans)