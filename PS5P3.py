principal = float(input("Enter principal amount: "))
years = int(input("Enter years to maturity: "))

if principal > 100000 and years == 5:
    interest_rate = 0.06
elif 50000 <= principal <= 100000 and years == 10:
    interest_rate = 0.05
elif 50000 <= principal <= 100000 and years == 5:
    interest_rate = 0.04
else:
    interest_rate = 0.02

interest = round(principal * interest_rate, 2)

print("Principal: $", principal)
print("Interest Rate:", interest_rate * 100, "%")
print("First-Year Interest: $", interest)
