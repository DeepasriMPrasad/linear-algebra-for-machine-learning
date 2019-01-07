import numpy as np


def isLinearDependent(vector_list):
    matrix = np.array(vector_list).reshape(
        (len(vector_list), len(vector_list)))
    rank = np.linalg.matrix_rank(matrix)
    return (rank == len(vector_list))
