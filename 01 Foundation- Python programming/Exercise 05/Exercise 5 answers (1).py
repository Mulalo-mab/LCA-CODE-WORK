# Question 1: Creating and Modifying Lists

# TODO: Create a list of fruits
fruits = ["Banana", "Apples", "Oranges", "Cherry"]
# TODO: Add a fruit to the end of the list
fruits.append("Mango")
# TODO: Insert a fruit at the beginning of the list
fruits.insert(1, "Grape")
# TODO: Remove a fruit from the list
fruits.remove("Banana")
# TODO: Print the modified list
print(fruits)

#-------------------------------------------------------------------------
# Question 2: List Operations

# TODO: Create a list of numbers from 1 to 5
numbers = [1, 2, 3, 4, 5]
# TODO: Create a new list with each number squared
square_numbers = [num ** 2 for num in numbers]
print(square_numbers)
# TODO: Find the sum and average of the original numbers
total_sum = sum(numbers)
average = total_sum / len(numbers)
# TODO: Print the results
print(f"Toltal Sum of numbers: {total_sum}")
print(f"Total average of numbers: {average}")

#-------------------------------------------------------------------------
# Question 3: Creating and Modifying Dictionaries

# TODO: Create a dictionary of countries and their capitals
countries_and_capitals = {
    "South Africa": "Pretoria",
    "France": "Paris",
    "Japan": "Tokyo",
    "Brazil": "Brasilia",
    "Italy": "Rome",
}
# TODO: Add a new country-capital pair
countries_and_capitals["Germany"] = "Berlin"

# TODO: Update the capital of an existing country
countries_and_capitals.update({"South Africa": "Cape Town"})
# TODO: Remove a country-capital pair
countries_and_capitals.pop("Japan")
# TODO: Print the modified dictionary
print(countries_and_capitals)

#-------------------------------------------------------------------------
# Question 4: Dictionary Operations

# TODO: Create a dictionary of fruit colors
fruits_color = {
    "Apple": "Green",
    "Grape": "Purple",
    "Banana": "Yellow",
    "Orange": "Orange"
    }
# TODO: Print all the fruits (keys)
print("fruits:", list(fruits_color.keys()))
# TODO: Print all the colors (values)
print("colors:", list(fruits_color.values()))
# TODO: Print each fruit and its color
for fruit, color in fruits_color.items():
    print(f"The color of {fruit} is {color}.")

# TODO: Check if a fruit is in the dictionary and print its color
fruit_to_check = "Apple"

if fruit_to_check in fruits_color:
    print(f"{fruit_to_check} is in the dictionary with color: {fruits_color[fruit_to_check]}")
else:
    print(f"{fruit_to_check} is not in the dictionary.")