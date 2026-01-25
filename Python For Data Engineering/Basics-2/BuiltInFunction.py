# ============================================================
# BUILT-IN FUNCTIONS IN PYTHON – QUICK SUMMARY
# ============================================================

# Python provides many built-in functions by default
# These functions are always available (no import needed)
# Examples: len(), print(), type(), abs(), round(), sum(), etc.

# ------------------------------------------------------------
# 1️⃣ Printing ALL built-in names (functions, exceptions, constants)
import builtins
print(dir(builtins))

# Explanation:
# - builtins is a module that contains all built-in objects
# - dir(builtins) returns a list of:
#   • Built-in functions   → len, print, abs, round, type, etc.
#   • Built-in exceptions → TypeError, ValueError, IndexError, etc.
#   • Built-in constants  → True, False, None
#
# NOTE:
# - dir() returns names as strings
# - Output is usually very long


# ------------------------------------------------------------
# 2️⃣ Getting documentation of a built-in function
print(help(len))

# Explanation:
# - help() displays detailed documentation
# - It explains:
#   • What the function does
#   • Its parameters
#   • Return type
#
# Example output summary for len():
# len(object) -> int
# Returns the number of items in an object


# ------------------------------------------------------------
# 3️⃣ Commonly used built-in functions
# len()    → returns number of elements
# type()   → returns data type
# abs()    → absolute value
# round()  → rounding numbers
# sum()    → sum of iterable
# max()    → largest value
# min()    → smallest value
# input()  → take user input
# print()  → display output


# ------------------------------------------------------------
# KEY POINTS
# - Built-in functions are available without importing anything
# - builtins module stores all built-in names
# - dir(builtins) → list all built-in objects
# - help(function) → detailed documentation of that function
#
# ============================================================
