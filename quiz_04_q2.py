# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 08:31:34 2021

@author: Torin

BE423
Quiz 04
Salt removal model
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

t_actual = np.linspace(0,20,5)



# 20 time steps:
t_cycle = np.linspace(0,19,20)

# 2 grams of salt = constant 
salt = 2
water = np.zeros(20)
C = np.zeros(20)

# initial water volume in mL:
water[0] = 1000

for i in range (1,20):
    water[i] =  water[i-1] - 50
    

#plt.plot(t_actual, Pe, 'bo', t_actual,P_actual, 'ro')
#plt.legend(['data','equation','exponential'], loc='upper right')