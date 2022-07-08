from debug import *
import json

JI = lambda : json.loads(input().strip())


###########################
class MagicDictionary:

    def __init__(self):
        self.root = dict()

    def buildDict(self, dictionary: list) -> None:
        for word in dictionary:
            node = self.root
            for char in word:
                node = node.setdefault(char, dict())
            node['#'] = True
    
    def search(self, searchWord: str) -> bool:
        def search_(node, word, skip):
            if word == "":
                return node.get('#', False) and skip == 0
            
            if skip < 0:
                return False
            
            for char in node:
                if char == '#':
                    continue
                elif char == word[0] and search_(node[char], word[1:], skip):
                    return True
                elif search_(node[char], word[1:], skip-1):
                    return True
            
            return False
        return search_(self.root, searchWord, 1)
        
# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)


###########################


#==============================================




#----------------------------------------------
a, b = JI(), JI()
obj = None

for x, y in zip(a, b):
	if x == "MagicDictionary":
		obj = MagicDictionary()
		print("null")
	elif x == "buildDict":
		obj.buildDict(*y)
		print("null")
	elif x == "search":
		print(obj.search(*y))
