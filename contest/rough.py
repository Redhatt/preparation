import sys
 
n, q = map(int, sys.stdin.readline().split())
a = [int(x) for x in sys.stdin.read().split()]
 
dest, h = [0] * (2 * n - 2), [0] * (n + 2)
for i in range(0, 2 * n - 2, 2):
    v, u = a[i:i + 2]
    h[v] += 1
    h[u] += 1
for i in range(1, len(h)):
    h[i] += h[i - 1]
for i in range(0, 2 * n - 2, 2):
    u, v = a[i:i + 2]
    dest[h[u] - 1], dest[h[v] - 1] = v, u
    h[u], h[v] = h[u] - 1, h[v] - 1
 
s, loc, par = [1], [h[1]], [0] * (n + 1)
cc, fc, tc, dd = 1, [0] * (n + 1), [0] * (n + 1), [0] * (n + 1)
fc[1] = 1
while len(s) > 0:
    v, z = s[-1], loc[-1]
    if z == h[v + 1]:
        s.pop(), loc.pop()
        cc += 1
        tc[v] = cc
        continue
    u, loc[-1] = dest[z], z + 1
    if u != par[v]:
        cc += 1
        fc[u] = cc
        dd[u] = dd[v] + 1
        par[u] = v
        s.append(u), loc.append(h[u])
fc[0], tc[0] = 0, cc + 1
 
t = [par]
for i in range(18):
    ti = t[-1]
    t.append([ti[ti[j]] for j in range(n + 1)])
 
r = []
for i in range(2 * n - 2, len(a), 2):
    x, y, k = a[i], a[i + 1], 17
    if fc[x] <= fc[y] and tc[y] <= tc[x]:
        r.append(str(dd[y] - dd[x]))
        continue
    while k >= 0:
        z = t[k][x]
        if not (fc[z] <= fc[y] and tc[y] <= tc[z]):
            x = z
        k = k - 1
    lca = t[0][x]
    r.append(str(dd[a[i]] + dd[a[i + 1]] - 2 * dd[lca]))
 
sys.stdout.write('\n'.join(r))