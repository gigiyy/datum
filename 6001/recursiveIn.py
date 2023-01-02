def isIn(char, aStr):
    """
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    """
    # Your code here
    strLen = len(aStr)
    if strLen == 0:
        return False
    if strLen == 1:
        return char == aStr
    else:
        idx = strLen // 2
        mid = aStr[idx]
        if mid == char:
            return True
        elif mid > char:
            return isIn(char, aStr[:idx])
        else:
            return isIn(char, aStr[idx + 1:])


print(isIn('a', 'bc'))
