# Question 1: Using a for loop with a list

# TODO: Create a list of fruits
fruits = ["Banana", "Mango", "Apple"]
# TODO: Use a for loop to print each fruit in the list
for fruit in fruits:
    print(fruit) 
    
#-------------------------------------------------------------------------
# Question 2: Using a while loop for countdown

# TODO: Use a while loop to create a countdown from 5 to 1
count = 5
while count > 0:
    print(count)
    count -= 1
print("Happy!!! Happy!!! December is here!!!")


#-------------------------------------------------------------------------
# Question 3: Using a for loop with range()

# TODO: Use a for loop to print the first 10 square numbers
for number in range (1, 11):
    square = number * number
    print(square)
    
#-------------------------------------------------------------------------

# Question 4: Using the random module

# TODO: Import the random module
import random

# TODO: Create a list of colors
colors = ["Red", "Yellow", "White", "Black", "Brown", "Blue"]
# TODO: Use a for loop to select and print 3 random colors from the list
for color in range(3):
    random_color = random.choice(colors)
    print(random_color)


#-------------------------------------------------------------------------
# Question 5: Creating and using a custom module

# TODO: Create a new file named 'math_operations.py' with the following content:


# TODO: Import the custom module and use its functions
import math_operations

# TODO: Use a while loop to create a simple calculator
while True:
    print("\nCalculator")
    print("+ : Add")
    print("- : Subtract")
    print("* : Multiply")
    print("/ : Divide")
    print("E : Exit")

    # Ask user to choose an operation
    choice = input("Choose an operation (+, -, *, /, E): ").upper()

    if choice == 'E':
        print("Exiting the calculator.")
        break

    # Get numbers from the user
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        continue

    # Perform the selected operation using functions from math_operations module
    if choice == '+':
        print(f"The result is: {math_operations.add(num1, num2)}")  # Call add function
    elif choice == '-':
        print(f"The result is: {math_operations.subtract(num1, num2)}")  # Call subtract function
    elif choice == '*':
        print(f"The result is: {math_operations.multiply(num1, num2)}")  # Call multiply function
    elif choice == '/':
        print(f"The result is: {math_operations.divide(num1, num2)}")  # Call divide function
    else:
        print("Invalid choice! Please select a valid operation.")