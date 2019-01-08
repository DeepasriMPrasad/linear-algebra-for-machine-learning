import numpy as np

def vectorProjection(a,b):
    np.dot(a,b) *b/np.dot(b,b)

# 1
print(np.linalg.norm(np.array([1,3,4,2])))

# 2
x = np.array([-5,3,2,8])
y = np.array([1,2,-1,0])
print(np.dot(x,y))



# 3
r = np.array([3,-4,0])
s = np.array([10,5,-6])
print(np.linalg.norm(vectorProjection(r,s)))

# 4
print(vectorProjection(r,s))

# 5
a = np.array([3,0,4])
b = np.array([0,5,12])
print(np.linalg.norm(a+b) < np.linalg.norm(a) + np.linalg.norm(b))
