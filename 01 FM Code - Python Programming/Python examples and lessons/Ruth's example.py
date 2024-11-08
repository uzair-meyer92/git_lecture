# Inputs from the user
age = int(input("Enter your age: "))  # Input for age
ticket_price = 12.00  # Base price of a ticket
discount_price = 8.00  # Discounted price for children or seniors
num_tickets = int(input("How many tickets do you want to buy? "))  # Number of tickets
has_discount = input("Do you have a discount code? (yes/no): ").lower() == "yes"  # Discount code
# Determine ticket price based on age (children and seniors get a discount)
if age <= 12 or age >= 65:
    price_per_ticket = discount_price
    print("You are eligible for a discounted ticket!")
else:
    price_per_ticket = ticket_price
    print("You need to pay the regular ticket price.")
# Apply an extra discount if the user has a discount code
if has_discount:
    print("Discount code applied!")
    #price_per_ticket -= 2  # Discount code reduces price by R2
else:
    print("No discount code applied.")
# Calculate the total cost
total_cost = price_per_ticket * num_tickets
# User inputs how much money they have
money_available = float(input("Enter how much money you have: "))
# Comparison to check if the user has enough money
can_buy = money_available >= total_cost
# Logical output based on comparison
if can_buy:
    print(f"You can buy the tickets! Your total is: R{total_cost:.2f}")
    remaining_money = money_available - total_cost  # Assignment operator to update money after purchase
    print(f"You will have R{remaining_money:.2f} left.")
else:
    print(f"Sorry, you don't have enough money. You need R{total_cost - money_available:.2f} more.")