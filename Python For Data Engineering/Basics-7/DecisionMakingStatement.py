"""
====================================================================
                IF–ELSE STATEMENT IN PYTHON 
====================================================================

This file explains:
1. What is if–else
2. Syntax of if, if–else, if–elif–else
3. How conditions are evaluated
4. Truthy & falsy values
5. Multiple real examples with outputs
6. Common mistakes and errors

Python Version: Python 3.x
====================================================================
"""

# ================================================================
# 1. WHAT IS if–else?
# ================================================================

"""
if–else is a DECISION-MAKING statement.

It allows the program to:
- Execute one block if condition is True
- Execute another block if condition is False
"""

# ================================================================
# 2. BASIC if STATEMENT
# ================================================================

x = 10

if x > 5:
    print("x is greater than 5")

# Output:
# x is greater than 5

# Why:
# Condition: x > 5 → 10 > 5 → True
# So, if-block executes


# ================================================================
# 3. if–else STATEMENT
# ================================================================

age = 17

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

# Output:
# Not eligible to vote

# Why:
# age >= 18 → 17 >= 18 → False
# else block executes


# ================================================================
# 4. if–elif–else STATEMENT
# ================================================================

marks = 72

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")

# Output:
# Grade C

# Why:
# marks >= 90 → False
# marks >= 75 → False
# marks >= 60 → True
# First True block executes, rest skipped


# ================================================================
# 5. MULTIPLE CONDITIONS USING LOGICAL OPERATORS
# ================================================================

salary = 50000
experience = 3

if salary >= 40000 and experience >= 2:
    print("Eligible for job")
else:
    print("Not eligible")

# Output:
# Eligible for job

# Why:
# salary >= 40000 → True
# experience >= 2 → True
# True and True → True


# ================================================================
# 6. NESTED if–else
# ================================================================

num = 5

if num > 0:
    if num % 2 == 0:
        print("Positive Even Number")
    else:
        print("Positive Odd Number")
else:
    print("Negative Number")

# Output:
# Positive Odd Number

# Why:
# num > 0 → True
# num % 2 == 0 → 5 % 2 = 1 → False
# else of inner if executes


# ================================================================
# 7. if WITH TRUTHY & FALSY VALUES
# ================================================================

value = 0

if value:
    print("Truthy value")
else:
    print("Falsy value")

# Output:
# Falsy value

# Why:
# 0 is a falsy value in Python


text = "Hello"

if text:
    print("Non-empty string is truthy")
else:
    print("Empty string")

# Output:
# Non-empty string is truthy

# Why:
# Non-empty strings are truthy


# ================================================================
# 8. SHORT-HAND if (TERNARY OPERATOR)
# ================================================================

a = 10
b = 20

result = "a is greater" if a > b else "b is greater"
print(result)

# Output:
# b is greater

# Why:
# a > b → 10 > 20 → False
# else part is chosen


# ================================================================
# 9. COMMON MISTAKES & ERRORS
# ================================================================

# ❌ Example 1: Missing colon
# if x > 5
#     print("Hello")

"""
Error:
SyntaxError: expected ':'

Why:
- if condition must end with colon
"""


# ❌ Example 2: Indentation error
# if x > 5:
# print("Hello")

"""
Error:
IndentationError: expected an indented block

Why:
- Code inside if must be indented
"""


# ❌ Example 3: Using = instead of ==
# if x = 5:
#     print("Hello")

"""
Error:
SyntaxError: invalid syntax

Why:
- = is assignment
- == is comparison
"""


# ================================================================
# 10. REAL-WORLD EXAMPLE
# ================================================================

username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid credentials")

# Output:
# Login successful

# Why:
# Both conditions are True


# ================================================================
# 11. IMPORTANT POINTS (EXAM / INTERVIEW)
# ================================================================

"""
1. if condition must be boolean or truthy/falsy
2. Indentation is mandatory
3. elif can be used multiple times
4. else is optional
5. Only ONE block executes in if–elif–else chain
"""

print("\n========== END OF IF–ELSE REVISION ==========")
    