# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 16:12:03 2016

@author: yorick
"""
Fe_vals = [0, 0.5, -0.5, -99, -4, -2, -1]
Mg_vals = [0, 0.47, -0.55]
kperm = 8248.98310351
rho = 10^-19
def cool(T, nH):
    return (1e-2)*T*3./2*kperm*(10**nH)*1000*10 #conversion factors, yay cgs

def getrho(nH):
    return nH

for Fe in Fe_vals:
    for Mg in Mg_vals:
        for rs in range(0,12):
              for nH in range(-24,-16):
                fil = open("coolingtables/"+"RadLoss_"+str(Fe)+"_"+str(Mg)+"_"+str(rs)+"_"+str(10**nH)+".rates",'w')
                fil.write(str(getrho(10**nH))+'\n')
                fil.write("bla"+'\n')
                for T in range(10,20000,20):
                    fil.write(str(T)+'\t'+str(cool(T, nH))+'\n')
                    T*=1.2
                fil.close()
