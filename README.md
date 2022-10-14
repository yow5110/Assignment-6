# Week 7 Assignment 

In this project we will simulate two particles connected by a spring, using an ODE solver of your choice to integrate the equation of motion. 

To calculate the force acting on each particle, we can start from the expression of the potential energy of the system

<a href="https://www.codecogs.com/eqnedit.php?latex=U^{el}=\frac{1}{2}k(r_{12}-r_{eq})^2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?U=\frac{1}{2}k(r_{12}-r_{eq})^2" title="U=\frac{1}{2}k(r_{12}-r_{eq})^2" /></a>

where 

<a href="https://www.codecogs.com/eqnedit.php?latex=r_{12}=|r_1-r_2|=\sqrt((x_1-x_2)^2+(z_1-z_2)^2)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?r_{12}=|r_1-r_2|=\sqrt((x_1-x_2)^2+(z_1-z_2)^2)" title="" /></a>

is the distance between the two particles, <a href="https://www.codecogs.com/eqnedit.php?latex=r_{eq}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?r_{eq}" title="r_{eq}" /></a> is the equilibrium position of the spring connecting particle 1 and 2, <a href="https://www.codecogs.com/eqnedit.php?latex=k" target="_blank"><img src="https://latex.codecogs.com/gif.latex?k" title="k" /></a> is the force constant of that spring.

The force acting on particle i can be evaluated from the partial derivative of the expression above with respect to the position of particle i, namely

<a href="https://www.codecogs.com/eqnedit.php?latex=f_{on\:&space;i}=-\frac{\partial&space;U}{\partial&space;r_i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f_{on\:&space;i}=-\frac{\partial&space;U}{\partial&space;r_i}" title="f_{on\: i}=-\frac{\partial U}{\partial r_i}" /></a>

TASKS: In the harmonic_motion.py program you will update all the functions to be able to work on the lists with the masses, coordinates, velocities, and forces of the two particles.

OPTIONAL TASK: Rewrite the program to exploit numpy arrays instead of lists.

EXPECTED OUTCOME: The results of the simulations should be easy to compare to the results of our previous programs on the motion of a single particle, although a small change of perspective may be needed.

