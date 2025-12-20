# ============================================================
#               PYTHON LOGICAL OPERATORS
# ============================================================
# Revision Notes + Coding Reference
#
# Logical operators are used to combine or modify
# relational / conditional expressions.
#
# They always return a BOOLEAN value:
#   → True
#   → False
#
# ------------------------------------------------------------
# Logical Operators in Python:
# ------------------------------------------------------------
# 1️⃣ and
# 2️⃣ or
# 3️⃣ not
#
# ------------------------------------------------------------
# Uses of Logical Operators:
# ------------------------------------------------------------
# ✔ Decision making (if / elif / else)
# ✔ Controlling the flow of a program
# ✔ Validating multiple conditions
# ============================================================


# ============================================================
# 1️⃣ AND OPERATOR
# ============================================================
# The 'and' operator returns True ONLY IF
# **both conditions are True**
#
# Syntax:
# condition1 and condition2
#
# Truth Table:
# True  and True  → True
# True  and False → False
# False and True  → False
# False and False → False
# ============================================================

print("\n--- AND OPERATOR EXAMPLE ---")

print("Please enter Yes or No when asked")

# Taking user inputs
knowledge = input("Do you have knowledge of Python? ").lower()
passout_year = int(input("Enter your passout year: "))

# Both conditions must be True
if knowledge == "yes" and passout_year >= 2022:
    print("You are eligible for the AICTE WBL.")
else:
    print("You are NOT eligible for the AICTE WBL.")


# ============================================================
# 2️⃣ OR OPERATOR
# ============================================================
# The 'or' operator returns True if
# **at least one condition is True**
#
# Syntax:
# condition1 or condition2
#
# Truth Table:
# True  or True  → True
# True  or False → True
# False or True  → True
# False or False → False
# ============================================================

print("\n--- OR OPERATOR EXAMPLE ---")

print("Please enter Yes or No when asked")

# Taking user inputs again
knowledge = input("Do you have knowledge of Python? ").lower()
passout_year = int(input("Enter your passout year: "))

# At least one condition should be True
if knowledge == "yes" or passout_year >= 2022:
    print("You are eligible for the AICTE WBL.")
else:
    print("You are NOT eligible for the AICTE WBL.")


# ============================================================
# 3️⃣ NOT OPERATOR
# ============================================================
# The 'not' operator reverses the result of a condition
#
# Syntax:
# not condition
#
# Truth Table:
# not True  → False
# not False → True
# ============================================================

print("\n--- NOT OPERATOR EXAMPLE ---")

print("Please enter Yes or No when asked")

# Taking user inputs again
knowledge = input("Do you have knowledge of Python? ").lower()
passout_year = int(input("Enter your passout year: "))

# NOT reverses the result of the combined condition
if not (knowledge == "yes" and passout_year >= 2022):
    print("You are eligible for the AICTE WBL.")
else:
    print("You are NOT eligible for the AICTE WBL.")


# ============================================================
# SHORT-CIRCUIT BEHAVIOR OF LOGICAL OPERATORS
# ============================================================
# Logical operators do NOT always return True or False.
# They return the LAST evaluated value.
#
# Rules:
# ------------------------------------------------------------
# True  and expression → expression
# False and expression → False
# True  or  expression → True
# False or  expression → expression
# ============================================================

print("\n--- LOGICAL OPERATOR BEHAVIOR ---")

a = 10
b = 5

# AND operator examples
print(True and a > b)     # True (both conditions are True)
print(False and a > b)    # False (False stops evaluation)

# OR operator examples
print(True or a < b)      # True (True stops evaluation)
print(False or a < b)     # False (expression evaluated)

# NOT operator examples
print(not True)           # False
print(not False)          # True


# ============================================================
# LOGICAL OPERATORS WITH NON-BOOLEAN VALUES
# ============================================================
# Python treats certain values as True or False
#
# Truthy values:
# ✔ Non-zero numbers
# ✔ Non-empty strings
#
# Falsy values:
# ❌ 0
# ❌ None
# ❌ Empty string ""
# ❌ Empty collections: (), [], {}
# ============================================================

print("\n--- NON-BOOLEAN VALUE BEHAVIOR ---")

print(True and 100)           # 100
print(True and "Rajan")       # "Rajan"
print("Rajan" and True)       # True

print(not 100)                # False (100 is truthy)
print(not "")                 # True (empty string is falsy)

print("" or "Hello")          # "Hello"
print(0 or 42)                # 42
print(0 and 42)               # 0


# ============================================================
# ✅ KEY TAKEAWAYS (REVISION POINTS)
# ============================================================
# ✔ 'and' → all conditions must be True
# ✔ 'or'  → at least one condition must be True
# ✔ 'not' → reverses the result
# ✔ Logical operators can return non-boolean values
# ✔ Python uses short-circuit evaluation
# ============================================================
