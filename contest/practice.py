from debug import *
# import sys, os, io; input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
from math import ceil, log2
from itertools import accumulate
inf = 10**9 + 1


S = lambda : input().strip()
L = lambda :list(map(int, input().split()))
I = lambda :int(input())
T = lambda :map(int, input().split())
mod = int(1e9) + 7


class SegTree:
    def __init__(self, price, pivot):
        self.pivot = pivot
        p = len(price)
        self.price = price
        self.n = 2**(ceil(log2(p)))
        self.tree = [inf]*self.n + [*price] + [inf]*(self.n - p)
        for i in reversed(range(1, self.n)):
            self.tree[i] = min(self.tree[i<<1], self.tree[(i<<1)|1])


    def update(self, i, val):
        i += self.n-1
        while i:
            self.tree[i] = min(self.tree[i<<1], self.tree[(i<<1)|1])
            i <<= 1

    def query(self, l, r):
        l, r = l+self.n-1, r+self.n-1
        ans = 0
        while l<=r:
            if l&1: ans+=self.tree[l]; l+=1;
            if r&1==0: ans += self.tree[r]; r-=1;
            l, r = l>>1, r>>1
        return ans

    def get_min_price(self, index):
        dis = abs(self.pivot - index)
        right_min = self.query(1, self.pivot) + dis
        left_min = self.query(index, self.n) - dis
        mid_min = min([self.price[i] + 2*(i-self.pivot) - dis for i in range(self.pivot, index)])
        return min(left_min, mid_min, right_min)


class Mapper:
    def __init__(self, lis):
        self.lis = lis
        self.n = len(lis)
        self.sqrt_n = int(self.n)

        self.segments = []
        for i in range(1, self.n, self.sqrt_n):
            lis = []


    def get_min_price(self, index):



n, q = T()
price = L()



 '''
    Time Complexity: O(2 ^ N * N ^ 2 + (N * |L|) ^ 2)
    Space Complexity: O(N * 2 ^ N + N ^ 2),
                
    where 'N' is the size of the set, 
    and '|L|' is the length of string present in the set.
'''

def optimalSuperstring(s, size):
    
    # Find for overlaps.
    for i in range (size):
        for j in range (size):
            if i != j and s[i] != "" and s[i] in s[j]:
                s[i] = ""
                
    updatedSet = []
    for i in s:
        if i != "":
            updatedSet.append(i)
            
    # Changing the size.
    size = len(updatedSet)
    
    targetMask = (1 << size) - 1
    mask = 0
    
    dp = [[-1 for j in range (targetMask + 1)] for i in range (size + 1)]
    computed = [[-1 for j in range (size + 1)] for i in range (size + 1)]
    
    def nonOverlappingSuffix(updated, last, current):
        if last == -1:
            return len(updated[current])
        # If nonOverlappingSuffix is already computed then return that value.
        if computed[last][current] != -1:
            return computed[last][current]
        
        a = updated[last]
        b = updated[current]
        
        n, m = len(a), len(b)
        
        # Matching the suffix of 'a' starting at index i with prefix of 'b'.
        for i in range (n):
            suffix = True
            j = 0
            while j < m and (i + j) < n:
                if b[j] != a[i + j]:
                    suffix = False
                    break
                j += 1
                
            if suffix:
                suffixLengthOfA = n - i
                computed[last][current] = m - suffixLengthOfA
                return m - suffixLengthOfA
            
        computed[last][current] = m
        return m
    
    def helper(updated, last, mas, target):
        if mas == target:
            dp[last + 1][mas] = 0
            return 0
        
        if dp[last + 1][mas] != -1:
            return dp[last + 1][mas]
        
        ans = 10**9
        
        # Trying all the not included strings to be included as next.
        for i in range (len(updated)):
            if ((1 << i) & mas) == 0:
                ans = min(ans, helper(updated, i, mas | (1 << i), target) + nonOverlappingSuffix(updated, last, i))
        
        dp[last + 1][mas] = ans
        
        return ans
    
    return helper(updatedSet, -1, mask, targetMask)
 