# Write a function to calculate the number of slices per person

def pizza_slices(num_people,slices_per_person):
    total_pizza_slices = num_people * slices_per_person
    return total_pizza_slices

# Ask the user how many guests they are inviting and how many slices of each person needs and wants
# Then, tell them how many slices of pizza they need.

num_people = int(input("How many people are invited?  "))
slices_per_person = int(input("How many slices will each person want or need?  "))

print(f"The total number for pizza slices needed is {pizza_slices(num_people,slices_per_person)}")
