# print all perfect numbers up to MAX

MAX = 1000
for i in range(1,MAX):
    sum = 0
    for j in range(1,i):
        if i % j == 0:
            sum += j
    if i == sum:
        print(f"{i} is a perfect number")

