balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

currentBalance = balance
monthlyInterestRate = annualInterestRate / 12

for month in range(12):
    paidAmount = currentBalance * monthlyPaymentRate
    currentBalance = currentBalance - paidAmount
    if currentBalance <= 0.001:
        break

    interest = currentBalance * monthlyInterestRate
    currentBalance = currentBalance + interest
    print("Month ", month + 1, " Remaining balance: ", round(currentBalance, 2))

print("Remaining balance: ", round(currentBalance, 2))
