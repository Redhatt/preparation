#=================================
# Author: Danish Amin
# Date: Mon Nov 30 17:46:57 2020
#=================================

from debug import *
import sys;input = sys.stdin.readline
sys.setrecursionlimit(1 + 10**5)
from collections import deque

I =  lambda :int(input())
L = lambda :list(map(int, input().split()))
T = lambda :map(int, input().split())
mod = int(1e9) + 7


n, m = T()
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = T()
    graph[a].append(b)
    graph[b].append(a)


color = [0]*(n+1)
ans = deque()


def dfs(node, parent):
    color[node] = 1
    ans.append(node)
    for nbr in graph[node]:
        if parent == nbr:
            continue
        elif color[nbr] == 0 and dfs(nbr, node):
            return True
        elif color[nbr] == 1:
            ans.append(nbr)
            return True
    color[node] = 2
    return False

for i in range(1, n+1):
    if color[i] == 0 and dfs(i, 0):
        break

if ans:
    while ans[-1] != ans[0]:
        ans.popleft()

    print(len(ans))
    print(*ans)
else:
    print("IMPOSSIBLE")


