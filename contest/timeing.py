import timeit
from debug import debug
import numpy as np

def time_(file):
	with open(file, 'r') as f:
		val = f.read()
		time = timeit.timeit(stmt=val, number=1)*1000
		# debug(Time=str(time)[:7 ]+"ms")
	return time

if __name__ == "__main__":
	# file = "contest01.py"
	file = "rough.py"

	n = 10
	a = []
	for i in range(n):
		a.append(time_(file))
	a = np.array(a, dtype=np.float32)
	debug(unit="sec", mean=a.mean(), var=a.var(), min=min(a), max=max(a))



# chain
# _____________________
# >mean = 0.19789999723434448, (<class 'numpy.float32'>)
# >var = 0.0011369922431185842, (<class 'numpy.float32'>)
# >min = 0.16479997336864471, (<class 'numpy.float32'>)
# >max = 0.27810001373291016, (<class 'numpy.float32'>)
# ---------------------


# reduce
# _____________________
# >mean = 0.7558600306510925, (<class 'numpy.float32'>)
# >var = 0.005067153833806515, (<class 'numpy.float32'>)
# >min = 0.7098000049591064, (<class 'numpy.float32'>)
# >max = 0.9624999761581421, (<class 'numpy.float32'>)
# ---------------------

# sum
# _____________________
# >mean = 1.0075899362564087, (<class 'numpy.float32'>)
# >var = 0.09194616228342056, (<class 'numpy.float32'>)
# >min = 0.7982000112533569, (<class 'numpy.float32'>)
# >max = 1.625, (<class 'numpy.float32'>)
# ---------------------

