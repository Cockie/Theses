import scipy as sp
import scipy.optimize
import pylab as pl
import numpy as np
import h5py


def plot(ax, t, noisy_y, st):
    ax.plot(t, noisy_y, st)
    # ax.plot(t, calc, 'bo')
    ax.legend(bbox_to_anchor=(1.05, 1.1), fancybox=True, shadow=True)

def func(x,a,b,c):
    return b*np.exp(-a*x)+c

E = np.array([])
t = np.array([])
E2 = np.array([])
t2 = np.array([])
E3 = np.array([])
t3 = np.array([])
E4 = np.array([])
t4 = np.array([])
'''
for i in range(100):
    f = h5py.File("exp2/flatdensity3d{0:03d}.hdf5".format(i), "r")
    energy = np.array(f["/PartType0/InternalEnergy"])
    # coords = np.array(f["/PartType0/Coordinates"])

    average = np.average(energy)
    t = np.append(t, f["/Header"].attrs["Time"])
    E = np.append(E, average)


for i in range(100):
    f = h5py.File("3d_l/flatdensity3d{0:03d}.hdf5".format(i), "r")
    energy = np.array(f["/PartType0/InternalEnergy"])
    # coords = np.array(f["/PartType0/Coordinates"])

    average = np.average(energy)
    t = np.append(t, f["/Header"].attrs["Time"])
    E = np.append(E, average)
'''
for i in range(101):
    f = h5py.File("test_gy/snapshot_{0:04d}.hdf5".format(i), "r")
    energy2 = np.array(f["/PartType0/InternalEnergy"])
    # coords = np.array(f["/PartType0/Coordinates"])

    average2 = np.average(energy2)
    t2 = np.append(t2, f["/Header"].attrs["Time"])
    E2 = np.append(E2, average2)

for i in range(100):
    f = h5py.File("3d/flatdensity3d{0:03d}.hdf5".format(i), "r")
    energy = np.array(f["/PartType0/InternalEnergy"])
    # coords = np.array(f["/PartType0/Coordinates"])

    average = np.average(energy)
    t = np.append(t, f["/Header"].attrs["Time"])
    E = np.append(E, average)
'''
for i in range(17):
    f = h5py.File("3d_bs_big/flatdensity3d{0:03d}.hdf5".format(i), "r")
    energy3 = np.array(f["/PartType0/InternalEnergy"])
    # coords = np.array(f["/PartType0/Coordinates"])

    average3 = np.average(energy3)
    t3 = np.append(t3, f["/Header"].attrs["Time"])
    E3 = np.append(E3, average3)
for i in range(17):
    f = h5py.File("3d_bs_big2/flatdensity3d{0:03d}.hdf5".format(i), "r")
    energy4 = np.array(f["/PartType0/InternalEnergy"])
    # coords = np.array(f["/PartType0/Coordinates"])

    average4 = np.average(energy4)
    t4 = np.append(t4, f["/Header"].attrs["Time"])
    E4 = np.append(E4, average4)
'''
# print(t)
# print(E)
# pl.plot(t, E, "r-")
'''
popt, pcov = scipy.optimize.curve_fit(func, t, E, p0=[0.01,E[0]/2,E[0]/2])
fit = [func(ti, popt[0], popt[1],popt[2]) for ti in t]
print(popt)
ideal = [func(ti, 0.01, E[0]/2, E[0]/2) for ti in t]'''
fig = pl.figure()
ax1 = fig.add_subplot(1, 1, 1)
'''
# Non-linear Fit
plot(ax1, t, E, 'ro')
plot(ax1, t, fit, 'b-')
plot(ax1, t, ideal, 'g-')
'''
plot(ax1, t, E, 'ro')
plot(ax1, t2, E2*(1e20), 'bo')
'''plot(ax1, t3, E3, 'ro')
plot(ax1, t4, E4, 'go')
'''
ax1.set_title('Non-linear Fit')

pl.show()