#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BE523 Biosystems Analysis & Design
HW4 - Problem 1b. Weird things happening on Mars

Problem 1. Option b. The CEAC finally makes it to Mars and sends 10 people
there. The population grows at a rate of 1 person every five years. Use the
python "growth model" program to calculate and plot the population for 50
years. Now adjust the model for a disaster that occurs in year 20, in which
all but 4 people die. Unfortunately, only females are left so NASA sends sperm
to Mars to restart the population. NASA refuses to send any more people there
because of the tragedy. Soon however, it becomes apparent that males are
infertile on Mars. As the biosystems modeler, you must tell the community how
many children each female must have in order to grow the population to 500 by
the Martian year 500 (that is the slogan, 500 by 500). For example, you could
specify that each female between the ages of 15 and 20 must have three children
each. Remember that only one out of every two children is a female. You will
need to set up a loop with some complexities. Also, write a paragraph on any
bioethical issues that might arise and how the community should deal with them.
Mark true if you figure all of this out, and put your code, graphs, and
paragraph in the Assignment box or github repository.

Created on Mon Feb 22 18:48:31 2021
@author: eduardo
"""
import numpy as np
import matplotlib.pyplot as plt

B0 = 0  # boys
G0 = 4  # girls
dt = 20  # time step, in years
years = 500  # end year
steps = int(years/dt)

t = np.array(range(0, years+1, dt))
B = np.zeros(steps+1)
G = np.zeros(steps+1)
B[0], G[0] = B0, G0

# find the birth rate to reach 500 by 500
birth_rate = 3.3  # the initial value is 1 @ 5 years = 4 @ 20 years
death_age = 60  # death rate = time step/death age

for i in range(steps):
    # Increase the population of the previous time step by the birth rate,
    # which should be applied only to a third of girls (reproductive age is 1/3
    # of life span), subtract the death rate
    B[i+1] = B[i] + birth_rate*0.5*(G[i]/3) - dt/death_age*B[i]
    G[i+1] = G[i] + birth_rate*0.5*(G[i]/3) - dt/death_age*G[i]

plt.plot(t, B, 'b-', t, G, 'r-')
plt.legend(['Boys', 'Girls'], loc='best')
plt.xlabel('t')
plt.ylabel('Population')
# plt.savefig('p1b_mars_waller_%dsteps.png' % Nt, dpi=300, bbox_inches='tight')
plt.show()