###############################################################################
 # This file is part of SWIFT.
 # Copyright (c) 2015 Bert Vandenbroucke (bert.vandenbroucke@ugent.be)
 #
 # This program is free software: you can redistribute it and/or modify
 # it under the terms of the GNU Lesser General Public License as published
 # by the Free Software Foundation, either version 3 of the License, or
 # (at your option) any later version.
 #
 # This program is distributed in the hope that it will be useful,
 # but WITHOUT ANY WARRANTY; without even the implied warranty of
 # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 # GNU General Public License for more details.
 #
 # You should have received a copy of the GNU Lesser General Public License
 # along with this program.  If not, see <http://www.gnu.org/licenses/>.
 #
 ##############################################################################

import h5py
import numpy as np
import pylab as pl

# This script sets up a square overdensity in equilibrium with a low density
# region. The entire flow gets a random velocity. This tests the Lorentz-
# invariance of the code.

# number of cartesian cells in one dimension
ncell = 20
# total number of cells
npart = ncell**3
# density in the low density and high density region
rhoIC = 1e1
# pressure in the entire region
pIC = 1e-11
# side of the overdense square
rsquare = 0.5
# velocity of the entire fluid
vIC = [0, 0, 0]
# box size
boxL = 1e11

# data arrays
coords = np.zeros((npart, 3))
v      = np.zeros((npart, 3))
m      = np.zeros((npart, 1))
rho    = np.zeros((npart, 1))
h      = np.zeros((npart, 1))
u      = np.zeros((npart, 1))
ids    = np.zeros((npart, 1), dtype='L')

# spacing between cells
dx = boxL/ncell

lims = [0.5*(boxL-rsquare), 0.5*(boxL-rsquare)+rsquare]
# fill data arrays
test=True
idx = 0
for i in range(ncell):
  for j in range(ncell):
    for k in range(ncell):
      coords[idx,0] = (i+0.5)*dx
      coords[idx,1] = (j+0.5)*dx
      coords[idx,2] = (k+0.5)*dx
      v[idx,0] = vIC[0]
      v[idx,1] = vIC[1]
      v[idx,2] = vIC[2]
      # value is ignored by GIZMO_HYDRO
      m[idx] = rhoIC*(dx**3)
      if test:
          print(m[idx])
          test=False
      rho[idx] = rhoIC
      # convert pressure to internal energy
      #  u = P/(gamma-1)/rho
      u[idx] = 1.5*pIC/rho[idx]
      # correct value is obtained during first loop
      h[idx] = 1.12/ncell # should be almost correct
      ids[idx] = idx
      idx += 1

#File
file = h5py.File("SquareTest.hdf5", 'w')

# Header
grp = file.create_group("/Header")
grp.attrs["BoxSize"] = boxL
grp.attrs["NumPart_Total"] =  [npart, 0, 0, 0, 0, 0]
grp.attrs["NumPart_Total_HighWord"] = [0, 0, 0, 0, 0, 0]
grp.attrs["NumPart_ThisFile"] = [npart, 0, 0, 0, 0, 0]
grp.attrs["Time"] = 0.0
grp.attrs["NumFilesPerSnapshot"] = 1
grp.attrs["MassTable"] = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
grp.attrs["Flag_Entropy_ICs"] = [False, False, False, False, False, False]

#Runtime parameters
grp = file.create_group("/RuntimePars")
grp.attrs["PeriodicBoundariesOn"] = 1

#Particle group
grp = file.create_group("/PartType0")
ds = grp.create_dataset('Coordinates', (npart, 3), 'd')
ds[()] = coords
ds = grp.create_dataset('Velocities', (npart, 3), 'f')
ds[()] = v
ds = grp.create_dataset('Masses', (npart,1), 'd')
ds[()] = m
ds = grp.create_dataset('Density', (npart,1), 'f')
ds[()] = rho
ds = grp.create_dataset('SmoothingLength', (npart,1), 'f')
ds[()] = h
ds = grp.create_dataset('InternalEnergy', (npart,1), 'f')
ds[()] = u
ds = grp.create_dataset('ParticleIDs', (npart, 1), 'L')
ds[()] = ids

file.close()