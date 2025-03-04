quantity = int(input("Enter quantity of widgets: "))

if quantity > 10000:
    price = 10
elif 5000 <= quantity <= 10000:
    price = 20
else:
    price = 30

extended_price = quantity * price
tax = round(extended_price * 0.07, 2)
total = round(extended_price + tax, 2)

print("Quantity:", quantity)
print("Price per Widget: $", price)
print("Extended Price: $", extended_price)
print("Tax: $", tax)
print("Total: $", total)
