#!/bin/python

import math

#constants
x_values=[2.81, 7.14, 2.72, 3.87, 1.90, 7.82 ]
y_values=[5.62, 8.00, 5.44, 7.44, 3.80, 8.00 ]
alpha=0.05
total_input_pairs=6
partial_derivatives=[0, 0]
flag=1

def get_partial_derivatives( guess_theta0, guess_theta1 ):
	global x_values, y_values, alpha, total_input_pairs, flag;

	sum0=0;
	sum1=0;

	for i in range(0, total_input_pairs) :
		h=( guess_theta0 + guess_theta1*x_values[i] ) - y_values[i]
		sum0=sum0 + h;
		sum1=sum1 + h*x_values[i]

	slope0 = ( sum0/total_input_pairs );
	slope1 = ( sum1/total_input_pairs );
	if ( -0.1<slope0<0.1 and -0.1<slope1<0.1 ) :
		flag=0;
	partial_derivatives[0] = (sum0/total_input_pairs);
	partial_derivatives[1] = (sum1/total_input_pairs);

	print partial_derivatives[0], partial_derivatives[1]


def main():
	global x_values, y_values, alpha, flag;

	guess_theta0=x_values[0];
	guess_theta1=y_values[0];
	
	print guess_theta0, guess_theta1
	while(flag):
		get_partial_derivatives(guess_theta0, guess_theta1)
		guess_theta0 = guess_theta0 - alpha*partial_derivatives[0];
		guess_theta1 = guess_theta1 - alpha*partial_derivatives[1];
	
	print "Equation of Linear Regression is : y=",guess_theta0, "+", guess_theta1,"*(x)" ;
main()
