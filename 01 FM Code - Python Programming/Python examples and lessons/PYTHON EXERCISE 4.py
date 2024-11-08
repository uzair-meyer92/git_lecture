# Create a list of fruits
fruits = ("Mango" , "Strawberry" , "Blueberry")

for fruit in fruits: 
    print(fruit) # Use a for loop to print each fruit in the list

# Use a while loop to create a countdown from 5 to 1
x = 5

while x > 0:
    print(x)
    x -= 1

# Use a for loop to print the first 10 square numbers
square_numbers = ("1" , "4" , "9" , "16" , "25" , "36" , "49" , "64" , "81" , "100")

for number in square_numbers:
    print(number)

# Import the random module
import random

colors = ["Red" , "Blue" , "Green" , "Yellow" , "Purple"]  # Create a list of colors

# Use a for loop to select and print 3 random colors from the list
for color in range(3):
    color = random.choice(colors)
    print(color)

# Import the custom module and use its functions
import math_operations as mam

calculate_power = True

while calculate_power == True: 