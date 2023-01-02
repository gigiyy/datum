# Paste your code into this box
s = 'xxxxxdddbobobxxxx'
count = 0
index = 0
while index < len(s):
    found = s[index:].find('bob')
    if found != -1:
        count += 1
        index = found + index + 1
    else:
        break

print('Number of times bob occurs is: ' + str(count))
