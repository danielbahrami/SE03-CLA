# Importing the Numpy library
import numpy as np
# Import the inverse function from the linear algebra library
from numpy.linalg import inv

# Declaring the 3x3 sample matrix
a = np.array([[0, 2, 0], [1, 4, 2], [4, 2, 0]])
# Declaring the 4x4 sample matrix
b = np.array([[0, 2, 0, 8], [1, 4, 2, -2], [4, 2, 0, -3], [2, -1, -6, 5]])
# Declaring the 5x5 sample matrix
c = np.array([[0, 2, 0, 8, 1], [1, 2, 2, -2, 5], [4, 2, 0, -3, 2], [2, -1, -6, 5, 0], [-5, 3, 8, 4, 4]])
# Declaring the nxn random matrix
d = np.array([[4, 5, 7, 8, 3, 9], [6, 2, 1, 0, 7, 5], [3, 7, 9, 9, 8, 4], [2, 1, 9, 3, 2, 6], [1, 8, 7, 3, 8, 5], [3, 5, 8, 7, 6, 0]])

# Printing the sample matrix
print ("Matrix:")
print (a)
# Printing the sample matrix inversed
print ("Inverse Matrix:")
print (inv(a))

print ("Matrix:")
print (b)
print ("Inverse Matrix:")
print (inv(b))

print ("Matrix:")
print (c)
print ("Inverse Matrix:")
print (inv(c))

print ("Matrix:")
print (d)
print ("Inverse Matrix:")
print (inv(d))
