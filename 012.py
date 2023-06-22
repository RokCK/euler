# Problem 012: Highly Divisible Triangular Number
import math

def triangle_divisors(n):
    factors = 0
    count = 1
    while factors <= n:
        triangle = count * (count + 1) // 2
        factors = divisors(triangle)
        count += 1
    return triangle

def divisors(n):
    factors = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors += 2
            if i * i == n:
                factors -= 1
    return factors

print(triangle_divisors(500))
