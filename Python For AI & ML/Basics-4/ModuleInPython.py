# What is Module in Python?
# A module in Python is a file containing Python code 
# that defines functions, classes, and variables
# which can be reused in other Python programs.
# Modules help organize code into manageable sections,
# promote code reuse, and improve maintainability.
# Creating a Module:
# To create a module, simply save your Python code in a file
# with a .py extension. The filename becomes the module name.
# Example: Create a file named my_module.py with the following content:
# ------------------------------------------------------------
# my_module.py
#   def greet(name):
#       return f"Hello, {name}!"
# ------------------------------------------------------------
# Using a Module:
# You can use a module in another Python program by importing it.
# Example: Import and use the my_module module.
# ------------------------------------------------------------
# main.py
import my_module
message = my_module.greet("Alice")
print(message)  # Output: Hello, Alice
# ------------------------------------------------------------
# Built-in Modules:
# Python comes with a standard library of built-in modules
# that provide various functionalities, such as math, os, sys, etc.
# You can import and use these modules in your programs.
# Example: Using the math module to calculate the square root.
import math
result = math.sqrt(16)
print("Square root of 16 is:", result)  # Output: Square root of 16 is: 4.0
# Summary:
# - A module is a file containing Python code that can be reused.
# - Create a module by saving code in a .py file.
# - Use the import statement to use a module in another program.
# - Python has many built-in modules for various tasks.
