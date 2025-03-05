tickets = int(input("Enter number of tickets: "))

if tickets >= 25:
    price_per_ticket = 50
elif 10 <= tickets <= 24:
    price_per_ticket = 60
elif 5 <= tickets <= 9:
    price_per_ticket = 70
else:
    price_per_ticket = 75

total_cost = tickets * price_per_ticket

print("Number of Tickets:", tickets)
print("Price per Ticket: $", price_per_ticket)
print("Total Cost: $", total_cost)
