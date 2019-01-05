import numpy as np

'''For general matrix A nxp, vectors b and x (nx1), representing a linear system of equations with
x unknown, the solution can be found by using np.linalg.solve, which decides on the best way to invert
the matrix (this depends on size, stability, sparsity and other properties of A)
and solve the simultaneous equations
Ax = b
'''

def SimSolver(d):
    """
    Simultaneous equation solver, using internal
    numpy linear algebra routines to solve the matrix inversion
    via most appropriate factorization
    """
    A = np.array(d['elementsA']).reshape(d['shapeA'])
    b = np.array(d['elementsB']).reshape(d['shapeB'])
    x = np.linalg.solve(A, b)
    return x

data1 = {'elementsA': [3, 2, 2, 3], 'shapeA': (
    2, 2), 'elementsB': [7, 8], 'shapeB': (2, 1)}

print(SimSolver(data1))


dataArray = [
    {
    'elementsA': [3, 2, 2, 3], 
    'shapeA': (2, 2), 
    'elementsB': [7, 8], 
    'shapeB': (2, 1)
    },
    {
    'elementsA': [9, -17, -13, 7], 
    'shapeA': (2, 2), 
    'elementsB': [-20, -94], 
    'shapeB': (2, 1)
    },
    {
    'elementsA': [5, -2, 4, 5], 
    'shapeA': (2, 2), 
    'elementsB': [-13,-6], 
    'shapeB': (2, 1)
    },
    {
    'elementsA': [5, 7, 20, -18], 
    'shapeA': (2, 2), 
    'elementsB': [11,39], 
    'shapeB': (2, 1)
    },
    {
    'elementsA': [3,-2,1,1,1,1,3,-2,-1], 
    'shapeA': (3, 3), 
    'elementsB': [7,2,3], 
    'shapeB': (3, 1)
    }
    ]

answerArray = map(SimSolver, dataArray)

print(list(answerArray))

