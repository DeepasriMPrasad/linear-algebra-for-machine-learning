import numpy as np

def vectorProjection(a,b):
    return np.dot(a,b) * b/np.dot(b,b)
