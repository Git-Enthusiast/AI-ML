# ternary_operator_example.py
"""
This Python script explains the ternary operator (conditional expression) 
with examples. The ternary operator is a one-line if-else expression used 
to assign a value based on a condition.
"""

# Syntax of ternary operator:
# value_if_true if condition else value_if_false

# Example 1: Basic usage
age = 18

# Assign a message based on age
message = "Eligible to vote" if age >= 18 else "Not eligible to vote"

print("Example 1:")
print(f"Age: {age} -> {message}")
print("-" * 40)

# Example 2: Ternary operator with arithmetic
num = 10

# Check if the number is even or odd
result = "Even" if num % 2 == 0 else "Odd"

print("Example 2:")
print(f"Number: {num} -> {result}")
print("-" * 40)

# Example 3: Nested ternary operator
marks = 75

# Determine grade using nested ternary operator
grade = "A" if marks >= 80 else ("B" if marks >= 60 else "C")

print("Example 3:")
print(f"Marks: {marks} -> Grade: {grade}")
print("-" * 40)

# Example 4: Ternary operator with function calls
def greet_morning():
    return "Good morning!"

def greet_evening():
    return "Good evening!"

hour = 15
greeting = greet_morning() if hour < 12 else greet_evening()

print("Example 4:")
print(f"Hour: {hour} -> {greeting}")
print("-" * 40)

# Example 5: Ternary operator in list comprehension
numbers = [1, 2, 3, 4, 5]
# Label numbers as 'Even' or 'Odd'
labels = ["Even" if n % 2 == 0 else "Odd" for n in numbers]

print("Example 5:")
print(f"Numbers: {numbers} -> Labels: {labels}")
print("-" * 40)

# Example 6: Ternary operator for inline assignment
temperature = 30
weather = "Hot" if temperature > 25 else "Cool"

print("Example 6:")
print(f"Temperature: {temperature}°C -> Weather: {weather}")
print("-" * 40)

"""
Summary:
- The ternary operator is a compact alternative to the regular if-else statement.
- Syntax: value_if_true if condition else value_if_false
- Can be used in variable assignment, function calls, list comprehensions, etc.
- Nested ternary operators are possible but should be used carefully for readability.
"""
