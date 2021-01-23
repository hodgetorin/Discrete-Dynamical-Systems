# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 08:31:34 2021

@author: Torin

BE423
Quiz 04 Question 2
Salt removal model
"""

import numpy as np
import matplotlib.pyplot as plt

# volume of solution is constant 1000mL
vol = 1000

c = np.zeros(101) 
salt = np.zeros(101)

salt[0] = 2
c[0] = salt[0]/vol

# mass of salt (g) in each time step =
# salt(n-1)(g) - concentration (n-1)(g/ml) * 50 (ml)

for i in range(1,100):
    salt[i] = salt[i-1] - c[i-1]*50   
    c[i] = salt[i]/vol

# 100 time steps:
t_cycle = np.linspace(0,100,101)

# mass of salt in solution after 20 steps:
# salt[20] = approx. 0.717 g
print(salt[20]) 

# plot with markers at every 20 time steps:
plt.plot(t_cycle,salt,'-rD', markevery = 20)
plt.xlabel("time step, n"); plt.ylabel("salt in solution (g)")
