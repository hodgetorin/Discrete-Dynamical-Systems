# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 15:30:02 2021

@author: Torin

BE 423 1/24/2021
Quiz 05 Question 4

"""

import numpy as np
import matplotlib.pyplot as plt

# empty arrays of length 100 for plotting time and dna mass
dna = np.zeros(100)
t = np.linspace(0,100,101)

# initial mass of dna = 1 picogram
dna[0] = 0.000000000001

# dna mass doubles every time step
for i in range(1, 101):
    dna[i] = dna[i-1]*2

# plot and print results:
plt.plot(t,dna)
plt.ylabel("DNA (picograms)")
plt.xlabel("time step")

print("grams of DNA at cycle 30:", dna[30])