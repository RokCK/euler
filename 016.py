# Problem 16
import math

def power_digit_sum():
    x = [int(i) for i in str(2 ** 1000)]
    return sum(x)

print(power_digit_sum())
