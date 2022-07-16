from debug import *
from bisect import *



def spiralOrder(A):
    if not A: return []
    return [*A[0]] + spiralOrder([k[0] for k in zip(i[::-1] for i in A)][1:])



A = [[10*i + 4*j for j in range(5)] for i in range(5)]

debug(b=A)
debug(a=[k for k in zip(*[i[::-1] for i in A])])
# s = spiralOrder(A)
# print(s)


print(*zip((12,3,4), (3,4,5)))