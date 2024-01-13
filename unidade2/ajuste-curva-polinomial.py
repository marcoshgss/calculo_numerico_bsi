from __future__ import  division
import numpy as np
from numpy import linalg
import matplotlib.pyplot as plt

P = [[3,1], [2.4,4], [8,3], [1.4,2], [1,4], [3,5]]

N = 6

xj2 = 0.0
yj = 0.0
xj = 0.0
xjyj = 0.0


for j in range(0,N-1):
  xj2 = P[j][0] **2 + xj2
  yj = P[j][1] + yj
  xj = P[j][0] + xj
  xjyj = P[j][0]*P[j][1] + xjyj


den = ((N*xj2)-xj**2)
a1 = (xj2*yj -xj*xjyj)/den
a2 = (N*xjyj - xj*yj)/den

def f(x): return a1+a2*x

xx = np.linspace(0,8)
plt.plot(xx, f(xx), 'r--')
plt.plot([3.1, 5,2],[4,3,1], 'bs')
plt.plot([3.8, 1,7],[1,8,3], 'bs')
plt.grid(); plt.show()
