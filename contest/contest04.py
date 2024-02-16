#=================================
# Author: Danish Amin
# Date: Mon Nov 30 17:47:32 2020
#=================================
from debug import * 
import sys;input = sys.stdin.readline
from bisect import *
from collections import defaultdict




exp = "s+(a-b/c)*(a/k-l)"

def solve(exp):
    stack = []
    op = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    for i in reversed(exp):
        if i in op.keys():
            a = stack.pop()
            b = stack.pop()
            c = '(' + a + i + b + ')'
            stack.append(c)
        else:
            stack.append(i)
        
    return stack.pop()

print(solve(exp))