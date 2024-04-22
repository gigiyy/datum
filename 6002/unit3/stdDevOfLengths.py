import math

def stdDevOfLength(L):
    if len(L) == 0:
        return float('NaN')
    mu = sum(len(s) for s in L) / len(L)
    std = math.sqrt(sum((len(s) - mu) ** 2 for s in L) / len(L))
    return std


if __name__ == "__main__":
    L1= ['a', 'z', 'x']
    L2 = ['apples', 'oranges', 'kiwis', 'pineapples']
    print(stdDevOfLength(L1))
    print(stdDevOfLength(L2))
