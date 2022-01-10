import sys
import time
sys.stdin=open('test_input.txt','r')
sys.stdout=open('output.txt','w')

def timit(func):
	"""
           timit Decorator
Its a debug decorator to get number of function calls and time taken to execute the function.
timit significantly affects running time of functions.
Runtime may increase by 133%.
But time returned by timit has a relative error of 6-10 %.
Actual Example.
>||Time = 2593.29ms|| actual
>||Time = 3672.60ms|| just wrapping
>||Time = 4731.96ms|| wrapping with calls
>||Time = 6051.84ms|| wrapping with calls and time
>||Time = 2784.02ms|| time determined by timit.
	"""
	def wrap(*args, **kwargs):
		wrap.call += 1
		val = func(*args, **kwargs)
		wrap.time = time.time() - wrap.time
		return val
	wrap.call = 0
	wrap.time =  time.time()
	return wrap

store = (set, list, tuple, dict)
def printrec(a, space=0, d=2, first=True, prefix=""):
	under = False
	if isinstance(a, list) or isinstance(a, tuple) or isinstance(a, dict):
		if isinstance(a, dict):
			for i in a.values():
				if isinstance(i, list) or isinstance(i, tuple) or isinstance(i, dict): under = True; break
		else:
			for i in a:
				if isinstance(i, list) or isinstance(i, tuple) or isinstance(i, dict): under = True; break
		if under:
			if isinstance(a, list):
				print(" "*(space) + prefix + '[')
				space+=len(prefix)
				for i in a:
					printrec(i, space=space+d, d=d, first=False)
				if first: print(" "*(space) + ']')
				else: print(" "*(space) + '],\n')

			elif isinstance(a, tuple):
				print(" "*(space) + prefix + '(')
				space+=len(prefix)
				for i in a:
					printrec(i, space=space+d, d=d, first=False)
				if first: print(" "*(space) + ')')
				else: print(" "*(space) + '),\n')

			elif isinstance(a, dict):
				print(" "*(space) + prefix + '{')
				space+=len(prefix)
				for k,v in a.items():
					printrec(v, space=space+d, d=d, first=False, prefix=f"{repr(k)}: ")
				if first: print(" "*(space) + '}')
				else: print(" "*(space) + '},\n')
		else:
			print(f'{" "*(space)+prefix}{a}', end=",\n")
	else: print(f'{" "*(space+ (1 if prefix=="" else 0))+prefix}{repr(a)}', end=",\n")

def debug(**kwargs):
	"""
	        debug
A debug function to print variable and objects in a nice and understandable format.
@params: keyWordArguments
@print -> variable_name_passed : variable_referenced_value
For more understanding run debug.py and check examples in main.
	"""
	print("_____________________")
	for i, j in kwargs.items():
		print(">", end="")
		if isinstance(j, list) or isinstance(j, tuple):
			if j and (isinstance(j[0], list) or isinstance(j[0], tuple) or isinstance(j[0], dict)):
				print(f"{i} = {len(j), len(j[0])}")
				printrec(j, space=1)
			else:
				print(f"{i} = ({len(j)})")
				printrec(j, space=1)
		elif isinstance(j, dict):
			print(f"{i} = ({len(j)})")
			printrec(j, space=1)
		else:
			if i == 'Time':
				print(f"||{i} = {j}||")
			else:
				print(f"{i} = {j}, ({type(j)})")
	print("---------------------")


def pr(func):
	"""
            pr Decorator
Its a debug decorator to print return value of function.
Use example. 
When you are directly passing function values and may want to know what you have passed.
rather than making dummy variable to store function values and printing it, just decorate the function with this decorator.
	"""
	def wrap(*args, **kwargs):
		val = func(*args, **kwargs)
		debug(function_name=func.__name__, returned=val)
		return val
	return wrap

if __name__ == "__main__":
	x = 1
	y = '2'
	z = [1,2,3,4]
	a = [[0,0,0],[1,1,1],[2,2,2]]	
	c = {1:[1,2,3], 2: 3}
	d = [[[{'a': 2, 'b': 3}, (1,2,3), ['a','b','c']],1,2,3,4], {1:1, 2:2, 3:3, 4:4}, (1,2,3,4), 'a']
	e = ['q',{'a':{1: '11', 2: 22, 3: 33, 4:{'r': 23, 's': 45}}, 'b': [1,2,3,4], 1: ('asd', 'car')},'2',3]
	f = {'distance': 1024,'name': 'danish','type': {'a': 1, 'b': 2, 'c': 3, 'd': [[1,2,3], [4,5,6]]},4: (1,2,3)}
	debug(x=x, y=y, z=z, a=a, d=d, e=e, f=f)
