import numpy as np


def randomization(n):
    """
    Arg:`
      n - an integer
    Returns:
      A - a randomly-generated nx1 Numpy array.
    """
    # Your code here
    return np.random.random([n, 1])


def operations(h, w):
    """
    Takes two inputs, h and w, and makes two Numpy arrays A and B of size
    h x w, and returns A, B, and s, the sum of A and B.

    Arg:
      h - an integer describing the height of A and B
      w - an integer describing the width of A and B
    Returns (in this order):
      A - a randomly-generated h x w Numpy array.
      B - a randomly-generated h x w Numpy array.
      s - the sum of A and B.
    """
    # Your code here
    a = np.random.random([h, w])
    b = np.random.random(([h, w]))
    return a, b, a + b


def norm(A, B):
    """
    Takes two Numpy column arrays, A and B, and returns the L2 norm of their
    sum.

    Arg:
      A - a Numpy array
      B - a Numpy array
    Returns:
      s - the L2 norm of A+B.
    """
    # Your code here
    return np.linalg.norm(A + B)


x = randomization(3)
print(x)

(a, b, c) = operations(3, 2)

print(c)
print(norm(a, b))
