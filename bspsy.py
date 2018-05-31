#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 01:00:48 2017

@author: suvendubrk
"""

import numpy as np
import matplotlib.pyplot as plt

a = 100
k = 10
m = 0.01
x0 = 10
y0 = 10

X = []
Y = []

X.append(x0)
Y.append(y0)


dt = 0.1
t_max = 1




def ln(n,x,y):

  blah = 0

  if (n=="1"):
      blah = np.sqrt((1+2*x/a)**2+(1-2*y/a)**2);
  elif (n=="2"):
      blah = np.sqrt((1-2*x/a)**2+(1-2*y/a)**2);
  elif (n=="3"):
      blah = np.sqrt((1-2*x/a)**2+(1+2*y/a)**2);
  elif (n=="4"):
      blah = np.sqrt((1+2*x/a)**2+(1+2*y/a)**2);
  else:
      blah = "err";
        
  return blah;


def x_updater(x,y):

   #b1 = (k*a/2**0.5)*( (4*2**0.5 - 1/ln("1",x,y) - 1/ln("2",x,y) - 1/ln("3",x,y) - 1/ln("4",x,y)) 
   #     + (2*x/a)*( -1/ln("1",x,y) + 1/ln("2",x,y) + 1/ln("3",x,y) - 1/ln("4",x,y)))
   
   b1 = -(k*a/m)*((1 - (1/(8**0.5))*(1/ln("3",x,y) + 1/ln("4",x,y)))*(1+2*y/a) - 
        (1 - (1/(8**0.5))*(1/ln("2",x,y) + 1/ln("1",x,y)))*(1-2*y/a))
            
   return b1


def y_updater(x,y):

   #b1 = (k*a/2**0.5)*( (4*2**0.5 - 1/ln("1",x,y) - 1/ln("2",x,y) - 1/ln("3",x,y) - 1/ln("4",x,y)) 
   #     + (2*x/a)*( -1/ln("3",x,y) + 1/ln("2",x,y) + 1/ln("1",x,y) - 1/ln("4",x,y)))
   #b1 = -1*k*y/m          
   
   b1 = -(k*a/m)*((1 - (1/(8**0.5))*(1/ln("1",x,y) + 1/ln("4",x,y)))*(1+2*x/a) - 
        (1 - (1/(8**0.5))*(1/ln("2",x,y) + 1/ln("3",x,y)))*(1-2*x/a))
   
   return b1


def calculate():

  x = 0
  y = 0

  for i in range(0,int(t_max/dt)):
  
    if(i==0):
    
      x = 2*X[i] + x_updater(X[i],Y[i])*dt**2
      y = 2*Y[i] + y_updater(X[i],Y[i])*dt**2
             
    else:
    
      x = 2*X[i] - X[i-1] + x_updater(X[i],Y[i])*dt**2
      y = 2*Y[i] - Y[i-1] + y_updater(X[i],Y[i])*dt**2
    

    X.append(x)
    Y.append(y)


calculate()

print(X,Y)

plt.plot(np.arange(0,t_max+dt,dt),X)
