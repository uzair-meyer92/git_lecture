# User inputs for item price and budget
item_price = float(input("Enter the price of the item: "))
budget = float(input("Enter your budget:"))

# Compare budget with item price
can_buy = budget >= item_price
print("Can you afford the item?", can_buy)