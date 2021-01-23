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


t = np.linspace(0,20,5)

# 1g injection:
c1 = [71,56,45,33,25]

# 5g injection:
c5 = [490,390,295,232,182]


plt.plot(t,c1,t,c5)
plt.xlabel("Time (minutes)");plt.ylabel("Mezlocillin concentration (mu.g/mL)")
plt.legend(['1g injection', '5g injection'], loc='upper right')