from debug import *

s = ""
while 1:
	try: s+=input()+"\n"
	except EOFError: break

def final(s):
	n = len(s)
	pos = []
	for i in range(n):
		if s[i] == '{': pos.append(2*i)
		elif s[i] == '}': pos.append(2*i+1)
	last = 0
	space = 0
	diff = 4
	for i in pos:
		if i&1==0: 
			index = i//2
			strings = s[last:index].split(";")
			k = 0
			while k<len(strings):
				# detecting while, for (auto) and if
				if (strings[k].find('while') != -1) or \
				(strings[k].find('for') != -1 and strings[k].find('auto') != -1) or\
				(strings[k]. find('if') != -1):
					temp = strings[k]
				elif strings[k].find('for') != -1:
					temp = strings[k]+'; '+strings[k+1]+'; '+strings[k+2]
					k+=2
				else:
					temp = strings[k]
				# temp = strings[k] # json
				if k != len(strings)-1: temp += ';'
				print(" "*space+temp.strip())
				k+=1
			print(" "*space+'{')
			space+=diff
			last = index+1
		else: 
			index = (i-1)//2
			index = i//2
			strings = s[last:index].split(";")
			for string in strings[:-1]: print(" "*space+string.strip()+";")
			space-=diff
			print(" "*space+'}')
			last = index+1

final(s)

