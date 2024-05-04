def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for 
        the largest value in L then for the second largest, and so on to 
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does 
                not yield a set of multipliers such that the equation sums to 's'
    """
    if len(L) == 0:
        return "no solution"
    if len(L) == 1:
        if s % L[0] != 0:
            return "no solution"
        else:
            return s // L[0]
    first = L[0]
    m0 = s // first
    while m0 >= 0:
        rest = greedySum(L[1:], s - m0 * first)
        if rest != "no solution":
            return m0 + rest
        else:
            m0 = m0 - 1
    return "no solution"

if __name__ == "__main__":
    print(greedySum([3], 9))
    print(greedySum([4], 9))
    print(greedySum([4, 5], 20))
    print(greedySum([4, 5], 25))
    print(greedySum([4, 5], 15))
    print(greedySum([4, 5], 11))
