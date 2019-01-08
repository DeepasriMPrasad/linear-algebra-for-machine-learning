import numpy as np
import linear_dependence as isLinearDependent
from vector_projection import vectorProjection
#1 vector projection
vectorProjection(np.array([1,2]), np.array([1,1]))

#2 scalar projection 
def scalarProjection(a,b):
    return np.dot(a,b)/np.dot(b,b)

scalarProjection(np.array([2,1]), np.array([3,-4]))
#3 vector change of basis
basisVectors = [np.array(1,2,3), np.array(-2,1,0), np.array(-3,-6,5)]
vector = np.array(-4,-3,8)
 
map(lambda bVector:scalarProjection(vector,bVector) , basisVectors)
#4 linear dependence
isLinearDependent([np.array(1,2,1), np.array(3,-4,5), np.array(1,-8,7)])
# 5 vector addition with scalar multiplication
np.array(3,2,4) + 2*np.array(-1,2,-3)