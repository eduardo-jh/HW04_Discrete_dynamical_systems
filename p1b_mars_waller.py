#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BE523 Biosystems Analysis & Design
HW4 - Problem 1b. Population on Mars

Created on Mon Feb 22 18:48:31 2021
@author: eduardo
"""
import numpy as np
import matplotlib.pyplot as plt

B0 = 0  # boys
G0 = 4  # girls
dt = 20  # time step, in years
Nt = 25  # steps

t = np.linspace(0, Nt*dt, Nt+1)
B = np.zeros(Nt+1)
G = np.zeros(Nt+1)
B[0], G[0] = B0, G0

birth_rate = 3.3
death_age = 60

for i in range(Nt):
    B[i+1] = B[i] + birth_rate*0.5*(G[i]/3) - dt/death_age*B[i]
    G[i+1] = G[i] + birth_rate*0.5*(G[i]/3) - dt/death_age*G[i]

plt.plot(t, B, 'b-', t, G, 'r-')
plt.legend(['Boys', 'Girls'], loc='best')
plt.xlabel('t')
plt.ylabel('Population')
# plt.savefig('p1b_mars_waller_%dsteps.png' % Nt, dpi=300, bbox_inches='tight')
plt.show()
