# ============================================================
# Python `dir()` Function: Detailed Revision Guide
# ============================================================

# The `dir()` function is a built-in Python function used to:
# 1. List all names (variables, functions, classes, etc.) in the current local scope.
# 2. List all attributes and methods of an object or module.
# ------------------------------------------------------------

# -------------------------
# 1. Using dir() in Local Scope
# -------------------------
print("=== Example 1: dir() in current scope ===")
# In the current scope, dir() lists all variables, functions, classes defined so far
print(dir())  
# Output: ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']

# Adding a variable and checking dir() again
x = 10
y = 20
def my_function():
    pass

print(dir())  
# Output will now include 'x', 'y', 'my_function'

# -------------------------
# 2. Using dir() inside a Function
# -------------------------
def demo():
    name = "Rajan"
    print("Inside function, dir():", dir())
    # Only names defined inside this function are shown
    # Output: ['name']

demo()

# -------------------------
# 3. Using dir() on Modules
# -------------------------
import math

print("=== Example 2: dir() on math module ===")
print(dir(math))
# This prints all attributes and methods of the math module, such as:
# 'sin', 'cos', 'pi', 'e', 'sqrt', etc.

# Another example with custom module:
# Suppose you have example_2.py with functions and classes
# import example_2
# import importlib
# importlib.reload(example_2)  # Reloads the module if updated

# -------------------------
# 4. Using dir() on Built-in Data Types
# -------------------------

# --- String ---
my_string = "Hello, World!"
print("\nAttributes & methods of string:", dir(my_string))
# Useful methods include: 'capitalize', 'count', 'find', 'replace', 'upper', 'lower', etc.

# --- List ---
my_list = [1, 2, 3, 4, 5]
print("\nAttributes & methods of list:", dir(my_list))
# Useful methods include: 'append', 'extend', 'insert', 'pop', 'remove', 'sort', 'reverse'

# --- Dictionary ---
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("\nAttributes & methods of dict:", dir(my_dict))
# Useful methods include: 'keys', 'values', 'items', 'get', 'update', 'pop', 'clear'

# --- Set ---
my_set = {1, 2, 3, 4, 5}
print("\nAttributes & methods of set:", dir(my_set))
# Useful methods include: 'add', 'remove', 'union', 'intersection', 'difference', 'update'

# -------------------------
# 5. Checking the Type of Object
# -------------------------
print("\n=== Example 3: Checking Type ===")
print(type(my_string))  # <class 'str'>
print(type(my_list))    # <class 'list'>
print(type(my_dict))    # <class 'dict'>
print(type(my_set))     # <class 'set'>

# -------------------------
# 6. Listing All Installed Modules
# -------------------------
print("\n=== Example 4: List all accessible modules ===")
# Prints all modules accessible in your Python environment
# This can be a long list
# Uncomment below line if needed
# print(help("modules"))

# -------------------------
# 7. Reloading a Module
# ============================================================
# Python Module Reloading: Detailed Revision Guide
# ============================================================

# In Python, when we import a module using `import module_name`, Python loads it **only once**.
# This means that even if we write the same `import` statement multiple times in a file,
# the module will not be reloaded. Python optimizes imports to avoid unnecessary loading.

# Example:
# Suppose we have a module named "example_2.py" with a simple function
# example_2.py:
# def greet():
#     print("Hello from example_2!")

# In another Python file, we import it:
# import example_2
# example_2.greet()   # Output: Hello from example_2!
# import example_2    # This will NOT reload the module
# example_2.greet()   # Output: Hello from example_2!

# ------------------------------------------------------------
# Problem:
# If we edit example_2.py after importing it (e.g., change the function to print
# "Hello again!"), Python will **not** pick up the changes automatically if we just
# run `import example_2` again. It still uses the version that was loaded first.

# ------------------------------------------------------------
# Solution: Use `importlib.reload()`
# Python provides the `importlib` module to reload a module at runtime.

import importlib
# Syntax:
# importlib.reload(module_object)

# Steps to reload a module:
# 1. Import the module normally.
# 2. Make changes in the module (edit the code).
# 3. Use importlib.reload(module_object) to reload the updated module.

# Example:
# Step 1: Import the module
# import example_2
# example_2.greet()   # Output: Hello from example_2!

# Step 2: Edit example_2.py (change function to print "Hello again!")

# Step 3: Reload the module
# importlib.reload(example_2)
# example_2.greet()   # Output: Hello again!

# Important Notes:
# 1. You must pass the **module object**, not the module name as a string, to reload().
#    Correct: importlib.reload(example_2)
#    Incorrect: importlib.reload("example_2")   # Will raise an error

# 2. Reloading is useful during development when you are frequently editing modules
#    and want the changes to reflect immediately without restarting Python.

# 3. Reloading does NOT reset variables in your current script that reference old objects
#    from the module. Only the module itself is reloaded.

# Example with custom module (simulated):
# Suppose we have another module called "math_utils.py" with a function
# def add(a, b):
#     return a + b

# In main.py:
# import math_utils
# print(math_utils.add(2, 3))  # Output: 5
# # Edit math_utils.py to add a print statement inside add() function
# importlib.reload(math_utils)
# print(math_utils.add(2, 3))  # Output: will show the updated print statement + 5

# ------------------------------------------------------------
# Key Summary Points:
# 1. Normal imports load modules **once** per session.
# 2. Use `importlib.reload(module_object)` to reload a module after editing.
# 3. Reload only affects the module itself, not variables already referencing objects.
# 4. Reloading is mainly for **development/debugging purposes**.
# 5. Always import `importlib` first before using reload.

# ------------------------------------------------------------
# Bonus Tip:
# To see all currently loaded modules in Python, you can use:
# import sys
# print(sys.modules)  # This shows a dictionary of all loaded modules
# The keys are module names, and the values are the module objects themselves.

# ------------------------------------------------------------
# Complete small working example:
# Suppose example_2.py exists in the same folder:
# example_2.py:
# def greet():
#     print("Hello from example_2!")

import example_2  # Step 1: Import
example_2.greet()  # Step 2: Call function, Output: Hello from example_2!

# Step 3: Reload after editing example_2.py
importlib.reload(example_2)
example_2.greet()  # Output: Updated function after editing module



# -------------------------
# 8. Summary Notes for Revision
# -------------------------
# 1. dir(): Returns names in current scope or attributes of object.
# 2. Useful inside functions to see local variables.
# 3. Can inspect modules and objects like str, list, dict, set.
# 4. Reload module using importlib if updated.
# 5. Use help("modules") to explore installed modules.

# -------------------------
# 9. Bonus: dir() on Custom Class
# -------------------------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hello, {self.name}!"

person = Person("Rajan", 25)
print("\nAttributes & methods of Person instance:", dir(person))
# Shows '__init__', 'greet', '__str__', '__class__', '__dict__', etc.
