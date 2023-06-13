# Problem 2

def sum_of_even_fibonacci(max_value):
    a, b = 0, 1
    s = 0 
    while a <= max_value: 
        if a % 2 == 0:
            s += a
        a, b = b, a + b 
    return s

print(sum_of_even_fibonacci(4000000))
