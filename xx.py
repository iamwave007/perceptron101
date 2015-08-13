from random import choice 
from numpy import array, dot, random 
from pylab import plot, ylim
# plot weight change over n and see the curve
# dot(w, x): the third value is random as well... ok. what if it's not?
# how to save the trained ability somewhere for later use?
# weird data:
# training_data = [ 
#   (array([0,0,1]), 1), 
#   (array([0,1,1]), 0), 
#   (array([1,0,1]), 0), 
#   (array([1,1,1]), 0), 
# ]

# ? dummy: if not for it, there might be cases where learning is not needed
#      and this won't be a good example then...
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
eta = 0.2   #0.2
n = 100 

for i in range(n):
  x, expected = choice(training_data) 
  result = dot(w, x) 
  error = expected - unit_step(result)
  errors.append(error) 
  w += eta * error * x
  print w[2],error
  # print w  # this is clumsy. changing each is better?

# for x, _ in training_data: 
#   result = dot(x, w)
#   print("{}: {} -> {}".format(x[:2], result, unit_step(result)))



from pylab import *
plot(range(n),errors)
show()