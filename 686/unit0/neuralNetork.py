import numpy as np
def neural_network(inputs, weights):
    """
     Takes an input vector and runs it through a 1-layer neural network
     with a given weight matrix and returns the output.

     Arg:
       inputs - 2 x 1 NumPy array
       weights - 2 x 1 NumPy array
     Returns (in this order):
       out - a 1 x 1 NumPy array, representing the output of the neural network
    """
    #Your code here
    return np.tanh(np.matmul(weights.transpose(), inputs))


x = np.random.random([2, 1])
w = np.random.random([2, 1])
print(x)
print(w)
z = neural_network(x, w)
print(z.shape)
print(z)
