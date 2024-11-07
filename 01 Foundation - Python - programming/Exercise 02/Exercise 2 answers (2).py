# Question 1: Arithmetic and Assignment Operators
x = 5 # assigning 5 to x
y = 4 # assigning 4 to y

# TODO: Add 3 to x using the += operator
x += 3
# TODO: Multiply y by 2 using the *= operator
y *= 2
# TODO: Divide x by y and store the result in a variable called 'result'
y /= x
result = x/y
# TODO: Print the value of 'result'
print(result)
#------------------------------------------------------------------------------------
# Question 2: Comparison and Logical Operators
a = 10
b = 5
c = 1

# TODO: Create a condition that checks if a is greater than b
a > b
# TODO: Create a condition that checks if b is even (hint: use the modulus operator)
b % 2 == 0
# TODO: Create a condition that checks if c is less than or equal to a
c <= a
# TODO: Combine the above conditions using logical operators to create a 'final_condition'
#       The 'final_condition' should be True if either:
#       - a is greater than b, or
#       - b is even and c is less than or equal to a
final_condition = (a > b) or (b % 2 == 0 and c < a)
# TODO: Print the value of 'final_condition'
print(f"The final_condition is: {final_condition}")
#------------------------------------------------------------------------------------
# Question 3: Conditional Statements

# TODO: Ask the user to input a test score (0-100) and store it in a variable called 'score'
score = float(input("What is your score (0-100): "))
# TODO: Implement a grading system using if-elif-else statements:
#       90-100: A2
#       80-89: B
#       70-79: C
#       60-69: D
#       Below 60: F
grade = score
if 90 <= score <= 100:
    grade = "A"
elif 80 <= score < 89:
    grade = "B"
elif 70 <= score < 79:
    grade = "C"
elif 60 <= score < 69:
    grade = "D"
else:
    grade = "F"
# TODO: Print the grade for the given score
print(f"Your grade is: {grade}")
#------------------------------------------------------------------------------------
# Question 4: Combining Operators and Conditionals

# TODO: Ask the user to input two numbers and store them in variables 'num1' and 'num2'
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
# TODO: Ask the user to input an operation (+, -, *, /) and store it in a variable called 'operation'
operation = input("Enter an operation (+, -, *, /): ")
# TODO: Use conditional statements to perform the chosen operation on num1 and num2
# TODO: Handle the case of division by zero
result = None

if operation == '+':
 result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 == 0:
     print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
else:
    print("Please enter one of the following: +, -, *, /")

# TODO: Print the result of the operation
if result is not None:
   print(f"The result of {num1} {operation} {num2} is: {result}")