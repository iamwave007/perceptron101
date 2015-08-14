import numpy as np


X = np.array([[0, 0],[0, 1],[1, 0],[1, 1]])
y = np.array([0, 1, 1, 0])

print X.shape[0]    # (4,)
print X[0].shape    # (2,)
print X[0].shape+X[1].shape     #(2,2)