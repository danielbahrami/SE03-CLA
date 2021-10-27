# Import the Numpy library
import numpy as np

# Defining the Gauss Jordan method
# The method takes 2 arguments: The matrix of coefficients and the vector of constant terms
def gaussJordan(a,b):
    a = np.array(a, float)
    b = np.array(b, float)
    n = len(b)

    # The main loop of the Gauss Jordan method
    # k will take all elements from 0 to n-1
    for k in range(n):
        # Here partial pivoting takes place
        # 1.0e-12 is written, as writing it as a fraction doesn't look nice.
        if np.fabs(a[k,k]) < 1.0e-12:
            for i in range(k+1,n):
                if np.fabs(a[i,k]) > np.fabs(a[k,k]):
                    for j in range(k,n):
                        a[k,j],a[i,j] = a[i,j],a[k,j]
                    b[k],b[i] = b[i],b[k]
                    break
        # After partial pivoting, the pivot row is being divided.
        pivot = a[k,k]
        for j in range(k,n):
            a[k,j] /= pivot
        b[k] /= pivot
        # The elimination step of the Gauss Jordan method
        for i in range(n):
            if i == k or a[i,k] == 0: continue
            factor = a[i,k]
            for j in range(k,n):
                a[i,j] -= factor * a[k,j]
            b[i] -= factor * b[k]
    # Returning the solution and the elimination of the Gauss Jordan method
    return b,a

# Defining the matrix and solution vector to test against
a = [[0,2,0,1],[2,2,3,2],[4,-3,0,1],[6,1,-6,-5]]
b = [0,-2,-7,6]

# Defining the matrix and solution vector as variables
X,Y = gaussJordan(a,b)

# Printing the matrix and solution vector variables
print("The solution:")
print(X)
print("The transformed matrix:")
print(Y)
