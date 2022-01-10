#=================================
# Author: Danish Amin
# Date: Mon Nov 30 17:46:57 2020
#=================================
from debug import *	
import sys;input = sys.stdin.readline

I =  lambda : int(input())
L = lambda :list(map(int, input().split()))
T = lambda :map(int, input().split())
mod = int(1e9) + 7


b = [1,2,2] * -2

print(b)