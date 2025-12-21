# ============================================================
#          SWAPPING OF TWO NUMBERS IN PYTHON
# ============================================================
# Swapping means exchanging the values of two variables.
#
# This file demonstrates FOUR different methods:
# 1️⃣ Using a Temporary Variable
# 2️⃣ Without Temporary Variable (Arithmetic)
# 3️⃣ Using Tuple Unpacking (Pythonic Way)
# 4️⃣ Using XOR Bitwise Operator
# ============================================================


# ============================================================
# METHOD 1: USING A TEMPORARY VARIABLE
# ============================================================
# Concept:
# - Store value of `a` in a temporary variable
# - Assign value of `b` to `a`
# - Assign temporary value to `b`

a = 5
b = 10

print("Before Swapping (Method 1):")
print("a =", a, "| b =", b)

temp = a   # Store original value of a
a = b      # Assign b to a
b = temp   # Assign original a to b

print("After Swapping (Method 1):")
print("a =", a, "| b =", b)


# ============================================================
# METHOD 2: WITHOUT TEMP VARIABLE (ARITHMETIC)
# ============================================================
# Concept:
# - Use addition and subtraction
# - Total is preserved and values are derived back
#
# ⚠ Limitations:
# - May cause overflow in other languages
# - Works only for numeric values

a = 5
b = 10

print("\nBefore Swapping (Method 2):")
print("a =", a, "| b =", b)

a = a + b   # a = 15
b = a - b   # b = 5
a = a - b   # a = 10

print("After Swapping (Method 2):")
print("a =", a, "| b =", b)


# ============================================================
# METHOD 3: USING TUPLE UNPACKING (MOST PYTHONIC)
# ============================================================
# Concept:
# - Python evaluates the RIGHT-HAND SIDE first
# - Creates a temporary tuple internally
# - Unpacks values to left-hand variables
#
# INTERNAL WORKING:
# -----------------
# Step 1: RHS evaluated first
#     (b, a) → (10, 5)
#
# Step 2: Tuple unpacking
#     a = 10
#     b = 5
#
# ✔ No data loss
# ✔ No extra variable
# ✔ Atomic and safe operation

a = 5
b = 10

print("\nBefore Swapping (Method 3):")
print("a =", a, "| b =", b)

# Python internally does:
# temp = (b, a)
# a = temp[0]
# b = temp[1]
a, b = b, a

print("After Swapping (Method 3):")
print("a =", a, "| b =", b)


# ============================================================
# METHOD 4: USING XOR BITWISE OPERATOR
# ============================================================
# Concept:
# XOR (^) property:
#   x ^ x = 0
#   x ^ 0 = x
#
# KEY IDEA:
# - XOR does not require extra memory
# - Bits cancel each other out intelligently
#
# BIT-LEVEL EXAMPLE:
# -----------------
# a = 5  → 0101
# b = 10 → 1010
#
# Step 1: a = a ^ b
#   0101
# ^ 1010
# --------
#   1111  → a = 15
#
# Step 2: b = a ^ b
#   1111
# ^ 1010
# --------
#   0101  → b = 5
#
# Step 3: a = a ^ b
#   1111
# ^ 0101
# --------
#   1010  → a = 10
#
# ✔ Swap achieved without temp variable
# ❌ Less readable
# ❌ Only works for integers

a = 5
b = 10

print("\nBefore Swapping (Method 4):")
print("a =", a, "| b =", b)

a = a ^ b   # Step 1: a holds XOR of a and b
b = a ^ b   # Step 2: b gets original a
a = a ^ b   # Step 3: a gets original b

print("After Swapping (Method 4):")
print("a =", a, "| b =", b)


# ============================================================
# ✅ FINAL COMPARISON SUMMARY (REVISION)
# ============================================================
# Method | Temp Var | Works for | Readability | Recommendation
# ------------------------------------------------------------
# 1️⃣     | Yes      | All types | ⭐⭐⭐⭐⭐      | Beginners
# 2️⃣     | No       | Numbers   | ⭐⭐⭐        | Avoid
# 3️⃣     | No       | All types | ⭐⭐⭐⭐⭐      | ✅ BEST
# 4️⃣     | No       | Integers  | ⭐⭐         | Interviews only
# ============================================================
