"""
example_2.py
=========================
This module demonstrates:
1. Module-level variables
2. Functions
3. Use of __all__ to control wildcard imports
"""

# -------------------------
# Module-level variable
# -------------------------
x = 100


# -------------------------
# Public function
# -------------------------
def personal_info():
    """
    Prints personal information message
    """
    print("This is Personal Info")


# -------------------------
# Another function (can be restricted)
# -------------------------
def private_info():
    """
    Prints private information message
    """
    print("This is Private Info")


# -------------------------
# Display function
# -------------------------
def display():
    """
    Prints greeting message
    """
    print("Hello")


# --------------------------------------------------
# __all__ controls what gets imported when using:
# from example_2 import *
# --------------------------------------------------


# -------------------------
# greet function
# -------------------------
def greet():
     print("Hello from example_2!")



__all__ = ["x", "personal_info", "display","greet"]

"""
Meaning:
- Only x, personal_info, and display will be imported
- private_info will NOT be imported using wildcard (*)
"""
