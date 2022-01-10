from debug import debug
import sys; input = sys.stdin.readline
sys.setrecursionlimit(int(2e5))
from collections import deque

# making graph and trans
n, m = map(int, input().split())
coins = list(map(int, input().split()))
graph = [[]for i in range(n)]
trans = [[]for i in range(n)]

for i in range(m):
	a, b = map(int, input().split())
	graph[a-1].append(b-1)
	trans[b-1].append(a-1)
	
# getting connected components.
stack = deque()
v = [0]*n
def dfs1(node):
	v[node] = 1
	for i in graph[node]:
		if not v[i]: dfs1(i)
	stack.appendleft(node)

# making new coins_ and graph_ from SCC as nodes wihch makes DAG
coins_ = [0]*n
graph_ = [[] for i in range(n)]
# so here v is cleverly designed. -1 means not visited and any other no: means its
# that node is inside the new graph of v value, kind of DSU.

def dfs2(node, p):
	v[node] = p
	coin = coins[node]
	for i in trans[node]:
		if v[i] == -1: coin += dfs2(i, p)
		elif v[i] != p: graph_[v[i]].append(p) # if node is visited and does not belong to the current one
	return coin                                # means it is connected to that SSC node in new graph.

for i in range(n):
	if v[i] == 0: dfs1(i)
v = [-1]*n
p = 0
for i in stack:
	if v[i] == -1:
		coins_[p] = dfs2(i, p)
		p+=1

# applying DP to find maximum coins
final = [-1]*n
def dfs3(node):
	if final[node] != -1: return final[node]
	e = 0
	for i in graph_[node]: e = max(e, dfs3(i))
	final[node] = coins_[node] + e
	return final[node]

# debug(graph_=graph_, coins_=coins_)
ans = 0
for i in range(len(graph_)): 
	ans = max(ans, dfs3(i))
print(ans)