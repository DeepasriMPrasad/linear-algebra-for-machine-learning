import numpy as np
from vector_projection import vectorProjection
def vectorProjection(a,b):
    np.dot(a,b) *b/np.dot(b,b)


def changeBasis(data):
    vector = data['vector']
    b_vectors = data['basis_vectors']
    res = list(map(lambda b: vectorProjection(vector,b), b_vectors))
    return res



dataArray =[ {
    'vector': ,
    'basis_vectors': ,

}, 
 {
    'vector': ,
    'basis_vectors': ,

}, 
 {
    'vector': ,
    'basis_vectors': ,

}, 
 {
    'vector': ,
    'basis_vectors': ,

}, 
 {
    'vector': ,
    'basis_vectors': ,

}, 
]

result_list =  map(changeBasis, dataArray)
