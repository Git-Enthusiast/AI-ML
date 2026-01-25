"""
===========================================================
PYTHON OPERATORS & TYPE BEHAVIOR — DETAILED REVISION FILE
===========================================================


Python Version: Python 3.14.2
===========================================================
"""

# =========================================================
# 1. ARITHMETIC OPERATORS
# =========================================================

# -------------------------
# ADDITION (+)
# -------------------------

print(5 + 3)
# Answer: 8
# Why:
# Both operands are integers
# Python performs integer addition
# Result remains int

print(type(5 + 3))
# Answer: <class 'int'>
# Why:
# int + int → int


print(5 + 3.0)
# Answer: 8.0
# Why:
# One operand is float
# Python performs implicit type conversion (int → float)
# Calculation becomes 5.0 + 3.0

print(type(5 + 3.0))
# Answer: <class 'float'>


# -------------------------
# SUBTRACTION (-)
# -------------------------

print(5 - 3)
# Answer: 2
# Why:
# int - int → integer subtraction

print(type(5 - 3))
# Answer: <class 'int'>


print(5 - 3.0)
# Answer: 2.0
# Why:
# int is converted to float
# Result becomes float

print(type(5 - 3.0))
# Answer: <class 'float'>


# -------------------------
# MULTIPLICATION (*)
# -------------------------

print(5 * 3)
# Answer: 15
# Why:
# int * int → int

print(type(5 * 3))
# Answer: <class 'int'>


print(5 * 3.0)
# Answer: 15.0
# Why:
# float involved → result is float

print(type(5 * 3.0))
# Answer: <class 'float'>


print("Hi" * 3)
# Answer: HiHiHi
# Why:
# String repetition using multiplication operator
# String is repeated integer times


# -------------------------
# TRUE DIVISION (/)
# -------------------------

print(36 / 4)
# Answer: 9.0
# Why:
# In Python 3, / is TRUE DIVISION
# True division ALWAYS returns float
# Internally: 36 → 36.0, 4 → 4.0

print(type(36 / 4))
# Answer: <class 'float'>


print(5 / 2)
# Answer: 2.5
# Why:
# True division keeps decimal precision

print(type(5 / 2))
# Answer: <class 'float'>


# -------------------------
# FLOOR DIVISION (//)
# -------------------------

print(36 // 4)
# Answer: 9
# Why:
# Floor division returns quotient without decimal
# Both operands are int → result is int

print(type(36 // 4))
# Answer: <class 'int'>


print(5 // 2)
# Answer: 2
# Why:
# Floor division → floor of 2.5 is 2

print(type(5 // 2))
# Answer: <class 'int'>


print(9 // 2.0)
# Answer: 4.0
# Why:
# One operand is float
# Result type becomes float even with //

print(type(9 // 2.0))
# Answer: <class 'float'>


# -------------------------
# MODULUS (%)
# -------------------------

print(9 % 2)
# Answer: 1
# Why:
# Remainder when 9 is divided by 2

print(type(9 % 2))
# Answer: <class 'int'>


print(9 % 2.0)
# Answer: 1.0
# Why:
# float involved → result is float

print(type(9 % 2.0))
# Answer: <class 'float'>


# -------------------------
# EXPONENTIATION (**)
# -------------------------

print(2 ** 3)
# Answer: 8
# Why:
# 2 raised to the power 3

print(type(2 ** 3))
# Answer: <class 'int'>


print(9 ** 0.5)
# Answer: 3.0
# Why:
# Square root of 9
# Power is float → result is float

print(type(9 ** 0.5))
# Answer: <class 'float'>


# =========================================================
# 2. LOGICAL OPERATORS (and / or)
# =========================================================

"""
Logical operators return one of the operands,
NOT True or False.
"""

print(100 and 49)
# Answer: 49
# Why:
# 'and' returns last operand if all are truthy
# 100 is truthy → returns 49

print(type(100 and 49))
# Answer: <class 'int'>


print(19.3 and 23.3)
# Answer: 23.3
# Why:
# Both values are non-zero → truthy
# 'and' returns the second operand

print(type(19.3 and 23.3))
# Answer: <class 'float'>


print(0 and 50)
# Answer: 0
# Why:
# 'and' stops at first falsy value
# 0 is falsy → returned immediately


print(100 or 49)
# Answer: 100
# Why:
# 'or' returns first truthy value

print(0 or 49)
# Answer: 49
# Why:
# 0 is falsy → returns next operand


print(0.0 or 23.3)
# Answer: 23.3
# Why:
# 0.0 is falsy → 'or' returns next truthy value


# =========================================================
# 3. COMPARISON OPERATORS
# =========================================================

print(5 > 3)
# Answer: True
# Why:
# 5 is greater than 3

print(type(5 > 3))
# Answer: <class 'bool'>


print(5 == 5)
# Answer: True
# Why:
# Both values are equal

print(5 != 3)
# Answer: True
# Why:
# Values are not equal


# =========================================================
# 4. BITWISE OPERATORS
# =========================================================

print(23 ^ 23)
# Answer: 0
# Why:
# XOR returns 1 only if bits are different
# 23 ^ 23 → all bits same → result 0

# Binary:
# 23 → 10111
# 23 → 10111
# XOR → 00000


# -------------------------
# BITWISE WITH FLOAT (ERROR)
# -------------------------

# print(23.3 ^ 23.3)
# ❌ TypeError
# Why:
# Bitwise operators work ONLY with integers
# Floats are not allowed


# =========================================================
# 5. COMMON CONFUSION
# =========================================================

print(23.3 ** 2)
# Answer: 542.89
# Why:
# ** is exponentiation
# Correct way to calculate power

# print(23.3 ^ 2)
# ❌ WRONG
# Why:
# ^ is bitwise XOR, not power


"""
==================== SUMMARY ====================

1. /  → always returns float
2. // → returns int only if both operands are int
3. If any operand is float → result is float
4. and → returns last truthy or first falsy
5. or  → returns first truthy
6. ^   → bitwise XOR (int only)
7. **  → exponentiation

=================================================
"""
