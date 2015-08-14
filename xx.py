from random import choice 
from numpy import array, dot, random 
import numpy as np
# how to save the trained ability somewhere for later use?
# what pattern does the vector w follow?

training_data = [ 
  (array([0,0,1]), 0), 
  (array([0,1,1]), 1), 
  (array([1,0,1]), 1), 
  (array([1,1,1]), 1), 
]

w = random.rand(3)
print w, " is w is here"
# unit_step = lambda x: 0 if x < 0 else 1
sigma =lambda x: 1/(1+np.exp(-x))

errors = []
weights_2=[]
eta = 0.2   
n = 100 

for i in range(n):
  x, expected = choice(training_data)
  result = dot(w, x) 
  error = expected - sigma(result)
  errors.append(error) 
  w += eta * error * x
  print w[2],error
  weights_2.append(w[2])


for x, _ in training_data: 
  result = dot(x, w)
  print("{}: {} -> {}".format(x[:2], result, sigma(result)))


import matplotlib.pyplot as plt
# plot(range(n),errors)
plt.plot(range(n),weights_2)
plt.show()