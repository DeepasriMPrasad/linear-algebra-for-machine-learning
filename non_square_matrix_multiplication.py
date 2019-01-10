import numpy as np

def matMul(d):
    A = np.array(d['A']).reshape(d['shapeA'])
    B = np.array(d['B']).reshape(d['shapeB'])
    prod = np.matmul(A,B)
    print(f'Question {d["questionNumber"]}')
    print(f'{A}') 
    print('MatMul(*)') 
    print(f'{B}  = {prod}')
    return prod

dataArray = [
    {
        'questionNumber': 1,
        'A':[2,4,5,6],
        'shapeA':[1,4],
        'B':[1,3,2,1],
        'shapeB':[4,1],
    },
     {
        'questionNumber': 2,
        'A':[1,3,2,1],
        'shapeA':[4,1],
        'B':[2,4,5,6],
        'shapeB':[1,4],
    },   {
        'questionNumber': 3,
        'A':[1,2,3,4,0,1],
        'shapeA':[2,3],
        'B':[1,1,0,0,1,1,1,0,1],
        'shapeB':[3,3],
    },
    {
        'questionNumber': 4,
        'A':[2,-1,0,3,1,0],
        'shapeA':[3,2],
        'B':[0,1,4,-1,-2,0,0,2],
        'shapeB':[2,4],
    },
    {
        'questionNumber': 5,
        'A':[1,0,0,1],
        'shapeA':[2,2],
        'B':[1,2,3,4,5,6],
        'shapeB':[2,3],
    },]

# answers = list(map(matMul, dataArray))
# print(answers)


dataArray2 = [{
        'questionNumber': 5,
        'A':[1,0, 1/3, 0, 1, -1/4],
        'shapeA':[2,3],
        'B':[6,2,3],
        'shapeB':[3,1],
    },
    {
        'questionNumber': 6,
        'A':[1,0, 1/3, 0, 1, -1/4],
        'shapeA':[2,3],
        'B':[5,-1,-3,7,4,-4,1,-2,9,3,0,12],
        'shapeB':[3,4],
    },]


answers2 = list(map(matMul, dataArray2))
print(answers2)


T3 = np.linalg.matrix_power(np.array([6,-1,2,3]).reshape([2,2]), 3)
print('#############',T3)
t3 = np.linalg.matrix_power(np.array([2,7,0,-1]).reshape([2,2]), 3)
print('#############',t3)
T5 = np.linalg.matrix_power(np.array([1,0,2,-1]).reshape([2,2]), 3)
print('############',T5)