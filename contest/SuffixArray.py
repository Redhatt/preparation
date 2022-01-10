from debug import *

a = ord(a)
s = "banana"
n = len(s)
sa = [[0, 0, 0] for i in range(n)]
for i in range(n):
	sa[i] = i, ord(s[i])-a, ord(s[i+1])-a if i+1<n else -1
sa.sort()

k = 4
while k<2*n:
	