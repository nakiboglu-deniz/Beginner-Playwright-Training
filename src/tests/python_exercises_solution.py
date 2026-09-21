"""
Python Exercises

Complete the TODO sections and run:

pytest test_exercises.py

All tests should pass when your solutions are correct.
"""


# Exercise 1: Prime Number Checker
def is_prime(number):
    """
    Return True if the number is prime, otherwise False.

    Examples:
    is_prime(2) -> True
    is_prime(4) -> False
    """
    if number <= 1:
        return False
    elif number == 2:
        return True
    else:    
        for i in range (2,number):
            if number % i == 0:
                return False
        else:
            return True
    


# Exercise 2: Simple Calculator
def add(a, b):
    """Return the sum of a and b."""
    return a+b
    


def subtract(a, b):
    """Return the result of a - b."""
    return (a-b)
    


def multiply(a, b):
    """Return the result of a * b."""
    return a*b
    


def divide(a, b):
    """
    Return the result of a / b.
    
    Raise ValueError if b is 0.
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    else:
        return a / b
    


# Exercise 3: Even Numbers Loop
def get_even_numbers():
    """
    Return a list containing all even numbers from 1 to 100.

    Example:
    [2, 4, 6, ..., 100]
    """
    start_number = 1
    end_number = 100
    even_numbers = []
    for i in range (start_number, end_number+1):
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers
    


# Exercise 4 (Bonus): List Comprehension
def get_even_numbers_comprehension():
    """
    Return a list containing all even numbers from 1 to 100.

    Use a list comprehension.
    """
    start = 1
    end = 100
    even_numbers = [number for number in range(start,end+1) if number % 2 ==0]
    return even_numbers
    