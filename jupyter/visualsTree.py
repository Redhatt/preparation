#=================================
# Author: Danish Amin
# Date: Wed Nov 11 00:40:04 2020
#=================================
# from debug import *    
import sys;input = sys.stdin.readline
from collections import deque
import random

class Node:
    def __init__(self, val=0):
        self.val = val
        self.data = val
        self.right = None
        self.left = None
    
    def __repr__(self):
        return str(hex(id(self)))
    
    def __str__(self):
        return str(self.val)
        
def notNull(node):
    if node is None: return False
    if isinstance(node, str): return node.lower() not in ('n', 'none', 'null')
    return True

def randomTree(height=4, sparse=0.5, max_range=100):
    def build(lis):
        n = len(lis)
        if n == 0: return None
        index = random.choice(list(range(n)) + list(range(n))[1:-1] + list(range(n))[1:-1])

        root = Node(lis[index])
        root.left = build(lis[:index])
        root.right = build(lis[index+1:])
        return root
    lis = random.sample(range(0, max_range), int((2**height)*sparse))
    return build(lis)

def makeLevel(level):
    if not level: return None
    root = Node(level[0])
    i = 1
    q = deque([root])
    
    while q and i<len(level):
        node = q.popleft()
        
        if notNull(level[i]):
            node.left = Node(level[i])
            q.append(node.left)
        i+=1
        if i>=len(level): break
        
        if notNull(level[i]):
            node.right = Node(level[i])
            q.append(node.right)
        i+=1
    return root
    

def make(level):
    level = list(level)
    n = len(level)
    node = [Node(i) if notNull(i) else None for i in level]
    for i in range(n):
        if notNull(level[i]):
            if 2*i+1<n: node[i].left = node[2*i+1]
            if 2*i+2<n: node[i].right = node[2*i+2]
    return node[0]

def makeMid(level):
    level = list(level)
    n = len(level)
    nlis = [Node(i) if i != 'N' else None for i in level]

    def BST(lis, start, end):
        if start > end: return None 

        mid = (start + end)//2
        root = lis[mid]
        root.left = BST(lis, start, mid-1)
        root.right = BST(lis, mid+1, end)

        return root

    return BST(nlis, start=0, end=n-1)


def frt(s, dis=5, v=" ", w=" "):
    from math import ceil
    s = str(s)
    k = (dis-len(s))/2
    a, b = int(k), ceil(k)
    return v*a + s + w*b


def visual(root, dis=5):
    def dfs(node, h=1, l=0):
        m = h
        e = l
        if node:
            if node.left: 
                a, b = dfs(node.left, h+1, l-1)
                m, e = max(a, m), min(e, b)
            if node.right: 
                a, b = dfs(node.right, h+1, l+1)
                m, e = max(a, m), min(e, b)
        return m, e

    mh, ml = dfs(root)
    x = 0
    for i in range(-ml):
        x += 2**(mh-i)

    q = deque([(0, x, root)])
    prev = 0
    last = 0
    s = ""    
    places = []
    line = []
    far_left = 0
    while q:
        h, pos, node = q.popleft()
        far_left = max(pos, far_left)
        if prev != h:
            prev = h
            places.append(line)
            line = []
        line.append((pos, node.val))
        if node.left: q.append((h+1, pos-2**(mh-h), node.left))
        if node.right: q.append((h+1, pos+2**(mh-h), node.right))
    places.append(line)
    print("-"*far_left)
    for line in places:
        last = 0
        for i in line:
            print(" "*(i[0]-last)+frt(i[1], dis=dis), end="")
            last = i[0]+dis
        print()
    print("_"*far_left)


def preOdr(root):
    def preOdr_(root):
        if root:
            print(root.data, end=" ")
            preOdr_(root.left)
            preOdr_(root.right)
    preOdr_(root)
    print()


def posOdr(root):
    def posOdr_(root):
        if root:
            posOdr_(root.left)
            posOdr_(root.right)
            print(root.data, end=" ")
    posOdr_(root)
    print()


def inOdr(root):
    def inOdr_(root):
        if root:
            inOdr_(root.left)
            print(root.data, end=" ")
            inOdr_(root.right)
    inOdr_(root)
    print()

def levOdr(root):
    if root is None: return None

    q = deque([root])

    while q:
        node = q.popleft()
        print(node.data, end=" ")
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)

    print()

from PIL import ImageFont
from PIL import Image, ImageDraw, ImageFont
from collections import defaultdict, deque
from math import log2, ceil, log10

