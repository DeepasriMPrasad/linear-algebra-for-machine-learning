import numpy as np

'''For general matrix A nxp, vectors b and x (nx1), representing a linear system of equations with 
x unknown, the solution can be found by using np.linalg.solve, which decides on the best way to invert 
the matrix (this depends on size, stability, sparsity and other properties of A) 
and solve the simultaneous equations
Ax = b
'''

A = np.array([3, 2, 2, 3]).reshape((2, 2))
b = np.array([7, 8]).reshape((2, 1))
x = np.linalg.solve(A, b)

print(x)


def SimSolver(dataA, shapeA, dataB, shapeB):
    """
    Simultaneous equation solver, using internal 
    numpy linear algebra routines to solve the matrix inversion
    via most appropriate factorization
    """
    A = np.array(dataA).reshape(shapeA)
    b = np.array(dataB).reshape(shapeB)
    x = np.linalg.solve(A, b)
    return x
