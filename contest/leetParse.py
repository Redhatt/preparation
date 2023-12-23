from debug import *
import json
from collections import defaultdict

JI = lambda : json.loads(input().strip())


###########################
class Node:
    def __init__(self):
        self.key = 0
        self.value = 0
        self.n = None
        self.p = None

    def __repr__(self):
        return f"[k:{self.key}, v:{self.value}]"
        
class List:
    def __init__(self):
        self.head, self.tail = Node(), Node()
        self.head.n, self.tail.p = self.tail, self.head
        
    def remove(self, node):
        before, after = node.p, node.n
        before.n, after.p = after, before
        
    def popleft(self):
        if self.head.n == self.tail:
            return 
        self.remove(self.head.n)

    def append(self, node):
        before, after = self.tail.p, self.tail
        before.n, node.p, node.n, after.p = node, before, after, node

    def __repr__(self):
        s = ""
        node = self.head.n
        while node != self.tail:
            s += node.__repr__() + ", "
            node = node.n
        return '(' + s[:-1] + ')'

class LRUCache:

    def __init__(self, capacity: int):
        self.c = capacity
        self.index = defaultdict(Node)
        self.recent = List()
        
    def _get(self, key):
        if key not in self.index:
            return None
        
        node = self.index[key]
        self.recent.remove(node)
        self.recent.append(node)
        return node

    def get(self, key: int) -> int:
        node = self._get(key)
        debug(r=self.recent)
        return node.value if node else -1
            
    def put(self, key: int, value: int) -> None:
        # print(self.recent)
        if self.c == 0:
            return 
        
        node = self._get(key)
        if node:
            node.value = value
            return 
        
        if len(self.index) == self.c:
            self.recent.popleft()
            self.index.pop(key)
        
        node = self.index[key]
        node.key, node.value = key, value
        self.recent.append(node)
        debug(r=self.recent)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

###########################
#==============================================




#----------------------------------------------
a, b = JI(), JI()
obj = None

for x, y in zip(a, b):
    temp = "null"
    if x == "LRUCache":
        obj = LRUCache(*y)
    elif x == "get":
        temp = obj.get(*y)
    elif x == "put":
        obj.put(*y)
    print(temp)