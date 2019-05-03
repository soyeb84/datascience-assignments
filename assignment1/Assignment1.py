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

print("Flattened array " + str(first_array))

first_10_elements = first_array[:10] 

print("First 10 elements " + str(first_10_elements))

last_10_elements = first_array[10:]

print("last 10 elements " + str(last_10_elements))

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

print("\nMax elements by row " + str(numpy.amax(mult_dim_array,1)))

print("\nMax elements by column " + str(numpy.amax(mult_dim_array,0)))

matrix_1 = numpy.array([[1,0,2],[2,3,4],[4,0,5]])
matrix_2 = numpy.array([[1,0,4],[5,6,4],[5,7,4]])

print("\nCommon element between first row of matrices " +
      str(numpy.intersect1d(matrix_1[0,0:],matrix_2[0,0:])))
print("\nCommon element between second row of matrices " +
      str(numpy.intersect1d(matrix_1[1,0:],matrix_2[1,0:])))
print("\nCommon element between third row of matrices " + 
      str(numpy.intersect1d(matrix_1[2,0:],matrix_2[2,0:])))

"""
Question 3:

Create 2 5X4 arrays with random elements

"""

matrix_rand_elements_1 = numpy.random.randint(0,10,size=(5,4))
matrix_rand_elements_2 = numpy.random.randint(0,10,size=(5,4))

print("\nFirst matrix with random elements \n" + str(matrix_rand_elements_1))
print("\nSecond matrix with random elements \n" + str(matrix_rand_elements_2))


"""
Question 4
    - Perform addition on matrices created in Q3
    - Perform subtraction on matrices created in Q3
"""

matrix_after_addition = matrix_rand_elements_1 + matrix_rand_elements_2
matrix_after_subtraction = matrix_rand_elements_1 - matrix_rand_elements_2

print("\nMatrix after addition \n" + str(matrix_after_addition))
print("\nMatrix after subtraction \n" + str(matrix_after_subtraction))

"""
     Question 5
      - Element wise multiplication of first matrix
"""

matrix_scalar_product = numpy.multiply(5,matrix_rand_elements_1)

print("\nFirst random elements matrix multiplied by 5 for each elements\n" + 
      str(matrix_scalar_product))

"""
Question 6 
  - Perform matrix multiplication on matrices created in Question 3.
    - Operation required to make this possible :
      - To make this possible both the matrices should be conformable if 
        number of columns of first Matrix is equal to number of Rows of 
        second matrix.
        The operation that flips rows into columns and vice versa is Transpose.
        so we will create a transpose of second matrix.
        
"""

matrix_rand_elements_transposed = numpy.matrix.transpose(matrix_rand_elements_2)

print("\n LHS of multiplication \n" + str(matrix_rand_elements_1))
print("\n RHS of multiplication \n" + str(matrix_rand_elements_transposed))

matrix_multiplication_results = matrix_rand_elements_1.dot(matrix_rand_elements_transposed)

print("Matrix multiplication results \n" + str(matrix_multiplication_results))

"""
Question 7 - Combine two matrices created in Question 3.
"""

concatenated_matrix = numpy.concatenate([matrix_rand_elements_1,matrix_rand_elements_2])

print("\nConcantenated matrix \n" + str(concatenated_matrix))
