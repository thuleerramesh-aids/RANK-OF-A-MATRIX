#Program to find the rank of a matrix.
#Developed by: THULEER.R
#RegisterNumber:212225230285
import numpy as np
matrixA =np.array([[1,2,3],[3,6,9]])
rank = np.linalg.matrix_rank(matrixA)
print(rank)
