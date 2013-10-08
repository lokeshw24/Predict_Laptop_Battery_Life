#!/bin/python

#constants
x_values=[]
y_values=[]
alpha=0.05
total_input_pairs=0
partial_derivatives=[0, 0]
flag=1

#Functions

def get_input_data():
	global x_values, y_values, total_input_pairs;

	lines = [line.strip() for line in open('input_data.txt')]

	for line in lines:
		temp=line.split(',')
		x_values.append(temp[0])
		y_values.append(temp[1])
	
	x_values = [ float(i) for i in x_values ]
	y_values = [ float(i) for i in y_values ]

	total_input_pairs=len(x_values)

	print x_values, y_values, total_input_pairs

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

	fault_tolerance=0.01

	if ( -fault_tolerance<slope0<fault_tolerance and -fault_tolerance<slope1<fault_tolerance ) :
		flag=0;
	partial_derivatives[0] = (sum0/total_input_pairs);
	partial_derivatives[1] = (sum1/total_input_pairs);

	print partial_derivatives[0], partial_derivatives[1]


def main():
	global x_values, y_values, alpha, flag;

	get_input_data();

	guess_theta0=x_values[0];
	guess_theta1=y_values[0];
	
	print guess_theta0, guess_theta1
	while(flag):
		get_partial_derivatives(guess_theta0, guess_theta1)
		guess_theta0 = guess_theta0 - alpha*partial_derivatives[0];
		guess_theta1 = guess_theta1 - alpha*partial_derivatives[1];
	
	print "Equation of Linear Regression is : y=",guess_theta0, "+", guess_theta1,"*(x)" ;

	print "----------- Testing the accuracy --------"
	for i in range(0, total_input_pairs) : 
		print ( y_values[i] - ( guess_theta0 + guess_theta1*(x_values[i] ) ))

main()
