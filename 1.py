# Problem 1
s = 0
for i in range(1,1000):
    print(i)
    if (i % 3 == 0 and i % 5 == 0) or (i % 3 ==0 and i % 5 != 0) or (i % 3 != 0 and i % 5 == 0):
        s += i
        print(s)
