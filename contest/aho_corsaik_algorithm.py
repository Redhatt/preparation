from debug import debug, timit
from collections import deque

# word = input().strip()
# words = [input().strip() for _ in range(int(input()))]
words = ["ab", "abab", "c", "cb", "ba"]
word = "ababc"
word += "$" # this here is important to add because in my code things process in last of for loop and in
# next iteration things get update but for last itr of for loop, last upadete doesn't happen if some additional
# letter is not added
class Node:
	def __init__(self, value=""):
		self.value = value
		self.end = 0
		self.d = dict()
		self.f = None

root = Node("#")

# making a trie...
def fill(root, w):
	if w == "": root.end = 1
	else:
		if w[0] not in root.d: root.d[w[0]] = Node(w[0])
		fill(root.d[w[0]], w[1:])

def find(root, w):
	if w == "": return root
	elif w[0] not in root.d: return None
	else: return find(root.d[w[0]], w[1:])

def dfs(root):
	print(root.value, root.end, end=" ")
	if root.f is not None: print(root.f.value)
	else: print()
	for i in root.d.values(): dfs(i)

for i in words: fill(root, i)

# making fail links...
q = deque()
root.f = root

# sort of base case because root is fail link of every root's child...
for i in root.d.values():
	i.f = root
	q.append(i)

# bfs to level order traversal...
while q:
	node = q.popleft()
	for child in node.d.values():
		# finding the value of child in the fail links of current node and connecting it to child's fail link
		if node.f: child.f = find(node.f, child.value)
		else: child.f = find(root, child.value) # if no fail links for curr node search it in root...
		q.append(child)

# dfs(root)
ans = 0
temp = root
for i in word:
	if temp.end: ans+=1 # got the word from words
	if i in temp.d: temp = temp.d[i] # keep going to down to get word
	elif temp.f is not None and i in temp.f.d: # if mismatch then search it in fail link
		if temp.f.end: ans+=1 # so it may happend the fail link itself is end so add 1 to answer and then go to its child
		temp = temp.f.d[i]
	elif i in root.d: temp = root.d[i] # if not in fail link then have to check in root.
	else: temp = root # if not in root then start from root
print(ans)

