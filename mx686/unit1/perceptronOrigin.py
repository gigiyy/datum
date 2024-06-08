import numpy as np
import matplotlib.pyplot as plt

def perceptronOrigin(training, T):
    x1, y1 = training[0]
    theta = np.zeros(x1.shape[0])
    hist = []
    for t in range(T):
        print(">>>round", t, ": ", theta, sep='')
        updated = False
        for i in range(len(training)):
            x, y = training[i]
            print("checking: ", x)
            if y * theta @ x <=0:
                updated = True
                theta += y * x
                print(">>>update to", theta)
                hist.append(theta.tolist())
        if not updated:
            break
    print(hist)
    return theta


def run(xs, ys):
    training = [(np.array(xs[i]), ys[i]) for i in range(len(xs))]
    theta = perceptronOrigin(training, 10)
    plt.scatter([x[0] for x in xs], [y[1] for y in xs], c=['r' if c == 1 else "b" for c in ys])
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    t = np.linspace(-3, 3, 60)
    sig = -1*theta[0]*t/theta[1]
    # plt.axis([-10, 10, -10, 10])
    plt.axis('equal')
    plt.plot(t, sig, color='green')
    plt.quiver(0, 0, *theta, angles='xy', scale_units='xy', scale=1)
    plt.show()

def u1h1():
    xs = [[-1, -1], [1, 0], [-1, 1.5]]
    ys = [1, -1, 1]
    run(xs, ys)
    xs = [[1, 0], [-1, -1], [-1, 1.5]]
    ys = [-1, 1, 1]
    run(xs, ys)
    xs = [[-1, -1], [1, 0], [-1, 10]]
    ys = [1, -1, 1]
    run(xs, ys)
    xs = [[1, 0], [-1, -1], [-1, 10]]
    ys = [-1, 1, 1]
    run(xs, ys)

def genXs(d):
    return [[ np.cos(np.pi * i) if i == t else 0 for i in range(1, d + 1)] for t in range(1, d + 1)]

def u1h6():
    d = 3
    xs = genXs(d)
    print(xs)
    ys = [1 for _ in range(0, d)]
    run(xs, ys)
    np.random.shuffle(xs)
    print(xs)
    run(xs, ys)

if __name__ == "__main__":
    # u1h1()
    u1h6()