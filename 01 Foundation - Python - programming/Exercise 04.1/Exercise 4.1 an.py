#Task 1: Function with Loop and Conditional Logic

# TODO: Define a function called 'check_attendance' that takes a list of names (students) and a list of absentees.
#       It should return a list of names of students who are absent.
def check_attendance(students, absentees):
    absent_students = []

    for students in students:
        if students in absentees:
            absent_students.append(students)

            return absent_students
# TODO: Call 'check_attendance' with a list of ["Alice", "Bob", "Charlie", "David"] 
#       and a list of absentees ["Bob", "David"], and print the result.
students_list = ["Alice", "Bob", "Charlie", "David"]
absentees_list = ["Bob", "David"]
result = check_attendance(students_list, absentees_list)
print(result)
# Task 2: Function for Real-Life Data Processing

# TODO: Define a function called 'calculate_average_grade' that takes a dictionary where the keys are student names 
#       and the values are their grades, and returns the average grade of the class.
def calculate_average_grade(grades):
    # Calculate the total sum of grades
    total = sum(grades.values())
    # Get the number of students
    num_students = len(grades)
    average = total / num_students if num_students > 0 else 0
    
    return average 
# TODO: Call the 'calculate_average_grade' function with the following dictionary:
#       {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 90}, and print the result.
grades_dict = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 90}
average_grade = calculate_average_grade(grades_dict)
print(average_grade)


# Task 3: Function Returning a Function (Higher-Order Function)
# TODO: Define a function called 'operation_selector' that takes a string "add" or "multiply" as a parameter,
#       and returns a function that either adds or multiplies two numbers.
def operation_selector(operation):
    if operation == "add":
        return lambda x, y: x + y
    elif operation == "multiply":
        return lambda x, y: x * y
    else:
        raise ValueError("Operation must be 'add' or 'multiply'.")

# Using 'operation_selector' to get the "add" function
add_function = operation_selector("add")
result_add = add_function(4, 6)
print("Addition Result:", result_add) 

# Using 'operation_selector' to get the "multiply" function
multiply_function = operation_selector("multiply")
result_multiply = multiply_function(3, 7)
print("Multiplication Result:", result_multiply) 

# TODO: Use 'operation_selector' to get the "add" function, and then call it to add 4 and 6.
add_function = operation_selector("add")
result_add = add_function(4, 6)
print("Addition Result:", result_add)  # Output: 10

# TODO: Use 'operation_selector' to get the "multiply" function, and then call it to multiply 3 and 7.
multiply_function = operation_selector("multiply")
result_multiply = multiply_function(3, 7)
print("Multiplication Result:", result_multiply) 

# Task 4: Function for a Practical Scenario

# TODO: Define a function called 'calculate_trip_cost' that takes three parameters:
# • distance (in km), fuel_efficiency (km per liter), fuel_price (price per liter),
# • and returns the total cost of fuel for the trip.
# Task : Using a for loop with a dictionary (Real-life Scenario: Grocery Shopping List)
def calculate_trip_cost(distance, fuel_efficiency, fuel_price):
    total_fuel_needed = distance / fuel_efficiency
    total_cost = total_fuel_needed * fuel_price
    return total_cost

distance = 150
fuel_efficiency = 15
fuel_price = 1.5
trip_cost = calculate_trip_cost(distance, fuel_efficiency, fuel_price)
print("Total trip cost:", trip_cost)

# TODO: Create a dictionary with grocery items as keys and their quantities in stock as values.
grocery_list = {
    "apples": 10,
    "bananas": 5,
    "carrots": 8,
    "dairy": 4}
# TODO: Use a for loop to print each item and its quantity in stock.
for item, quantity in grocery_list.items():
    print(f"{item}: {quantity}")
# TODO: Calculate and print the total number of items in stock (sum of all values in the dictionary).
total_items = sum(grocery_list.values())
print("Total number of items in stock:", total_items)

