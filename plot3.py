# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 14:59:11 2016

@author: bk
"""

import scipy as sp
import scipy.optimize
import scipy.interpolate
import pylab as pl
import numpy as np
import h5py

x= [0.5, 0.25, 0.166667, 0.125, 0.1, 0.0833333, 0.0714286, 0.0625, 0.0555556, 0.05, 0.0454545, 0.0416667, 0.0384615, 0.0357143, 0.0333333, 0.03125]
values= [-330.994, -531.592, -611.968, -648.956, -667.439, -678.152, -684.957, -689.965, -693.538, -696.112, -698.039, -699.288, -700.267, -701.103, -701.856, -702.502]
x2 = [i/1000. for i in range(500)]


def plot(ax, t, noisy_y, st):
    ax.plot(t, noisy_y, st)
    # ax.plot(t, calc, 'bo')
    ax.legend(bbox_to_anchor=(1.05, 1.1), fancybox=True, shadow=True)


calcvec = []
for i in range(len(values)):
    calcvec.append([])
    for j in range(len(values)+2):
        calcvec[i].append(0)


def x_(j):
    #print(1. / (2*(j+1)))
    return 1. / (2*(j+1))


def fit(xi):
    for j in range(len(values)):
        #print(j)
        calcvec[j][1] = values[j]
        for k in range(2, j + 3):
            try:
                calcvec[j][k] = calcvec[j][k - 1] + (calcvec[j][k - 1] - calcvec[j - 1][k - 1]) / (
                (xi - x[j - k+1]) / (xi - x[j]) * (
                1 - (calcvec[j][k - 1] - calcvec[j - 1][k - 1]) / (calcvec[j][k - 1] - calcvec[j - 1][k - 2])) - 1)
            except Exception:
                calcvec[j][k] = calcvec[j][k - 1]
    for i in range(len(values)):
        st=""
        for j in range(len(values)+2):
            st+=str(calcvec[i][j])+" "
        #print(st)
    return calcvec[len(values)-1][len(values) + 1]


#fit = scipy.interpolate.lagrange(x,values)
y2 = [fit(stuff) for stuff in x2]
print(fit(0))
#fit(0.5)
# print(t)
# print(E)
# pl.plot(t, E, "r-")


fig = pl.figure()
ax1 = fig.add_subplot(1, 1, 1)

# Non-linear Fit
plot(ax1, x, values, 'ro')
plot(ax1, x2, y2, 'b-')
ax1.set_title('Non-linear Fit')

pl.show()