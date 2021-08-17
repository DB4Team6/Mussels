# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 10:57:50 2021
<3 80085  C=====3
@author: Nico1
"""

#input is t_max which is time since last feeding 
# and measured_Ca which is measured c of algea in cells/ml
def feed_amount(measured_Ca):

    #Questionable choices
    dt = 1/3; #time step in min
    N_m = 1; #How many mussels?
    t_max = 36 #Food every 12 min

    #Values from our data
    mu_m = 0.012/60; #Growth constant of Algae in mussel tank [min^-1]
    emu_m = 2.718**(mu_m*dt); #Another constant
    #Fm = 3*1000/60; #Feeding rate of a mussel in mL/min
    max_Cm = 7000; #Concentration in mussel tank cell/mL
    Vm = 2*1000; #Start volume in mussel tank [mL]

    #Initialize stuff
    Cm = [] #Simulated concentration in Mussel tank
    Cm.append(max_Cm)

    #Explicit Euler
    for t in range(int(t_max/dt)):
        Fm = (-0.00003163 * Cm[t]**2 + 0.5624*Cm[t] + 498.3370)/60#Feeding rate of a mussel in mL/min
        Cm.append(Cm[t]*(-Fm/Vm*dt*N_m+emu_m)) #Change in mussel tank
    Vr = Vm*(max_Cm-Cm[-1])/(measured_Ca-max_Cm) #Finding volume of bolus needed

    return Vr

