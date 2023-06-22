# Problem 007: 10001st Prime
import math

def nth_prime(n):
    upper_limit = int(n * (math.log(n) + math.log(math.log(n)))) + 1
    sieve = [True] * upper_limit
    sieve[0] = sieve[1] = False
    for i, is_prime in enumerate(sieve):
        if is_prime:
            for j in range(i*i, upper_limit, i):
                sieve[j] = False
    primes = [x for x in range(2, upper_limit) if sieve[x]]
    return primes[n-1]

print(nth_prime(10001))
