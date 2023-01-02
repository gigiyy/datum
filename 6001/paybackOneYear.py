balance = 320000
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate / 12


def canPaybackWith(monthlyAmount):
    currentBalance = balance

    for month in range(12):
        currentBalance = currentBalance - monthlyAmount
        print("Month ", month, " Remaining balance: ", round(currentBalance, 2))
        interest = currentBalance * monthlyInterestRate
        currentBalance = currentBalance + interest

    if abs(currentBalance) <= 0.1:
        return month
    elif currentBalance < 0:
        return month - 1
    else:
        return month + 1


low = round(balance / 12.0, 2)
high = round((balance * (1 + monthlyInterestRate) ** 12) / 12.0, 2)

while True:
    mid = round((low + high) / 2.0, 2)
    print("Testing with amount: ", mid, " while high: ", high, " and low: ", low)
    paidBackAt = canPaybackWith(mid)
    if paidBackAt == 11 or abs(high - low) < 0.1:
        print("Lowest payment: ", mid)
        break
    elif paidBackAt > 11:
        low = round(mid, 2)
    else:
        high = round(mid, 2)

