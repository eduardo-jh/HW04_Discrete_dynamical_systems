#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BE523 Biosystems Analysis & Design
HW4 - Problem 1b. Weird things happening on Mars

NOTE: This code does not solve the problem in the way that is expected!!!
      Needs more work and a different approach.

Created on Tue Jan 26 01:23:20 2021
@author: eduardo
"""
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm  # allows linear regression without intercept

P0 = 10  # initial population
r = 1  # rate of change in population
steps = 50  # years in the future
dt = 5  # time interval
P0dis = 4 # population after the disaster

t = np.linspace(0, steps, int(steps/dt)+1)  # actual time vector
P = np.zeros(len(t))
Pdis = np.zeros(len(t))
dP = np.zeros(len(t))
dPdis = np.zeros(len(t))
P[0] = P0
Pdis[0] = P0

# Generate the population growth data
for i in range(1, len(t)):
    P[i] = P[i-1] + r
    Pdis[i] = Pdis[i-1] + r
    # A disaster in year 20, only 4 people alive
    if t[i] == 20:
        Pdis[i] = P0dis
    # Difference between time steps
    dP[i] = P[i] - P[i-1]
    dPdis[i] = Pdis[i] - Pdis[i-1]

# The 'normal' and 'disaster' population growth
print('t=', t, '\nP=', P, '\nPdis=', Pdis)

# Perform a linear regression with P and dP, then plot (dP vs P)
# WARNING: rate is constant (r=1), this does not make sense!!!
model = sm.OLS(dP, P)  # No intercept by default, force through the origin??
results = model.fit()
slope = results.params[0]  # rate of population growh
print("slope=", slope)  # should be close to 'r'

modeldis = sm.OLS(dPdis, Pdis)  # No intercept by default, force through the origin??
resultsdis = modeldis.fit()
slope_dis = resultsdis.params[0]  # rate of population growh
print("slope disaster=", slope_dis)  # should be close to 'r'

# # Figure 0, plotting P and Pdis vs t
# plt.figure(0)
# plt.plot(t, P, 'kx', t, Pdis, 'b-')
# plt.legend(['normal growth', 'disaster growth'], loc='best')
# plt.xlabel('Time (years)')
# plt.ylabel('Population')
# plt.savefig('p1b_mars_%dyears.png' % steps , dpi=300, bbox_inches='tight')

# Figure 1, plotting dP vs P
plt.figure(1)
plt.plot(P, dP, 'kx', P, slope*P, 'b-', Pdis, dPdis, 'b+', Pdis, slope_dis*Pdis, 'g--')
plt.legend(['normal growth',
            'lin. reg. normal $R^2$=%.3f' % results.rsquared,
            'disaster growth',
            'lin. reg, disaster $R^2$=%.3f' % resultsdis.rsquared],
            loc='best')
plt.xlabel('Population (P)')
plt.ylabel('Population change (dP)')
plt.savefig('p1b_mars_linear.png', dpi=300, bbox_inches='tight')

# Make predictions using the models
Pop = P[0]*(slope+1)**(t/dt)
Popdis = Pdis[0]*(slope_dis+1)**(t/dt)

# Generate an exponential equation (exact solution) for the normal growth
tdouble = (np.log(0.5)/np.log(1+slope))*dt
mu = np.log(0.5)/tdouble
Pexp = P[0] * np.exp(mu*t)

# ... and for the disaster population growth
tdouble_dis = (np.log(0.5)/np.log(1+slope_dis))*dt
mu_dis = np.log(0.5)/tdouble_dis
PDisexp = Pdis[0] * np.exp(mu_dis*t)
print('tdouble normal   =', tdouble, 'mu =', mu, 'b =', slope+1)
print('tdouble disaster =', tdouble_dis, 'mu dis =', mu_dis, 'b dis =', slope_dis+1)

plt.figure(2)
plt.plot(t, P, 'kx', t, Pdis, 'r.-', t, Pop, 'b-', t, Popdis, 'g--')
plt.legend(['population growth',
            'disaster',
            'pop P=%g$\cdot$(1+%.4f)$^t$' % (P[0], slope),
            'dis P=%g$\cdot$(1+%.4f)$^t$' % (P[0], slope_dis)],
            loc='best')
plt.xlabel('Time (years)')
plt.ylabel('Population')
plt.savefig('p1b_mars_%dyears_init.png' % steps, dpi=300, bbox_inches='tight')

# ********************** Population for 500 years ****************************

start = steps  # start with the initial condition calculated before
end = 500
dt = 20
females = 0.5
time = np.linspace(start, end, int((end-start)/dt)+1)  # actual time vector
Pop = np.zeros(len(time))
PopDis = np.zeros(len(time))
Pop[0], PopDis[0] = P[-1], Pdis[-1]  # The initial conditions are the last element

# Make 'predictions' using the analytical solution to the linear dynamical system,
# (also an exponential equation) in the form P(t) = P[0]*R^t with R>1
# we don't need to know the previous value, each calculation is only dependant of the time 't'
Pop500 = females*P[0]*(slope+1)**(time/dt)
Popdis500 = females*Pdis[0]*(slope_dis+1)**(time/dt)

# Predictions with exponential equation
Pop_exp500 = females*Pop[0] * np.exp(mu*time)
Ppopdis_exp500 = females*PopDis[0] * np.exp(mu_dis*time)

# Print out the results
print("At the end of the %d years, there will be %d people" % (end, Pop_exp500[-1]))
print("and with the disaster conditions the population will be: %d" % Ppopdis_exp500[-1])

# Plot the predictions of the population growth
plt.figure(3)
plt.plot(t, P, 'kx', t, Pdis, 'b+',
          time, Pop500, 'b-',
          time, Popdis500, 'g--',
          time, Pop_exp500, 'g^',
          time, Ppopdis_exp500, 'm*')
plt.legend(['population growth',
            'disaster',
            'pop P=%g$\cdot$(1+%.4f)$^t$' % (Pop[0], slope),
            'dis P=%g$\cdot$(1+%.4f)$^t$' % (PopDis[0], slope_dis),
            'exp growth',
            'exp disaster'],
            loc='best')
plt.xlabel('Time (years)')
plt.ylabel('Population')
plt.savefig('p1b_mars_%dyears_pop.png' % end, dpi=300, bbox_inches='tight')