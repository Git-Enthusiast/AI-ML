# Inputs in Python
# Taking Input from user in Python
# Syntax: input([prompt])
# Prompt: It's a message, representing a default message
# before input. it is optional.
# Example: input("Please Enter a Number: ")
# Note: By default Input() Function take "Sting" as input
# we have to First TypeCaste it into required data type i.e. int
# Example: 
my_int = input("Please Enter an Integer: ")
print(type(my_int))
print(my_int)
name = input("Enter Your name: ")
print("Your name is ",name)
print(type(name))

# Take Input from user to add two number.
num1 = int(input("Please Enter 1st number: "))
num2 = int(input("Please Enter your 2nd number: "))
sum = num1 + num2
print("The sum of ",num1," and ",num2," is ",sum)
