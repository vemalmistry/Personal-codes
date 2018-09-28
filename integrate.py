import math

def func(x):
	f = math.exp(-x**2)       #Let f be the function of x
	return f

# Upper and lower integration limits
cut_off = 1
#Integral from 0 to infinity with random cut_off point

# Number of steps
steps = 1000000
integral = 0

x = 0.5/steps
while (x < cut_off):
	area = func(x)/steps
	integral = integral + area
	x = x + 1/steps
	
y = 0.5/steps
while (y < cut_off**-1):
	area = (func(y**-1)*y**-2)/steps
	integral = integral + area
	y = y + 1/steps
	
print((2*integral)**2)