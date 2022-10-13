# Week 8 Assignment A

In this project we will add features to the program that simulates the one-dimensional motion of multiple particle connected by springs, using the Velocity Verlet method to integrate the equation of motion. This assignment will consider a system of two particles connected by a single spring.

The problem to solve is a system of coupled second order differential equations in position and time. For the one-dimensional motion of each particle we have

<a href="https://www.codecogs.com/eqnedit.php?latex=\left\{\begin{matrix}&space;m_1\frac{d^2x_1}{dt^2}=&f_{on\:1}(x_1(t),x_2(t))&space;\\&space;m_2\frac{d^2x_2}{dt^2}=&f_{on\:2}(x_1(t),x_2(t))&space;\end{matrix}\right." target="_blank"><img src="https://latex.codecogs.com/gif.latex?\left\{\begin{matrix}&space;m_1\frac{d^2x_1}{dt^2}=&f_{on\:1}(x_1(t),x_2(t))&space;\\&space;m_2\frac{d^2x_2}{dt^2}=&f_{on\:2}(x_1(t),x_2(t))&space;\end{matrix}\right." title="\left\{\begin{matrix} m_1\frac{d^2x_1}{dt^2}=&f_{on\:1}(x_1(t),x_2(t)) \\ m_2\frac{d^2x_2}{dt^2}=&f_{on\:2}(x_1(t),x_2(t)) \end{matrix}\right." /></a>

In order to use the velocity Verlet algorithm, we need to be able to compute the force acting on each particle. For the considered system, the expression of the potential energy is just the one for the spring

<a href="https://www.codecogs.com/eqnedit.php?latex=U^{el}=\frac{1}{2}k(x_{12}-x_{eq})^2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?U^{el}=\frac{1}{2}k(x_{12}-x_{eq})^2" title="U^{el}=\frac{1}{2}k(x_{12}-x_{eq})^2" /></a>

where 

<a href="https://www.codecogs.com/eqnedit.php?latex=x_{12}=\|x_1-x_2\|" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x_{12}=\|x_1-x_2\|" title="x_{12}=\|x_1-x_2\|" /></a>

is the distance between the two particles, <a href="https://www.codecogs.com/eqnedit.php?latex=x_{eq}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x_{eq}" title="x_{eq}" /></a> is the equilibrium position of the spring connecting particle 1 and 2, <a href="https://www.codecogs.com/eqnedit.php?latex=k" target="_blank"><img src="https://latex.codecogs.com/gif.latex?k" title="k" /></a> is the force constant of that spring.

The force acting on particle i can be evaluated from the partial derivative of the expression above with respect to the position of particle i, namely

<a href="https://www.codecogs.com/eqnedit.php?latex=f_{on\:&space;i}=-\frac{\partial&space;U}{\partial&space;x_i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f_{on\:&space;i}=-\frac{\partial&space;U}{\partial&space;x_i}" title="f_{on\: i}=-\frac{\partial U}{\partial x_i}" /></a>

In this assignment we will rewrite the code developed in the previous weeks to model the motion of the two particles.

TASKS: In the harmonic_motion.py program you will update all the functions to be able to work on the lists with the masses, coordinates, velocities, and forces of the two particles.

OPTIONAL TASK: Rewrite the program to exploit numpy arrays instead of lists.

EXPECTED OUTCOME: The results of the simulations should be easy to compare to the results of our previous programs on the motion of a single particle, although a small change of perspective may be needed.

