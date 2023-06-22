# Problem 014: Longest Collatz Sequence

def collatz(n):
    while n != 1:
        yield n
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    yield 1
longest_chain = (0, 0)
for i in range(1, 1000000):
    length = len(list(collatz(i)))
    if length > longest_chain[1]:
        longest_chain = (i, length)

print(longest_chain[0])
