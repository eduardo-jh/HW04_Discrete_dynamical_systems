#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BE523 Biosystems Analysis & Design
HW4 - Problem 4. Polymerase chain reaction

Created on Tue Jan 26 13:36:57 2021
@author: eduardo
"""
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm  # allows linear regression without intercept

P0 = 1e-12  # initial condition
r = 1  # rate of change
steps = 30  # cicles
dt = 1  # time interval
dP = np.zeros(steps)

t = np.linspace(0, (steps-1)*dt, steps)  # actual time vector

# Generate the growth data with model: P(t+1) = P[0]*(r+1)^t
P = P0 * (r + 1)**t

for i in range(1, steps):
    dP[i] = P[i] - P[i-1]  # difference between time steps
    
# Perform a linear regression with P and dP, then plot (dP vs P)
model = sm.OLS(dP, P)  # No intercept by default, force through the origin??
results = model.fit()
slope = results.params[0]  # growth rate
print("slope=", slope)  # should be close to 'r'

# Figure 1, plotting dP vs P
plt.figure(1)
plt.plot(P, dP, 'kx', P, slope*P, 'b-')
plt.legend(['data', 'linear regression $R^2$=%.2f' % results.rsquared], loc='best')
plt.xlabel('P')
plt.ylabel('dP')
plt.savefig('p4_polymerase_linear2.png', dpi=300, bbox_inches='tight')

# Generate an exponential equation (exact solution)
tdouble = np.log(2)/np.log(1+slope)*dt
print('tdouble =', tdouble)
K = np.log(2)/tdouble
Pexp = P[0] * np.exp(K*t/dt)

# Generate predictions with the model (numerical solution)
Pmodel = P[0]*(slope+1)**(t/dt)
print("The DNA amount after %d cicles is: %g" % (steps, Pmodel[-1]))

# Figure 2, plotting P (from data and model) vs t
plt.figure(2)
plt.plot(t, Pmodel, 'bo', t, Pexp, 'r-')
plt.legend(['numerical P=%g*(1+%.4f)^t' % (P[0], slope),
            'exact P=%g*exp(%.4f*t)' % (P[0], K)],
            loc='best')
plt.xlabel('Time (cicles)')
plt.ylabel('Amount of DNA')
plt.savefig('p4_polymerase_model2.png', dpi=300, bbox_inches='tight')