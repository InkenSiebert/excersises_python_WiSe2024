import numpy as np
M= np.array([3,2,1,4]).reshape(2,2)

M_inv = np.linalg.inv(M)

I = np.matmul (M_inv, M)


A=np.array([7,5,-3, 3, -5, 2, 5, 3, -7]).reshape(3,3)

r=np.array([16, -8, 0]).reshape(3,1)

A_inv=np.linalg.inv(A)

b= np.matmul(A_inv, r)