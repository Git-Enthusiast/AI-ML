# ============================================================
# VARIABLES AND THEIR TYPES
# ============================================================

name           = "Rajan"
age            = 22
is_student     = True
height         = 5.8
siblings       = ("Ansiha", "Nigam", "Sonam", "Ravi")
personal_info  = {
    "name": "rajan",
    "mobile_no": 9608757113
}

# Checking types
print(type(name))          # <class 'str'>
print(type(age))           # <class 'int'>
print(type(is_student))    # <class 'bool'>
print(type(height))        # <class 'float'>
print(type(siblings))      # <class 'tuple'>
print(type(personal_info)) # <class 'dict'>


# ============================================================
# FUNCTION TYPES AND RETURN VALUES
# ============================================================

# Function with return
def sample_function():
    return "This is a sample function."

# Function without return (only prints)
def print_function():
    print("This is a print function. It does not return any value.")

# Checking return types
print(type(sample_function()))   # <class 'str'>
print(type(print_function()))    # <class 'NoneType'>


# ------------------------------------------------------------
# FUNCTION RETURN TYPE – QUICK SUMMARY
# ------------------------------------------------------------

def example():
    return 10

# 1️⃣ Function reference (without ())
print(type(example))        # <class 'function'>

# 2️⃣ Function execution (with ())
print(type(example()))      # <class 'int'>

# 3️⃣ Function without return → returns None
def print_func():
    print("Hello")

print(type(print_func()))   # <class 'NoneType'>

# 4️⃣ Best practice: Use type annotations
def sample_function_annotated() -> str:
    return "Hello"

def no_return_function() -> None:
    print("No return value")

# Checking declared return type without execution
print(sample_function_annotated.__annotations__)  # {'return': <class 'str'>}
print(no_return_function.__annotations__)         # {'return': None}


# ============================================================
# id() FUNCTION IN PYTHON – QUICK SUMMARY
# ============================================================

# id() returns the unique identity of an object in memory

# 1️⃣ Basic example
a = 10
b = 10
print(id(a))  # Same id for small integers
print(id(b))

# 2️⃣ Different objects → different id
x = [1, 2, 3]
y = [1, 2, 3]
print(id(x))  # Different id
print(id(y))

# 3️⃣ Mutable object behavior (id does NOT change on modification)
lst = [1, 2]
print(lst, id(lst))
lst.append(3)
print(lst, id(lst))  # Same id

# 4️⃣ Immutable object behavior (id CHANGES on modification)
num = 5
print(id(num))
num += 1
print(id(num))  # Different id

# 5️⃣ id() with functions
def another_function():
    return "Hello"

print(id(another_function))     # Function object id
print(id(another_function()))   # Return value id

# 6️⃣ id() vs == 
a = [1, 2]
b = [1, 2]
print(a == b)          # True → same values
print(id(a) == id(b))  # False → different objects

# ------------------------------------------------------------
# KEY POINTS
# - id() gives unique identity of an object
# - Same object → same id
# - Mutable objects keep same id when changed
# - Immutable objects get new id when changed
# - id() is often used for debugging and memory behavior analysis
# ============================================================

# bin() function in Python – Quick Summary

# bin() converts an integer to its binary string representation
# 1️⃣ Basic usage
num = 10
binary_representation = bin(num)
print(f"Binary representation of {num} is {binary_representation}")  # Output: 0b1010
# 2️⃣ Negative numbers
neg_num = -10
neg_binary = bin(neg_num)
print(f"Binary representation of {neg_num} is {neg_binary}")  # Output: -0b1010
# 3️⃣ Using bin() in expressions
a = 5
b = 3
sum_binary = bin(a + b)
print(f"Binary representation of {a} + {b} is {sum_binary}")  # Output: 0b1000
# 4️⃣ Converting back to integer
binary_str = '0b1010'
integer_value = int(binary_str, 2)
print(f"Integer value of {binary_str} is {integer_value}")  # Output: 10
# 5️⃣ Key points
# - bin() converts integers to binary strings prefixed with '0b'
# - Works with both positive and negative integers
# - Input must be an integer only else raises TypeError
# - Can be used in expressions and combined with int() for conversions back to integers
# ============================================================


# pow() function in Python – Quick Summary
# pow() raises a number to the power of an exponent
# 1️⃣ Basic usage
base = 2
exponent = 3
result = pow(base, exponent)
print(f"{base} raised to the power of {exponent} is {result}")  # Output: 8
# 2️⃣ Using pow() with three arguments (modulus)
modulus = 3
mod_result = pow(base, exponent, modulus)
print(f"{base} raised to the power of {exponent} modulo {modulus} is {mod_result}")  # Output: 2






# ============================================================
# round() FUNCTION IN PYTHON – QUICK SUMMARY
# ============================================================

# round() is used to round a floating-point number
# It can round to:
# - Nearest integer (default)
# - Specified number of decimal places

# ------------------------------------------------------------
# 1️⃣ Basic usage: Rounding to given decimal places
num = 5.6789
rounded_num = round(num, 2)
print(rounded_num)   # Output: 5.68

# Explanation:
# num = 5.6789
# Rounded to 2 decimal places → 5.68


# ------------------------------------------------------------
# 2️⃣ Rounding to nearest integer (one argument)
rounded_int = round(num)
print(rounded_int)   # Output: 6

# Explanation:
# Decimal part >= 0.5 → rounded up
# Decimal part < 0.5  → rounded down


# ------------------------------------------------------------
# 3️⃣ Rounding negative numbers
neg_num = -2.3456
rounded_neg = round(neg_num, 2)
print(rounded_neg)   # Output: -2.35

# Explanation:
# round() works for both positive and negative numbers


# ------------------------------------------------------------
# 4️⃣ IMPORTANT RULES
# - round() accepts ONLY one or two arguments
#   round(number)
#   round(number, ndigits)
#
# - round(number) → returns nearest integer
# - round(number, ndigits) → rounds to ndigits decimal places
#
# - round() uses "banker's rounding"
#   (rounds to nearest even number in .5 cases)
#
# - Returns:
#   int   → if ndigits is not provided
#   float → if ndigits is provided
#
# ============================================================






# ============================================================
# abs() FUNCTION IN PYTHON – QUICK SUMMARY
# ============================================================

# abs() returns the absolute (non-negative) value of a number
# Absolute value = distance from zero (sign is removed)

# ------------------------------------------------------------
# 1️⃣ Basic usage with integers
num = -10
absolute_value = abs(num)
print(absolute_value)   # Output: 10

# Explanation:
# -10 → 10 (negative sign is removed)


# ------------------------------------------------------------
# 2️⃣ Works with floating-point numbers
float_num = -5.67
absolute_float = abs(float_num)
print(absolute_float)   # Output: 5.67

# Explanation:
# abs() preserves decimal value but removes sign


# ------------------------------------------------------------
# 3️⃣ Works with complex numbers
complex_num = 3 - 4j
absolute_complex = abs(complex_num)
print(absolute_complex)   # Output: 5.0

# Explanation:
# For complex numbers:
# abs(a + bj) = sqrt(a² + b²)
# Here: sqrt(3² + (-4)²) = sqrt(9 + 16) = 5.0


# ------------------------------------------------------------
# 4️⃣ IMPORTANT RULES
# - abs() works with:
#   int, float, complex
#
# - Always returns a NON-NEGATIVE value
#
# - Return types:
#   int     → for int input
#   float   → for float input
#   float   → for complex input
#
# - Raises TypeError if input is non-numeric
#   Example: abs("hello") → TypeError
#
# ============================================================




