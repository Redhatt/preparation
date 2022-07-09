#=================================
# Author: Danish Amin
# Date: Mon Nov 30 17:46:57 2020
#=================================

from debug import *
import sys;input = sys.stdin.readline
import time

I =  lambda :int(input())
L = lambda :list(map(int, input().split()))
T = lambda :map(int, input().split())
mod = int(1e9) + 7

class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)
        mod = 7 + 10**9
        prime = 31
        ans = 0
        d = {""}
        
        get = lambda x: ord(x) - ord('a') + 1
        
        def getHash(s):
            ans = 0
            n = len(s)
            for i, x in enumerate(s):
                ans = (ans + get(x) * pow(prime, n-1-i))%mod
            return ans
        
        def rollHash(value, size, insert, pop):
            value = (value - get(pop)*pow(prime, size-1))%mod
            value = (value*prime + get(insert))%mod
            return value
        
        for half in range(1, 1 + n//2):
            ah = getHash(text[:half])
            bh = getHash(text[half:2*half])
            
            if ah == bh and ah not in d:
                d.add(ah)
                ans += 1
            
            start, end = 1, 2*half
            while end<n:
                p1 = text[start - 1]
                i1 = text[start + half - 1]
                
                p2 = i1
                i2 = text[end]
                
                ah = rollHash(ah, half, i1, p1)
                bh = rollHash(bh, half, i2, p2)
                
                if ah == bh and ah not in d:
                    d.add(ah)
                    ans += 1
                
                start += 1
                end += 1
        
        return ans


s = input().strip()
obj = Solution()

profile(obj.distinctEchoSubstrings, s)
