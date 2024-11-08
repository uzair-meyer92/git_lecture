# Add 3 to x using the += operator
x = int(input("Enter a number: "))
x += 3
print("3 added to the value is" , x )
# Multiply y by 2 using the *= operator
y = int(input("Enter a number: "))
y *= 2
print("The value multiplied by 2 is" , y )
# Divide x by y and store the result in a variable called 'result'
result = (x/y)
# Print the value of 'result'
print("The result of x divided by y is" , result )
# Create a condition that checks if a is greater than b
a = int(input("Enter a value a: "))
b = int(input("Enter a value b: "))
c = int(input("Enter a value c: "))
if a > b:
    print("a is greater than b")
# Create a condition that checks if b is even (hint: use the modulus operator)
if b % 2 == 0:
    print("b is even")
else:
    print("b is odd")
# Create a condition that checks if c is less than or equal to a
if c <= a:
    print("c is less than a")
# Combine the above conditions using logical operators to create a 'final_condition'
final_condition = (a > b) or (b % 2 == 0 and c <= a)
if final_condition: # Print the value of 'final_condition'
    print("The final condition is True")
else:
    print("The final condition is False")
# Ask the user to input a test score (0-100) and store it in a variable called 'score'
score = int(input("Enter your score: "))
if 90 <= score <= 100:
    grade = "A"
elif 80 <= score <= 89:
    grade = "B"
elif 70 <= score <= 79:
    grade = "C"
elif 60 <= score <= 69:
    grade = "D"
elif score <60:
    grade = "F"
# Print the grade for the given score
print(f"The student has grade" , (grade))
# Ask the user to input two numbers and store them in variables 'num1' and 'num2'
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
# Ask the user to input an operation (+, -, *, /) and store it in a variable called 'operation'
operation = input("Enter any operation (+, -, *, /): ")
if operation == "+" :
    operation_result = num1 + num2
elif operation == "-" :
    operation_result = num1 - num2
elif operation == "*" :
    operation_result = num1 * num2
elif operation == "/" :
    if num2 != 0:
      operation_result = num1 / num2
    else: 
      operation_result = ("Error message, division by zero")
else: 
    operation_result = print("Invalid operation")  
# Print the result of the operation
print(f"The result is " , (operation_result))  