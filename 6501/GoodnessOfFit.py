sample = [5, 6, 1, 6, 4, 1, 2, 4, 6, 6, 1, 6, 6, 3, 5]

n = len(sample)

hatp = [sample.count(x)/n for x in range(7)[1:]]

print(n)
print(hatp)

sum = 0
for x in range(6):
    sum += (hatp[x] - 1/6)**2*6

print(n*sum)




