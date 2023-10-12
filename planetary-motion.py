import matplotlib.pyplot as plt
import numpy as np
import myode #make sure myode.py is in the same directory

G = 
Msun = 
R1 = 147.1e9  # perihelion
R2 = 152.1e9  # aphelion

# Calculate zvel1 analytically and write down your steps 
zvel1 = 

def diffeq(y):
    [xpos, xvel, zpos, zvel] = y # first we unpack the vector y
    r = # magnitude of Earth-Sun distance
    xacc = 
    zacc = 
    ydot = np.array([xvel, xacc, zvel, zacc])
    return ydot


# Explain how you choose dt here
dt=
t_total = # task 4 (one year) and task 6 (two hundred years). Make sure it's in the right units
t_range = np.arange(0, t_total, dt)

# xpos xvel zpos zvel
y0 = [ , , , ] 
y = y0
x_sol = []
z_sol = []
EKin = []
EPot = []
Etot = []

for t in t_range:




#plotting section
fig, ax = plt.subplots(1)
ax.plot(0,0,'ro')
ax.text(0,0, 'Sun', horizontalalignment='left', verticalalignment='bottom', color='red')

ax.plot(-R1, 0,'k.')
ax.text(-R1, 0, 'Perihelion', horizontalalignment='left', verticalalignment='bottom')

ax.plot( R2, 0,'k.')
ax.text( R2, 0, 'Aphelion', horizontalalignment='right', verticalalignment='bottom')

ax.plot( ,  ,'b-') 

ax.set_ylabel('y position')
ax.set_xlabel('x position')
ax.set_aspect('equal', 'box')

plt.show()

