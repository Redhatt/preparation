import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from debug import *

points = []

s = "C:\\Users\\d09am\\Desktop\\hld.txt"
with open(s, 'r') as f:
	while 1:
		e = f.readline()
		if not e: break
		a = list(map(float, e.strip().split()))
		if a: points.append(a)

print(len(points))
x, y, z = zip(*points)
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(x,y,z)
# plt.show()