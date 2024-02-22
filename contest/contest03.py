from debug import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)




# Point class for 
# 2-D points

class point:
    def __init__(self, x, y) :

        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x},{self.y})"


def dis(a,b):
    print(a,b)
    return (a.x-b.x)**2 + (a.y-b.y)**2

def bruteForce(lis):
    ans = 10**13
    for i in range(len(lis)):
        for j in range(i):
            ans = min(ans, dis(lis[i], lis[j]))
    return ans


def closestPair(cordinates, n) :
    xcords = sorted(cordinates, key=lambda p:p.x)
    ycords = sorted(cordinates, key=lambda p:p.y)

    def getStrip(lis, mid, d):
        store = []
        for p in lis:
            if dis(p, point(mid, p.y)) <= d:
                store.append(p)
        return store

    def rec(xlis, ylis):
        if len(xlis) <= 5: return bruteForce(xlis)
        # split
        xleft, xright = xlis[:n//2], xlis[n//2:]
        yleft, yright = [], []
        mid = xleft[-1]
        for p in ylis:
            if p.x <= mid.x: yleft.append(p)
            else: yright.append(p)
        
        d1 = rec(xleft, yleft)
        d2 = rec(xright, yright)
        d = min(d1, d2)
        store = getStrip(ylis, mid, d)
        final = 10**13
        for i in range(len(store)):
            for j in range(1, 16):
                if i+j<len(store):
                    final = min(final, dis(store[i], store[i+j]))
        
        return min(final, d)
            
    # Your code here
    # return square of minimum distance between n points
    return rec(xcords, ycords)


#taking inpit using fast I/O
def takeInput() :
    
    n = int(input().strip())

    if n == 0 :
        return list(), n

    cordinates = [point(0,0) for i in range(n)]

    for i in range(n) :
        arr = list(map(int,stdin.readline().strip().split(" ")))
        cordinates[i] = point(arr[0], arr[1])

    return cordinates, n


#main
cordinates, n = takeInput()
print(closestPair(cordinates, n))
