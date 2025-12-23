"""
example_1.py
=========================
This file explains different ways of importing modules
and how namespace conflicts occur.
"""

# ==================================================
# METHOD 1: import module_name
# ==================================================

# import example_2
#
# In this approach:
# - The module name acts as a namespace
# - Attributes do NOT come directly into local scope
#
# Access syntax:
# example_2.x
# example_2.display()

# Example:
# print(example_2.x)
# example_2.display()

# Check local namespace
# print(dir())

"""
Output will include only:
['example_2', '__name__', '__file__', ...]
"""


# ==================================================
# METHOD 2: from module_name import *
# ==================================================

from example_2 import *

# Now attributes come directly into local scope
print(dir())

"""
Because __all__ is defined in example_2.py,
ONLY these names are imported:

['x', 'personal_info', 'display']

private_info is NOT imported
"""

# ==================================================
# USING IMPORTED MEMBERS
# ==================================================

print(x)                 # 100
personal_info()          # This is Personal Info
display()                # Hello

# private_info()         ❌ NameError (not imported)


# ==================================================
# NAME CONFLICT EXAMPLE
# ==================================================

# Suppose we create a variable with same name
x = 1000

print(x)
"""
Output: 1000

Explanation:
- Local variable overrides imported variable
- This is why wildcard imports (*) are risky
"""


# ==================================================
# WHY __all__ IS IMPORTANT
# ==================================================

"""
Without __all__:
- ALL names would be imported
- High risk of name conflicts
- Poor code readability

With __all__:
- Controlled imports
- Cleaner namespace
- Better maintainability
"""
