import scipy as sp
import scipy.optimize
import pylab as pl
import numpy as np
import h5py

t = np.array([])
E = []
readnext = False
with open("flatdensity3d.log") as f:
    for line in f:
        if line.startswith("T="):
            if readnext:
                E.append(float(line.strip("T=")))
                readnext=False
        elif line.startswith("Saving"):
            readnext=True
del E[len(E)-1]
E=np.array(E)
for i in range(100):
    f = h5py.File("exp2/flatdensity3d{0:03d}.hdf5".format(i), "r")
    t = np.append(t, f["/Header"].attrs["Time"])
print(t)
print(E)

def plot(ax, t, noisy_y, st):
    ax.plot(t, noisy_y, st)
    # ax.plot(t, calc, 'bo')
    ax.legend(bbox_to_anchor=(1.05, 1.1), fancybox=True, shadow=True)


def func(x, a, b):
    return b * np.exp(-a * x)

popt, pcov = scipy.optimize.curve_fit(func, t, E, p0=[0.01,E[0]])
print(popt)
fit = [func(ti, popt[0], popt[1]) for ti in t]
ideal = [func(ti, 0.01, E[0]) for ti in t]
fig = pl.figure()
ax1 = fig.add_subplot(1, 1, 1)

# Non-linear Fit
plot(ax1, t, E, 'ro')
plot(ax1, t, fit, 'b-')
plot(ax1, t, ideal, 'g-')


ax1.set_title('Non-linear Fit')

pl.show()