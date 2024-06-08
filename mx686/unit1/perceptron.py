import numpy as np
import matplotlib.pyplot as plt

def perceptron(training, T):
    x1, y1 = training[0]
    theta = np.zeros(x1.shape[0])
    theta0 = 0
    hist = []
    for t in range(T):
        updated = False
        print(">>>round", t, ":", theta, theta0)
        for i in range(len(training)):
            x, y = training[i]
            print("checking:", x)
            if y * (theta @ x + theta0) <=0:
                updated = True
                theta += y * x
                theta0 += y
                print("<<<updated:", theta, theta0)
                hist.append((theta.tolist(), theta0))
        if not updated:
            break
    print(hist)
    return (theta, theta0)

def run(xs, ys):
    training = [(np.array(xs[i]), ys[i]) for i in range(len(xs))]
    theta, theta0 = perceptron(training, 10)
    ax = plt.subplot()
    ax.scatter([x[0] for x in xs], [y[1] for y in xs], c=['r' if c == 1 else "b" for c in ys])
    ax.axhline(0, color='black')
    ax.axvline(0, color='black')
    t = np.linspace(-3, 3, 60)
    sig = -1*(theta[0]*t + theta0)/theta[1]
    # plt.axis([-4, 4, -4, 4])
    ax.axis('equal')
    ax.plot(t, sig, color='green')
    ax.quiver(0, 0, *theta, angles='xy', scale_units='xy', scale=1)
    plt.show()

def u1h2():
    xs = [[-4, 2], [-2, 1], [-1, -1], [2, 2], [1, -2]]
    ys = [1, 1, -1, -1, -1]
    run(xs, ys)

def u1h3():
    xs = [[-1, 1], [1, -1], [1, 1], [2, 2]]
    ys = [1, 1, -1, -1]
    run(xs, ys)

if __name__ == "__main__":
    u1h2()
    u1h3()