# Problem 001: Multiples of 3 or 5

def sum_of_multiples(limit):
    return sum(i for i in range(limit) if i % 3 == 0 or i % 5 == 0)

print(sum_of_multiples(1000))
