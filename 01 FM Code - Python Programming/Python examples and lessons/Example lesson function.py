# Function to calculate amount of pizzas per people
def calculate_slices(num_people, slices_per_person):
    total_slices = num_people * slices_per_person
    return total_slices

# Example usage
num_people = int(input("Enter the number of people: "))
slices_per_person = int(input("Enter the number of slices each person eats: "))

print(f"Total number of slices needed: {calculate_slices(num_people, slices_per_person)}")

