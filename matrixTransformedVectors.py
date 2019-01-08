import numpy as np

#1
A = np.array([1/2,-1, 0,3/4]).reshape([2,2])
answer0 = np.matmul(A, np.array([3,2]))
print(answer0)
#2 
answer1 = np.matmul(A, np.array([-2,4]))
# print(answer1)

#4 

#5
answer2 = np.matmul(np.array([1,0,0,8]).reshape([2,2]), np.array([1,0,-1/2,1]).reshape([2,2]))
# print(answer2)

#5
answer3 = np.linalg.inv(answer2)
# print(answer3)
B =  [[1, 1, 1],[3,2,1],[2,1,2]]

print(np.linalg.inv(B))