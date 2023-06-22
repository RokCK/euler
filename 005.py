# Problem 005: Smallest Multiple
import math

def smallest_multiple(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i // math.gcd(result, i)
    return result

print(smallest_multiple(20))
