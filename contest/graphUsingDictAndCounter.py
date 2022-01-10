from debug import debug
import sys; input = sys.stdin.readline
from collections import deque, Counter

# finding Eularian path and circuit for directed graph

# what all needed
# finding in-degree and out-degree
# checking strongly connectivity
# requirments - a data structure supporting easy in-degree and out-degree stuff, easy graph transpose, 
# easy removal of edges. - > dictionary with Counter will work

# graph input
graph = dict()
nodes = set()
# graph model
# { node : {0: counter_object, 1: counter_object}} 0->in-degree, 1->out-degree
# counter_object{node: no_of_edges_with_parent_node}

# n,m = map(int, input().split())
for _ in range(m):
	a,b = map(int, input().split())
	nodes.add(a)
	nodes.add(b)
	if a in graph: graph[a][1].update({b:1})
	else: graph[a] = {0: Counter(dict()), 1: Counter({b:1})}
	if b in graph: graph[b][0].update({a:1})
	else: graph[b] = {0: Counter({a:1}), 1: Counter(dict())}

# checking in and out degrees
start, stop = -1, -1
g = 1
count = 0
for k,v in graph.items():
	if len(v[0]) != len(v[1]):
		if len(v[0])-len(v[1]) == 1 and stop == -1: stop = k
		if len(v[0])-len(v[1]) == 1 and stop != -1: g = 0; break
		if len(v[0])-len(v[1]) == -1 and start == -1: start = k
		if len(v[0])-len(v[1]) == -1 and start != -1: g = 0; break
		if abs(len(v[0])-len(v[1])) > 1: g = 0; break
# debug(graph=graph)
if g:
	# checking strongly connectivity using kosaraju
	v = set()
	node = 1
	if node not in v:
		v.add(node)
		q = deque([node])
		while q:
			node = q.popleft()
			for out in graph[node][1]:
				if out not in v:
					v.add(out)
					q.append(out)
	if len(v) != len(nodes): g = 0
	else:
		v = set()
		node = 1
		if node not in v:
			v.add(node)
			q = deque([node])
			while q:
				node = q.popleft()
				for out in graph[node][0]:
					if out not in v:
						v.add(out)
						q.append(out)
		if len(v) != len(nodes): g = 0
if g:
	if start == -1: start = 1
	stack = []
	stack = [start]
	path = []
	while stack:
		node = stack[-1]
		if len(graph[node][1]) == 0:
			stack.pop()
			path.append(node)
		else:
			nn, v = graph[node][1].popitem()
			if v-1 > 0: 
				graph[node][1].update({nn: v-1})
				graph[nn][0].update({node: -1})
			else:
				graph[nn][0].pop(node)
			stack.append(nn)
	print(*path[::-1])

