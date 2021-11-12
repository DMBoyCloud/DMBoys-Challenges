#!/usr/bin/env python

import operator

print("Basic python calculator")
print('***********************')

operator_simbol = {
    '*': operator.mul,
    '+': operator.add,
    '/': operator.truediv,
    '-': operator.sub
    }

number_1 = input('Enter your first number: ')
number_2 = input('Enter your second number: ')
operation = input('Enter the calculation symbol to perform: ')

operation = operator_simbol.get(operation)

if operation is not None:
    result = operation(float(number_1), float(number_2))
else:
    result = "Unknown operator"
print("result is: " + str(result))