class DrawTree:
    def __init__(self, root, size=None):        
        self.root = root
        
        # width, height
        self.size = size
        self.bg_size = (10000, 10000)            
        self.node_size = (400, 400)
        self.font_size = 130
        self.line_width = 10
        self.startx = self.node_size[0]
        self.starty = self.node_size[1]
        
        self.clrs = {
                     'white': (245, 245, 245), 
                     'blue': (191, 213, 255), 
                     'green': (191, 255, 192), 
                     'red': (255, 191, 191), 
                     'cyan': (184, 255, 251),
                     'black': (20, 20, 20),
                    }
        self.bg_clr = (255, 255, 255, 50)
        self.node_clr = 'white'
        self.font_clr = 'black'
        self.outline_clr = 'black'
        self.max_chrs = 6
        
        self.left = self.bg_size[0]
        self.right = 0
        self.top = self.bg_size[1]
        self.bottom = 0
        
        self.nodemap = dict()
    
    def drawPoint(self, pos, clr='red'):
        self.draw.ellipse(tuple(map(int, (pos[0]-50, pos[1]-50, pos[0]+50, pos[1]+50))), fill=self.clrs[clr], outline=self.outline_clr)
        
    def drawNode(self, root, pos):
        if root is None: return 
        x1, y1 = pos[0] - self.node_size[0]/2, pos[1] - self.node_size[1]/2
        x2, y2 = pos[0] + self.node_size[0]/2, pos[1] + self.node_size[1]/2
        
        posf = ((pos[0] + x1)/2, (pos[1] + y1)/2)
#         self.draw.rectangle(tuple(map(int, (x1, y1, x2, y2))), fill=self.clrs[self.node_clr], outline=self.outline_clr, width=self.line_width)
        self.draw.ellipse(tuple(map(int, (x1, y1, x2, y2))), fill=self.clrs[self.node_clr], outline=self.outline_clr, width=self.line_width)
        self.drawFont(tuple(map(int, (x1, y1))), root.val)
#         self.drawPoint((x1, y1))
    
    def drawLine(self, point1, point2):
        self.draw.line(tuple(map(int, (*point1, *point2))), fill=self.clrs[self.outline_clr], width=self.line_width)
    
    def drawFont(self, pos, string):
        string = str(string)
        if len(string) > self.max_chrs: string = string[:4] + '..'
        font = ImageFont.truetype("arial", self.font_size)
        W, H = pos
        w, h = self.draw.textsize(string)
        w *= 12
        h *= 12
        a, b = self.node_size
#         self.drawPoint((W + (a-w)/2, H + (b-h)/2))
        self.draw.text(tuple(map(int, (W + (a-w)/2, H + (b-h)/2))), string, fill=self.font_clr, font=font)
    
    def drawTree(self, color='white'):
        self.node_clr = color if color in self.clrs else 'white'
        
        self.image = Image.new('RGBA', self.bg_size, self.bg_clr)
        self.draw = ImageDraw.Draw(self.image)
        
        self.setNodePos(self.root)
        self.drawEdges(self.root)
        self.drawNodes(self.root)
        
        area = (self.left-self.node_size[0], self.top - self.node_size[0], 
                self.right + self.node_size[0], self.bottom + self.node_size[0])
        self.image = self.image.crop(area)
        
        width, height = area[2] - area[0], area[3] - area[1]
        if self.size:
            factor = self.size[0]/width
            self.resize = (width * factor, height*factor)
        else:
            self.resize = (500, 300)
            
        self.resize = tuple(map(int, self.resize))
        self.image = self.image.resize(self.resize, resample=Image.ANTIALIAS)
        self.image.save('tree.png')
        return self.image
    
    def setNodePos(self, root):
        if root is None: return
        self.starty += self.node_size[1]*1.1
        self.setNodePos(root.left)
        
        self.nodemap[root] = (self.startx, self.starty, root)
        
        self.left = min(self.left, self.startx)
        self.right = max(self.right, self.startx)
        self.top = min(self.top, self.starty)
        self.bottom = max(self.bottom, self.starty)
        
        self.startx += self.node_size[1]*0.55
        
        self.setNodePos(root.right)
        self.starty -= self.node_size[1]*1.1
        
    def drawEdges(self, root, last=None):
        if root is None: return
        self.drawEdges(root.left, root)
        
        if last in self.nodemap:
            self.drawLine(self.nodemap[root][:-1], self.nodemap[last][:-1])
            
        self.drawEdges(root.right, root)
            
    
    def drawNodes(self, root):
        for node in self.nodemap:
            self.drawNode(self.nodemap[node][-1], self.nodemap[node][:-1])
    
    def getHeight(self, root):
        if root is None: return 0
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))
    
def jdraw(root):
    return DrawTree(root, (300, 300)).drawTree()

if __name__ == '__main__':
    level = list(range(0, 12))
    one = make(level)
    oneMid = makeMid(level)

    root = Node(0)
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)
    f = Node(6)
    g = Node(7)
    h = Node(800)

    root.left = a
    root.right = b

    b.left = c
    b.right = d

    d.left = e
    d.right = f

    f.left = g
    f.right = h

    visual(one)
    visual(oneMid)
    visual(root)
