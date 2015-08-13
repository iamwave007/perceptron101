import numpy as np
from random import random, randint
import pprint
pp=pprint.PrettyPrinter(indent=2)
# pp.pprint(X)

# # strategies = [ADD.count_from_either_strategy, ADD.random_strategy, ADD.count_from_one_once_strategy,
# #               ADD.count_from_one_twice_strategy, ADD.min_strategy] # ADD.random_strategy

# input_units = 14
# hidden_units=30
# output_units = 18
# layers=[input_units, hidden_units, output_units]

# # NN = nn1.NeuralNetwork([input_units, hidden_units, output_units])
# # NN = nn1.NeuralNetwork(layers)

# # i=1,2
# # r = 2 * np.random.random((layers[i - 1] + 1, layers[i] + 1)) - 1
# r = 2 * np.random.random((15, 19)) - 1
# # 15 by 19 matrix of -1 to 1

# # r=2*np.random.random((3,3))-1
# print r





def addends_matrix(a1, a2):
    lis = [0] * 14
    lis[a1 - 1] = 1
    lis[a1] = 1
    lis[a1 + 1] = 1

    lis[a2 + 6] = 1
    lis[a2 + 7] = 1
    lis[a2 + 8] = 1
    return lis
# result=addends_matrix(0,5)
# pp.pprint(result)


X = []
for i in range(1, 6):
    for j in range(1, 6):
        X.append(addends_matrix(i, j))

pp.pprint(X)
# print "=========================="
# pp.pprint(np.array(X))

