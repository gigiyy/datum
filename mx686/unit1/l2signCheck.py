import numpy as np
import matplotlib.pyplot as plt


def checkSign():
    theta = np.array([1, -1]).transpose()
    theta0 = -1
    points = [np.array(p) for p in [[1, -1], [1, 0], [0, 1], [0, 0]]]

    for point in points:
        print(point, "+" if theta @ point + theta0  > 0 else "-")


if __name__ == "__main__":
    checkSign()
