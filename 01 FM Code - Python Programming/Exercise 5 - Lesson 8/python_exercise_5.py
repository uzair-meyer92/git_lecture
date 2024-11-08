# Create a list of fruits
fruits = ["Mango" , "Pineapple" , "Guava" , "Watermelon"]
print(fruits)

fruits.append("Dragonfruit") # Add a fruit to the end of the list
print(fruits)

fruits.insert(0 , "Strawberry") # Insert a fruit at the beginning of the list
print(fruits)

fruits.remove("Guava") # Remove a fruit from the list
print(fruits , "\n") # Print the modified list

# Create a list of numbers from 1 to 5
numbers = [1,2,3,4,5]
print(numbers)
square_numbers = [] # Create a new list with each number squared
for i in numbers:
    square_numbers.append(i ** 2)
print(square_numbers) # New list created with square numbers

# Find the sum and average of the original numbers
average = sum(numbers)/len(numbers)
print(f"The average of the original numbers is" , round(average)) # Print the results
print("\n")

# Create a dictionary of countries and their capitals
countrydict = {
     "Japan": "Tokyo" ,
     "Germany" : "Berlin" ,
     "Netherlands" : "Amsterdam"
    
}
print(countrydict)

countrydict["Brazil"] = "Brasília" # Add a new country-capital pair
countrydict.update({"Brazil" :"Brasília"})
print(countrydict)

countrydict.pop("Germany") # Remove a country-capital pair
print(countrydict , "\n") # Print the modified dictionary

fruitcolordict = {     # Fruit color dictionary created
    "Strawberry" : "Red" ,
    "Watermelon" : "Green" ,
    "Pineapple"  : "Yellow" ,

}
print(fruitcolordict) # Print each fruit and its color

# Check if a fruit is in the dictionary and print its color

fruitcheck = input("Check fruit in dictionary:  ")
if fruitcheck in fruitcolordict:
    print(fruitcolordict[fruitcheck] , "\n") # Print its color
