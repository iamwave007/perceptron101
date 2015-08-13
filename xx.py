from random import choice 
from numpy import array, dot, random 
from pylab import plot, ylim

# dot(w, x): the third value is random as well...what if it's not? # no matter
# weird data:
# training_data = [ 
#   (array([0,0,1]), 1), 
#   (array([0,1,1]), 0), 
#   (array([1,0,1]), 0), 
#   (array([1,1,1]), 0), 
# ]

# how to save the trained ability somewhere for later use?
# what pattern does the vector w follow?

training_data = [ 
  (array([0,0,1]), 0), 
  (array([0,1,1]), 1), 
  (array([1,0,1]), 1), 
  (array([1,1,1]), 1), 
]

w = random.rand(3)
# w=[0,0,0]
print w, " is w is here"
unit_step = lambda x: 0 if x < 0 else 1 
errors = []
weights_2=[]
eta = 0.2   #0.2
n = 100 

for i in range(n):
  x, expected = choice(training_data) 
  result = dot(w, x) 
  error = expected - unit_step(result)
  errors.append(error) 
  w += eta * error * x
  print w[2],error
  weights_2.append(w[2])


for x, _ in training_data: 
  result = dot(x, w)
  print("{}: {} -> {}".format(x[:2], result, unit_step(result)))


# plot weight change over n and see the curve

from pylab import *
# plot(range(n),errors)
plot(range(n),weights_2)
show()


