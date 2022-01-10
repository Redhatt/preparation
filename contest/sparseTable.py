from debug import debug
from math import ceil, log2
inf = int(1e3)

lis = [7,2,3,0,5,10,3,12,18]
n = len(lis)

def table(lis, inf = int(1e10)):
	n = len(lis)
	k = int(log2(n))+1
	grid = [[inf for _ in range(k)] for _ in range(n)]
	for i in range(n): grid[i][0] = lis[i]
	i = 0; j = 1
	while j<k:
		i = 0
		while i+(1<<j)-1<n:
			grid[i][j] = min(grid[i][j-1], grid[i+(1<<(j-1))][j-1])
			i+=1
		j+=1
	return grid

def querry(table, a, b):
	s = log2(b-a+1)
	if int(s) == ceil(s):
		return table[a][int(s)]
	s = int(s)
	return min(table[a][s], table[b-(1<<s)+1][s])

if __name__ == "__main__":
	t = table(lis)
	debug(lis=lis,grid=t)
	for i in range(n):
		for j in range(i+1):
			ans = querry(t, j, i)
			if not (ans==min(lis[j:i+1])):
				print(j, i, ans, min(lis[j:i+1]))