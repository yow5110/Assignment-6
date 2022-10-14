"""
Week 7 Assignment
"""
import matplotlib.pyplot as plt
import numpy as np
import ode  # this is the ode.py module we wrote in class, containing move_Euler() and move_RK2()

mass = 1    # mass of each particle, kg
k = 1       # spring constant connecting two particles, N/m
r_eq = 1.2   # equilibrium spring length, m

def f(y):
    #we first unpack y
    [x1, vx1, z1, vz1, x2, vx2, z2, vz2] = y  
    r12 = np.sqrt() # inter-particle distance
    ax1 = #acceleration along x for particle 1
    az1 = #acceleration along z for particle 1
    ax2 = #acceleration along x for particle 2
    az2 = #acceleration along z for particle 2
    
    #finally we return the time derivative of every argument, in the same order
    ydot = np.array([vx1, ax1, vz1, az1, vx2, ax2, vz2, az2 ])
    return ydot

omega = np.sqrt(2*k/mass)
period = 2*np.pi/omega
dt = 0.02*period #  dt chosen based on the timescale of the system, in seconds

t_total = int(30*period/dt) #total timesteps, unitless
t_range = range(t_total)

#initialize positions and velocities for two particles
x1 = -0.5
z1 = -0.5
x2 = 0.5
z2 = 0.5
vx1 = vx2 = vz1 = 0
vz2=0.1

y=[x1, vx1, z1, vz1, x2, vx2, z2, vz2] 
xr1=[]
zr1=[]
xr2=[]
zr2=[]

####### Solve ODE and make static plot #########
for t in t_range:
    y= #choose your favorite ODE solver here and supply the arguments in the correct order
    xr1.append(y[0]) # this is x1
    zr1.append(y[2]) # this is z1
    xr2.append(y[4]) # this is x2
    zr2.append(y[6]) # this is z2

fig, ax = plt.subplots(1)

ax.plot(xr1,zr1,'b.')
ax.plot(xr2,zr2,'r.')
ax.set_ylabel('y position')
ax.set_xlabel('x position')
ax.set_aspect('equal', 'box')
plt.show()
####### end of static plot section  ##########


####### solve ODE and generate animation #######

"""
import matplotlib.animation as ani
# Define the function that performs a single step of the animation
def animate(i):
    global y
    y = ode.move_RK2(f, y, dt)
    a.set_data([y[0],y[4]],[y[2],y[6]]) # we update the plot
    return a,

# The following command setup the visualization of plot, where the particle is represented by a green filled circle
fig, axes = plt.subplots(1)
axes.set_aspect('equal', 'box')

axes.set_xlim(-2, 2)
axes.set_ylim(-2, 10)
a,=axes.plot([],[],'bo') # We generate a plot with the starting configuration


# We perform the animation using the FuncAnimation function from the animation module of matplotlib. 
# This function requires as an argument the user-defined animate() function above
anim = ani.FuncAnimation(fig, animate, frames=t_total, interval=1, blit=True, repeat=True)

"""
####### End of animation section  #######







