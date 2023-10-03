#!/usr/bin/env python3

def greet_programmer():
    # Output the string "Hello, programmer!" to the terminal
    print("Hello, programmer!")


def greet(name):
    # Output the string "Hello, name!" to the terminal, where 'name' is replaced by the argument value
    print(f"Hello, {name}!")


def greet_with_default(name="programmer"):
    # Output the string "Hello, name!" to the terminal, using the provided 'name' or defaulting to "programmer" if no argument is provided
    print(f"Hello, {name}!")


def add(num1, num2):
    # Return the sum of 'num1' and 'num2'
    return num1 + num2


def halve(number):
    # Return 'number' divided by 2
    return number / 2
