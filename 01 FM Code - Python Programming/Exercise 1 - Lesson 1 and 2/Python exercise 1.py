# Ask for the user's name and store it in a variable
print("What is your name?")
name = input()
# Ask the user for their age and store it in a variable
print("What is your age?")
age = input()
# Print a greeting using the name and age variables
print("Hi there, " +name+ " you are " +age+ " years old")
# Ask for the length of a rectangle and store it as an integer
print("Enter the length of a rectangle?")
length = int(input())
# Ask for the width of a rectangle and store it as an integer
print("Enter the width of the rectangle?")
width = int(input())
#  Calculate the area of the rectanglefc
area = length * width
# Print the result
print("The result of the area of the rectangle is")
print(area)
# Ask the user for a temperature in Celsius and store it as a float
c = float(input("Ensert a temperature in degrees celsius:"))
# Convert the temperature to Fahrenheit using the formula: (C * 9/5) + 32
print("Convert the temperature into farenheit:")
f = (float(c*9/5)+32)
# Print the result rounded to two decimal places
print(f"{f:.2f}")