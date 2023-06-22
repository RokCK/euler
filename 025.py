# Problem 025: 1000-digit Fibonacci Number

def fibonacci_index(digits):
    a, b = 1, 1
    index = 2
    while len(str(b)) < digits:
        a, b = b, a + b
        index += 1
    return index

print(fibonacci_index(1000))
