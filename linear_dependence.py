import numpy as np


def isLinearIndependent(d):
    vectorList = d['vectorList']
    matrix = np.array(vectorList).reshape(
        (len(vectorList), len(vectorList)))
    rank = np.linalg.matrix_rank(matrix)
    flag = rank == len(vectorList)
    return (flag)
