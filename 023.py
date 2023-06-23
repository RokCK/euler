# Problem 023: Non-Abundant Sums

def sum_divisors(n):
    result = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            if n // i == i:
                result = result + i
            else:
                result = result + (i + n//i)
        i += 1
    return result - n
abundant_nums = [i for i in range(1, 28124) if sum_divisors(i) > i]
abundant_sums = [False] * 28124
for i in range(len(abundant_nums)):
    for j in range(i, 28124):
        if abundant_nums[i] + abundant_nums[j] < 28124:
            abundant_sums[abundant_nums[i] + abundant_nums[j]] = True
        else:
            break

total = sum(i for i in range(1, 28124) if abundant_sums[i] == False)
print(total)
