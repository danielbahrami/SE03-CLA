# This file is the python template for the 1st assignment of Calculus
# and Linear Algebra. Feel free to adapt it to your needs.
import numpy as np

# Function to obtain the index of the row with the maximum absolute
# value (in the column col
def index_of_max_abs(A, row, col):
    idx_max = row
    for i in range(row + 1, len(A)):
        if abs(A[i][col]) > abs(A[idx_max][col]):
            idx_max = i

    return idx_max

# Function to swap the rows row1 and row2 in the matrix A. Since the
# matrix is passed by reference the it will be changed after calling
# the function, i.e.  no need to return a new matrix
def swap_rows(A, row1, row2):
    temp = np.copy(A[row1])
    A[row1] = A[row2]
    A[row2] = temp
    return A

# Implementation of the Gauss-Jordan elimination algorithm for inverse
# calculation
def inverse(A):
    # Make sure the matrix given as an argument is a square matrix
    m = A.shape[0]  # Number of rows in matrix A
    if A.shape[1] != m:
        raise Execution("Matrix must be square")

    # Create empty tildeA matrix adding the identity matrix to A
    tildeA = np.append(A, np.eye(m, dtype=np.float32), axis=1)

    # Number of columns of matrix tildeA (it should be 2*n)
    n = tildeA.shape[1]

    # TODO: Implement your algorithm for inverse calculation here
    pivot_row = 0
    pivot_col = 0
    while(pivot_row < m and pivot_col < m):
        idx_max = index_of_max_abs(tildeA, pivot_row, pivot_col)
        if tildeA[idx_max][pivot_col] == 0:
            pivot_col = pivot_col + 1
        else:
            tildeA = swap_rows(tildeA, pivot_row, idx_max)
            for i in range(pivot_row + 1, m):
                a = (tildeA[i][pivot_col] / tildeA[pivot_row][pivot_col])
                tildeA[i][pivot_col] = 0
                for j in range(pivot_col + 1, n):
                    tildeA[i][j] = tildeA[i][j] - a * tildeA[pivot_row][j]
            pivot_row = pivot_row + 1
            pivot_col = pivot_col + 1

    pivot = m - 1

    while pivot >= 0:
        if abs(tildeA[pivot][pivot]) < 0.000001:
            raise Exception("Error, Singular Matrix")
        else:
            for i in range(pivot - 1, -1, -1):
                a = (tildeA[i][pivot] / tildeA[pivot][pivot])
                tildeA[i][pivot] = 0
                for j in range(pivot + 1, n):
                    tildeA[i][j] = tildeA[i][j] - a * tildeA[pivot][j]
            a = 1 / tildeA[pivot][pivot]
            for j in range(1, n):
                tildeA[pivot][j] = a * tildeA[pivot][j]
            pivot = pivot - 1

    # Extract the inverse matrix from the matrix tildeA
    InvA = tildeA[:, m:]

    # Return the inverse matrix
    return InvA

def test():
    # Test for the inverse matrix calculation
    # test = 0: sample 3x3 matrix
    # test = 1: sample 4x4 matrix
    # test = 2: sample 5x5 matrix
    # test = 3: random nxn matrix
    test = 0
    n = 6
    if test == 0:
        A = np.array([[0, 2, 0], [1, 4, 2], [4, 2, 0]], dtype=np.float32)
    elif test == 1:
        A = np.array([[0, 2, 0, 8], [1, 4, 2, -2], [4, 2, 0, -3], [2, -1, -6, 5]], dtype=np.float32)
    elif test == 2:
        A = np.array([[0, 2, 0, 8, 1], [1, 2, 2, -2, 5], [4, 2, 0, -3, 2], [2, -1, -6, 5, 0], [-5, 3, 8, 4, 4]], dtype=np.float32)
    else:
        A = np.random.rand(n, n)

    # Calculate the inverse matrix of A
    InvA = inverse(A)
    print('The inverse of matrix A:')
    print(A)
    print('Is:')
    print(InvA)

    print('The (rounded) product of Inv(A)*A is:')
    print(np.rint(np.matmul(A, InvA)))  # rint() rounds the result to the nearest integer
    print('The product of Inv(A)*A is:')
    print(np.matmul(A, InvA))  # rint() rounds the result to the nearest integer

if __name__ == "__main__":
    print('Running test')
    test()
