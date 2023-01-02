s = 'bfucjzslygervvnpxejv'

lst = s[0]
maxStr = lst
maxLen = 1
curMax = lst
curLen = 1

for c in s[1:]:
    if c >= lst:
        curLen += 1
        curMax = curMax + c
        if curLen > maxLen:
            maxStr = curMax
            maxLen = curLen
    else:
        curMax = c
        curLen = 1
    lst = c

print('Longest substring in alphabetical order is: ' + maxStr)