#------------------------------------------------------------------------------------
# Task 5: Using a while loop for banking (Real-life Scenario: ATM Pin Retry System)
# TODO: Ask the user to input their PIN.
correct_pin = "2468"
# TODO: If the PIN is incorrect, ask the user to try again, but only allow 3 attempts.
attempts = 3
# TODO: After 3 incorrect attempts, print "Account Locked". If the PIN is correct, print "Access Granted".
# TODO: Use a while loop to implement the retry system.
while attempts > 0:
    user_pin = input("Please enter your PIN: ")
    
    if user_pin == correct_pin:
        print("Access Granted.")
        break  
    else:
        attempts -= 1  # Decrement the attempts
        print(f"Incorrect PIN. You have {attempts} attempts left.")
if attempts == 0:
    print("Account Locked.")

#------------------------------------------------------------------------------------
# Task 6: Using a for loop with range() for a School Grading System
# TODO: Create a list with 10 random assignment scores (between 0 and 100).
# TODO: Use a for loop to calculate the total score.
# TODO: Calculate and print the average score for the class.
# Bonus: Use conditional logic to print a congratulatory message if the average is above 75.
# List of 10 student scores.
import random  # Import the random module

# Generate 10 random scores between 0 and 100
scores = [random.randint(0, 100) for _ in range(10)]
print("Assignment Scores:", scores)

# Calculate the total score
total_score = sum(scores)

# Calculate the average score
average_score = total_score / len(scores)

# Print the results
print("Total Score:", total_score)
print("Average Score:", average_score)

# Check if the average score is above 75
if average_score > 75:
    print("Congratulations! The average score is above 75!")
    
#------------------------------------------------------------------------------------
# Task 7: Using the random module (Real-life Scenario: Random Team Selection)
# TODO: Create a list with the names of 20 participants.
# TODO: Use the random module to select 5 random participants.
# TODO: Print the names of the selected team members.
# List of participants.
import random

participants = [
    "Alice", "Bob", "Charlie", "David", "Eva",
    "Frank", "Grace", "Hannah", "Ian", "Jack",
    "Kathy", "Leo", "Mia", "Nina", "Oscar",
    "Paul", "Quinn", "Rita", "Sam", "Tina"
]
selected_team = random.sample(participants, 5)
# TODO: Randomly select 5 people from the participants list.
print("Selected team members:")
for member in selected_team:
    print(member)

#------------------------------------------------------------------------------------
# Task 8: Custom module for a Fitness Tracker (Real-life Scenario: Tracking Calories Burned)
# Step 1: Create a module named 'fitness_tracker.py' with the following functions:



# Step 9: Use the custom module in your main script:
# TODO: Import the custom 'fitness_tracker' module.
import fitness_tracker
# TODO: Ask the user to input the distance they walked, ran, and cycled today.
distance_walked = float(input("Enter distance walked (km): "))
distance_ran = float(input("Enter distance ran (km): "))
distance_cycled = float(input("Enter distance cycled (km): "))

# TODO: Calculate and print the total calories burned for each activity.
calories_walked = fitness_tracker.walk_calories(distance_walked)
calories_ran = fitness_tracker.run_calories(distance_ran)
calories_cycled = fitness_tracker.cycle_calories(distance_cycled)

# TODO: Sum and print the total calories burned for the day.
total_calories = calories_walked + calories_ran + calories_cycled
print("Total calories burned today:", total_calories)

#------------------------------------------------------------------------------------


# Task 10: Using a while loop to Simulate Loan Repayment (Real-life Scenario: Paying Off a Loan)
# TODO: Ask the user to input the total loan amount.
total_loan = float(input("Enter the total loan amount: "))
# TODO: Ask the user to input their monthly repayment amount.
monthly_repayment = float(input("Enter your monthly repayment amount: "))
# TODO: Use a while loop to simulate monthly payments, reducing the loan each month.
# TODO: Print the remaining loan amount after each payment.
# TODO: When the loan is fully paid off, print a congratulatory message.

# TODO: Use a while loop to simulate the repayment process.
while total_loan > 0:
    total_loan -= monthly_repayment
    if total_loan < 0:
        total_loan = 0
print(f"Remaining loan amount: ${total_loan:.2f}")
print("Congratulations! The loan has been fully paid off.")