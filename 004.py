# Problem 4
def largest_palindrome_product():
    max_product = 0
    for i in range(999, 99, -1):
        for j in range(i, 99, -1):
            product = i * j
            if str(product) == str(product)[::-1] and product > max_product:
                max_product = product
    return max_product
print(largest_palindrome_product())
