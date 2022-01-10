# from debug import *

from collections import deque
import sys; input = sys.stdin.readline

n, m = map(int, input().strip().split())
matrix = [["" for i in range(m)] for i in range(n)]
parent = [[(-1, -1) for i in range(m)] for i in range(n)]
pos = []
exit = (0, 0)

for i in range(n):
    lis = list(input().strip())
    for j in range(m):
        matrix[i][j] = lis[j]

        if lis[j] == 'A':
            pos.insert(0, (i, j, lis[j]))
            if i in (0, n-1) or j in (0, m-1):
                print("YES")
                print(0)
                print()
                sys.exit()

        elif lis[j] == 'M':
            pos.append((i, j, lis[j]))

def path(a, b, x, y):
    if (x-a, y-b) == (1, 0): return 'D'
    if (x-a, y-b) == (-1, 0): return 'U'
    if (x-a, y-b) == (0, 1): return 'R'
    if (x-a, y-b) == (0, -1): return 'L'


def valid(x, y): return (0<=x<n) and (0<=y<m)


moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

flag = 0
q = deque(pos)

while q:
    x, y, val = q.popleft()
    val = matrix[x][y]

    if val == 'A' and (x in (0, n-1) or y in (0, m-1)):
        exit = (x, y)
        flag = 1
        break

    for u, v in moves:
        xx, yy = x+u, y+v

        if valid(xx, yy):
            if matrix[xx][yy] == '.':
                matrix[xx][yy] = val
                q.append((xx, yy, val))

                if val == 'A':
                    parent[xx][yy] = (x, y)

            elif matrix[xx][yy] == 'A' and val == 'M':
                matrix[xx][yy] = 'M'
                q.append((xx, yy, 'M'))

if flag:
    print("YES")
    ans = ""
    while parent[exit[0]][exit[1]] != (-1, -1):
        x, y = exit[0], exit[1]
        a, b = parent[x][y]
        ans += path(a, b, x, y)
        exit = (a, b)
    print(len(ans))
    print(ans[::-1])
else:
    print("NO")

 
for i in parent: print(*i)

