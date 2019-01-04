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


def SimSolver(d):
    """
    Simultaneous equation solver, using internal
    numpy linear algebra routines to solve the matrix inversion
    via most appropriate factorization
    """
    A = np.array(d['dataA']).reshape(d['shapeA'])
    b = np.array(d['dataB']).reshape(d['shapeB'])
    x = np.linalg.solve(A, b)
    return x


data = {'dataA': [3, 2, 2, 3], 'shapeA': (
    2, 2), 'dataB': [7, 8], 'shapeB': (2, 1)}

print(SimSolver(data))


def sim_solver(dataA, dataB, shapeA, shapeB):
    """
    Simultaneous equation solver, using internal
    numpy linear algebra routines to solve the matrix inversion
    via most appropriate factorization
    """
    A = np.array(dataA).reshape(shapeA)
    b = np.array(dataB).reshape(shapeB)
    x = np.linalg.solve(A, b)
    return x


data = {'dataA': [3, 2, 2, 3], 'shapeA': (
    2, 2), 'dataB': [7, 8], 'shapeB': (2, 1)}
print(sim_solver(**data))
