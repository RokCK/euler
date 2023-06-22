# Problem 009: Special Pythagorean Triplet

def pythagorean_triplet(n):
    for a in range(1, n):
        for b in range(a, n):
            c = n - a - b
            if a * a + b * b == c * c:
                return a * b * c
    return -1

print(pythagorean_triplet(1000))
