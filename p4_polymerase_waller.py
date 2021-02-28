#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BE523 Biosystems Analysis & Design
HW4 - Problem 4. Polymerase chain reaction
Professor Waller solution

Created on Mon Feb 22 20:53:14 2021
@author: eduardo
"""
import numpy as np
import matplotlib.pyplot as plt

B_0 = 1e-12
dt = 1
N_t = 25

t = np.linspace(0, (N_t+1)*dt, N_t+2)
B = np.zeros(N_t+2)

B[0] = B_0
for n in range(N_t+1):
    B[n+1] = B[n] + (1)*B[n]

plt.plot(t, B, 'bo', t, B_0*pow(2, t/dt), 'r-')
plt.legend(['numerical', 'exact'],loc='best')
plt.xlabel('Time (cicles)')
plt.ylabel('Amount of DNA')