#numpy is a library used for mathematical and statistical operations in python
#numpy stands for numeric python
#importing numpy
import numpy as np
print("successful")

#comparison with respect to list
list_var = [1,2,3,4,5,6]
print(type(list_var))
print(list_var)

#one dimensional array
#creating a list to an array
list_to_array = np.array(list_var) #array() it is a function which returns a value to form array
print(type(list_to_array))
print(list_to_array) #returns the value of list but it contains no comma which signify it in form of an array

#tuple to array (same)
tuple_var = [1,2,3,4,5,6]
print(type(tuple_var))
print(tuple_var)

tuple_to_array = np.array(list_var) #array() it is a function which returns a value to form array
print(type(tuple_to_array))
print(tuple_to_array)

#two dimensional array
array_2d = np.array([[1,2,3],[4,5,6]])
print(type(array_2d))
print(array_2d)

print("\n") #\n adds a space or line between two texts

#three dimensional array
array_3d = np.array([[[1,2,3],
                      [4,5,6],
                      [9,8,7]]])
print(array_3d)

#adding two array 
"""array_1 = np.array([1,2,3,4,5])
array_2 = np.array({6,7,8,9,10})
sum_list = array_1+array_2
print("Sum of the array is : ", sum_list, sep = '\n' )"""