''''
3.2 Construct and analyze code segments that perform console input  and output operations 
Read input from console
print formatted text using string.format() method
print formatted text  using f-String method
missing ->input and output operations using command-line arguments 
'''

# Using input() to read input from the console
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

# Example with string.format() method
formatted_string_format = "Hello, {}! You are {} years old.".format(user_name, user_age)
print(formatted_string_format)

number = 123.456789
formatted_string_format = "The number is {:.2f}".format(number)
print(formatted_string_format)

# Example with f-string method (available in Python 3.6 and later)
formatted_f_string = f"Hello, {user_name}! You are {user_age} years old."
print(formatted_f_string)

number = 123.456789
formatted_f_string = f"The number is {number:.2f}"
print(formatted_f_string)



## Command line SYS
import sys

# Console Input
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Command-Line Arguments
script_name = sys.argv[0]  # script name
arguments = sys.argv[1:]  # no other arguements 
print(f"Script Name: {script_name}")
print(f"Arguments: {arguments}")

# run the above script from the console using:
#  python script.py argument1 argument2

## Command line ARGPARSE
import argparse

# Command-Line Arguments
parser = argparse.ArgumentParser()
parser.add_argument("--name", help="User's name")
args = parser.parse_args()

# Console Input
if args.name:
    name = args.name
else:
    name = input("Enter your name: ")

# Greeting
print(f"Hello, {name}!")

#run the above script from the console using:
# python script.py --name Jill

