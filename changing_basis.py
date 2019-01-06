import numpy as np

def changeBasis(data):
    vector = data['vector']
    b_vectors = data['basis_vectors']
    res = list(map(lambda b: np.cross(vector, b), b_vectors))
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
