# Part 2: Multiplication and Division
# Asking the user to input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Multiplication
multiplication_result = num1 * num2

# Division
# Handling division by zero
if num2 != 0:
    division_result = num1 / num2
else:
    division_result = "undefined (division by zero is not allowed)"

# Displaying the results
print(f"The multiplication of {num1} and {num2} is: {multiplication_result}")
print(f"The division of {num1} by {num2} is: {division_result}")