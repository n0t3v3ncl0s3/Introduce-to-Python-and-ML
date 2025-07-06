import numpy as np
A = np.array([1,2,3,4])
B = np.array([[5, 6],[7, 8],[9,10]])
# x = A^-1 . B
newA = A.reshape(2,2)
newB = B.reshape(2,3)
x = np.matmul(np.linalg.inv(newA),newB)
print(x)