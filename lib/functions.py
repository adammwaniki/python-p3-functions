#!/usr/bin/env python3
# function to print a string with no parameters or arguments
def greet_programmer():
    return "Hello, programmer!"

print(greet_programmer())

# Function to print a string with one parameter and argument
def greet(name):
    return f"Hello, {name}!"
 
print(greet("Naureen"))

# Function to print a string with a parameter that has a default value
def greet_with_default(name="programmer"):
    return f"Hello, {name}"

print(greet_with_default('Sunny'))

# Function to print the sum of two parameters
def add(num1, num2):
    return num1 + num2
print(add(num1=1, num2=2))

# Function to print the halving of a given number
# This function will reject non-numeric values
def halve(number):
    return float(number)/2
print(halve(4))