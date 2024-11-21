import numpy as np

M = np.eye(5, dtype="int")

M[0:2, 3:5]= 3   #2,5 ist exklusiv
M[3:5, 0:2]=2