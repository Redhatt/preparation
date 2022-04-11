# from debug import *
import sys
from math import log2, ceil

input = sys.stdin.readline

n, q = map(int, input().split())
K = 1 + ceil(log2(n))
N = n + 1

inn, out, level = [0]*N, [0]*N, [0]*N
graph = [[] for i in range(N)]
up = [[-1]*K for i in range(N)]

def dfs(node: int, parent: int, time: int) -> int:
    stack = [(node, parent, 0, 0)]
    time = 0
    while stack:
        node, parent, depth, location = stack.pop()
        if location == 0:
            time += 1
            inn[node] = time
            up[node][0] = parent
            level[node] = depth

            stack.append((node, parent, depth, 1))

            for k in range(1, K):
                if up[node][k-1] == -1: break
                up[node][k] = up[up[node][k-1]][k-1]

            for nbr in graph[node]:
                if nbr == parent: continue
                stack.append((nbr, node, depth+1, 0))
        else:
            time += 1
            out[node] = time

def getDis(u, v):
    if (inn[u]<=inn[v]) and (out[u]>=out[v]): 
        ancestor = u

    elif ((inn[v]<=inn[u]) and (out[v]>=out[u])):
        ancestor = v

    else:
        for k in reversed(range(K)):
            t = up[u][k]
            if t != -1 and not ((inn[t]<=inn[v]) and (out[t]>=out[v])):
                u = t

        ancestor = up[u][0]

    return abs(level[ancestor] - level[u]) + abs(level[ancestor] - level[v])

for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(1, -1, 0)

for i in range(q):
    u, v = map(int, input().split())
    print(getDis(u, v))
