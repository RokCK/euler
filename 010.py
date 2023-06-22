# Problem 010: Summation of Primes

def sum_of_primes(n):
    sieve = [True] * n
    sieve[0] = sieve[1] = False
    for i, is_prime in enumerate(sieve):
        if is_prime:
            for j in range(i*i, n, i):
                sieve[j] = False
    primes = [x for x in range(2, n) if sieve[x]]
    return sum(primes)

print(sum_of_primes(2000000))
