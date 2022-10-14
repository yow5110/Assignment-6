# Week 7 Assignment 

In this project we will simulate two particles connected by a spring, using an ODE solver of your choice to integrate the equation of motion. 

To calculate the force acting on each particle, we can start from the expression of the potential energy of the system

<a href="https://www.codecogs.com/eqnedit.php?latex=U^{el}=\frac{1}{2}k(r_{12}-r_{eq})^2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?U=\frac{1}{2}k(r_{12}-r_{eq})^2" title="U=\frac{1}{2}k(r_{12}-r_{eq})^2" /></a>

where 

<a href="https://www.codecogs.com/eqnedit.php?latex=r_{12}=|r_1-r_2|=((x_1-x_2)^2+(z_1-z_2)^2)^\frac{1}{2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?r_{12}=|r_1-r_2|=((x_1-x_2)^2+(z_1-z_2)^2)^\frac{1}{2}" title="" /></a>

is the distance between the two particles, <a href="https://www.codecogs.com/eqnedit.php?latex=r_{eq}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?r_{eq}" title="r_{eq}" /></a> is the equilibrium position of the spring connecting particle 1 and 2, <a href="https://www.codecogs.com/eqnedit.php?latex=k" target="_blank"><img src="https://latex.codecogs.com/gif.latex?k" title="k" /></a> is the force constant of that spring.

The force acting on particle i can be evaluated from the partial derivative of the expression above with respect to the position of particle i, namely

<a href="https://www.codecogs.com/eqnedit.php?latex=f_{on\:&space;i}=-\frac{\partial&space;U}{\partial&space;r_i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f_{on\:&space;i,x}=-\frac{\partial&space;U}{\partial&space;x_i}" title="f_{on\: i,x}=-\frac{\partial U}{\partial x_i}" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=f_{on\:&space;i}=-\frac{\partial&space;U}{\partial&space;r_i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f_{on\:&space;i,z}=-\frac{\partial&space;U}{\partial&space;z_i}" title="f_{on\: i,z}=-\frac{\partial U}{\partial z_i}" /></a>

TASK 1: In the harmonic_motion.py program you will update two sections: the f() function block, where you'll work on calculating the forces on the two particles, and the two lines with the comment "choose your favorite ODE solver here", where you choose between Euler and RK2. Generate the trajectories of the two particles. An example output using a the Runge-Kutta 2nd order solver is attached in "example trajectory.png".

TASK 2: Comment out the entire "ODE solving and plotting" section, and uncomment the second "ODE solving and animation" section to activate it. You should see an animation of the simulation. And example output is given in "example animation.gif". Describe how the particles's motion can be considered a superposition of multiple types of simple motions. Did you expect this before the simulation by just looking at the initial conditions? 




