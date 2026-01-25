"""
============================================================
                TYPE CASTING IN PYTHON
============================================================

Type casting means converting one data type into another.

Python supports:
1. Implicit Type Casting  (done automatically by Python)
2. Explicit Type Casting  (done manually by the programmer)
 
"""

# ==========================================================

# 1. WHAT IS TYPE CASTING?
# ==========================================================
"""
Type Casting = Changing the data type of a value

Example:
int  -> float
str  -> int
float -> int
"""

# ==========================================================
# 2. IMPLICIT TYPE CASTING
# ==========================================================
"""
Implicit type casting is done automatically by Python.
Python converts smaller data types into larger data types
to avoid data loss.
"""

# Example 1: int + float
a = 10        # int
b = 2.5       # float
result = a + b

print("Implicit Type Casting Example")
print("a =", a, "type:", type(a))
print("b =", b, "type:", type(b))
print("result =", result, "type:", type(result))
# int is automatically converted to float


# Example 2: int + complex
x = 5         # int
y = 2 + 3j    # complex
z = x + y

print("\nImplicit Casting with Complex")
print("z =", z, "type:", type(z))


"""
IMPORTANT NOTES:
- int -> float -> complex (safe conversion)
- Python NEVER converts complex to int or float implicitly
"""


# ==========================================================
# 3. EXPLICIT TYPE CASTING
# ==========================================================
"""
Explicit type casting is done manually using built-in functions.

Common type casting functions:
int()
float()
str()
bool()
list()
tuple()
set()
"""

# ----------------------------------------------------------
# 3.1 int() TYPE CASTING
# ----------------------------------------------------------

print("\nExplicit Casting using int()")

# float to int (decimal part is removed, NOT rounded)
a = 10.9
b = int(a)
print("a =", a, "->", b)

# string to int (string must contain only digits)
num_str = "123"
num_int = int(num_str)
print("Converted int:", num_int)

# ❌ Invalid conversion (will cause error)
# int("12.5")  -> ValueError
# int("abc")   -> ValueError


# ----------------------------------------------------------
# 3.2 float() TYPE CASTING
# ----------------------------------------------------------

print("\nExplicit Casting using float()")

x = 5
y = float(x)
print("x =", x, "->", y)

num_str = "45.67"
num_float = float(num_str)
print("Converted float:", num_float)

# ❌ Invalid
# float("abc")


# ----------------------------------------------------------
# 3.3 str() TYPE CASTING
# ----------------------------------------------------------

print("\nExplicit Casting using str()")

a = 100
b = str(a)
print("a =", a, "type:", type(a))
print("b =", b, "type:", type(b))

# Useful for concatenation
age = 22
print("My age is " + str(age))


# ----------------------------------------------------------
# 3.4 bool() TYPE CASTING
# ----------------------------------------------------------

print("\nExplicit Casting using bool()")

print(bool(1))        # True
print(bool(0))        # False
print(bool(-5))       # True
print(bool(""))       # False
print(bool("Rajan"))  # True
print(bool(None))     # False

"""
False values in Python:
0, 0.0, "", None, False, [], {}, ()
Everything else is True
"""


# ----------------------------------------------------------
# 3.5 list(), tuple(), set() TYPE CASTING
# ----------------------------------------------------------

print("\nType Casting with Collections")

# string to list
name = "Rajan"
print(list(name))   # ['R', 'a', 'j', 'a', 'n']

# tuple to list
t = (1, 2, 3)
print(list(t))

# list to tuple
l = [4, 5, 6]
print(tuple(l))

# list to set (duplicates removed)
l2 = [1, 2, 2, 3, 3]
print(set(l2))


# ==========================================================
# 4. TYPE CASTING WITH INPUT()
# ==========================================================
"""
By default, input() returns STRING.
So explicit casting is required.
"""

# Example:
a = input("Enter number: ")
print(type(a))  # str

# Correct way:
a = int(input("Enter number: "))
b = int(input("Enter number: "))
print("Sum:", a + b)
print("Enter a number: ")
x = int(input())
print(x)


# ==========================================================
# 5. COMMON ERRORS IN TYPE CASTING
# ==========================================================
"""
1. Converting invalid strings to numbers
   int("abc") ❌
   float("xyz") ❌

2. Forgetting input() returns string
   input() + input()  -> string concatenation

3. Expecting rounding in int()
   int(9.9) -> 9 (not 10)
"""


# ==========================================================
# 6. QUICK REVISION SUMMARY
# ==========================================================
"""
Implicit Casting:
- Automatic
- Safe conversion
- int -> float -> complex

Explicit Casting:
- Manual
- Uses functions like int(), float(), str()

input() always returns string

int() removes decimal part, does NOT round

bool():
- False: 0, "", None, [], {}, ()
- True: everything else
"""

print("\n--- END OF TYPE CASTING REVISION ---")
