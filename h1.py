import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style
start = -3
end = 3
step = 0.001
x1 = np.linspace(start, end, int((end-start) / step))
y1 = np.exp(-3*x1)
plt.plot(x1, y1, color='red')
plt.xlabel('t')
plt.ylabel('x1(t)')
plt.show()


y2 = y1*np.heaviside(x1,1)
plt.plot(x1,y2 , color='green')
plt.xlabel('t')
plt.ylabel('x2(t)')
plt.show()

y3 =y2+2*np.sin(x1+2)
plt.plot(x1,y3,color='blue')
plt.xlabel('t')
plt.ylabel('x3(t)')
plt.show()

y4 = np.where(x1 > 1,np.exp(-x1)*(np.sin(x1)+np.cos(x1)*np.heaviside(x1,1)), (np.where(x1 < -1, 0, 1)))
plt.plot(x1,y4,color ='orange')
plt.xlabel('t')
plt.ylabel('x4(t)')
plt.show()


