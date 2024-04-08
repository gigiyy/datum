import random

# Code Sample A
def sampleA():
    mylist = []

    for i in range(random.randint(1, 10)):
        random.seed(0)
        if random.randint(1, 10) > 3:
            number = random.randint(1, 10)
            if number not in mylist:
                mylist.append(number)
    print(mylist)

def sampleB():
    mylist = []

    random.seed(0)
    for i in range(random.randint(1, 10)):
        if random.randint(1, 10) > 3:
            number = random.randint(1, 10)
            mylist.append(number)
    print(mylist)

sampleA()
sampleB()