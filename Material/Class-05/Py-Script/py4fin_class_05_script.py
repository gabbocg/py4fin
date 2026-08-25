# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 23:25:58 2021

@author: Habac
"""

# list as a "matrix"
x = list([[1,2,3],[4,5,6],[7,8,9]])
x

# extracting element ij
x[1][1]

# load the numpy library
import numpy as np

mat_x = np.array(x) # the array is generated
mat_x

mat_x.ndim # it has two dimensions

m, n = mat_x.shape # number of rows and columns
m, n

mat_x.size # number of elements in the matrix

# the array class is checked
type(mat_x)

# the range version but in numpy
np.arange(1,10).reshape(-1,3)

#%% '''NumPy'''

'''1.a'''
num = [3, 0, 2, 2, 0, 2, 0, 1, 1]

list_to_array = np.array(num)
a = list_to_array.reshape((3,3))

# way 1
a.T

# way 2
a.transpose()

'''1.b'''
b = np.linalg.inv(a)

'''1.c'''
a.dot(b)

# to generate an identity matrix 
np.eye(3)

'''1.d'''
mean_a = np.ones((1,3)).dot(a).dot(np.ones((3,1))) / a.size
mean_a[0][0]


'''2.a'''
c = np.array([[2,4],[5, -6]])
d = np.array([[9,-3],[3,6]])

# addition
c + d
# subtraction
c - d
# multiplication
c * d
# division
c / d

'''2.b'''
c.dot(d)


'''3.a'''
mat_a = np.array([[1,2,3],[4,5,6]])
mat_b = np.array([[1,2,3],[4,5,6]])

def manual_mult(mat_a, mat_b):
  '''
  multiplies element ij of matrix a with element ij of matrix b 
  ''' 
  m,n = mat_a.shape

  zero_mat = np.zeros((m,n))
  zero_mat.fill(np.nan)

  for i in range(m):
    for j in range(n):
      zero_mat[i][j] = mat_a[i][j] * mat_b[i][j] 

  return(zero_mat)

# we test the function
manual_mult(mat_a, mat_b)

#%% '''Random Numbers'''

'''1.a'''
np.random.seed(10)

array_norm = np.random.randn(10000)

# reshape
e = array_norm.reshape((100,100)) 

# resize
array_norm.resize((100,10), refcheck=False)
array_norm # in-place, but it must not have been referenced, for example with reshape

'''2.b'''
e_flatten_col = e.flatten(order='C') # flattened by column
e_flatten_row = e.flatten(order='F') # flattened by row

e_flatten_col.mean() # mean
e_flatten_col.std() # standard deviation

array_norm

#%% '''System of Equations'''

'''1.a'''
# the matrices are generated (unknowns + result)
mat1 = np.array([[1, 1, 1], [3, -2, 1], [2, 1, -1]])
mat1_res = np.array([6, 2, 1])

# the system of equations is solved
np.linalg.solve(mat1, mat1_res)

'''1.b'''
# the matrices are generated (unknowns + result)
mat2 = np.array([[3, 4, -5, 1], [2, 2, 2, -1], [1, -1, 5, -5], [5, 0, 0, 1]])
mat2_res = np.array([10, 5, 7, 4])

# the system of equations is solved
np.linalg.solve(mat2, mat2_res)