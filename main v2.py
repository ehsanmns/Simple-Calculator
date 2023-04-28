"""
Title: Simple Calculator
Author: Ehsan Mansouri
Date: April 28, 2023
Description: A basic calculator that performs addition, subtraction, multiplication, and division.
"""

def add(num1, num2):
    """Adds two numbers"""
    return num1 + num2

def subtract(num1, num2):
    """Subtracts two numbers"""
    return num1 - num2

def multiply(num1, num2):
    """Multiplies two numbers"""
    return num1 * num2

def divide(num1, num2):
    """Divides two numbers"""
    if num2 == 0:
        raise ValueError("Cannot divide by zero")
    return num1 / num2

# Main program
if __name__ == "__main__":
    print("Welcome to the Simple Calculator")
    print("--------------------------------")

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print(f"\n{num1} + {num2} = {add(num1, num2)}")
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
    print(f"{num1} x {num2} = {multiply(num1, num2)}")
    print(f"{num1} / {num2} = {divide(num1, num2)}")