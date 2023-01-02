def getPrimes():
    previous = []
    next = 2
    while True:
        yield next
        previous.append(next)
        next = next + 1
        while not isPrime(next, previous):
            next = next + 1

def isPrime(next, previous):
    for e in previous:
        if next % e == 0:
            return False

    return True