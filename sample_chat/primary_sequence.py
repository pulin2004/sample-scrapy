# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: pulin

import matplotlib.pyplot as plt
from matplotlib.patches import Circle
fig = plt.figure()
ax = fig.add_subplot(111)
cir1= Circle(xy=(0.0,0.0),radius=0.38,alpha=0.2,color="b")
cir2= Circle(xy=(1.0,1.0),radius=0.38,alpha=0.2,color="b")
ax.add_patch(cir1)
ax.add_patch(cir2)
x=[0,1]
y=[1,0]
ax.plot(x,y,"g-.")
plt.xlabel('Instability(I)')
plt.ylabel('Abstractness(A)')
plt.ylim(0, 1)
plt.xlim(0, 1)
plt.title('Main Sequence')

plt.plot(0.85,0.33,"r",marker="o",ms=10)
plt.plot(0.5,0.14,"r",marker="o",ms=10)
plt.plot(1,0,"r",marker="o",ms=10)
plt.show()