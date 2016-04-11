# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 16:12:03 2016

@author: yorick
"""

def f(x1, x2, x3, x4, x5):
    return 10**(x1+x2+x3+x4+x5)

def g(x1, x2, x3):
    return x3

for i in range(0,10):
    for j in range(0,10):
        for k in range(0,10):
             for l in range(0,10):
                fil=open("coolingtables/"+"RadLoss_"+str(i)+"_"+str(j)+"_"+str(k)+"_"+str(g(i,j,l))+".rates",'w')
                fil.write(str(l)+'\n')
                fil.write("bla"+'\n')
                for m in range(0,10):
                    fil.write(str(m)+'\t'+str(f(i,j,k,l,m))+'\n')
                fil.close()
