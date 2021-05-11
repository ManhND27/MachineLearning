import numpy as np

np.array(object, dtype = None, ndmin = 0)
_A = [[1,2,3],[4,5,6]]
_B = [[1,2,3],[4,5,6]] 
_C = [1,1,1]
A = np.array(_A)
B = np.array(_B)
C = np.array(_C)
print(np.shape(C))
print("A + B : \n", A + B)
print("A - B : \n", A - B)
print("A * C : \n", A.dot(C))
print("A * C : \n", A@C)
print('a[0,1]:',A[0,0])
print('a[:,1]:',A[:,0])
print('a[1,:]:',A[0,:])
print(np.eye(5) == 1)
print(A*B)