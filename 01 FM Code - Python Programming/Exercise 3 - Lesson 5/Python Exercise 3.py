# Define a function called 'greet' that prints "Hello, World!"
def greet():
    print("Hello,World!")


greet() # Call the 'greet' function

# Define a function called 'personalized_greeting' that takes a name as a parameter and prints a personalized greeting
def personalizes_greeting(name):
    name = (input("Enter your name: "))
    print("Hello there,"   +name)


personalizes_greeting(__name__) # Call the 'personalized_greeting' function with your name

# Define a function called 'square' that takes a number as a parameter and returns its square
def square(number):
    return number ** 2

result = square(5)
print(f"The square of 5 will result to" , (result)) #Call the 'square' function with the number 5 and print the result
    
# Define a function called 'rectangle_area' that takes length and width as parameters and returns the area of the rectangle
def rectangle_area(length,width):
    area = length * width  
    print("The area of a rectangle with length of 4 and width of 5 will be" , (area))

rectangle_area(4,5)   # Call the 'rectangle_area' function with length 4 and width 5, and print the result

# Define a function called 'apply_operation' that takes a function and a number as parameters, and returns the result of applying the function to the number 
def apply_operation(func, num):
    return func(num)

# Define a function called 'double' that takes a number as a parameter and returns its double
def double(double_number):
    return double_number * 2

# Use the 'apply_operation' function with the 'double' function and the number 7, and print the result
applyresult = apply_operation(double, 7)
print(applyresult)

# Use the 'apply_operation' function with the 'square' function (defined in Question 3) and the number 3, and print the result
result1 = apply_operation(square, 3)
print(result1)
