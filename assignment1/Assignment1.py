#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 18:44:11 2019

Numpy Assignment#1

@author: soyeb84

"""

"""
Question 1 :
Create 1 dimensional array containing number 0 to 23 and
    - print first 10 elements
    - print last 10 elements
"""

import numpy
from functools import reduce

first_array = numpy.arange(24)

print(first_array)

first_10_elements = first_array[:10] 

print("First 10 elements " + str(first_10_elements))

last_10_elements = first_array[10:]

print("First 10 elements " + str(last_10_elements))

"""
Question 2:

Convert the first array to size 6X4
  - print elements of second column
  - print elements of third row
  - print largest integer in each row
  - print largest integer in each column
  - find common elements if any between the rows of two matrices
    
"""

mult_dim_array = first_array.reshape(6,4)

print("2D array from the first 1D array \n" + str(mult_dim_array))

print("\nElements of second column " + str(mult_dim_array[:6,1]))

print("\nElements of third row " + str(mult_dim_array[2,:4]))

print(numpy.amax(mult_dim_array,1)
