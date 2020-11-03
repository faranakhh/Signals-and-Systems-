import numpy as np
from matplotlib import pyplot as plt
import math


pi = math.pi
start = -20
end = 20
step = 1
n = np.linspace(start, end, int((end - start) / step))

y1 = np.heaviside(n, 1) - np.heaviside(n - 3, 1) + np.heaviside(n - 5, 1)
plt.stem(n, y1,use_line_collection=True)
plt.xlabel('t')
plt.ylabel('x1(t)')
plt.show()

y2_1 = 2 * np.cos(2 * n * pi)  # for k=1
plt.stem(n, y2_1,use_line_collection=True)
plt.xlabel('t')
plt.ylabel('x2_1(t)')
plt.show()

y2_1 = 2 * np.cos(2 * n * pi * 2)  # for k=2
plt.stem(n, y2_1,use_line_collection=True)
plt.xlabel('t')
plt.ylabel('x2_2(t)')
plt.show()

y2_3 = 2 * np.cos(2 * n * pi * 3)  # for k=3
plt.stem(n, y2_3,use_line_collection=True)
plt.xlabel('t')
plt.ylabel('x2_3(t)')
plt.show()

y3_1 = 2 * np.cos(2 * n)  # for k=1
plt.stem(n, y3_1,use_line_collection=True)
plt.xlabel('t')
plt.ylabel('x3_1(t)')
plt.show()

y3_2 = 2 * np.cos(2 * n * 2)  # for k=2
plt.stem(n, y3_2,use_line_collection=True)
plt.xlabel('t')
plt.ylabel('x3_2(t)')
plt.show()

y3_3= 2 * np.cos(2 * n * 3)  # for k=3
plt.stem(n, y3_3,use_line_collection=True)
plt.xlabel('t')
plt.ylabel('x3_3(t)')
plt.show()
