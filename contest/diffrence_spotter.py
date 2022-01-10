from debug import debug
s = 0
if s:
	s1 = input().strip()
	s2 = input().strip()
else:
	s1 = list(input().strip().split(','))
	s2 = list(input().strip().split(','))

print(len(s1), len(s2))
for i in range(max(len(s1), len(s2))):
	a,b = "$", "#"
	if i<len(s1): a = s1[i]
	if i<len(s2): b = s2[i]
	if a != b: print(f"{a}  {b}  diff at {i}")
	# else: print(f"{a}  {b}  OK")
	