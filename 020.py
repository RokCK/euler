# Problem 020: Factorial Digit Sum
from math import factorial

def factorial_digit_sum():
    x = [int(i) for i in str(factorial(100))]
    return sum(x)

print(factorial_digit_sum())
