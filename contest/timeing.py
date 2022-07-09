import timeit
from debug import debug

def time_(file):
	with open(file, 'r') as f:
		val = f.read()
		debug(Time=str(timeit.timeit(stmt=val, number=1)*1000)[:7 ]+"ms")

if __name__ == "__main__":
	# file = "contest01.py"
	file = "rough.py"
	time_(file)
