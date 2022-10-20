import matplotlib.pyplot as plt
import numpy as np
import ode #make sure you have your ode.py in the same directory

G = # task 2
Msun = # task 2
R1 = 147.1e9  # perihelion
R2 = 152.1e9  # aphelion

zvel1 = # task 1

def f(y):
    [xpos, xvel, zpos, zvel] = y # first we unpack the vector y
    r = # magnitude of Earth-Sun distance
    xacc = # task 2 & 5
    zacc = # task 2 & 5
    
    return np.array([xvel, xacc, zvel, zacc])


# set up time range and time step
dt= # task 2
t_total = # task 3 (one year) & 5 (two hundred years). Make sure it's in the right units
t_range = range( int(t_total/dt) )

# xpos xvel zpos zvel
y0 = [ , , , ] # task 2
y = y0
x_sol = []
z_sol = []
EKin = []
EPot = []
Etot = []

for t in t_range:
    # task 3. Choose your ODE solver to integrate the equation of motion
    # task 4. Define the energies that need to be plotted and calculate/store them here, to be plotted later.



#plotting section
fig, ax = plt.subplots(1)
ax.plot(0,0,'ro')
ax.text(0,0, 'Sun', horizontalalignment='left', verticalalignment='bottom', color='red')

ax.plot(-R1, 0,'k.')
ax.text(-R1, 0, 'Perihelion', horizontalalignment='left', verticalalignment='bottom')

ax.plot( R2, 0,'k.')
ax.text( R2, 0, 'Aphelion', horizontalalignment='right', verticalalignment='bottom')

ax.plot( ,  ,'b-') # task 3. Plot your results here

ax.set_ylabel('y position')
ax.set_xlabel('x position')
ax.set_aspect('equal', 'box')

plt.show()

#Extra credits: optional animation section
