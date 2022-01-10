from debug import debug
import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline
# n, m = map(int, sys.stdin.readline().split())

# t and n
t_ = int(input())
while t_:
	t_-=1
	n = int(input())

# t, (a,b,c)	
t_ = int(input())
while t_:
	t_-=1
	a,b,c = map(int, input().split())

# t, n, lis
t_ = int(input())
while t_:
	t_-=1
	n = int(input())
	lis = list(map(int, input().split()))
	
# t, (n,k), lis
t_ = int(input())
while t_:
	t_-=1
	n, k = map(int, input().split())
	lis = list(map(int, input().split()))

	lis = list(input().strip())

# graph 
n,m = map(int, input().split())
graph = [[] for i in range(n)]
for _ in range(m):
	a,b = map(int, input().split())
	graph[a-1].append(b-1)

# matrix 
n = int(input())
n,m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
	#string
matrix = [[list(input().strip())] for _ in range(n)]


