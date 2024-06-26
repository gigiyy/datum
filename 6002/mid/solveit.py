def solveit(test):
    """ test, a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True
        Returns an int, x, with the smallest absolute value such that test(x) is True 
        In case of ties, return any one of them. 
    """
    def ints():
        x = 0
        yield x
        while True:
            x += 1
            yield x
            yield -x
    
    for x in ints():
        if test(x):
            return x

    # x = 0
    # while not test(x):
    #     x += 1
    #     if test(x):
    #         return x
    #     elif test(-x):
    #         return -x
    # return x


#### This test case prints 49 ####
def f(x):
    return (x+15)**0.5 + x**0.5 == 15
print(solveit(f))

#### This test case prints 0 ####
def f(x):
    return x == 0
print(solveit(f))