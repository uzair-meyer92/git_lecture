
# Create a list of fruits
fruits = ["Mango" , "Strawberry" , "Blueberry"]

for fruit in fruits: 
    print(fruit) # Use a for loop to print each fruit in the list
print("\n")
# Use a while loop to create a countdown from 5 to 1
x = 5

while x > 0:
    print(x)
    x -= 1
print("\n")
# Use a for loop to print the first 10 square numbers
square_numbers = []
for number in range(1,11):
    square_numbers.append(number ** 2)
print(square_numbers,"\n")

# Import the random module
import random

colors = ["Red" , "Blue" , "Green" , "Yellow" , "Purple"]  # Create a list of colors

# Use a for loop to select and print 3 random colors from the list
for color in range(3):
    color = random.choice(colors)
    print(color)
print("\n")

# Import the custom module and use its functions
import math_operations as mo # Shortening math_operations to mo for easy use

# Usage of functions
# print(mo.add())
# print(mo.divide())
# print(mo.multiply())
# print(mo.subtract())

# Use a while loop to create a simple calculator
def calculator():
    while True:
        print("Please select calculation operation")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = int(input("Enter choice(1,2,3,4,5):   "))
        if choice == int(5):
            print("Bye, bye!")
            break
        num1 = int(input("Enter your first value:  "))
        num2 = int(input("Enter your second value:  "))
        if choice == int(1):
            result =  mo.add(num1 , num2)
        
        if choice == int(2):
            result = mo.subtract(num1 , num2)
        
        if choice == int(3):
            result = mo.multiply(num1 , num2)
        
        if choice == int(4):
            result = mo.divide(num1 , num2)
        
        print("\n============== RESULTS ===============\n")
        print(result)
        print("\n===============================\n")
        
        
calculator()