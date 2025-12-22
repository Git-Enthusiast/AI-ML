import addition as a
import subtraction as s
import multiplication as m
import division as d

def calculator(x, y, operation):
    if operation == 'add':
        return a.add_numbers(x, y)
    elif operation == 'subtract':
        return s.subtract_numbers(x, y)
    elif operation == 'multiply':
        return m.multiply_numbers(x, y)
    elif operation == 'divide':
        return d.divide_numbers(x, y)
    else:
        return "Error: Unsupported operation."

# Example usage:
if __name__ == "__main__":
    num1 = 234
    num2 = 56

    print("Addition:", calculator(num1, num2, 'add'))
    print("Subtraction:", calculator(num1, num2, 'subtract'))
    print("Multiplication:", calculator(num1, num2, 'multiply'))
    print("Division:", calculator(num1, num2, 'divide'))

# This is a simple calculator that performs addition, subtraction, 
# multiplication, and division
# by importing functions from separate modules for each operation.