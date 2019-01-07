import numpy as np


def isLinearIndependent(d):
    vectorList = d['vectorList']
    matrix = np.array(vectorList).reshape(
        (len(vectorList), len(vectorList)))
    rank = np.linalg.matrix_rank(matrix)
    isLinearlyIndependent = rank == len(vectorList)
    msg = (
        f'The vectors {vectorList} in question'
        f'{d["questionNumber"]} are Linearly'
        f'{"Independent" if isLinearIndependent else "Dependent"}'
    )
    print(msg)
    return (isLinearIndependent)
