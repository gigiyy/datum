def h(y):
    x = x + 1
    """
    since you are trying to assign value to x, x is now a local variable
    so the value x + 1 is trying to referencing the the local variable too
    """


x = 5
h(x)
print(x)
