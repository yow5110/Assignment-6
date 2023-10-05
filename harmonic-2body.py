import matplotlib.pyplot as plt
import numpy as np
import myode  # this is the myode.py module we wrote in class, containing move_Euler() and move_RK2()

mass = 1    # mass of each particle, kg
k = 1       # spring constant connecting two particles, N/m
r_eq = 1.2   # equilibrium spring length, m

def diffeq(y):
    #we first unpack y
    x1, vx1, z1, vz1, x2, vx2, z2, vz2 = y  
    r12 = ?
    ax1 = ? #acceleration along x for particle 1
    az1 = ? #acceleration along z for particle 1
    ax2 = ? #acceleration along x for particle 2
    az2 = ? #acceleration along z for particle 2
    
    #finally we return the time derivative of every argument, in the same order
    ydot = np.array([vx1, ax1, vz1, az1, vx2, ax2, vz2, az2 ])
    return ydot

omega = np.sqrt(2*k/mass) #angular frequency of the oscillation
period = 2*np.pi/omega    #period of the oscillation
dt = ? #  dt chosen based on the timescale of the system, in seconds

t_total = 20*period #total simulation time
t_range = np.arange(0,t_total,dt)

#Initialize positions and velocities for two particles
x1 = -0.5
z1 = -0.5
x2 = 0.5
z2 = 0.5
vx1 = vx2 = vz1 = 0
vz2 = 0.1

y=[x1, vx1, z1, vz1, x2, vx2, z2, vz2] 
xr1=[]
zr1=[]
xr2=[]
zr2=[]

####### Solve ODE ########
for t in t_range:
    y= #choose your favorite ODE solver here and supply the arguments in the correct order
    xr1.append(y[?]) # this is x1
    zr1.append(y[?]) # this is z1
    xr2.append(y[?]) # this is x2
    zr2.append(y[?]) # this is z2

#### Make static plot of the two particles' trajectories #########
fig, ax = plt.subplots(1)
ax.plot(xr1, zr1, 'b.')
ax.plot(xr2, zr2, 'r.')

ax.set_ylabel('y position')
ax.set_xlabel('x position')
ax.set_aspect('equal', 'box')
plt.show() 
