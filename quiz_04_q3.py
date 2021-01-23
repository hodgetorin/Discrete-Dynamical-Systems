# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 13:50:17 2021

@author: Torin

BE423
Quiz 04 Question 3
Penicillin Pill
"""

import numpy as np
import matplotlib.pyplot as plt

# create an array of 21 time steps from 0 to 100:
t = np.linspace(0,100,21)

# create two arrays of length 21 for concentration in the intestine and plasma:
intestine = np.zeros(21)
plasma = np.zeros(21)

# initial concentration of penicillin in the intestine is 500 mg:
intestine[0] = 500

for i in range(1,21):
    # the concentration of penicillin in the intestine decreases by 10% 
    # of the concentration in the previous time step:
    intestine[i] = intestine[i-1] - intestine[i-1] * 0.1
    
    # the concentration of penicillin in the plasme increases by 10% 
    # of the intestine concentration in the previous time step and decreases
    # by 15% of the plasma concentration from the previous time step:
    plasma[i] = plasma[i-1] + intestine[i-1]*0.1 - plasma[i-1]*0.15
    
# plot concentration vs time for the plasma and the intestine
plt.plot(t,intestine,t,plasma)
plt.xlabel("Time (minutes)");plt.ylabel("Penicillin Concentration (mg)")
plt.legend(['Intestine', 'Plasma'], loc='upper right')