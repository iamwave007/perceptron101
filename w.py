import numpy as np 

def sigmoid(x):
  return 1.0/(1.0+np.exp(-x))

def sigmoid_prime(x):
  return sigmoid(x)*(1.0-sigmoid(x))

def tanh(x):
  return np.tanh(x)

def tanh_prime(x):
  return 1.0-x**2

class NeuralNetwork:
  def __init__(self,layers,activation='tanh'):
    self.activation = sigmoid
    self.activation_prime = sigmoid_prime
    self.weights = []
    for i in range(1,len(layers)-1):
      r = 2*np.random.random((layers[i-1]+1,layers[i]+1))-1
      self.weights.append(r)
    r = 2*np.random.random((layers[i]+1,layers[i+1]))-1
    self.weights.append(r)




if __name__ == '__main__':
  nn=NeuralNetwork([2,2,1])
  # X=np.array([[0,0],
  #             [0,1],
  #             [1,0],
  #             [1,1]])
  # y=np.array([0,1,1,0])
  # nn.fit(X,y)

