from debug import *
from math import ceil, log2
# import sys, os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

I =  lambda :int(input().strip())
L = lambda :list(map(int, input().split()))
T = lambda :map(int, input().split())


def checkIndices(arr, a, b):
    # Write your code here.
    from bisect import insort, bisect_left
    temp = []
    for i in range(a):
        insort(temp, arr[i])


    for i in range(a, len(arr)):
        if i>a:
            insort(temp, arr[i])
        index = bisect_left(temp, arr[i]+b)
        if index < len(temp) and abs(arr[i] - temp[index]) <= b:
            return True

        index = bisect_left(temp, arr[i]-b)
        if index < len(temp) and abs(arr[i] - temp[index]) <= b:
            return True

        temp.remove(arr[i-a])

    return False


n = I()
for i in range(n):
    N,a,b = T()
    arr = L()
    ans = checkIndices(arr, a, b)
    print(ans)