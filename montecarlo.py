import math, random

#Function to integrate
def func(x):
	f = math.cos(x) 
	return f

#Random number generator within the limits	
def rand(x1, x2):
	return x1 + random.random()*(x2-x1)

#Limits of the integration	
xmin = 0 
xmax = math.pi
ymin = -1
ymax = 1

#Number of points for simulation. Use a larger number for more accuracy
points = 1000000
inside_points = 0

#Random co-ordinates are chosen from random numbers. 
#Counter increases if points lies within the function.
for n in range(0, points):
	x = rand(xmin, xmax)
	y = rand(ymin, ymax)
	if (y < func(x)):
		inside_points = inside_points + 1
		
integral = inside_points/points*(xmax-xmin)*(ymax-ymin)
print(integral)