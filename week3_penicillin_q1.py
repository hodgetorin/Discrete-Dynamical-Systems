# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 08:31:34 2021

@author: Torin
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


dP = np.zeros(5)
dP[0] = 200
Pe = np.zeros(5)
t_actual = np.linspace(0,20,5)
P_actual = [200,152,118,93,74]

# for i in range(1,6):
#    dP[i] = dP[i-1]

#plt.plot(t_actual,P_actual)
plt.xlabel('time, minutes'); plt.ylabel('P, concentration')
slope, intercept, r_value,p_value,std_err = stats.linregress(t_actual, P_actual)

#tdouble = np.log(2)/np.log(1+slope)*dt
#print('tdouble = ', tdouble)
#K = np.log(2)/tdouble

Pe[0] = P_actual[0]
for i in range(0,5):
    Pe[i] = P_actual[0] * np.exp(-.05 * t_actual[i])
    
plt.plot(t_actual, Pe, 'bo', t_actual,P_actual, 'ro')
plt.legend(['data','equation','exponential'], loc='upper right')